# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from contact import Contact

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class Python_add_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def adding_new_contact(self, wd, contact):
        # adding new contact and its info
        wd.find_element_by_link_text("add new").click()
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("photo").send_keys(contact.photo)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phonenumber)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_number)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_number)
        wd.find_element_by_name("fax").click()
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email1)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.website)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[24]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[24]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[8]").click()
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.Byear)
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]//option[21]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]//option[11]").click()
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.secondary_address)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.secondary_phone)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.secondary_notes)

    def Submit_new_contact(self, wd):
        # submitting new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def add_new_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.adding_new_contact(wd, Contact(firstname="Brad", middlename="BP", lastname="Pitt", nickname="Braddy", photo="'C:\\12.jpg'", title="Junior", company="21 Fox", address="Hollywood",
                                home_phonenumber="123456789", mobile_number="987654321", work_number="678901234", fax_number="123123123", email1="test1@test.com", email2="test2@test.com",
                                email3="test3@test.com", website="www.pitt.com", Byear="1989", ayear="2012", secondary_address="Miami", secondary_phone="Secondary Home",
                                secondary_notes="Just Notes"))
        self.Submit_new_contact(wd)
        self.logout(wd)

    def add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.adding_new_contact(wd, Contact("Angelina", "AJ", "Jolie", "Braddy", "'C:\\12.jpg'", "Junior", "21 Fox", "Hollywood",
                                "123456789", "987654321", "678901234", "123123123", "test1@test.com", "test2@test.com",
                                "test3@test.com", "www.pitt.com", "1989", "2012", "Miami", "Secondary Home",
                                "Just Notes"))

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()

