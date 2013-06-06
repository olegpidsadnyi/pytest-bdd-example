Scenario: Successful login
	Given I'm an admin user

	When I go to the admin login page
	And I fill in the login credentials
	And I post the form

	Then I shouldn't see an error message
	And I should see the Dashboard page


Scenario: Unsuccessful login

	When I go to the admin login page
	And I fill in wrong login credentials
	And I post the form

	Then I should see an error message
