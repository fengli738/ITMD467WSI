import unittest
import models
import views
class TestMethodFunc(unittest.TestCase):


    def test_views_login(self):
        views.login()

    def test_views_add(self):
        views.art_add()

    def test_views_register(self):
        views.register();
    def test_change_filename(self):
        views.change_filename(name="abc")

    def test_art_update(self):
        views.art_update();

    def test_art_delete(self):
        views.art_delete();

    def test_art_list(self):
        views.art_list();
    def test_check_password(User):
        models.test_check_password(User, 123456)
