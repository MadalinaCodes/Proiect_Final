# from time import sleep
# from behave import *
# from pages.buttons_page import ButtonsPage
#
# buttons_page = ButtonsPage()
#
#
# # first button
# @when('buttons: I double click the first button')
# def step_impl(context):
#     buttons_page.double_click_first_button()
#     sleep(1)
#
# @then('buttons: I validate that first message is displayed')
# def step_impl(context, first_message):
#     buttons_page.validate_first_button_message(first_message)
#
# # second button
# @when('buttons: I right click the second button')
# def step_impl(context):
#     buttons_page.right_click_second_button()
#     sleep(1)
#
# @then('buttons: I validate that second message is displayed')
# def step_impl(context):
#     buttons_page.validate_second_button_message()
#
# # third button
# @when('buttons: I right click the second button')
# def step_impl(context):
#     buttons_page.dynamic_click_third_button()
#     sleep(1)
#
# @then('buttons: I validate that third is displayed')
# def step_impl(context):
#     buttons_page.validate_third_button_message()