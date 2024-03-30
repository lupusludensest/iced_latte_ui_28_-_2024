# Created by rapid at 3/30/2024
Feature: # 5_user_forgot_password

  Scenario: # 5_user_forgot_password
    Given Loginpage
    Then Click user authorization icon
    Then Click on Forgot password button
    Then Send email to email field to reset password
    Then Click on Send reset link button
    Then Click on Continue to change your password button
    Then Send code "861-539-280" from email to the field
    Then Send new password "asdfghjkl12!@" to the field
    Then Send new password confirmation "asdfghjkl12!@" to the filed
    Then Click on Reset password button
    And Verify message "Server Error: Incorrect token" is here