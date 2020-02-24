## Models
```
User
	first_name
	last_name
	email
	password
	address 
		address 
		city
		state
		zip
		country 


Business
	owner FK: User
	category
	image
	business_name
	about
	address 
		address
		city
		state
		zip
		country


Post
	business FK: Business
	image
	content
	date


Subscription
	following FK: Business
	follower FK: User 

Comment 
	post FK: Post
	commenter FK: User
	content
	date


--Stretch Goal--

Message
	sender FK: User 
	recipient FK: User 
	content
	date 



```

## Routes

| Route | HTTP Method | Description |
|:------|:------------|:------------|
|/api/v1/users/register | POST | user register route |
|/api/v1/users/login | POST | user login route |
|/api/v1/users/logout | GET | user logout route |
|/api/v1/posts | GET | post index route |
|/api/v1/posts | POST | post create route |
|/api/v1/posts/<id> | DELETE | post destroy route |
|/api/v1/posts/<id> | PUT | post update route |
|/api/v1/comments/<post_id> | GET | comment index route |
|/api/v1/comments/<post_id> | POST | comment create route |
|/api/v1/comments/<post_id> | DELETE | comment destroy route |
|/api/v1/businesses | GET | business index route |
|/api/v1/businesses/<id> | GET | business show route |
|/api/v1/businesses | POST | business create route |
|/api/v1/businesses/<id> | DELETE | business destroy route |
|/api/v1/businesses/<id> | PUT | business update route |
|/api/v1/subscription/<business_id> | GET | subscription index route |
|/api/v1/subscription/<business_id> | POST | subscription create route |
|/api/v1/subscription/<business_id> | DELETE | subscription destroy route |