from time import sleep

from browser import Browser
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest

# clasa BasePage mosteneste din Browser ca sa putem initializa in fiecare testcase si sa avem acces la browser peste tot
class BasePage(Browser, unittest.TestCase): # din libraria unittest importam clasa TestCase ca sa ne marcam toate testele ca niste testcase-uri si sa le putem raporta si sa avem acces tot din clasa asta si la niste seturi mai profesioniste

    def wait_for_elem(self, xpath_selector): # spre deosebire de sleep care opreste executia testului, tehnica de explicit wait cauta automat testul si in mom in care a gasit elementul trece mai departe, creste viteza testelor
        WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath_selector)))
        # metoda asta spune: vreau sa folosesc un WebDriverWait si timp de 5 secunde caut prezenta unui element in functie de un xpath si trec mai departe doar dupa ce am gasit acel element

    def browser_back(self):
        self.driver.back()

    def alert_ok(self):
        sleep(1)
        self.driver.switch_to.alert.accept()


