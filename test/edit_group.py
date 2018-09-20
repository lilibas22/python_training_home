from model.edit_group import EditGroup
from model.group import Group


def test_edit_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test", header="header", footer="footer"))
    app.group.edit_first_group(EditGroup(name="group2", header="header2", footer="footer2"))
