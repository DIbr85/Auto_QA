import time

from pages.base_page import BasePage
from pages.elements_page import TextBoxPage


class TestElements:
    class TestTextBox:

        def test_text_box(self, driver):
            text_box_page = TextBoxPage(driver, 'https://demoqa.com/text-box/')
            text_box_page.open()
            full_name, email, current_address, permanent_address = text_box_page.fill_all_fields()
            output_name, output_email, output_cur_address, output_perm_address = text_box_page.check_filled_form()
            assert full_name == output_name, "the full_name dont much"
            assert email == output_email, "the email dont much"
            assert current_address == output_cur_address, "the current_address dont much"
            assert permanent_address == output_perm_address, "the permanent_address dont much"

            time.sleep(5)
