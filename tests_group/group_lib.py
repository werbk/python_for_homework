class Group:
    def __init__(self, group_name=None, group_header=None, group_footer=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer


class GroupBase:
    def __init__(self, app):
        self.app = app

    def group_line(self, Group):
        wd = self.app.wd
        if Group.group_name:
            wd.find_element_by_name("group_name").click()
            wd.find_element_by_name("group_name").clear()
            wd.find_element_by_name("group_name").send_keys(Group.group_name)
        if Group.group_header:
            wd.find_element_by_name("group_header").click()
            wd.find_element_by_name("group_header").clear()
            wd.find_element_by_name("group_header").send_keys(Group.group_header)
        if Group.group_footer:
            wd.find_element_by_name("group_footer").click()
            wd.find_element_by_name("group_footer").clear()
            wd.find_element_by_name("group_footer").send_keys(Group.group_footer)

    def create(self, Group):
        wd = self.app.wd
        wd.find_element_by_name("new").click()

        self.group_line(Group)

        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_css_selector("span.group").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()

    def click_group_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def edit_group(self, Group):
        wd = self.app.wd

        wd.find_element_by_link_text("groups").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()
        self.group_line(Group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()


