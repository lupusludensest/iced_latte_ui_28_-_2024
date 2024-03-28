from pages.all_locators_bdd import *
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string

class MainPage(Page):

    # test_sendsafely_pytested_blue_top_1
    # Click button "Accept" cookies
    def accpt_ccks_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(ACPT_CCKS_BTN)).click()
    # End of the above code
    # End of the above code

    # 4 Verify "https://www.sendsafely.com/auth/#signup" is open
    def vtf_sgn_p_url_pn(self):
        self.driver.find_element(*GT_STRTD_BTN)
        if self.driver.current_url == 'https://www.sendsafely.com/auth/#signup':
            print(f'\nhttps://www.sendsafely.com/auth/#signup is here')
        else:
            print(f'\nhttps://www.sendsafely.com/auth/#signup is not here')
        self.driver.back()
    # End of the above code
