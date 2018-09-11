from model.edit_contact import EditContact

def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_contact(EditContact(firstname="Brad2", middlename="BP2", lastname="Pitt2", nickname="Braddy2", photo="C:\\20.jpg",
                title="Junior2", company="21 Fox2", address="Hollywood2", homenumber="1234567892",
                mobile="9876543212", worknumber="678901234", fax="123123123", website="www.pitt2.com",
                email="test2@test.com", byear="1989", ayear="1900",
                address2="Miami2", phone2="785269552", notes="Notes here2"))
    app.session.logout()
