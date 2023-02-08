from ...parabank.src.pages.main_pages.services_page import ServicesPage


class TestPageServices:

    def test_service_tables_headings(self, driver):
        page = ServicesPage(driver)
        page.logger.logger.info("\nServices page tables' headings:")
        headings = page.get_service_tables_headings()
        for heading in headings:
            page.logger.logger.info(heading.strip(':'))
        assert len(headings) == 5
