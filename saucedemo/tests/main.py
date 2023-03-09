if __name__ == "__main__":
    import pytest
    pytest_args = [
        'test_user_login_allure.py',
        'test_header_and_footer_navigation_allure.py',
        'test_inventory_page_allure.py',
        'test_cart_page_allure.py',
        'test_checkout_pages_allure.py',
    ]
    pytest.main(pytest_args)

# if __name__ == "__main__":
#     import pytest
#     pytest_args = [
#         'test_user_login.py',
#         'test_header_and_footer_navigation.py',
#         'test_inventory_page.py',
#         'test_cart_page.py',
#         'test_checkout_pages.py',
#     ]
#     pytest.main(pytest_args)
