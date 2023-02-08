from ...parabank.src.pages.main_pages.admin_page import AdminPage
import pytest

input_data_web = ["200", "50", "test", ""]
input_data_app = ["200", "50", "0", "-5"]
input_data_app_negative = ["test", "@#$%^", ""]
input_data_default = ["515.50", "100", "20"]


class TestPageAdmin:

    @pytest.fixture(scope="module")
    def admin_page(self, driver) -> AdminPage:
        page = AdminPage(driver)
        return page

    def test_click_database_initialize_button(self, admin_page):
        admin_page.database_initialize_button.click()
        assert admin_page.get_status_message() == "Database Initialized"

    def test_click_database_clean_button(self, admin_page):
        admin_page.database_clean_button.click()
        assert admin_page.get_status_message() == "Database Cleaned"

    def test_click_jms_service_button_start(self, admin_page):
        assert admin_page.get_jms_service_button_name() == "Startup"
        assert admin_page.get_jms_service_status_message() == "Stopped"
        admin_page.jms_service_button.click()
        assert admin_page.get_jms_service_button_name() == "Shutdown"
        assert admin_page.get_jms_service_status_message() == "Running"
        assert admin_page.get_status_message() == ""

    def test_click_jms_service_button_stop(self, admin_page):
        assert admin_page.get_jms_service_button_name() == "Shutdown"
        assert admin_page.get_jms_service_status_message() == "Running"
        admin_page.jms_service_button.click()
        assert admin_page.get_jms_service_button_name() == "Startup"
        assert admin_page.get_jms_service_status_message() == "Stopped"
        assert admin_page.get_status_message() == ""

    def test_radio_buttons(self, admin_page):
        admin_page.logger.logger.info("\nRadio buttons clicked:")
        for button in admin_page.radio_buttons:
            button.click()
            admin_page.logger.logger.info(admin_page.get_selected_radio_button())

    @pytest.mark.parametrize("data", input_data_web,
                             ids=[f"Test {i+1} with web service input '{input_data_web[i]}'"
                                  for i in range(len(input_data_web))]
                             )
    def test_web_services_inputs(self, admin_page, data):
        admin_page.input_web_form_data_simplified(data)
        admin_page.submit_button.click()
        assert admin_page.is_success()

    @pytest.mark.parametrize("data", input_data_app,
                             ids=[f"Positive test {i+1} with input '{input_data_app[i]}'"
                                  for i in range(len(input_data_app))]
                             )
    def test_application_settings_correct_inputs(self, admin_page, data):
        admin_page.input_app_form_data_simplified(data)
        admin_page.submit_button.click()
        assert admin_page.is_success()

    @pytest.mark.parametrize("data", input_data_app_negative,
                             ids=[f"Negative test {i+1} with input '{input_data_app_negative[i]}'"
                                  for i in range(len(input_data_app_negative))]
                             )
    def test_application_settings_incorrect_inputs(self, admin_page, data):
        admin_page.input_app_form_data_simplified(data)
        admin_page.submit_button.click()
        admin_page.print_admin_form_errors()
        assert not admin_page.is_success()

    def test_application_settings_input_back_to_default(self, admin_page):
        admin_page.input_app_form_data(*input_data_default)
        admin_page.submit_button.click()
        assert admin_page.is_success()

    def test_dropdowns_descriptions(self, admin_page):
        for dropdown in admin_page.dropdowns:
            admin_page.logger.logger.info("\nDropdown '{}':".format(dropdown.dropdown_id))
            for option in dropdown.get_dropdown_options():
                admin_page.logger.logger.info(option)

    def test_dropdowns_selections(self, admin_page):
        for i in range(len(admin_page.dropdowns)):
            dropdown = admin_page.dropdowns[i]
            values = dropdown.get_dropdown_options()
            admin_page.logger.logger.info("\nDropdown '{}':".format(dropdown.dropdown_id))
            for j in range(len(values)):
                admin_page.logger.logger.info("\nSelected value: {}".format(dropdown.get_selected()))
                admin_page.logger.logger.info("Select: {}".format(values[j]))
                dropdown.select(values[j])
                admin_page.submit_button.click()
                admin_page.logger.logger.info("Selected value: {}".format(dropdown.get_selected()))
                assert values[j] == dropdown.get_selected()
