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

    # 1_iced_latte_ui_register_new_user
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

    # 2_iced_latte_ui_registered_user_logged_in
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

    # End of the above code

    # 3_iced_latte_ui_registered_user_clicked_on_cart
    # 1 Click user authorization icon
    # 2 Send registered email to email field
    # 3 Send valid password to password field
    # 4 Click login button
    # 5 Click on cart icon
    def clck_on_cart_btn(self):
        self.driver.find_element(*CLCK_ON_CART_ICN).click()

    # 6 Assert shopping cart page is open
    # 6.1 Text "Shopping cart" is here
    def txt_spng_crt_here(self, txt_spng_crt_here):
        actual_txt_spng_crt_here = self.driver.find_element(*SHPNG_CRT_TXT)
        expected_text = txt_spng_crt_here
        actual_text = actual_txt_spng_crt_here.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 6.2 URL "https://iced-latte.uk/cart" is active
    def url_cart_here(self, url_cart_here):
        self.driver.get(url_cart_here)
        if self.driver.current_url == url_cart_here:
            print(f"The expected URL '{url_cart_here}' is open.")
        else:
            print(f"Unexpected URL opened: {self.driver.current_url}")

    # 6.3. Text "Your cart is empty" is displayed
    def yr_crt_is_empty_here(self, yr_crt_is_empty_here):
        actual_yr_crt_is_empty_here = self.driver.find_element(*YR_CRT_IS_EMPTY)
        expected_text = yr_crt_is_empty_here
        actual_text = actual_yr_crt_is_empty_here.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 6.4 Continue shopping button is here with text "Continue Shopping"'
    def cntnue_shpng_btn_is_hr(self, cntnue_shpng_btnn_wth_txt_hr):
        actual_cntnue_shpng_btnn_wth_txt_hr = self.driver.find_element(*CNTNUE_SHPNG_BTN)
        expected_text = cntnue_shpng_btnn_wth_txt_hr
        actual_text = actual_cntnue_shpng_btnn_wth_txt_hr.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # End of the above code

    # 4_iced_latte_ui_registered_user_continue_shop
    # 1 Click user authorization icon
    # 2 Send registered email to email field
    # 3 Send valid password to password field
    # 4 Click login button
    # 5 Click on cart icon

    # 6 Click on Continue Shopping button
    def clck_on_cntnue_shpng_btn(self):
        self.driver.find_element(*CNTNUE_SHPNG_BTN).click()

    # 7 Click on "plus" button, adding Turkish Coffee to the cart
    def clck_on_plus_btn(self):
        self.driver.find_element(*ADD_TRKSH_CFFE).click()

    # 8 Click on cart icon after adding
    def clck_on_cart_icon_after_adding_btn(self):
        self.driver.find_element(*CRT_BTN_AFTR_ADDING).click()

    # 9 Verify the coffee is in the cart
    # 9.1 Counter "1" is here
    def vrfy_coffee_is_in_the_cart_one_is_here(self, one_is_here):
        actual_vrfy_coffee_is_in_the_cart_one_is_here = self.driver.find_element(*CNTR_1_HERE)
        expected_text = one_is_here
        actual_text = actual_vrfy_coffee_is_in_the_cart_one_is_here.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.2 Text "Turkish Coffee" is in the page in cart
    def vrfy_turkish_coffe_is_in_the_cart(self, turkish_coffe_is_in_the_cart):
        actual_turkish_coffe_is_in_the_cart = self.driver.find_element(*TRKSH_CFF_IN_THE_CRT)
        expected_text = turkish_coffe_is_in_the_cart
        actual_text = actual_turkish_coffe_is_in_the_cart .text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.3 "500 g." is in the page in cart
    def vrfy_gramms_in_the_page(self, gramms_in_the_page):
        actual_gramms_in_the_page = self.driver.find_element(*FIVE_HNDRD_GRMS_TXT)
        expected_text = gramms_in_the_page
        actual_text = actual_gramms_in_the_page.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 9.4 Text "$4.49" is in the page in cart after purchase
    def total_dollars_in_cart(self, total_dollars_in_cart):
        actual_total_dollars_in_cart = self.driver.find_element(*FOUR_HUNDRED_FORTY_NINE_DLRS)
        expected_text = total_dollars_in_cart
        actual_text = actual_total_dollars_in_cart.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 10 Button "Go to checkout" is here
    def go_to_chck_out_btn(self, go_to_chck_out_btn):
        actuel_go_to_chck_out_btn = self.driver.find_element(*GO_TO_CHCK_OUT_BTN)
        expected_text = go_to_chck_out_btn
        actual_text = actuel_go_to_chck_out_btn.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # End of the above code

    # 5_iced_latte_ui_user_forgot_password
    # 1 Click user authorization icon
    # 2 Click on Forgot password button
    def clck_on_forgot_password_btn(self):
        self.driver.find_element(*FRGT_PSSWD).click()

    # 3 Send email to email field to reset password
    def send_email_to_email_field_to_reset_pswrd(self):
        first_name_field = self.driver.find_element(*ENTR_YR_EML_ADDRSS_FLD_RST_PSWD)
        first_name_field.clear()
        first_name_field.send_keys(email_valid)

    # 4 Click on Send reset link button
    def clck_on_rst_lnk_btn(self):
        self.driver.find_element(*SND_RST_LNK).click()

    # 5 Click on Continue to change your password button
    def clck_on_cntnue_to_chng_your_pswrd(self):
        self.driver.find_element(*CNTNUE_TO_CNHG_YR_PSWRD).click()

    # 6 Send code "861-539-280" from email to the field
    def send_fake_code_from_email_to_the_field(self, fake_code_from_email_to_the_field):
        code_from_email_field = self.driver.find_element(*CODE_FROM_EMAIL_FLD)
        code_from_email_field.clear()
        code_from_email_field.send_keys(fake_code_from_email_to_the_field)

    # 7 Send new password "asdfghjkl12!@" to the field
    def send_fake_password_to_the_field(self, fake_password_to_the_field):
        new_password_field = self.driver.find_element(*NEW_PASSWORD_FLD)
        new_password_field.clear()
        new_password_field.send_keys(fake_password_to_the_field)

    # 8 Send new password confirmation to the filed
    def send_new_psswrd_cnfrmtn_to_the_field(self, fake_password_to_the_field):
        new_password_confirmation_field = self.driver.find_element(*CNFRM_YR_PSWRD_FLD)
        new_password_confirmation_field.clear()
        new_password_confirmation_field.send_keys(fake_password_to_the_field)

    # 9 Click on Reset password button
    def clck_on_rst_passwrd_btn(self):
        self.driver.find_element(*RESET_PSWRD_BTN).click()

    # 10 Verify message "Server Error: Incorrect token" is here
    def vrfy_srvr_err_msg_is_hre(self, srvr_err_msg_is_hre):
        incorrect_token_text = self.driver.find_element(*INCORRECT_TOKEN_TEXT)
        expected_text = srvr_err_msg_is_hre
        actual_text = incorrect_token_text.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # End of the above code

    # 6_iced_latte_ui_add_item_to_cart_via_fav_and_delete
    # 1 Click Heart icon
    def clck_hrt_btn(self):
        self.driver.find_element(*HEART_ICON_FAVORITIES).click()

    # 2 Click on Continue Shopping button

    # 3 Click on Heart icon on Vanilla Latte
    def clck_on_hrt_icn_on_vnll_ltte(self):
        self. driver.find_element(*HEART_VANILLA_LATTE).click()

    # 4 Click on Heart icon on Turkish Coffee
    def clck_on_hrt_icn_on_trksh_cffee(self):
        self.driver.find_element(*HEART_TURKISH_COFFEE).click()

    # 5 Click Heart icon again
    def clck_on_hrt_icn_again(self):
        self.driver.find_element(*HEART_ICON_FAVORITIES).click()

    # 6 Verify Turkish Coffee text is here
    def vrfy_trksh_cffee_txt_hre(self, trksh_cffee_txt_hre):
        turkish_coffee_text = self.driver.find_element(*TRKSH_CFF_IN_THE_CRT)
        expected_text = trksh_cffee_txt_hre
        actual_text = turkish_coffee_text.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 7 Text "$4.49" is in the page in cart after this purchase
    def vrfy_trksh_cffee_total_dollrs_hre(self, trksh_cffee_total_dollrs_hre):
        four_forty_nine_dlrs_txt = self.driver.find_element(*FOUR_POINT_FOURTY_NINE_DOLLARS)
        expected_text = trksh_cffee_total_dollrs_hre
        actual_text = four_forty_nine_dlrs_txt.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # 8 Verify "Vanilla Latte" text is here in this step
    def vrfy_vnlla_ltte_txt_hre(self, vnlla_ltte_txt_hre):
        vanilla_coffee_text = self.driver.find_element(*VANILLA_LATTE_TEXT)
        expected_text = vnlla_ltte_txt_hre
        actual_text = vanilla_coffee_text.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # Text "$4.85" is in the page in cart $4.85
    def vrfy_four_eigthy_five_dlrs_txt_hre(self, four_eigthy_five_dlrs_txt_hre):
        four_eigthy_five_dlrs_txt = self.driver.find_element(*FOUR_POINT_EIGTHY_FIVE_DOLLARS)
        expected_text = four_eigthy_five_dlrs_txt_hre
        actual_text = four_eigthy_five_dlrs_txt.text
        assert expected_text == actual_text, f'Expected {expected_text}, but got {actual_text}'

    # End of the above code


