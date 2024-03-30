# Created by rapid at 3/28/2024
Feature: # 2_registered_user_logged_in

  Scenario: # 2_registered_user_logged_in_2
    Given Loginpage
    Then Click user authorization icon
    Then Send registered email to email field
    Then Send valid password to password field
    Then Click login button
    Then Assert user is logged in. Expected "Viachesla..." is here
