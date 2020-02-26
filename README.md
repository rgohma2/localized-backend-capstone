## Models
```
User
	address FK: Address
	first_name
	last_name
	email
	password



Business
	address FK: Address
	owner FK: User
	category
	image
	business_name
	about

Address
	address_1 
	address_2 
	city 
	state
	zip_code 
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
|/api/v1/posts/`<business_id>` | POST | post create route |
|/api/v1/posts/`<id>` | DELETE | post destroy route |
|/api/v1/posts/`<id>` | PUT | post update route |
|/api/v1/comments/`<post_id>` | GET | comment index route |
|/api/v1/comments/`<post_id>` | POST | comment create route |
|/api/v1/comments/`<id>` | DELETE | comment destroy route |
|/api/v1/businesses | GET | business index route |
|/api/v1/businesses/`<id>` | GET | business show route |
|/api/v1/businesses | POST | business create route |
|/api/v1/businesses/`<id>` | DELETE | business destroy route |
|/api/v1/businesses/`<id>` | PUT | business update route |
|/api/v1/subscription/`<business_id>` | GET | subscription index route |
|/api/v1/subscription/`<business_id> `| POST | subscription create route |
|/api/v1/subscription/`<business_id> `| DELETE | subscription destroy route |


## Development Process

* 1st Sprint: Feb 24th - Feb 26th
	* Full CRUD on User, Business, and Post models
* 2nd Sprint : Feb 26th - 28th
	* Full CRUD on Subscriptions and comments, and set up cloudinary











