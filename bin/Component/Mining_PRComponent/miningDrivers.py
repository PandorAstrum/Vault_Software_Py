# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import re
import time
from os.path import expanduser

from selenium import webdriver
from bs4 import BeautifulSoup
from Core.baseInterface import DriverBase
from bin.Component.Mining_PRComponent.reusable import _ScrapField
import utils
from Core.ErrorHandling import Snacks

from bin.libPackage.xpop import XFileOpen
from bin.libPackage.xpop.notification import XMessage, XError, XConfirmation, XProgress


class MiningHelpTabDrivers:
    pass


class MiningSeleniumTabDrivers(DriverBase):
    def __init__(self, instances, **kwargs):
        super(MiningSeleniumTabDrivers, self).__init__(**kwargs)
        self.instances = instances
        self.snacks = Snacks()
        self.scrap_field_box = self.instances.ids.scrap_field_box_id
        self.field_instance = []
        self._make()

    def _make(self):
        # first create a scrap field
        if len(self.scrap_field_box.children) < 1:
            scrap_field = _ScrapField(self, "0")
            self.scrap_field_box.add_widget(scrap_field)

    # Buttons Behave
    @utils.clocked()
    def add_new_field(self):
        num = str(len(self.scrap_field_box.children) + 1)
        self.scrap_field_box.add_widget(_ScrapField(self, num))

    @utils.threaded(thread_name="email check")
    def check_email(self, email):
        # Simple Regex for syntax checking
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        if email != str:
            email_address = str(email)
        else:
            email_address = email
        # Syntax check
        match = re.match(regex, email_address)
        if match == None:
            self._xpop("error", msg="Its not an email address!")
            # raise ValueError('Bad Syntax')
        else:
            self.instances.ids.email_check_btn_id.disabled = True
            _get = utils.email_check(email)
            if _get:
                self._xpop("msgbox", msg="Looks Like the Email address is valid", title="Email Found")
            else:
                self._xpop("msgbox", msg="It's a fake email address", title="Email not Found")

    @utils.threaded(thread_name="scrapping Thread")
    def start_scrapping(self):
        wait_time = round(self.instances.ids.time_id.value,1)
        driver = None
        # def _progress_test(self, pdt=None):
        #     if pop.is_canceled():
        #         return
        #
        #     pop.inc()
        #     pop.text = 'Progress... (%d / %d)' % \
        #                          (pop.value, pop.max)
        #     if pop.value < pop.max:
        #         Clock.schedule_once(_progress_test, .01)
        #     else:
        #         pop.complete()
        #
        # pop = XProgress(title='Scrapping In Progress',
        #           text='Progress...', max=100)
        # Clock.schedule_once(_progress_test, .1)
        # check browser settings
        if self.instances.ids.google_chrome_id.active:
            driver = webdriver.Chrome(executable_path=".\\dll\\chrome_drivers\\chromedriver.exe")
        elif self.instances.ids.mozilla_firefox_id.active:
            driver = webdriver.Firefox(executable_path=".\\dll\\firefox_drivers\\geckodriver.exe")
        elif self.instances.ids.ie_id.active:
            driver = webdriver.Ie(executable_path=".\\dll\explorer_drivers\\IEDriverServer.exe")
        else:
            self.snacks.snackbar("simple", "Please Choose a Browser")

        if not driver == None:
            self._collect_login(driver, wait_time)
            data = self._collect_link(driver, wait_time)
        #
            curr = utils.get_computer_date_time()
            utils.dict_to_csv(filename=f"{curr}_scrap.csv", dict_data=data)
        #
        # time.sleep(wait_time)
        # web_driver.quit()


    def _collect_login(self, web_driver, wait_time):
        if self.instances.ids.login_option_id.active:
            if self.instances.ids.linkedin_id.active:
                user_name = self.instances.ids.linkedin_username_id.text
                pass_word = self.instances.ids.linkedin_password_id.text
                web_driver.get("https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin")
                time.sleep(wait_time)
                web_driver.find_element_by_xpath('//*[@id="session_key-login"]').send_keys(user_name)
                web_driver.find_element_by_xpath('//*[@id="session_password-login"]').send_keys(pass_word)
                time.sleep(wait_time)
                web_driver.find_element_by_xpath('//*[@id="btn-primary"]').click()
                time.sleep(wait_time)
            elif self.instances.ids.custom_login_id.active:
                user_name = self.instances.ids.custom_username_id.text
                pass_word = self.instances.ids.custom_password_id.text
                url = self.instances.ids.sign_in_url_id.text
                web_driver.get(url)
                time.sleep(wait_time)
                u_xpath = self.instances.ids.custom_username_xpath_id.text
                p_xpath = self.instances.ids.custom_password_xpath_id.text
                web_driver.find_element_by_xpath(u_xpath).send_keys(user_name)
                web_driver.find_element_by_xpath(p_xpath).send_keys(pass_word)
                time.sleep(wait_time)
                login_btn_xpath = self.instances.ids.sing_in_btn_xpath_id.text
                web_driver.find_element_by_xpath(login_btn_xpath).click()
                time.sleep(wait_time)
        else:
            # no need of login
            pass

    def _collect_link(self, web_driver, wait_time):
        data = None
        temp = None
        if self.instances.ids.single_link_id.active:
            link_to_scrap = self.instances.ids.link_to_scrap_id.text
            web_driver.get(link_to_scrap)
            time.sleep(wait_time)
            if self.instances.ids.next_page_id.active:
                xpath = self.instances.ids.next_page_xpath_id.text
                # loop to click next

                html_doc = web_driver.page_source
                soup = BeautifulSoup(html_doc, "lxml")
                temp = self._collect_data_per_page(soup)
                time.sleep(wait_time)
                web_driver.find_element_by_xpath(xpath).click()
                time.sleep(wait_time)

            elif self.instances.ids.continuous_id.active:
                xpath = self.instances.ids.anchor_tag_xpath_id.text
                # grab the xpath
                pass
            else:
                html_doc = web_driver.page_source
                soup = BeautifulSoup(html_doc, "lxml")
                data = self._collect_data_per_page(soup)

        else:
            # csv
            csv_file_path = self.instances.ids.import_csv_file_path_id.text

            pass
        # process data
        self._process_generic_parameter()
        return data


    def _xpop(self, sid, msg=None, title=None):
        if sid == 'msgbox':
            XMessage(text=msg, title=title, on_dismiss=self._xmsg_callback)
        elif sid == 'error':
            XError(text=msg)
        elif sid == 'confirm':
            XConfirmation(text='Do you see a confirmation?',
                          on_dismiss=self._confirmation_callback)
        elif sid == "fileOpen":
            XFileOpen(on_dismiss=self._filepopup_callback, path=expanduser(u'~'),
                      multiselect=False)

    def _filepopup_callback(self, instance):
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

            self.instances.ids.file_path_id.text = instance.selection[0]

    @staticmethod
    def _confirmation_callback(instance):
        if instance.is_canceled():
            return

    def _xmsg_callback(self, instance):
        self.instances.ids.email_check_btn_id.disabled = False



    def import_csv(self):
        self._xpop("fileOpen")









    def _process_generic_parameter(self):
        pass


    def _check_selector_parameter(self, tag_selector):
        if tag_selector.cls_selector_chk.active:
            return "cls"
        elif tag_selector.id_selector_chk.active:
            return "id"
        elif tag_selector.str_selector_chk.active:
            return "str"
        else:
            return "default"

    def _check_field_value(self, scrap_field ,data):
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
        else:
            for d in data:
                temp.append(d)
            pass
        return temp


    def _soup_find(self, soup, find_all=False, tag_field = None,
                   selector_text=None, selector_parameter="default"):
        if find_all:
            if selector_text == None:
                return soup.find_all(tag_field)
            else:
                if selector_parameter == "cls":
                    return soup.find_all(tag_field, {"class":selector_text})
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

    def _check_selector_text(self, tag_selector):
        if not utils.is_empty(tag_selector.selector_field.text):
            return tag_selector.selector_field.text
        else:
            return None

    def _get_items(self, soup, pre_content, item):
        tmp = []
        selector_text = self._check_selector_text(item)
        print(selector_text)
        if not utils.is_empty(pre_content):
            for p in pre_content:
                if item.find_chk.active:
                    tmp = self._soup_find(p, find_all=True,
                                          tag_field=item.tag_field.text,
                                          selector_text=selector_text,
                                          selector_parameter=self._check_selector_parameter(item))

                else:
                    tmp.append(self._soup_find(p, tag_field=item.tag_field.text,
                                               selector_text=selector_text,
                                               selector_parameter=self._check_selector_parameter(item)))

            return tmp

        else:
            if item.find_chk.active:
                tmp = self._soup_find(soup, find_all=True,
                                      tag_field=item.tag_field.text,
                                      selector_text=selector_text,
                                      selector_parameter=self._check_selector_parameter(item))
                return tmp
            else:
                tmp.append(self._soup_find(soup, tag_field=item.tag_field.text,
                                           selector_text=selector_text,
                                           selector_parameter=self._check_selector_parameter(item)))
                return tmp

    def _collect_data_per_page(self, soup):
        # return a dictonary of tag_field.text : content
        dict = {}
        for scrap_field in self.instances.ids.scrap_field_box_id.children:
            # determine tag_selector len
            total_tag_selector = len(scrap_field.tag_selector_list)
            starting_number = 0
            temp_data_holder = []
            pre_content = None
            tmp = []
            while total_tag_selector > 1:
                # get the first list item
                item = scrap_field.tag_selector_list[starting_number]
                if not utils.is_empty(item.tag_field.text):
                    pre_content = self._get_items(soup, pre_content, item)
                else:
                    # error
                    pass
                total_tag_selector -= 1
                starting_number += 1

            last_item = scrap_field.tag_selector_list[starting_number]
            if not utils.is_empty(last_item.tag_field.text):
                pre_content = self._get_items(soup, pre_content, last_item)
            # write to dict
            dict[scrap_field.field_name.text] = self._check_field_value(scrap_field, pre_content)
        return dict

    def _collect_parameter(self):
        pass





class MiningScrapyTabDrivers(DriverBase):
    pass


from utils.appDirs import get_current_directory

print(get_current_directory())