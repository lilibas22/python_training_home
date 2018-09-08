# -*- coding: utf-8 -*-
from model.contact import Contact

def test_Added_new_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.new_contact(Contact(firstname="Brad", middlename="BP", lastname="Pitt", nickname="Braddy", photo="C:\\12.jpg", title="Junior", company="21 Fox", address="Hollywood", homenumber="123456789",
                         mobile="987654321", worknumber="678901234", fax="123123123", website="www.pitt.com", email="test1@test.com", byear="1989", ayear="1900",
                         address2="Miami", phone2="785269555", notes="Notes here"))
    app.session.logout()
