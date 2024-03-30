# Created by rapid at 3/30/2024
Feature: # 3_registered_user_clicked_on_cart

  Scenario: # 3_registered_user_clicked_on_cart
    Given Loginpage
    Then Click user authorization icon
    Then Send registered email to email field
    Then Send valid password to password field
    Then Click login button
    Then Click on cart icon
    Then Text "Shopping cart" is here
    Then URL "https://iced-latte.uk/cart" is active
    Then Text "Your cart is empty" is displayed
    Then Continue shopping button is here with text "Continue Shopping"

