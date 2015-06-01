class Group:
    def __init__(self, group_name=None, group_header=None, group_footer=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer


class GroupBase:
    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith('/group.php') and len(wd.find_elements_by_name('new')) > 0):
            wd.find_element_by_link_text("groups").click()

    def count(self):
        wd = self.app.wd
        self.open_group_page()
        return len(wd.find_elements_by_name("selected[]"))

    def validation_of_group_exist(self):
        if self.count() == 0:
            self.create(Group(group_name='test'))
            self.click_group_page()

    def group_line(self, field, text):
        wd = self.app.wd
        if text:
            wd.find_element_by_name(field).click()
            wd.find_element_by_name(field).clear()
            wd.find_element_by_name(field).send_keys(text)

    def create(self, Group):
        wd = self.app.wd

        self.open_group_page()
        wd.find_element_by_name("new").click()

        self.group_line('group_name', Group.group_name)
        self.group_line('group_header', Group.group_header)
        self.group_line('group_footer', Group.group_footer)

        wd.find_element_by_name("submit").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        wd.find_element_by_css_selector("span.group").click()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//div[@id='content']/form/input[5]").click()
        self.click_group_page()

    def click_group_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    def edit_group(self, Group):
        wd = self.app.wd

        self.open_group_page()
        if not wd.find_element_by_name("selected[]").is_selected():
            wd.find_element_by_name("selected[]").click()
        wd.find_element_by_name("edit").click()

        self.group_line('group_name', Group.group_name)
        self.group_line('group_header', Group.group_header)
        self.group_line('group_footer', Group.group_footer)

        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()


