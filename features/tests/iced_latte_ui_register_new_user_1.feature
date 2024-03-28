# Created by rapid at 28 march 2024
Feature: # iced_latte_ui_register_new_user_1

  Scenario: # iced_latte_ui_register_new_user_1
    Given Loginpage
    Then Click user authorization icon
    Then Click user registration button
    Then Send first name to first name field
    Then Send last name to last name field
    Then Send email to email field
    Then Send password to password field
    And Click user register user button
