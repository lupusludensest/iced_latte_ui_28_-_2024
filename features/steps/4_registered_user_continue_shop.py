from behave import *

@then('Click on Continue Shopping button')
def clck_on_cntnue_shpng_btn(context):
    """
    Click on Continue Shopping button
    """
    context.app.main_page.clck_on_cntnue_shpng_btn()

@then('Click on "plus" button, adding Turkish Coffee to the cart')
def clck_on_plus_btn(context):
    """
    Click on "plus" button, adding Turkish Coffee to the cart
    """
    context.app.main_page.clck_on_plus_btn()

@then('Click on cart icon after adding')
def clck_on_cart_icon_after_adding_btn(context):
    """
    Click on cart icon after adding
    """
    context.app.main_page.clck_on_cart_icon_after_adding_btn()

@then('Verify the coffee is in the cart. Counter "{one_is_here}" is here')
def vrfy_coffee_is_in_the_cart_one_is_here(context, one_is_here):
    """
    Verify the coffee is in the cart. Counter "1" is here
    """
    context.app.main_page.vrfy_coffee_is_in_the_cart_one_is_here(one_is_here)

@then('Text "{turkish_coffe_is_in_the_cart}" is in the page in cart')
def vrfy_turkish_coffe_is_in_the_cart(context, turkish_coffe_is_in_the_cart):
    """
    Text "Turkish Coffee" is in the page in cart
    """
    context.app.main_page.vrfy_turkish_coffe_is_in_the_cart(turkish_coffe_is_in_the_cart)

@then('"{gramms_in_the_page}" is in the page in cart')
def vrfy_gramms_in_the_page(context, gramms_in_the_page):
    """
    "500 g." is in the page in cart
    """
    context.app.main_page.vrfy_gramms_in_the_page(gramms_in_the_page)

@then('Text "{total_dollars_in_cart}" is in the page in cart after purchase')
def total_dollars_in_cart(context, total_dollars_in_cart):
    """
    Text "$4.49" is in the page in cart after purchase
    """
    context.app.main_page.total_dollars_in_cart(total_dollars_in_cart)

@then('Button "{go_to_chck_out_btn}" is here')
def go_to_chck_out_btn(context, go_to_chck_out_btn):
    """
    Button "Go to checkout" is here
    """
    context.app.main_page.go_to_chck_out_btn(go_to_chck_out_btn)