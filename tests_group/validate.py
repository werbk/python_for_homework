from tests_group.group_helper import Group


def validate_group_list(app, new_groups, old_groups, check_ui):

    def clean(group):
        return Group(id=group.id, group_name=group.group_name.strip())

    #db_list = map(clean, new_groups)
    assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max)

    if check_ui:
        db_list = map(clean, new_groups)
        assert sorted(db_list, key=Group.if_or_max) == sorted(app.group.get_group_list(), key=Group.if_or_max), 'Group list is different'