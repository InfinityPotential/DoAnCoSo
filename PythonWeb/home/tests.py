from django.test import TestCase, SimpleTestCase

# Create your tests here.
class SimpleTest(SimpleTestCase):
    def test_home_page_status(self):
        respone = self.client.get('/')
        self.assertEquals(respone.status_code, 404)