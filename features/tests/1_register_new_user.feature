# # Created by rapid at 3/28/2024
Feature: # 1_register_new_user

  Scenario: # 1_register_new_user
    Given Loginpage
    Then Click user authorization icon
    Then Click user registration button
    Then Send first name to first name field
    Then Send last name to last name field
    Then Send email to email field
    Then Send password to password field
    And Click user register user button
