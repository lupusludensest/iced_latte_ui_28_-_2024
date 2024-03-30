from behave import *

@then('Click on Forgot password button')
def clck_on_forgot_password_btn(context):
    """
    Click on Forgot password button
    """
    context.app.main_page.clck_on_forgot_password_btn()

@then('Send email to email field to reset password')
def send_email_to_email_field_to_reset_pswrd(context):
    """
    Send email to email field to reset password
    """
    context.app.main_page.send_email_to_email_field_to_reset_pswrd()

@then('Click on Send reset link button')
def clck_on_rst_lnk_btn(context):
    """
    Click on Send reset link button
    """
    context.app.main_page.clck_on_rst_lnk_btn()

@then('Click on Continue to change your password button')
def clck_on_cntnue_to_chng_your_pswrd(context):
    """
    Click on Continue to change your password button
    """
    context.app.main_page.clck_on_cntnue_to_chng_your_pswrd()

@then('Send code "{fake_code_from_email_to_the_field}" from email to the field')
def send_fake_code_from_email_to_the_field(context, fake_code_from_email_to_the_field):
    """
    Send code "861-539-280" from email to the field
    """
    context.app.main_page.send_fake_code_from_email_to_the_field(fake_code_from_email_to_the_field)

@then('Send new password "{fake_password_to_the_field}" to the field')
def send_fake_password_to_the_field(context, fake_password_to_the_field):
    """
    Send new password "asdfghjkl12!@" to the field
    """
    context.app.main_page.send_fake_password_to_the_field(fake_password_to_the_field)

@then('Send new password confirmation "{new_psswrd_cnfrmtn_to_the_field}" to the filed')
def send_new_psswrd_cnfrmtn_to_the_field(context, new_psswrd_cnfrmtn_to_the_field):
    """
    Send new password confirmation "asdfghjkl12!@" to the filed
    """
    context.app.main_page.send_new_psswrd_cnfrmtn_to_the_field(new_psswrd_cnfrmtn_to_the_field)

@then('Click on Reset password button')
def clck_on_rst_passwrd_btn(context):
    """
    Click on Reset password button
    """
    context.app.main_page.clck_on_rst_passwrd_btn()

@then('Verify message "{srvr_err_msg_is_hre}" is here')
def vrfy_srvr_err_msg_is_hre(context, srvr_err_msg_is_hre):
    """
    Verify message "Server Error: Incorrect token" is here
    """
    context.app.main_page.vrfy_srvr_err_msg_is_hre(srvr_err_msg_is_hre)