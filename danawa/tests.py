from django.test import TestCase
from .services.danawa_separator import DanawaSeparator
# Create your tests here.
class DanawaSeparatorTest(TestCase):
    def test_get_model_name(self):
        ds = DanawaSeparator(dict())
        self.assertIsNotNone(ds.get_model_name())
        print(ds.get_model_name())
