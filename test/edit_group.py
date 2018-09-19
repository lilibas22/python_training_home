from model.edit_group import EditGroup


def test_edit_first_group(app):

    app.group.edit_first_group(EditGroup(name="group2", header="header2", footer="footer2"))
