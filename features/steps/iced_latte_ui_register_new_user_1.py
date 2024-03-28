from behave import *


@given("Loginpage")
def open_homepage(context):
    """
    Loginpage
    """
    context.app.main_page.open_page()

@then('Click user authorization icon')
def clck_usr_authrztn_icn(context):
    """
    Click user authorization icon
    """
    context.app.main_page.clck_usr_authrztn_icn()

@then('Click user registration button')
def clck_usr_rgstrtn_btn(context):
    """
    Click user registration button
    """
    context.app.main_page.clck_usr_rgstrtn_btn()

@then('Send first name to first name field')
def snd_frst_nm_to_fld(context):
    """
    Send first name to first name field
    """
    context.app.main_page.snd_frst_nm_to_fld()

@then('Send last name to last name field')
def snd_lst_nm_to_fld(context):
    """
    Send last name to last name field
    """
    context.app.main_page.snd_lst_nm_to_fld()

@then('Send email to email field')
def snd_eml_to_fld(context):
    """
    Send email to email field
    """
    context.app.main_page.snd_eml_to_fld()

@then('Send password to password field')
def snd_pswrd_to_fld(context):
    """
    Send password to password field
    """
    context.app.main_page.snd_pswrd_to_fld()

@then('Click user register user button')
def clck_usr_rgstr_usr_btn(context):
    """
    Click user register user button
    """
    context.app.main_page.clck_usr_rgstr_usr_btn()