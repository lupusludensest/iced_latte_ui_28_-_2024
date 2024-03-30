# Created by rapid at 3/30/2024
Feature: # 4_registered_user_continue_shop

  Scenario: # 4_registered_user_continue_shop
    Given Loginpage
    Then Click user authorization icon
    Then Send registered email to email field
    Then Send valid password to password field
    Then Click login button
    Then Click on cart icon
    Then Click on Continue Shopping button
    Then Click on "plus" button, adding Turkish Coffee to the cart
    Then Click on cart icon after adding
    Then Verify the coffee is in the cart. Counter "1" is here
    Then Text "Turkish Coffee" is in the page in cart
    Then "500 g." is in the page in cart
    Then Text "$4.49" is in the page in cart after purchase
    And Button "Go to checkout" is here