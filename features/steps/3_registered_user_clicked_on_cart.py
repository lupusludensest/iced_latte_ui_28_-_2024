from behave import *

@then('Click on cart icon')
def clck_on_cart_btn(context):
    """
    Click on cart icon
    """
    context.app.main_page.clck_on_cart_btn()

@then('Text "{txt_spng_crt_here}" is here')
def txt_spng_crt_here(context, txt_spng_crt_here):
    """
    Text "Shopping cart" is here
    """
    context.app.main_page.txt_spng_crt_here(txt_spng_crt_here)

@then('URL "{url_cart_here}" is active')
def url_cart_here(context, url_cart_here):
    """
    URL "https://iced-latte.uk/cart" is active
    """
    context.app.main_page.url_cart_here(url_cart_here)

@then('Text "{yr_crt_is_empty_here}" is displayed')
def yr_crt_is_empty_here(context, yr_crt_is_empty_here):
    """
    Text "Your cart is empty" is displayed
    """
    context.app.main_page.yr_crt_is_empty_here(yr_crt_is_empty_here)

@then('Continue shopping button is here with text "{cntnue_shpng_btnn_wth_txt_hr}"')
def cntnue_shpng_btn_is_hr(context, cntnue_shpng_btnn_wth_txt_hr):
    """
    Continue shopping button is here with text "Continue Shopping"'
    """
    context.app.main_page.cntnue_shpng_btn_is_hr(cntnue_shpng_btnn_wth_txt_hr)