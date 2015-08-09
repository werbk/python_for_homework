from sys import maxsize


class Group:
    def __init__(self, group_name=None, group_header=None, group_footer=None, id=None):
        self.group_name = group_name
        self.group_header = group_header
        self.group_footer = group_footer
        self.id = id

    def __repr__(self):
        return '%s:%s:%s;%s' % (self.id, self.group_name, self.group_header, self.group_footer)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.group_name == other.group_name

    def if_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize


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
        self.group_cache = None

    def delete_first_group(self):
        self.delete_group_by_index(0)

    def click_group_page(self):
        wd = self.app.wd
        wd.find_element_by_css_selector("div.msgbox").click()
        wd.find_element_by_link_text("group page").click()

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:

            wd = self.app.wd
            self.open_group_page()
            self.group_cache = []
            for element in wd.find_elements_by_css_selector('span.group'):
                text = element.text
                id = element.find_element_by_name('selected[]').get_attribute('value')
                self.group_cache.append(Group(group_name=text, id=id))

        return list(self.group_cache)

    def select_group_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_group_by_index(self, index):
        wd = self.app.wd
        self.open_group_page()
        self.select_group_by_index(index)
        wd.find_element_by_name('delete').click()
        self.click_group_page()
        self.group_cache = None

    def edit_group_by_index(self, Group, index):
        wd = self.app.wd

        self.open_group_page()

        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_name("edit").click()

        self.group_line('group_name', Group.group_name)
        self.group_line('group_header', Group.group_header)
        self.group_line('group_footer', Group.group_footer)

        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("groups").click()
        self.group_cache = None


