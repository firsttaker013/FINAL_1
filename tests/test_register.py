import requests

from page.register import (
    Register,
    name_page,
    name_form_path,
    email_form_path,
    button_class,
    password_repeat_path,
    warning_form_password_lenght,
    warning_form_password_number,
    password_form_path,
    warning_form_password_sybmol,
    warning_form_path,
    warning_form_not_password
)

test_name = 'Test_name'
test_email = 'Test_email@gmail.ru'
test_password = 'Password1!'

def test_status_code():
    '''Проверка ответа сервера == 200'''
    response = requests.get('https://startupium.ru/create-account')
    assert response.status_code == 200, f'Ошибка получен статус: {response.status_code}'


def test_open_site(browser):
        '''Поиск элемента "Создание аккаунта"'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(name_page)
        element_text = register_page.find(name_page)
        assert element_text == 'Создание аккаунта', 'Текст на странице не соответствует'


def test_form_name(browser):
        '''Проверка наличия поля ввода имени'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(name_form_path)
        element_name = register_page.find(name_form_path)
        assert element_name.get_attribute('placeholder') == 'Введите имя', 'Поле ввода имени отсутствует'


def test_form_email(browser):
        '''Проверка наличия поля ввода email'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(email_form_path)
        element_email = register_page.find(email_form_path)
        assert element_email.get_attribute('placeholder') == 'Введите email', 'Поле ввода email отсутствует'


def test_form_password(browser):
        '''Проверка наличия поля ввода пароля'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        assert element_password.get_attribute('placeholder') == 'Придумайте пароль', 'Поле ввода пароля отсутствует'


def test_form_repeat_password(browser):
        '''Проверка налчия поля повторного ввода пароля'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_repeat_path)
        element_password = register_page.find(password_repeat_path)
        assert element_password.get_attribute('placeholder') == 'Повторите пароль', 'Поле повтора пароля отсутствует'


def test_search_button(browser):
        '''Проверка наличия кнопки подтверждения регистрации'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(button_class)
        button = register_page.find(button_class)
        assert button is not None, 'Кнопка подтверждения регистрации отсутствует'

def test_all_form_not_name(browser):
        '''Проверка незаполненного поля имени'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(email_form_path)
        element_email = register_page.find(email_form_path)
        element_email.send_keys(test_email)
        register_page.wait_element(password_form_path)
        password_element = register_page.find(password_form_path)
        password_element.send_keys(test_password)
        register_page.wait_element(password_repeat_path)
        password_rep_element = register_page.find(password_repeat_path)
        password_rep_element.send_keys(test_password)
        button = register_page.find(button_class)
        button.click()
        register_page.wait_element(warning_form_path)
        message_error = register_page.find(warning_form_path)
        assert message_error is not None, 'Сообщение о незаполненном поле имени не появилось'


def test_all_form_not_email(browser):
    '''Проверка незаполненного поля email'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    element_name.send_keys(test_name)
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    password_element.send_keys(test_password)
    register_page.wait_element(password_repeat_path)
    password_rep_element = register_page.find(password_repeat_path)
    password_rep_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном поле email не появилось'

def test_all_form_not_password(browser):
    '''Проверка незаполненного поля пароля'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    email_element.send_keys(test_email)
    register_page.wait_element(password_repeat_path)
    password_rep_element = register_page.find(password_repeat_path)
    password_rep_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном поле пароля не появилось'

def test_all_form_not_password_repeat(browser):
    '''Проверка незаполненного поля пароля'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(name_form_path)
    element_name = register_page.find(name_form_path)
    element_name.send_keys(test_name)
    register_page.wait_element(email_form_path)
    email_element = register_page.find(email_form_path)
    email_element.send_keys(test_email)
    register_page.wait_element(password_form_path)
    password_element = register_page.find(password_form_path)
    password_element.send_keys(test_password)
    button = register_page.find(button_class)
    button.click()
    register_page.wait_element(warning_form_path)
    message_error = register_page.find(warning_form_path)
    assert message_error is not None, 'Сообщение о незаполненном повторном поле пароля не появилось'

def test_form_password_not_number(browser):
        '''Проверка появления уведомления об отсуствие цифр в пароле'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        element_password.send_keys('Test_password')
        register_page.wait_element(warning_form_password_number)
        form_elements = register_page.find(warning_form_password_number)
        assert form_elements is not None, 'Сообщение о не валидности пароля не появилось'


def test_form_password_not_upper_leng(browser):
    '''Проверка появления уведомления об отсуствие прописной буквы в пароле'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(password_form_path)
    element_password = register_page.find(password_form_path)
    element_password.send_keys('test_password1')
    register_page.wait_element(warning_form_password_lenght)
    form_elements = register_page.find(warning_form_password_lenght)
    assert form_elements is not None, 'Сообщение о не валидности пароля не появилось'

def test_form_password_not_symbol(browser):
    '''Проверка появления уведомления об отсуствие символа в пароле'''
    register_page = Register(browser)
    register_page.open()
    register_page.wait_element(password_form_path)
    element_password = register_page.find(password_form_path)
    element_password.send_keys('Testpassword1')
    register_page.wait_element(warning_form_password_sybmol)
    form_elements = register_page.find(warning_form_password_sybmol)
    assert form_elements is not None, 'Сообщение о не валидности пароля не появилось'

def test_password_mismatch(browser):
        '''Проверка появления уведомления об несовпадение пароля в поле повторного пароля'''
        register_page = Register(browser)
        register_page.open()
        register_page.wait_element(password_form_path)
        element_password = register_page.find(password_form_path)
        element_password.send_keys('Test_password1')
        register_page.wait_element(password_repeat_path)
        element_password_rep = register_page.find(password_repeat_path)
        element_password_rep.send_keys('Test_password2')
        register_page.wait_element(warning_form_not_password)
        form_elements = register_page.find(warning_form_not_password)
        assert form_elements is not None, 'Сообщение о не совпадение паролей'
