# from selenium.webdriver.common.by import By
# from selenium.webdriver import ActionChains
# from pages.base_page import BasePage
# from scripts.test_buttons import driver
# from time import sleep
#
# action = ActionChains(driver)
# action.context_click()
#
# class ButtonsPage(BasePage):
#     # selectors
#     ELEMENTS_BUTTON = '//*[text()="Elements"]'
#     BUTTONS_BUTTON = '//*[text()="Buttons"][1]'
#     DOUBLE_CLICK_ME_BUTTON = '//*[@id="doubleClickBtn"]'
#     RIGHT_CLICK_ME_BUTTON = '//*[@id="rightClickBtn"]'
#     CLICK_ME_BUTTON = '//*[text()="Click Me"]'
#     DOUBLE_CLICK_MESSAGE = '//*[@id="doubleClickMessage"]'
#     RIGHT_CLICK_MESSAGE = '//*[@id="rightClickMessage"]'
#     DYNAMIC_CLICK_MESSAGE = '//*[@id="dynamicClickMessage"]'
#
#
#     #actions
#     def click_elements_button(self):
#         self.wait_for_elem(self.ELEMENTS_BUTTON)
#         self.driver.find_element(By.XPATH, self. ELEMENTS_BUTTON).click()
#
#     def click_buttons_button(self):
#         self.wait_for_elem(self.BUTTONS_BUTTON)
#         self.driver.find_element(By.XPATH, self. BUTTONS_BUTTON).click()
#
#     def double_click_first_button(self):
#         self.wait_for_elem(self.DOUBLE_CLICK_ME_BUTTON)
#         double_click = self.driver.find_element(By.XPATH, self. DOUBLE_CLICK_ME_BUTTON)
#         action.double_click(double_click).perform()
#
#     def right_click_second_button(self):
#         self.wait_for_elem(self.RIGHT_CLICK_ME_BUTTON)
#         right_click = self.driver.find_element(By.XPATH, self.RIGHT_CLICK_ME_BUTTON)
#         action.context_click(right_click).perform()
#
#     def dynamic_click_third_button(self):
#         self.wait_for_elem(self.CLICK_ME_BUTTON)
#         right_click = self.driver.find_element(By.XPATH, self.CLICK_ME_BUTTON)
#         action.click(right_click).perform()
#
#     # validations
#     def validate_correct_url(self):
#         sleep(1)
#         expected = 'https://demoqa.com/buttons'
#         actual = self.driver.current_url
#         self.assertEqual(expected, actual, 'Url is incorrect')
#     def validate_first_button_message(self, expected_message):
#         sleep(1)
#         self.wait_for_elem(self.DOUBLE_CLICK_MESSAGE)
#         expected_message = 'You have done a double click'
#         actual = self.driver.current_url
#         self.assertEqual(expected_message, actual, 'You did not use the first button correctly, try double clicking.')
#
#     def validate_second_button_message(self):
#         sleep(1)
#         self.wait_for_elem(self.RIGHT_CLICK_MESSAGE)
#         expected_message = 'You have done a right click'
#         actual = self.driver.current_url
#         self.assertEqual(expected_message, actual, 'You did not use the second button correctly, try right clicking it.')
#
#     def validate_third_button_message(self):
#         sleep(1)
#         self.wait_for_elem(self.DYNAMIC_CLICK_MESSAGE)
#         expected_message = 'You have done a dynamic click'
#         actual = self.driver.current_url
#         self.assertEqual(expected_message, actual, 'You did not use the second button correctly, try right clicking it once.')
#
