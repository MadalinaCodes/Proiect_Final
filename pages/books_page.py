from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class BooksPage(BasePage):
    # selectors
    LOGIN_BUTTON = '//button[@id="login"]'
    NUMBER_OF_BOOKS = '//div[@class="action-buttons"]'
    SEARCH_INPUT = '//input[@id="searchBox"]'
    BOOK_TITLE = '//div[@class="action-buttons"]//a'


    # actions
    def click_login_button(self):
        self.wait_for_elem(self.LOGIN_BUTTON)
        self.driver.find_element(By.XPATH, self.LOGIN_BUTTON).click()

    def fill_search_input(self, query):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.clear()
        search.send_keys(query)

    def clear_search_input(self):
        self.wait_for_elem(self.SEARCH_INPUT)
        search = self.driver.find_element(By.XPATH, self.SEARCH_INPUT)
        search.send_keys(Keys.CONTROL, 'a')
        search.send_keys(Keys.BACKSPACE)

 # validations
    def validate_correct_url(self):
        sleep(1)
        expected = 'https://demoqa.com/books'
        actual = self.driver.current_url
        self.assertEqual(expected, actual, 'Url is incorrect')

    def validate_books_count(self, expected_number): # parametrizam expected_number ca sa putem refolosi functia de cate ori dorim
        sleep(1)
        actual = len(self.driver.find_elements(By.XPATH, self.NUMBER_OF_BOOKS))
        self.assertEqual(expected_number, actual, 'Number of books is incorrect')

    def validate_book_title(self, expected_title):
        self.wait_for_elem(self.BOOK_TITLE)
        actual_title = self.driver.find_element(By.XPATH, self.BOOK_TITLE).text
        self.assertEqual(expected_title, actual_title, 'Book title is incorrect')

