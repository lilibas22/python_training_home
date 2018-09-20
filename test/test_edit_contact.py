from model.edit_contact import EditContact
from model.contact import Contact


def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.new_contact(Contact(firstname="Brad", middlename="BP", lastname="Pitt", nickname="Braddy", photo="C:\\12.jpg", title="Junior", company="21 Fox", address="Hollywood", homenumber="123456789",
                         mobile="987654321", worknumber="678901234", fax="123123123", website="www.pitt.com", email="test1@test.com", byear="1989", ayear="1900",
                         address2="Miami", phone2="785269555", notes="Notes here"))
    app.contact.edit_contact(EditContact(firstname="Brad2", middlename="BP2", lastname="Pitt2", nickname="Braddy2", photo="C:\\20.jpg",
                title="Junior2", company="21 Fox2", address="Hollywood2", homenumber="1234567892",
                mobile="9876543212", worknumber="678901234", fax="123123123", website="www.pitt2.com",
                email="test2@test.com", byear="1989", ayear="1900",
                address2="Miami2", phone2="785269552", notes="Notes here2"))
