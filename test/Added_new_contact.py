# -*- coding: utf-8 -*-
from fixture.contact_application import Application
import pytest
from model.contact import Contact

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

    
def test_Added_new_contact(app):
    app.login(username="admin", password="secret")
    app.new_contact(Contact(firstname="Brad", middlename="BP", lastname="Pitt", nickname="Braddy", photo="C:\\12.jpg", title="Junior", company="21 Fox", address="Hollywood", homenumber="123456789",
                         mobile="987654321", worknumber="678901234", fax="123123123", website="www.pitt.com", email="test1@test.com", byear="1989", ayear="1900",
                         address2="Miami", phone2="785269555", notes="Notes here"))
    app.logout()
