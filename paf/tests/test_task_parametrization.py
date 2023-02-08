"""
Есть в приложении поле ввода. Хотим его протестировать на 3-ёх версиях браузера (для этого используем структуры ниже).
Реализовать передачу в тест инстанс браузера, его названия, тестовые параметры используя параметризацию и
фикстуры значений.
Сам тест выводит на консоль значения: текущее значение, ожидаемое сообщение.
Должно получиться 18 тестов. Тесты должны быть проиндексированы.
"""
import os

import pytest

# -------------------------
# Initial task requirements
# -------------------------


class Browser:
    @staticmethod
    def set_int(int_value):
        print(int_value)


class Browser1(Browser):
    def __init__(self):
        self.name = 'explovet'


class Browser2(Browser):
    def __init__(self):
        self.name = 'firefox'


class Browser3(Browser):
    def __init__(self):
        self.name = 'chrome'


browsers_dict = {
    'browser1': Browser1,
    'browser2': Browser2,
    'browser3': Browser3
}

tests_values = {
    'ok':  # ожидаемое сообщение
        [1, 2, 3],  # значения, при которых получаем сообщение “ok”
    'not ok':  # ожидаемое сообщение
        ['bad1', 'bad2', 'bad3']  # значения, при которых получаем сообщение “not ok”
}


# ---------------
# Browser fixture
# ---------------

@pytest.fixture(params=browsers_dict.values(), ids=browsers_dict.keys())
def browser(request):
    return request.param


# ------------------------------------------------------------------------------------------------
# Test function printing the detailed test output to the console using all available functionality
# ------------------------------------------------------------------------------------------------

def print_output(browser, message, value, index=None):
    if index is None:
        print()
    else:
        print('\nTest: ' + str(index))
    print('Browser: ' + browser().name)
    print('Value: ', end='')
    browser.set_int(value)
    print('Message: ' + message)


# ------------------------------------------------------------------------
# Additional test function returning a couple of corresponding test values
# ------------------------------------------------------------------------

def value_for_test():
    for i in zip(tests_values.keys(), tests_values.values()):
        for j in range(len(i[1])):
            yield i[0], i[1][j]


# -------------------------------------------------------------------------------------------------------
# Additional test function returning a browser, a couple of corresponding test values and the test number
# -------------------------------------------------------------------------------------------------------

def value_and_browser_for_test():
    index = 0
    for browser in browsers_dict.values():
        for value in zip(tests_values.keys(), tests_values.values()):
            for i in range(len(value[1])):
                index += 1
                yield value[0], value[1][i], browser, index


# ------------------------------------------
# Test input using fixture + parametrization
# ------------------------------------------

@pytest.mark.parametrize("message, value", value_for_test(),
                         ids=[f"Test message '{i[0]}' for value '{i[1]}'" for i in value_for_test()])
def test_input1(browser, message, value):
    print_output(browser, message, value)


# ---------------------------------------
# Test input using double parametrization
# ---------------------------------------

@pytest.mark.parametrize("message, value", value_for_test(),
                         ids=[f"Test message '{i[0]}' for value '{i[1]}'" for i in value_for_test()])
@pytest.mark.parametrize("browser", [i for i in browsers_dict.values()],
                         ids=[f"{i[0]}" for i in zip(browsers_dict.keys(), browsers_dict.values())])
def test_input2(browser, message, value, request):
    print_output(browser, message, value)
    # print(request.node.callspec.id)
    # print(os.environ.get('PYTEST_CURRENT_TEST'))


# -------------------------------------------------------------------------
# Test input using simple parametrization with more elaborate test function
# -------------------------------------------------------------------------

@pytest.mark.parametrize("message, value, browser, index", value_and_browser_for_test(),
                         ids=[f"Test {i[3]}: browser '{i[2]().name}', message '{i[0]}' for value '{i[1]}'"
                              for i in value_and_browser_for_test()]
                         )
def test_input3(browser, message, value, index):
    print_output(browser, message, value, index)


# ----------------------------------------------------------------------------
# Test input using fixture + parametrization without additional test functions
# ----------------------------------------------------------------------------

@pytest.mark.parametrize("message, value", [(i[0], i[1][j])
                                            for i in zip(tests_values.keys(), tests_values.values())
                                            for j in range(len(i[1]))],
                         ids=[f"Test message '{i[0]}' for value '{i[1][j]}'"
                              for i in zip(tests_values.keys(), tests_values.values())
                              for j in range(len(i[1]))]
                         )
def test_input4(browser, message, value):
    print_output(browser, message, value)


# --------------------------------------------------------------------------------------------------
# Test input using fixture + parametrization without additional test functions, more elegant version
# --------------------------------------------------------------------------------------------------

@pytest.mark.parametrize("message, value", [(i, j)
                                            for i in tests_values.keys()
                                            for j in tests_values[i]],
                         ids=[f"Test message '{i}' for value '{j}'"
                              for i in tests_values.keys()
                              for j in tests_values[i]]
                         )
def test_input5(browser, message, value):
    print_output(browser, message, value)
