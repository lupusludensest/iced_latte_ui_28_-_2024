from behave import *

@then("Click Heart icon")
def clck_hrt_btn(context):
    """
    Click Heart icon
    """
    context.app.main_page.clck_hrt_btn()

@then("Click on Heart icon on Vanilla Latte")
def clck_on_hrt_icn_on_vnll_ltte(context):
    """
    Click on Heart icon on Vanilla Latte
    """
    context.app.main_page.clck_on_hrt_icn_on_vnll_ltte()

@then("Click on Heart icon on Turkish Coffee")
def clck_on_hrt_icn_on_trksh_cffee(context):
    """
    Click on Heart icon on Turkish Coffee
    """
    context.app.main_page.clck_on_hrt_icn_on_trksh_cffee()

@then("Click Heart icon again")
def clck_on_hrt_icn_again(context):
    """
    Click Heart icon again
    """
    context.app.main_page.clck_on_hrt_icn_again()

@then('Verify "{trksh_cffee_txt_hre}" text is here')
def vrfy_trksh_cffee_txt_hre(context, trksh_cffee_txt_hre):
    """
    Verify "Turkish Coffee" text is here
    """
    context.app.main_page.vrfy_trksh_cffee_txt_hre(trksh_cffee_txt_hre)

@then('Text "{trksh_cffee_total_dollrs_hre}" is in the page in cart after this purchase')
def vrfy_trksh_cffee_total_dollrs_hre(context, trksh_cffee_total_dollrs_hre):
    """
    Text "$4.49" is in the page in cart after this purchase
    """
    context.app.main_page.vrfy_trksh_cffee_total_dollrs_hre(trksh_cffee_total_dollrs_hre)

@then('Verify "{vnlla_ltte_txt_hre}" text is here in this step')
def vrfy_vnlla_ltte_txt_hre(context, vnlla_ltte_txt_hre):
    """
    Verify "Vanilla Latte" text is here in this step
    """
    context.app.main_page.vrfy_vnlla_ltte_txt_hre(vnlla_ltte_txt_hre)

@then('Text "{four_eigthy_five_dlrs_txt_hre}" is in the page in cart with Vanilla Latte')
def vrfy_four_eigthy_five_dlrs_txt_hre(context, four_eigthy_five_dlrs_txt_hre):
    """
    Text "$4.85" is in the page in cart with Vanilla Latte
    """
    context.app.main_page.vrfy_four_eigthy_five_dlrs_txt_hre(four_eigthy_five_dlrs_txt_hre)

