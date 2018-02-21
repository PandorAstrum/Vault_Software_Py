# -*- coding: utf-8 -*-

import re
import time
import urllib.request as urllib2
from functools import partial

from kivy.clock import mainthread
from selenium import webdriver
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from bs4 import BeautifulSoup

import utils
from Core.drivers import DriverBase
from bin.Component.Miner_PRComponent.reusable import ScrapField
from utils.webcheck import parse
from utils.whois import whois

__all__         = [
    "MinerScrapyTabDrivers",
    "MinerSeleniumTabDrivers",
    "MinerUtilityTabDrivers"
]
__author__      = "Ashiquzzaman Khan"
__copyright__   = "2018 GPL"
__desc__        = """Miner Drivers"""


class MinerScrapyTabDrivers(DriverBase):
    pass

    # check for robots or sitemap in the website
    # if exists then settings delay and other from that

    # check the website with builtswith

    # check the owner with python-whois

    # check if the slug is important or not

    # download a webpage
    def download(self, url, user_agent='wswp', num_retries=2):
        print('Progress bar -> Downloading:', url)
        headers = {'User-agent': user_agent}
        request = urllib2.Request(url, headers=headers)
        try:
            html = urllib2.urlopen(request).read()
        except urllib2.URLError as e:
            print('Progress bar -> Download error:', e.reason)
            html = None
            if num_retries > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:  # recursively retry 5xx HTTP errors
                    return self.download(url, user_agent, num_retries-1)
        return html


class MinerSeleniumTabDrivers(DriverBase):
    def __init__(self, instances, **kwargs):
        super(MinerSeleniumTabDrivers, self).__init__(**kwargs)
        self.instances = instances
        self.scrap_field_box = self.instances.ids.scrap_field_box_id
        self.field_instance = []
        self.scrapping_progress = None
        self.driver = None
        self.total_progress_count = 0
        self._make()

    def _make(self):
        """
        Make the first Scrap field Default
        :return:
        """
        if len(self.scrap_field_box.children) < 1:
            scrap_field = ScrapField(self, "0")  # init with assign first number for grouping
            # button bind
            scrap_field.check_field_btn.bind(on_release=partial(self.check_field_button,
                                                                scrap_field_instance=scrap_field))
            self.scrap_field_box.add_widget(scrap_field)

    # scrap link collect
    def _collect_link(self, enclose=True):
        """
        Scrap Link Collector
        :param enclose: bool value to trigger List or Text
        :return: List or text depending on default
        """
        if not enclose:
            if self.instances.ids.single_link_id.active:
                return self.instances.ids.link_to_scrap_id.text
            # csv link
            elif self.instances.ids.multi_link_id.active:
                csv_file_path = self.instances.ids.import_csv_file_path_id.text
                with open(csv_file_path, newline='') as csvfile:
                    first_column = [line.split(',')[0] for line in csvfile]
                    first_column.pop(0)
                    return first_column[0]
            else:
                return None  # snacks bar raise
        else:
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
                return None  # snack bar raise

    # login prerequisite
    def _check_login_prerequisite(self, driver, wait_time):
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

    # generic parameters
    def _execute_parameter(self, param="scroll", **kwargs):
        if param == "scroll":
            driver = kwargs.get("driver")
            wait_time = kwargs.get("wait_time")
            if self.instances.ids.scroll_to_bottom_id.active:  # check if this is active
                last_height = driver.execute_script("return document.body.scrollHeight")  # Get scroll height
                while True:
                    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")  # Scroll down to bottom
                    time.sleep(wait_time)  # Wait to load page
                    # Calculate new scroll height and compare with last scroll height
                    new_height = driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        break
                    last_height = new_height
            else:
                return  # pass
        elif param == "limit":
            if self.instances.ids.limit_id.active:  # check if its active
                return int(self.instances.ids.limit_text_id.text) - 1
            else:
                return int(0)
        elif param == "link":
            if self.instances.ids.missing_link_id.active:  # check if its active
                tmp = []
                missing_link = self.instances.ids.missing_link_text_id.text
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_link_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in kwargs.get("raw_data").keys():
                            for i in kwargs.get("raw_data")[field_name]:
                                tmp.append(f"{missing_link}{i}")
                            kwargs.get("raw_data")[field_name] = tmp
            else:
                return  # pass
        elif param == "string":
            if self.instances.ids.fix_text_id.active:  # check if its active
                tmp = []
                replace_text = f"{self.instances.ids.string_fix_text_id.text}".split(',')

                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_text_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in kwargs.get("raw_data").keys():
                            for i in kwargs.get("raw_data")[field_name]:
                                for ch in replace_text:
                                    if ch in i:
                                        i = i.replace(ch, "")
                                tmp.append(i.strip())
                            kwargs.get("raw_data")[field_name] = tmp
            else:
                return  # pass
        elif param == "email":
            kwargs.get("raw_data")
            if self.instances.ids.email_cheker_id.active:
                tmp = []
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    if scrap_field.mark_email_chk.active:
                        field_name = scrap_field.field_name.text
                        if field_name in kwargs.get("raw_data").keys():
                            for i in kwargs.get("raw_data")[field_name]:
                                if utils.email_check(i):
                                    tmp.append(i)
                                else:
                                    tmp.append("Email Not Valid")
                            kwargs.get("raw_data")[field_name] = tmp
            else:
                return  # pass

    # extract data from soup
    def _extract_data(self, check_scrap_filed=False, soup=None, **kwargs):
        # collect data per page from soup object
        def _get_selector_text(tag_item):
            if not utils.is_empty(tag_item.selector_field.text):
                return tag_item.selector_field.text
            else:
                return None

        def _get_selector_param(tag_item):
            if tag_item.cls_selector_chk.active:
                return "cls"
            elif tag_item.id_selector_chk.active:
                return "id"
            elif tag_item.str_selector_chk.active:
                return "str"
            else:
                return "default"

        def _get_selector_attr(tag_item, extracted_data):
            temp = []
            if tag_item.get_value_chk.active:
                for d in extracted_data:
                    temp.append(d)
            elif tag_item.get_href_chk.active:
                for d in extracted_data:
                    temp.append(d["href"])
            elif tag_item.get_str_chk.active:
                for d in extracted_data:
                    temp.append(d.text.strip())
            elif tag_item.get_title_chk.active:
                for d in extracted_data:
                    temp.append(d["title"])
            elif tag_item.get_src_chk.active:
                for d in extracted_data:
                    temp.append(d["src"])
            else:
                for d in extracted_data:
                    temp.append(d)
            return temp

        def _soup_find(soup, find_all=False, tag_field_text=None,
                       selector_text=None, selector_parameter="default"):
            if find_all:
                if selector_text is None:
                    return soup.find_all(tag_field_text)
                else:
                    if selector_parameter == "cls":
                        return soup.find_all(tag_field_text, {"class": selector_text})
                    elif selector_parameter == "id":
                        return soup.find_all(tag_field_text, {"id": selector_text})
                    elif selector_parameter == "str":
                        return soup.find_all(tag_field_text, string=selector_text)
                    elif selector_parameter == "default":
                        return soup.find_all(tag_field_text)
            else:
                if selector_text is None:
                    return soup.find(tag_field_text)
                else:
                    if selector_parameter == "cls":
                        return soup.find(tag_field_text, {"class": selector_text})
                    elif selector_parameter == "id":
                        return soup.find(tag_field_text, {"id": selector_text})
                    elif selector_parameter == "str":
                        pass
                    else:
                        return soup.find(tag_field_text)

        def _get_tag_items(soup, extracted_data, tag_item):
            tmp = []
            if not utils.is_empty(extracted_data):  # have previous data
                for p in extracted_data:
                    # find all
                    if tag_item.find_chk.active:
                        tmp = _soup_find(p, find_all=True,
                                         tag_field_text=tag_item.tag_field.text,
                                         selector_text=_get_selector_text(tag_item),
                                         selector_parameter=_get_selector_param(tag_item))
                    # find single
                    else:
                        tmp.append(_soup_find(p, tag_field_text=tag_item.tag_field.text,
                                              selector_text=_get_selector_text(tag_item),
                                              selector_parameter=_get_selector_param(tag_item)))
                return tmp
            else:  # have no previous entry
                if tag_item.find_chk.active:  # find all
                    tmp = _soup_find(soup, find_all=True,
                                     tag_field_text=tag_item.tag_field.text,
                                     selector_text=_get_selector_text(tag_item),
                                     selector_parameter=_get_selector_param(tag_item))
                    return tmp
                else:  # find single
                    tmp.append(_soup_find(soup, tag_field_text=tag_item.tag_field.text,
                                          selector_text=_get_selector_text(tag_item),
                                          selector_parameter=_get_selector_param(tag_item)))
                    return tmp

        def _extract_tag(soup, scrap_field_instance):
            """

            :param soup:
            :return: dict
            """
            total_tag_selector = len(scrap_field_instance.tag_selector_list)
            starting_number = 0
            extracted_data = None
            while total_tag_selector > 1:
                single_tag_item = scrap_field_instance.tag_selector_list[starting_number]
                if not single_tag_item.tag_field.text == "":
                    extracted_data = _get_tag_items(soup, extracted_data, single_tag_item)
                else:
                    # error
                    pass
                total_tag_selector -= 1
                starting_number += 1
            #
            last_tag_item = scrap_field_instance.tag_selector_list[starting_number]
            if not utils.is_empty(last_tag_item.tag_field.text):
                extracted_data = _get_tag_items(soup, extracted_data, last_tag_item)
            return extracted_data # list

        if check_scrap_filed:
            scrap_field_instance = kwargs.get("scrap_field_instance")
            data = _extract_tag(soup, scrap_field_instance)
            checked = _get_selector_attr(scrap_field_instance, data)
            tmp_str = ""
            for i in checked:
                tmp_str = tmp_str + str(i) + ","
            return tmp_str
        else:
            _single_dict = kwargs.get("_single_dict")
            _dict = {}
            if _single_dict:
                for scrap_field in self.instances.ids.scrap_field_box_id.children:
                    data = _extract_tag(soup, scrap_field)
                    _dict[scrap_field.field_name.text] = _get_selector_attr(scrap_field, data)

                return _dict
            else:
                if kwargs.get("_dict_list") is not None:
                    for scrap_field in self.instances.ids.scrap_field_box_id.children:
                        data = _extract_tag(soup, scrap_field)
                        _dict[scrap_field.field_name.text] = _get_selector_attr(scrap_field, data)
                    kwargs.get("_dict_list").append(_dict)
            #         if _dict_list is not None:
            #             _dict_list.append(_collect_data_per_page(soup))
            # return _dict_list


        def _collect_data_per_page(soup):
            """
            Either returns a single dict or multiple dict
            :param soup:
            :return: a dictionary of tag_field.text : content list
            """
            # _dict = {}
            # for scrap_field in self.instances.ids.scrap_field_box_id.children:
            #     # determine tag_selector len
            #     total_tag_selector = len(scrap_field.tag_selector_list)
            #     starting_number = 0
            #     pre_content = None
            #     while total_tag_selector > 1:
            #         item = scrap_field.tag_selector_list[starting_number]
            #         if not item.tag_field.text == "":
            #             pre_content = self._get_items(soup, pre_content, item)
            #         else:
            #             # error
            #             pass
            #         total_tag_selector -= 1
            #         starting_number += 1
            #
            #     last_item = scrap_field.tag_selector_list[starting_number]
            #     if not utils.is_empty(last_item.tag_field.text):
            #         pre_content = self._get_items(soup, pre_content, last_item)
            #     # write to dict
            #     _dict[scrap_field.field_name.text] = _check_field_value(scrap_field, pre_content)
            #     print(_dict)
            # return _dict

        # if soup is not None:
        #     if _single_dict:
        #         _s_dict = _collect_data_per_page(soup)
        #         return _s_dict
        #     else:
        #         if _dict_list is not None:
        #             _dict_list.append(_collect_data_per_page(soup))
            # return _dict_list

    # make soup object
    def _make_soup(self, driver=None, **kwargs):
        if driver is None:
            url = kwargs.get("url")
            user_agent = kwargs.get("user_agent")
            retries = kwargs.get("retries")
            html = utils.download_webpage(url, user_agent, retries)
            if html is not None:
                soup = BeautifulSoup(html, "lxml")
                return soup
            else:
                return None

        else:
            wait_time = kwargs.get("wait_time")
            self._execute_parameter(param="scroll", driver=driver, wait_time=wait_time)
            html_doc = driver.page_source
            soup = BeautifulSoup(html_doc, "lxml")
            return soup


    @utils.clocked()
    def add_new_field(self):
        """
        scrap box main button callback
        :return:
        """
        num = str(len(self.scrap_field_box.children) + 1)
        new_scrap_field = ScrapField(self, num)
        new_scrap_field.check_field_btn.bind(on_release=partial(self.check_field_button,
                                                                scrap_field_instance=new_scrap_field))
        self.scrap_field_box.add_widget(new_scrap_field)

    @utils.threaded(thread_name="scrapping Thread")
    def start_scrapping(self):
        """
        start_scrapping_btn_id callback
        :return:
        """
        # buttons callback
        def export_csv(raw_data):
            curr = utils.get_computer_date_time()
            utils.dict_to_csv(filename=f"{curr}_scrap.csv", dict_data=raw_data)

        def export_xlsl():
            print("export xlsl")

        def cancel():
            print("cancel")

        # get browser
        def _init_browser(driver_executable="chrome"):
            """

                :param _wait_time:
                :param driver_executable_path:
                choose any three from
                ".\\dll\\chrome_drivers\\chromedriver.exe" for chrome
                ".\\dll\\firefox_drivers\\geckodriver.exe" for firefox
                ".\\dll\explorer_drivers\\IEDriverServer.exe" for ie
                :return:
                """
            if driver_executable == "chrome":
                return webdriver.Chrome(executable_path=".\\dll\\chrome_drivers\\chromedriver.exe")
            elif driver_executable == "firefox":
                return webdriver.Firefox(executable_path=".\\dll\\firefox_drivers\\geckodriver.exe")
            else:
                return webdriver.Ie(executable_path=".\\dll\explorer_drivers\\IEDriverServer.exe")

                # _scrap_link_list = self._collect_link(default=False)  # collect link to scrap
                #
                # if _scrap_link_list is None:
                #     self.snacks("simple", "Please select a Scrap Link option")
                #     return None
                # elif _scrap_link_list == [""]:
                #     self.snacks("simple", "No link to scrap")
                #     return None
                # else:
                # self.instances.ids.start_scrapping_btn_id.disabled = True
                # if driver_executable == "chrome":
                #     self.driver = webdriver.Chrome(executable_path=".\\dll\\chrome_drivers\\chromedriver.exe")
                # elif driver_executable == "firefox":
                #     self.driver = webdriver.Firefox(executable_path=".\\dll\\firefox_drivers\\geckodriver.exe")
                # else:
                #     self.driver = webdriver.Ie(executable_path=".\\dll\explorer_drivers\\IEDriverServer.exe")

                # page_load_time = round(self.instances.ids.pageload_time_id.value, 0)
                # self.driver.set_page_load_timeout(page_load_time)  # set webdriver timeout for page loading
                #
                # _collect_login(self.driver, wait_time)  # collect if login data available

                # for link in _scrap_link_list:
                #     try:
                #         self.driver.get(link)  # first link from the kv
                #         time.sleep(wait_time)  # wait to load the page
                #     except TimeoutException:
                #         self.snacks(type="button", duration=999,
                #                     message=f"Timeout. Page is taking more than {page_load_time} seconds to load")
                #
                #     _next = _process_next(self.driver, wait_time)  # Collect if next available
                #
                #     if _next is not None:
                #         _dict_list = []
                #         limit_count = 0
                #         parameter_limiter = _get_parameter_limit()
                #         while _next is not None:
                #             if limit_count == parameter_limiter:
                #                 break
                #             _soup(self.driver, wait_time, _dict=_dict_list)  # make soup and gather data
                #             self.driver.execute_script("arguments[0].click();", _next)
                #             time.sleep(wait_time)
                #             _next = _process_next(self.driver, wait_time)  # Collect next link from the page
                #             limit_count += 1
                #         # last page
                #         _soup(self.driver, wait_time, _dict=_dict_list)  # make soup and gather data
                #         # finally merge all dict into one
                #         main_dict = utils.combine_dict(*_dict_list)
                #
                #     else:  # no next available
                #         if self.instances.ids.multi_link_id.active:
                #             _dict_list = []
                #             try:
                #                 _dict_list.append(_soup(self.driver, wait_time, _s_dict=True))
                #             except:
                #                 pass
                #             main_dict = utils.combine_dict(*_dict_list)
                #         else:
                #             try:
                #                 _single_dict = _soup(self.driver, wait_time, _s_dict=True)
                #             except:
                #                 _single_dict = None
                #             main_dict = _single_dict
                # self.driver.quit()
                # return main_dict

        # next
        def _process_next(driver, wait_time):
            """
            doctring
            :param driver:
            :return: driver next element to click
            """
            if self.instances.ids.next_page_id.active:
                next_page_css_selector = self.instances.ids.next_page_tag_id.text
                if not next_page_css_selector == "":
                    try:
                        self._execute_parameter(param="scroll", driver=driver, wait_time=wait_time)
                        return driver.find_element_by_css_selector(f"{next_page_css_selector}")
                        # return driver.find_element_by_xpath(f"{next_page_xpath}")
                    except NoSuchElementException:  # element not found
                        self.snacks("simple", "Next link not found")
                        return None
            elif self.instances.ids.continuous_id.active:
                # TODO: implementation of continuous comment
                pass
            else:
                # no continue
                return None

        def collect(wait_time):
            """
            collect data function
            :param wait_time: float get from time_id.value
            :return: single dict or combined dict from single page or all page
            """
            main_dict = {}

            if self.instances.ids.google_chrome_id.active:
                # collect scrap link
                _scrap_link_list = self._collect_link(enclose=False)

                if _scrap_link_list is None:
                    self.snacks("simple", "Please select a Scrap Link option")
                    return None
                elif _scrap_link_list == [""]:
                    self.snacks("simple", "No link to scrap")
                    return None
                else:
                    # init browser Google
                    self.driver = _init_browser()
                    # set page load
                    page_load_time = round(self.instances.ids.pageload_time_id.value, 0)
                    # set web driver timeout for page loading
                    self.driver.set_page_load_timeout(page_load_time)

                    # check login and collect if available
                    self._check_login_prerequisite(self.driver, wait_time)

                    for link in _scrap_link_list:
                        try:
                            self.driver.get(link)  # first link from the kv
                            time.sleep(wait_time)  # wait to load the page
                            _next = _process_next(self.driver, wait_time)  # check and collect next page
                            if _next is not None:
                                _dict_list = []
                                limit_count = 0
                                param_limit = self._execute_parameter(param="limit")
                                while _next is not None:
                                    if limit_count == param_limit:
                                        break
                                    # make the soup
                                    soup = self._make_soup(driver=self.driver, wait_time=wait_time)
                                    # _soup(self.driver, wait_time, _dict=_dict_list)  # make soup and gather data

                                    # gather data from soup object
                                    self._extract_data(soup=soup, _single_dict=False, _dict_list=_dict_list)
                                    # click next
                                    self.driver.execute_script("arguments[0].click();", _next)
                                    time.sleep(wait_time)
                                    _next = _process_next(self.driver, wait_time)  # Collect next link from the page
                                    limit_count += 1
                                # last page
                                soup = self._make_soup(driver=self.driver, wait_time=wait_time)
                                # gather data
                                self._extract_data(soup=soup, _dict_list=_dict_list)
                                # finally merge all dict into one
                                main_dict = utils.combine_dict(*_dict_list)

                            else:  # no next available
                                if self.instances.ids.multi_link_id.active:
                                    _dict_list = []
                                    try:
                                        soup = self._make_soup(driver=self.driver, wait_time=wait_time)
                                        _dict_list.append(self._extract_data(soup=soup, _single_dict=True))

                                        # _dict_list.append(_soup(self.driver, wait_time, _s_dict=True))
                                    except:
                                        pass
                                    main_dict = utils.combine_dict(*_dict_list)
                                else:
                                    try:
                                        soup = self._make_soup(driver=self.driver, wait_time=wait_time)
                                        _single_dict = self._extract_data(soup=soup, _single_dict=True)
                                    except:
                                        _single_dict = None
                                    main_dict = _single_dict

                        except TimeoutException:
                            self.driver.quit()
                            self.snacks(type="button", duration=999,
                                        message=f"Timeout. Page is taking more than {page_load_time} seconds to load")

                        finally:
                            self.driver.quit()
                            return main_dict


            elif self.instances.ids.mozilla_firefox_id.active:
                self.driver = _init_browser(driver_executable="firefox")
            elif self.instances.ids.ie_id.active:
                self.driver = _init_browser(driver_executable="ie")
            else:
                self.snacks("simple", "Please Choose a Browser")
                return None

        def _process_write_data(raw_data):
            """

            :param raw_data:
            :return:
            """
            # print(raw_data)


            if raw_data is not None:
                self._execute_parameter(param="link", raw_data=raw_data)
                self._execute_parameter(param="string", raw_data=raw_data)
                self._execute_parameter(param="email", raw_data=raw_data)
                # upgrade progress bar

                # show modal
                @mainthread
                def show_modal(raw_data):
                    content = self.add_table(table_content=raw_data)
                    modal = self.add_modal_dialog(dialog_title="Scrapped Data",
                                              title_align="center",
                                              size_hint_x=0.8, size_hint_y=0.8,
                                              content=content, content_table=True, buttons=None, title_colors=True,
                                              button_anchor_x="center")

                    modal.add_action_button("Export CSV", action=lambda *x: modal.dismiss(export_csv(raw_data)))
                    modal.add_action_button("Export Xlsl", action=lambda *x: modal.dismiss(export_xlsl()))
                    modal.add_action_button("Cancel", action=lambda *x: modal.dismiss(cancel()))
                    modal.open()

                show_modal(raw_data)

                # send a notification
                # email_body = f"scrapping done in {self.instances.ids.link_to_scrap_id.text}" \
                #              f"at {curr}"
                # utils.send_a_mail(email_subject=f"Scrapping Done at {curr}",
                #                   email_body=email_body,login_pass="chr0niclesOFana&ash")

        wait_time = round(self.instances.ids.action_time_id.value, 1)

        # progress
        # self.scrapping_progress = self.pop.pop_progress(title="Scrapping In Progress", text="",
        #                       max_value=100, cancel_callback=self.on_progress_cancel)

        # self.pop.test(self.scrapping_progress, "[Phase 1/3] Initializing...",
        #                          self._calculate_phase(5, 10))


        raw_data = collect(wait_time)
        _process_write_data(raw_data)

    def import_csv(self):
        # callback
        def _import_callback(instance):
            if instance.is_canceled():
                return
            s = 'Path: %s' % instance.path
            if instance.__class__.__name__ == 'XFileSave':
                s += ('\nFilename: %s\nFull name: %s' %
                      (instance.filename, instance.get_full_name()))
            else:
                s += ('\nSelection: %s' % instance.selection)

            self.instances.ids.import_csv_file_path_id.text = instance.selection[0]

        self.show_pop_fileopen(on_dismiss_callback=_import_callback)

        # Clock.schedule_once(lambda dt: self.update_progress(progress_text="initializing....", pn_delta=0), .1)

    @utils.threaded(thread_name="check button thread")
    def check_field_button(self, instance, scrap_field_instance):
        """
         button callback of check_field_btn from scrap_field
        :param instance: button instance default
        :param scrap_field_instance: a scrap field instance which this buttons belongs to
        :return:
        """

        # Internal buttons callback from modal
        def valid_confirm():
            instance.disabled = False

        def not_yet():
            instance.disabled = False

        # grab the link
        link = self._collect_link(enclose=False)
        if link is not None:
            # disable the button
            instance.disabled = True
            # download the page source # make beautiful soup
            soup = self._make_soup(url=link, user_agent="Vault", retries=2)
            if soup is None:
                self.snacks("simple", "Internet Connectivity disrupts")
                instance.disabled = False
            else:
                # gather criteria from tag selector field
                if utils.is_empty(scrap_field_instance.field_name.text):
                    dialog = "Check"
                else:
                    dialog = scrap_field_instance.field_name.text + " check"
                # extract data
                extracted_checked_data = self._extract_data(check_scrap_filed=True,
                                                            soup=soup,
                                                            scrap_field_instance=scrap_field_instance)
                # open modal
                @mainthread
                def show_modal(extracted_checked_data):
                    content = self.add_md_label(text=extracted_checked_data, auto_size=True)
                    modal = self.add_modal_dialog(dialog_title=dialog,
                                              title_align="center",
                                              size_hint_x=0.6, size_hint_y=None,
                                              height=200,
                                              content=content, buttons=None,
                                              button_anchor_x="center")

                    modal.add_action_button("Confirm", action=lambda *x: modal.dismiss(valid_confirm()))
                    modal.add_action_button("Not Yet", action=lambda *x: modal.dismiss(not_yet()))
                    modal.open()

                show_modal(extracted_checked_data)

        else:
            self.snacks("simple", "Please provide a link first")





    def on_complete_progress(self):
        self.instances.ids.view_data_btn_id.disabled = False
        self.instances.ids.start_scrapping_btn_id.disabled = False
        self.snacks.snacks("simple", "Scrapping finished in 2.0s")
        print("Completed")

    def on_progress_cancel(self, instance):
        self.instances.ids.start_scrapping_btn_id.disabled = False
        if self.driver is not None:
            self.driver.quit()
        self.snacks("simple", "Scrapping Canceled")

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


class MinerUtilityTabDrivers(DriverBase):
    def __init__(self, instances, **kwargs):
        super(MinerUtilityTabDrivers, self).__init__(**kwargs)
        self.instances = instances

    @utils.threaded(thread_name="email check thread")
    def email_check(self, email):
        def _on_dismiss_callback():
            self.instances.ids.check_email_btn_id.disabled = False

        # Simple Regex for syntax checking
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        if email != str:
            email_address = str(email)
        else:
            email_address = email

        # Syntax check
        match = re.match(regex, email_address)
        if match == None:
            self.snacks("simple", "Please Provide an Email address")
        else:
            self.instances.ids.check_email_btn_id.disabled = True
            _get = utils.email_check(email)
            if _get:
                content = self.add_md_label(font_style="Body1",
                                            text="Looks like the Email is valid",
                                            halign="center")
                self.show_pop_modal(size_hint_x=0.5, size_hint_y=None,
                                    height=200, title_align="center", title_colors=True,
                                    dialog_title="Email Found", content=content,
                                    dismiss_callback=_on_dismiss_callback)
            else:
                content = self.add_md_label(font_style="Body1",
                                            text="Oops the Email seems fake",
                                            halign="center")
                self.show_pop_modal(size_hint_x=0.5, size_hint_y=None,
                                    height=200, title_align="center", title_colors=True,
                                    dialog_title="Email Not Found", content=content,
                                    dismiss_callback=_on_dismiss_callback)

    @utils.threaded(thread_name="website check thread")
    def website_check(self, website):
        def _on_dismiss_callback():
            pass
        web_framwork_dict = parse(website)

        # TODO: implement modal to organize and show data
        data = {'web-servers': ['gunicorn'], 'programming-languages': ['Python'], 'font-scripts': ['Font Awesome'], 'widgets': ['OWL Carousel'], 'javascript-frameworks': ['jQuery'], 'photo-galleries': ['jQuery', 'OWL Carousel'], 'web-frameworks': ['Twitter Bootstrap']}
        # {"Service Name": [], "Service Type": []}


        # raw_data = construct_table_dict(web_framwork_dict)
        # show modal
        @mainthread
        def show_modal(raw_data):
            content = self.add_table(table_content=raw_data)
            modal = self.add_modal_dialog(dialog_title="Web framework Data",
                                          title_align="center",
                                          size_hint_x=0.8, size_hint_y=0.8,
                                          content=content, content_table=True, buttons=None, title_colors=True,
                                          button_anchor_x="center")

            modal.add_action_button("Okay", action=lambda *x: modal.dismiss())
            modal.open()

        # show_modal(raw_data)

    @utils.threaded(thread_name="whois check thread")
    def whois_check(self, website):
        def modal_btn_callback():
            pass

        whois_object = None
        try:
            whois_object = whois(website)
        except: # check for time out
            pass
        # wait for grabbing all

        # make fill column and rows with who is object keys and value
        if whois_object is not None:
            # add a gridlayout as content
            grid = self.add_grid_layout()
            # organize content
            grid.cols = len(whois_object)

            # for key, value in whois_object.items():
            #     make lbl
            #  assign them on col and rows

            # init md dialog with button ok size 8 by 8 (clear)
            self.show_pop_modal(size_hint_x=.7, size_hint_y=.7,
                                title_colors=True, title_align="center", dialog_title="WHOIS",
                                content=grid)
        # add gridlayout content into scrolview of md dialog
        print(whois_object)