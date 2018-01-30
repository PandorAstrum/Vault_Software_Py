# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import re
from functools import partial
import threading
import time

from kivy.clock import mainthread, Clock
from kivy.factory import Factory
from selenium import webdriver
from bs4 import BeautifulSoup

from bin.Component.Mining_PRComponent.reusable import ScrapField
import utils
from Core.baseInterface import DriverBase
from Core.spawner import Spawn
from Core.snacksbar import Snacks
from Core.popups import Popups


class MiningSeleniumTabDrivers(DriverBase):
    def __init__(self, instances, **kwargs):
        super(MiningSeleniumTabDrivers, self).__init__(**kwargs)
        self.instances = instances
        self.snacks = Snacks()
        self.pop = Popups()
        self.spawn = Spawn()
        self.scrap_field_box = self.instances.ids.scrap_field_box_id
        self.field_instance = []
        self.scrapping_progress = None
        self.driver = None
        self.total_progress_count = 0
        self._make()

    def _make(self):
        """
        Make the first Scrap field
        :return:
        """
        if len(self.scrap_field_box.children) < 1:
            scrap_field = ScrapField(self, "0")
            self.scrap_field_box.add_widget(scrap_field)

    @utils.clocked()
    def add_new_field(self):
        """
        scrap box main button callback
        :return:
        """
        num = str(len(self.scrap_field_box.children) + 1)
        self.scrap_field_box.add_widget(ScrapField(self, num))

    @utils.threaded(thread_name="email check")
    def check_email(self, email):
        """
        email_check_btn_id callback
        :param email: str from single_email_text_id.text
        :return:
        """
        def on_finish_callback():
            self.instances.ids.email_check_btn_id.disabled = False
        # Simple Regex for syntax checking
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        if email != str:
            email_address = str(email)
        else:
            email_address = email
        # Syntax check
        match = re.match(regex, email_address)
        if match == None:
            self.snacks.snacks("simple", "Please Provide an Email address")
        else:
            self.instances.ids.email_check_btn_id.disabled = True
            _get = utils.email_check(email)
            if _get:
                content = self.spawn.add_md_label(font_style="Body1",
                                                  text="Looks like the Email is valid",
                                                  halign="center")
                self.pop.pop_modal(size_hint_x=0.5, size_hint_y=None, height=200,
                                   title_align="center", dialog_title="Email Found",
                                   final_button="Okay", content=content,
                                   custom_callback=on_finish_callback)
            else:
                content = self.spawn.add_md_label(font_style="Body1",
                                                  text="Oops the Email seems fake",
                                                  halign="center")
                self.pop.pop_modal(size_hint_x=0.5, size_hint_y=None, height=200,
                                   title_align="center", dialog_title="Email Not Found",
                                   final_button="okay", content=content,
                                   custom_callback=on_finish_callback)

    @utils.threaded(thread_name="scrapping Thread")
    def start_scrapping(self):
        """
        start_scrapping_btn_id callback
        :return:
        """
        def _collect_link():
            """
            docstring
            :return: list of scrapping link
            """
            # self.pop.test(self.scrapping_progress,
            #                          "[Phase 1/3] Getting link...",
            #                          self._calculate_phase(5, 10))
            if self.instances.ids.single_link_id.active:
                return [self.instances.ids.link_to_scrap_id.text]
            # csv link
            elif self.instances.ids.multi_link_id.active:
                csv_file_path = self.instances.ids.import_csv_file_path_id.text
                with open(csv_file_path, newline='') as csvfile:
                    first_column = [line.split(',')[0] for line in csvfile]
                    first_column.pop(0)
                    return first_column
            else:
                return None

        def _collect_login(driver, wait_time):
            # self.pop.test(self.scrapping_progress,
            #                          "[Phase 1/3] Collecting login...",
            #                          self._calculate_phase(5, 10))
            if self.instances.ids.login_option_id.active:
                if self.instances.ids.linkedin_id.active:
                    user_name = self.instances.ids.linkedin_username_id.text
                    pass_word = self.instances.ids.linkedin_password_id.text
                    driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
                    time.sleep(wait_time)
                    driver.find_element_by_xpath('//*[@id="session_key-login"]').send_keys(user_name)
                    driver.find_element_by_xpath('//*[@id="session_password-login"]').send_keys(pass_word)
                    time.sleep(wait_time)
                    driver.find_element_by_xpath('//*[@id="btn-primary"]').click()
                    time.sleep(wait_time)
                elif self.instances.ids.custom_login_id.active:
                    user_name = self.instances.ids.custom_username_id.text
                    pass_word = self.instances.ids.custom_password_id.text
                    url = self.instances.ids.sign_in_url_id.text
                    driver.get(url)
                    time.sleep(wait_time)
                    u_xpath = self.instances.ids.custom_username_xpath_id.text
                    p_xpath = self.instances.ids.custom_password_xpath_id.text
                    driver.find_element_by_xpath(u_xpath).send_keys(user_name)
                    driver.find_element_by_xpath(p_xpath).send_keys(pass_word)
                    time.sleep(wait_time)
                    login_btn_xpath = self.instances.ids.sing_in_btn_xpath_id.text
                    driver.find_element_by_xpath(login_btn_xpath).click()
                    time.sleep(wait_time)

            else:
                # no need of login
                pass

        def _get_parameter_scroll(driver, wait_time):
            if self.instances.ids.scroll_to_bottom_id.active:
                # Get scroll height
                last_height = driver.execute_script("return document.body.scrollHeight")
                while True:
                    time.sleep(wait_time)
                    # Scroll down to bottom
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    # Wait to load page
                    time.sleep(wait_time)
                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
            else:
                pass

        def _get_parameter_limiter():
            if self.instances.ids.limiter_id.active:
                return int(self.instances.ids.limiter_text_id.text) - 1
            else:
                return 0

        def _get_parameter_missing_link(raw_data):
            if self.instances.ids.missing_link_id.active:
                tmp = []
                missing_link = self.instances.ids.missing_link_text_id.text
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_link_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in raw_data.keys():
                            for i in raw_data[field_name]:
                                tmp.append(f"{missing_link}{i}")
                            raw_data[field_name] = tmp
            else:
                pass

        def _get_parameter_string_fix(raw_data):
            if self.instances.ids.fix_text_id.active:
                tmp = []
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_text_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in raw_data.keys():
                            for i in raw_data[field_name]:
                                tmp.append(i.strip())
                            raw_data[field_name] = tmp
            else:
                pass

        def _get_parameter_email_fix(raw_data):
            if self.instances.ids.email_cheker_id.active:
                tmp = []
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_email_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in raw_data.keys():
                            for i in raw_data[field_name]:
                                if utils.email_check(i):
                                    tmp.append(i)
                                else:
                                    tmp.append("Email Not Valid")
                            raw_data[field_name] = tmp
            else:
                pass

        def _process_next(driver, wait_time):
            """
            doctring
            :param driver:
            :return: driver next element to click
            """
            if self.instances.ids.next_page_id.active:
                next_page_tag = self.instances.ids.next_page_tag_id.text
                next_page_tag_class = self.instances.ids.next_page_class_id.text
                next_page_final_tag = self.instances.ids.next_page_final_id.text
                if self.instances.ids.next_page_btn_id.active:
                    # process as buttons
                    try:
                        _get_parameter_scroll(driver, wait_time)
                        _next = driver.find_element_by_xpath(f"//button[@class='{next_page_tag_class}']")
                    except:
                        _next = None
                    finally:
                        return _next
                else:
                    # process without buttons
                    if not next_page_final_tag == "":
                        try:
                            _next = driver.find_element_by_xpath(
                                f"//{next_page_tag}[@class='{next_page_tag_class}']/child::{next_page_final_tag}")
                        except:
                            _next = None
                        finally:
                            return _next
                    else:
                        try:
                            _get_parameter_scroll(driver, wait_time)
                            _next = driver.find_element_by_xpath(f"//{next_page_tag}[@class='{next_page_tag_class}']")
                        except:
                            _next = None
                        finally:
                            return _next

            elif self.instances.ids.continuous_id.active:
                pass
            else:
                # no continue
                return None

        def _soup_find(soup, find_all=False, tag_field=None,
                       selector_text=None, selector_parameter="default"):
            if find_all:
                if selector_text == None:
                    return soup.find_all(tag_field)
                else:
                    if selector_parameter == "cls":
                        return soup.find_all(tag_field, {"class": selector_text})
                    elif selector_parameter == "id":
                        return soup.find_all(tag_field, {"id": selector_text})
                    elif selector_parameter == "str":
                        return soup.find_all(tag_field, string=selector_text)
                    elif selector_parameter == "default":
                        return soup.find_all(tag_field)
            else:
                if selector_text == None:
                    return soup.find(tag_field)
                else:
                    if selector_parameter == "cls":
                        return soup.find(tag_field, {"class": selector_text})
                    elif selector_parameter == "id":
                        return soup.find(tag_field, {"id": selector_text})
                    elif selector_parameter == "str":
                        pass
                    else:
                        return soup.find(tag_field)

        def _check_selector_text(tag_selector):
            if not utils.is_empty(tag_selector.selector_field.text):
                return tag_selector.selector_field.text
            else:
                return None

        def _check_selector_parameter(tag_selector):
            if tag_selector.cls_selector_chk.active:
                return "cls"
            elif tag_selector.id_selector_chk.active:
                return "id"
            elif tag_selector.str_selector_chk.active:
                return "str"
            else:
                return "default"

        def _get_items(soup, pre_content, item):
            tmp = []
            selector_text = _check_selector_text(item)
            if not utils.is_empty(pre_content):
                for p in pre_content:
                    if item.find_chk.active:
                        tmp = _soup_find(p, find_all=True,
                                         tag_field=item.tag_field.text,
                                         selector_text=selector_text,
                                         selector_parameter=_check_selector_parameter(item))

                    else:
                        tmp.append(_soup_find(p, tag_field=item.tag_field.text,
                                              selector_text=selector_text,
                                              selector_parameter=_check_selector_parameter(item)))
                return tmp
            else:
                if item.find_chk.active:
                    tmp = _soup_find(soup, find_all=True,
                                     tag_field=item.tag_field.text,
                                     selector_text=selector_text,
                                     selector_parameter=_check_selector_parameter(item))
                    return tmp
                else:
                    tmp.append(_soup_find(soup, tag_field=item.tag_field.text,
                                          selector_text=selector_text,
                                          selector_parameter=_check_selector_parameter(item)))
                    return tmp

        def _check_field_value(scrap_field, data):
            temp = []
            if scrap_field.get_value_chk.active:
                for d in data:
                    temp.append(d)
            elif scrap_field.get_href_chk.active:
                for d in data:
                    temp.append(d["href"])
            elif scrap_field.get_str_chk.active:
                for d in data:
                    temp.append(d.text)
            elif scrap_field.get_title_chk.active:
                for d in data:
                    temp.append(d["title"])
            elif scrap_field.get_src_chk.active:
                for d in data:
                    temp.append(d["src"])
            else:
                for d in data:
                    temp.append(d)
            return temp

        def _collect_data_per_page(soup):
            """

            :param soup:
            :return: a dictionary of tag_field.text : content list
            """
            dict = {}
            for scrap_field in self.instances.ids.scrap_field_box_id.children:
                # determine tag_selector len
                total_tag_selector = len(scrap_field.tag_selector_list)
                starting_number = 0
                pre_content = None
                while total_tag_selector > 1:
                    item = scrap_field.tag_selector_list[starting_number]
                    if not item.tag_field.text == "":
                        pre_content = _get_items(soup, pre_content, item)
                    else:
                        # error
                        pass
                    total_tag_selector -= 1
                    starting_number += 1

                last_item = scrap_field.tag_selector_list[starting_number]
                if not utils.is_empty(last_item.tag_field.text):
                    pre_content = _get_items(soup, pre_content, last_item)
                # write to dict
                dict[scrap_field.field_name.text] = _check_field_value(scrap_field, pre_content)
            return dict

        def _soup(driver, wait_time, _dict=None, _s_dict=False):
            time.sleep(wait_time)
            _get_parameter_scroll(driver, wait_time)
            html_doc = driver.page_source
            soup = BeautifulSoup(html_doc, "lxml")
            if not _dict == None:
                _dict.append(_collect_data_per_page(soup))
                # return _dict_list
            elif _s_dict:
                _single_dict = _collect_data_per_page(soup)
                return _single_dict
            else:
                return soup

        def collector(wait_time):
            """
            docstring
            :param wait_time: float get from time_id.value
            :return: single dict or combined dict from single page or all page
            """
            main_dict = {}
            # collect browser
            if self.instances.ids.google_chrome_id.active:
                _scrap_link_list = _collect_link()
                if _scrap_link_list is None:
                    self.snacks.snacks("simple", "Please select an option in Scrap Link")
                    return None
                elif _scrap_link_list == [""]:
                    self.snacks.snacks("simple", "No link to scrap")
                    return None
                else:
                    # self.pop.test(self.scrapping_progress,
                    #                          "[Phase 1/3] Getting Browser...",
                    #                          self._calculate_phase(5, 10))
                    # self.instances.ids.start_scrapping_btn_id.disabled = True
                    self.driver = webdriver.Chrome(executable_path=".\\dll\\chrome_drivers\\chromedriver.exe")
                    # self.pop.test(self.scrapping_progress,
                    #                          "[Phase 1/3] Opening Browser...",
                    #                          self._calculate_phase(5, 10))

                    _collect_login(self.driver, wait_time)
                    for link in _scrap_link_list:
                        # check for next
                        try:

                            self.driver.get(link)
                            time.sleep(wait_time)
                        except:
                            self.driver = None

                        try:
                            _next = _process_next(self.driver, wait_time)
                        except:
                            _next = None

                        if _next is not None:
                            _dict_list = []
                            limit_count = 0
                            while _next is not None:
                                if limit_count == _get_parameter_limiter():
                                    break
                                _soup(self.driver, wait_time, _dict=_dict_list)
                                _next.click()
                                time.sleep(wait_time)
                                _next = _process_next(self.driver, wait_time)
                                limit_count += 1
                            # last page
                            _soup(self.driver, wait_time, _dict=_dict_list)
                            # finally merge all dict into one
                            main_dict = utils.combine_dict(*_dict_list)

                        else:
                            if self.instances.ids.multi_link_id.active:
                                dict_list = []
                                dict_list.append(_soup(self.driver, wait_time, _s_dict=True))
                                main_dict = utils.combine_dict(*dict_list)
                            else:
                                try:
                                    _single_dict = _soup(self.driver, wait_time, _s_dict=True)
                                except:
                                    _single_dict = None
                                main_dict = _single_dict
                    self.driver.quit()
                    return main_dict

            elif self.instances.ids.mozilla_firefox_id.active:
                self.driver = webdriver.Firefox(executable_path=".\\dll\\firefox_drivers\\geckodriver.exe")
                self._collect_login(self.driver, wait_time)
            elif self.instances.ids.ie_id.active:
                self.driver = webdriver.Ie(executable_path=".\\dll\explorer_drivers\\IEDriverServer.exe")
                self._collect_login(self.driver, wait_time)
            else:
                self.snacks.snacks("simple", "Please Choose a Browser")
                return None

        def _process_write_data(raw_data):
            """

            :param raw_data:
            :return:
            """
            if raw_data is not None:
                _get_parameter_missing_link(raw_data)
                _get_parameter_string_fix(raw_data)
                _get_parameter_email_fix(raw_data)
                # upgrade progress bar
                curr = utils.get_computer_date_time()
                utils.dict_to_csv(filename=f"{curr}_scrap.csv", dict_data=raw_data)
                # upgrade progress bar to finish
                # take temporary copy to view
                # send a notification
                email_body = f"scrapping done in {self.instances.ids.link_to_scrap_id.text}" \
                             f"at {curr}"
                utils.send_a_mail(email_subject=f"Scrapping Done at {curr}",
                                  email_body=email_body,login_pass="chr0niclesOFana&ash")

        wait_time = round(self.instances.ids.time_id.value, 1)
        # self.scrapping_progress = self.pop.pop_progress(title="Scrapping In Progress", text="",
        #                       max_value=100, cancel_callback=self.on_progress_cancel)

        # self.pop.test(self.scrapping_progress, "[Phase 1/3] Initializing...",
        #                          self._calculate_phase(5, 10))

        raw_data = collector(wait_time)
        _process_write_data(raw_data)

    def import_csv(self):
        # callback
        def import_callback(instance):
            if instance.is_canceled():
                return
            s = 'Path: %s' % instance.path
            if instance.__class__.__name__ == 'XFileSave':
                s += ('\nFilename: %s\nFull name: %s' %
                      (instance.filename, instance.get_full_name()))
            else:
                s += ('\nSelection: %s' % instance.selection)
            # XNotification(title='Pressed button: ' + instance.button_pressed,
            #               text=s, show_time=5)

            self.instances.ids.import_csv_file_path_id.text = instance.selection[0]
        self.pop_up._xpop("fileOpen", on_dismiss_callback=import_callback)

        # Clock.schedule_once(lambda dt: self.update_progress(progress_text="initializing....", pn_delta=0), .1)
    def on_complete_progress(self):
        self.instances.ids.view_data_btn_id.disabled = False
        self.instances.ids.start_scrapping_btn_id.disabled = False
        self.snacks.snacks("simple", "Scrapping finished in 2.0s")
        print("Completed")

    def on_progress_cancel(self, instance):
        self.instances.ids.start_scrapping_btn_id.disabled = False
        if self.driver is not None:
            self.driver.quit()
        self.snacks.snacks("simple", "Scrapping Canceled")

    def _calculate_phase(self, phase_total, phase_value):
        return phase_value * 1.0/phase_total


    def total_progress_counter(self):
        # phase 1 intializing 2
        # phase 1 getting browser 2
        # phase 1 opening browser 2
        # phase 1 getting link 2
        # phase 1 collecting login 2
        # phase 2 collecting next page
        # phase 2 collecting scrap field
        # phase 2 collecting parameter
        # phase 2 collecting data
        # phase 3 preparing data
        # phase 3 finalizing and dumping data
        # finish
        total = 100
        collecting_browser = 1
        opening_page = 1
        raw_data = 1
        writing_data = 1
        checking_link = 1
        if self.instances.ids.login_option_id.active:
            login = 1
        else:
            login = 0
        self.total_progress_count = 4


    @staticmethod
    def _confirmation_callback(instance):
        if instance.is_canceled():
            return


    def view_data(self):
        # make buttons
        # buttons callback

        self.pop.pop_modal()
        # get the csv or data file
        # create a modal with scrollview
        # create the grid with data
        # attach it to scrollview
        # bind buttons with functions
        # show
        print("viewing Data")

    def export_to_csv(self):
        pass
    def export_to_excel(self):
        pass
