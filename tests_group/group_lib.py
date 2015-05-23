import unittest
from TestBase import BaseClass

class Group:
    def __init__(self, group_name, group_header, group_footer):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer


class GroupTestBase(BaseClass):

    def create_group(self, wd, Group):
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(Group.group_name)
        wd.find_element_by_name("group_header").click()
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(Group.group_header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(Group.group_footer)
        wd.find_element_by_name("submit").click()

    def delete_group(self):
        self.wd.find_element_by_link_text("groups").click()
        self.wd.find_element_by_css_selector("span.group").click()
        if not self.wd.find_element_by_name("selected[]").is_selected():
            self.wd.find_element_by_name("selected[]").click()
        self.wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()

    def click_group_page(self, wd):
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()