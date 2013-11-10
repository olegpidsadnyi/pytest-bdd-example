Scenario: Entry is displayed
	Given I have an entry
	When I go to the blog
	Then I should see my entry


Scenario: No form for visitors
	Given I'm a visitor
	When I go to the blog
	Then I shouldn't see an entry form 


Scenario: Create an entry
	Given I'm an admin
	When I go to the blog
	And I enter entry title
	And I enter entry text
	And I click the Share button
	Then I should see "New entry was successfully posted"
	And I should see the entry title
	And I should see the entry text