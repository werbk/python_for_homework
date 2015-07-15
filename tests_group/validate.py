from tests_group.group_helper import Group


def validate_group_list(db, new_groups, old_groups, validate=False):
    ui_list = new_groups
    def clean(group):
        return Group(id=group.id, group_name=group.group_name.strip())

    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.if_or_max) == sorted(db_list, key=Group.if_or_max)

    if validate:
        assert sorted(old_groups, key=Group.if_or_max) == sorted(new_groups, key=Group.if_or_max), 'Group list is different'