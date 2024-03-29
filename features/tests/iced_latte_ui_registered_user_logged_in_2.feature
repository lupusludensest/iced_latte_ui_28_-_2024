# Created by rapid at 3/28/2024
Feature: # iced_latte_ui_registered_user_logged_in_2

  Scenario: # iced_latte_ui_registered_user_logged_in_2
    Given Loginpage
    Then Click user authorization icon
    Then Send registered email to email field
    Then Send valid password to password field
    Then Click login button
    Then Assert user is logged in
