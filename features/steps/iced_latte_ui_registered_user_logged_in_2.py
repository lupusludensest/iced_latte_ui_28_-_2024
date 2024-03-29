from behave import *

@then('Send registered email to email field')
def snd_rgstrd_eml_to_eml_fld(context):
    """
    Send registered email to email field
    """
    context.app.main_page.snd_rgstrd_eml_to_eml_fld()

@then('Send valid password to password field')
def snd_vald_pswrd_to_pswrd_fld(context):
    """
    Send valid password to password field
    """
    context.app.main_page.snd_vald_pswrd_to_pswrd_fld()

@then('Click login button')
def clck_lgn_btn(context):
    """
    Click login button
    """
    context.app.main_page.clck_lgn_btn()

@then('Assert user is logged in')
def assrt_usr_is_lggd_in(context):
    """
    Assert user is logged in
    """
    context.app.main_page.assrt_usr_is_lggd_in()