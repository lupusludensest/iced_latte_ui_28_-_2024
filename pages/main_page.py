from pages.all_locators_bdd import *
from credentials import *
from pages.base_page import Page
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import random
import string

class MainPage(Page):

    # iced_latte_ui_register_new_user_1
    # 1 Click user authorization icon
    def clck_usr_authrztn_icn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(USER_AUTH_ICON)).click()

    # 2 Click user registration button
    def clck_usr_rgstrtn_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(REGISTER_BTN)).click()

    # 3 Send first name to first name field
    def snd_frst_nm_to_fld(self):
        first_name_field = self.driver.find_element(*FRST_NM_FLD)
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    # 4 Send last name to last name field
    def snd_lst_nm_to_fld(self):
        last_name_field = self.driver.find_element(*LST_NM_FLD)
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    # 5 Send email to email field
    def snd_eml_to_fld(self):
        email_field = self.driver.find_element(*EML_FLD)
        email_field.clear()
        email_field.send_keys(email_valid)

    # 6 Send password to password field
    def snd_pswrd_to_fld(self):
        password_field = self.driver.find_element(*PSWRD_FLD)
        password_field.clear()
        password_field.send_keys(password_valid)

    # 7 Click user register user button
    def clck_usr_rgstr_usr_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(REGISTER_USER_BTN)).click()

    # End of the above code

    # iced_latte_ui_registered_user_logged_in_2
    # 1 Click user authorization icon
    # 2 Send registered email to email field
    def snd_rgstrd_eml_to_eml_fld(self):
        email_field = self.driver.find_element(*EML_FLD)
        email_field.clear()
        email_field.send_keys(email_valid)

    # 3 Send valid password to password field
    def snd_vald_pswrd_to_pswrd_fld(self):
        passwrd_field = self.driver.find_element(*PSWRD_FLD)
        passwrd_field.clear()
        passwrd_field.send_keys(password_valid)

    # 4 Click login button
    def clck_lgn_btn(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.element_to_be_clickable(LGN_BTN)).click()

    # 5 Assert user is logged in
    def assrt_usr_is_lggd_in(self, expected_word_here):
        registered_user_logged_logo = self.driver.find_element(*REGISTERED_USR_LOGGED_LOGO)
        expected_text = expected_word_here
        actual_text = registered_user_logged_logo.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'
