from django.test import TestCase
from .forms import ItemForm

# Create your tests here.

class TestItemForm(TestCase):

    def test_item_name(delf):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid)
        self.assertEqual(form.errors['name'][0], 'This field is required.')
    
    def test_done_field_is_not_required(self):
        form = ItemForm ({'name': 'test to do item'})
        self.assertTrue(form.is_vaid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = ItemForm()
        self.assertAlmostEqual(form.Meta.fiels, ['name' 'done'])
