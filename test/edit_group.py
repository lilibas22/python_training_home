from model.edit_group import EditGroup


def test_edit_first_group(app):

    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(EditGroup(name="group2", header="header2", footer="footer2"))
    app.session.logout()
