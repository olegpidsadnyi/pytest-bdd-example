Scenario: Successful login
	Given I'm not logged in
	
	When I go to login page
	And I enter "admin" username
	And I enter "default" password
	And I click login button
	
	Then I should see "You were logged in"


Scenario: Invalid username
	Given I'm not logged in
	
	When I go to login page
	And I enter "wrong" username
	And I enter "default" password
	And I click login button
	
	Then I should see "Error: Invalid username"


Scenario: Invalid password
	Given I'm not logged in
	
	When I go to login page
	And I enter "admin" username
	And I enter "wrong" password
	And I click login button
	
	Then I should see "Error: Invalid password"

