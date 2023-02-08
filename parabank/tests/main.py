if __name__ == "__main__":
    import pytest
    pytest_args = [
        'test_page_about.py',
        'test_page_contact.py',
        'test_page_home.py',
        'test_page_news.py',
    ]
    pytest.main(pytest_args)
