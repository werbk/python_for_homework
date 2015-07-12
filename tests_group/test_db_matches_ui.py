from tests_group.group_helper import Group


def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, group_name=group.group_name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.if_or_max) == sorted(db_list, key=Group.if_or_max)