# Created by rapid at 3/30/2024
Feature: # 6_add_item_to_cart_via_fav_and_delete

  Scenario: # 6_add_item_to_cart_via_fav_and_delete
    Given Loginpage
    Then Click Heart icon
    Then Click on Continue Shopping button
    Then Click on Heart icon on Vanilla Latte
    Then Click on Heart icon on Turkish Coffee
    Then Click Heart icon again
    Then Verify "Turkish Coffee" text is here
    Then Text "$4.49" is in the page in cart after this purchase
    Then Verify "Vanilla Latte" text is here in this step
    Then Text "$4.85" is in the page in cart with Vanilla Latte
