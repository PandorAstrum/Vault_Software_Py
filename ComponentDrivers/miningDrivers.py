# -*- coding: utf-8 -*-
"""
__author__ = "Ashiquzzaman Khan"
__desc__ = "Main Exe file to Run"
"""
import re
import time

from kivymd.snackbar import Snackbar
from selenium import webdriver
from bs4 import BeautifulSoup
from Core.baseInterface import DriverBase, MiningField
import utils
from bin.libPackage.xpop.notification import XNotification, XMessage, XError, XConfirmation


class MiningHelpTabDrivers:
    pass


class MiningSeleniumTabDrivers(DriverBase):
    def __init__(self, instances, **kwargs):
        super(MiningSeleniumTabDrivers, self).__init__(**kwargs)
        self.instances = instances

    @staticmethod
    def _snackbar(snack_type, msg):
        """
        Creating snack bar type
        :param snack_type: str type
        :param msg: str message
        :return:
        """
        if snack_type == 'simple':
            Snackbar(text=msg).show()
        elif snack_type == 'button':
            Snackbar(text="This is a snackbar", button_text="with a button!", button_callback=lambda *args: 2).show()
        elif snack_type == 'verylong':
            Snackbar(text="This is a very very very very very very very long snackbar!").show()

    def _xpop(self, sid, msg, title=None):
        if sid == 'msgbox':
            XMessage(text=msg, title=title)
        elif sid == 'error':
            XError(text=msg)
        elif sid == 'confirm':
            XConfirmation(text='Do you see a confirmation?',
                          on_dismiss=self._confirmation_callback)

    @staticmethod
    def _confirmation_callback(instance):
        if instance.is_canceled():
            return


    def add_new_field(self):
        self.instances.ids.field_card_id.add_widget(MiningField())


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
            self._xpop("error", "Its not an email address!")
            # raise ValueError('Bad Syntax')
        else:
            _get = utils.email_check(email)
            if _get:
                self._xpop("msgbox", "Looks Like the Email address is valid", title="Email Found")
            else:
                self._xpop("msgbox", "It's a fake email address", title="Email not Found")

    def _collect_scrap_link(self):
        if self.instances.ids.single_link_id.active:
            # login check
            # self._collect_login(web_driver, wait_time)
            link_to_scrap = self.instances.ids.link_to_scrap_id.text
            # check multipage option tick
            # check continous page tick
            return link_to_scrap
        elif self.instances.ids.multi_link_id.active:
            return ""
        else:
            return ""



    @utils.threaded(thread_name="scrapping Thread")
    def start_scrapping(self):
        web_driver = None
        login_flag = False
        user_name = None
        password = None
        user_name_xpath = None
        password_xpath = None
        login_url = None
        sign_in_btn_xpath = None
        # link_to_scrap = self.instances.ids.link_to_scrap_id.text
        multipage_btn_xpath = None
        continuous_anchor_xpath = None
        wait_time = None
        link_to_scrap = None
        html_doc = None
        field_dict = {}
        # disable buttons
        # self.instances.ids.start_scrapping_btn_id.disabled = True
        # set timer
        wait_time = round(self.instances.ids.time_id.value,1)

        # check browser settings
        if self.instances.ids.google_chrome_id.active or self.instances.ids.mozilla_firefox_id.active or self.instances.ids.ie_id.active:
            # check scrap link
            if self.instances.ids.single_link_id.active or self.instances.ids.multi_link_id.active:
                # check fields

                # set drivers
                if self.instances.ids.google_chrome_id.active:
                    web_driver = webdriver.Chrome(executable_path="dll/chrome_drivers/chromedriver.exe")
                elif self.instances.ids.mozilla_firefox_id.active:
                    web_driver = webdriver.Firefox(executable_path="dll/firefox_drivers/geckodriver.exe")
                elif self.instances.ids.ie_id.active:
                    web_driver = webdriver.Ie(executable_path="dll/explorer_drivers/IEDriverServer.exe")

                # login collect if ticked
                if self.instances.ids.linkedin_id.active:
                    user_name = self.instances.ids.linkedin_username_id.text
                    password = self.instances.ids.linkedin_password_id.text
                    web_driver.get('https://www.linkedin.com/uas/login?session_redirect=&goback=&trk=hb_signin')
                    time.sleep(wait_time)
                    linkedin_username_xpath = web_driver.find_element_by_xpath('//*[@id="session_key-login"]')
                    linkedin_password_xpath = web_driver.find_element_by_xpath('//*[@id="session_password-login"]')
                    linkedin_username_xpath.send_keys(user_name)
                    linkedin_password_xpath.send_keys(password)
                    linkedin_signin_btn_xpath = web_driver.find_element_by_xpath('//*[@id="btn-primary"]')
                    time.sleep(wait_time)
                    linkedin_signin_btn_xpath.click()
                    time.sleep(wait_time)
                else:
                    user_name = self.instances.ids.custom_username_id.text
                    password = self.instances.ids.custom_password_id.text
                    # user_name_xpath =
                    # password_xpath =
                    # login_url =
                    # sign_in_btn_xpath =

                # collect fields
                for child in self.instances.ids.field_card_id.children:
                    name = child.children[0].children[2].text
                    xpath = child.children[0].children[1].text
                    field_dict[name] = xpath

                # scrap link collect
                if self.instances.ids.single_link_id.active:
                    link_to_scrap = self.instances.ids.link_to_scrap_id.text
                    web_driver.get(link_to_scrap)
                    time.sleep(wait_time)

                    if self.instances.ids.multipage_id.active:
                        pass
                    elif self.instances.ids.continuous_id.active:
                        pass

                    # html_doc = web_driver.page_source
                    # soup = BeautifulSoup(html_doc, "lxml")
                    # test_with_class = soup.find_all("p", class_ = "name")
                    # test_with_id = soup.find_all("p", {"id": "id_name"})
                    # test_with_string = soup.find_all("p", string = "str")
                    # # next siblings and previous option



                elif self.instances.ids.multi_link_id.active:
                    pass
            else:
                self._snackbar("simple", "No Scrap link given")
        else:
            self._snackbar("simple", "Select a Browser First")






        # collect fields

        # collect parameters
        # start scrapping
        # if login_flag == False:
        #     web_driver.get(link_to_scrap)
        #     html_doc = web_driver.page_source

        # put the data into temp csv
        # close the web_driver
        time.sleep(wait_time)
        # web_driver.quit()

    # web_driver = webdriver.Firefox(executable_path="")
    # web_driver = webdriver.Ie(executable_path="")


class MiningScrapyTabDrivers(DriverBase):
    pass

