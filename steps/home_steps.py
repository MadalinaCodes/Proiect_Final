from pages.home_page import HomePage
from behave import *  # * import tot

# Gerkin Syntax are urmatoarele cuvinte cheie
# given - seteaza situatia initiala
# when - actiunile intermediare
# then - verificarea finala
'''BDD foloseste sintaxa Gherkin ca sa uniformizeze comunicarea tuturor membrilor din echipa. 
Acesta este scopul principal al BDD.
(cu sintaxa Gherkin vom putea scrie testele in limba engleza)
 
Cu given, when, then putem ne facem testcase-urile. 
'''
# Un exemplu de testcase ar fi:
''''
Given I am a user on home page 
When I click bookstore application card
When I click login button
When I login with valid credentials
Then I should land on books page
'''
'''Noi primim aceste scenarii fie de la echipa de business, fie de la echipa de manual testing 
si le automatizam si la final generam niste rapoarte in html.
Rapoartele au rolul de leave-in documentation in BDD.
Acestea sunt mari avantaje pentru care ai vrea sa alegi BDD cu POM si Sintaxa Gerkin'''

home_page = HomePage()
@given('home: I am a user on home page')
def step_impl(context):
    home_page.driver.delete_all_cookies()
    home_page.navigate_to_home_page()

@when('home: I click bookstore application card')
def step_impl(context):
    home_page.click_book_store_application_card()

    