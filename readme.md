# Covid Case
## Overview
In this project users can visually see the statistics for corona virus for each country. Simple thresholds are used to determine the safety level of each country, displayed using a traffic light system (green, orange, red).
The website's business function is to sell facemasks and other corona virus-related products, such as hand sanitizers and visors.
The user has the ability to sign in and purchase these items.
Below you will find admin login details
Email: testUser@gmail.com
Password: Ask me

## UX
The user design aims to create an application that is an intuitive shopping experience.
The web design links the need to purchase masks with the number of COVID-19 cases per country. The interactive map gives you more information about each country when you hover over it. There are a number of COVID-19 related products available to purchase underneath it. Hovering over the product will show you an alternative image of the product if there is one available.

The application navigation is very simple and easy to understand. The customer's decision making is simplified by using visual pictures of the products rather than lengthy descriptions. The customer does not need to have an account to view and purchase the products. The user can sign up at a later date and still see their order history from before they registered.
### Wireframes
Home Page.
<a href="https://gyazo.com/8907744c87dbac915e4b6de2ac8aee4d">
<img src="/readmeimage/wireframe-homepage-covid-case.png" alt="homepage-wireframe" width="200" height="200"/>
</a>
Login Page
<a href="https://gyazo.com/8907744c87dbac915e4b6de2ac8aee4d">
<img src="/readmeimage/wireframe-login-covid-case.png" alt="homepage-login-page" width="200" height="200"/>
</a>
Sign up Page
<a href="https://gyazo.com/8907744c87dbac915e4b6de2ac8aee4d">
<img src="/readmeimage/wireframe-signup-covid-case.png" alt="homepage-login-page" width="200" height="200"/>
</a>


# Features
## Existing Functionality

### Nav Bar
* The nav bar is used to navigate throughout the website pages. There is different functionality depending on the user's access level.
* Before a user is logged in, they can navigate to the home page, can log in or sign up and can see their shopping basket.
* When a user is signed in, they can also reach their profile through "My Profile" and view their order history through "My Orders".
* When logged in as an admin, the user has additional privileges to add products.

### Home Page
* The home page contains the world map and the products users can buy.
* You can zoom in on the Highcharts world map to find the number of cases, deaths and number recovered for each country. You can also print or export the map in different formats. The countries are categorized green, orange or red depending on the thresholds.
* Underneath this is a gallery of the different products for sale, each containing a picture, description, price, quantity and buttons to interact with it. This also clearly shows if any products are out of stock.
* Users can choose "Add to Bag" to place the item in their checkout basket.
* Admins can also click "Update" to be taken to the "Update Product" page.

### Update Product - ADMIN
* An admin can update the product fields such as name, price, colour, number in stock etc.
* They can also delete products.

### Add Products - ADMIN
* Admins can find the "Add Products" page in the nav bar.
* Here they add a product and define all of the features related to the product, which will then get added to the home page.
* They also can see a preview of the images they uploaded.

### My Profile
* The user has the ability to view the current information associated with their profile.
* They can also edit this information here.
* The user can also reset their password from this page. They are sent a email which contain a reset password link.

### My Orders
* The user can see their full order history, and have the ability to reorder the items from this order (if the product(s) is still in stock).

### Sign up
* On this page the user can fill out the form to register an account with Covid-Case.
* If they clicked the wrong page there is a link to log in on the sign up form.

### Login
* The user can log into the account they have created.
* They can also reset their password here if they have forgotten it.

### View bag
* When the user clicks the little bag icon on the nav bar they will be taken to an overview of their shopping bag.
* They can increase and decrease the quantity of their products, and also remove them from the bag.
* The user can then continue to the checkout page.

### Checkout
* The user can fill in their billing details to let them buy their products.
* It shows a list of items in the bag.

### Order Summary
1. After completing order process the user can see a other summary page wich showcases
2. A overview of the order the users delivery information and a small table of the items ordered.
3. There is also a home button witch brings the user back to the home page and if the user is logged in a My profile button that takes the user to there profile.
## Database Schema
* Below you will find a picture of my database schema i couldnt get the exact SQL code ran by django to create this so i did it manually. This isnt 100% accurate but it give you an idea of what it looks like.
![https://gyazo.com/38b8fe5a21fb608c4750434f6be1cb39](/readmeimage/database_schema.png)

## Future Enhancements
1. Search/filter functionality would be a good addition
2. Customer reviews
3. List of all orders received that admins can see
4. The application could be improved with Internationalization for coving date, time and currency format

## Technologies Used
1. [VSCODE](https://code.visualstudio.com/) - VSCODE was used as the development environment.
3. [Bootstrap Version 4.4.1](https://getbootstrap.com/) - Bootstrap components such as grid, card, button, table, navbar where used in my project to simplify creating responsive web application.
4. [Github](https://github.com/) - GitHub has been used for version control of the code by using Git functions in the control panel.
5. [Font-awesome Version 5.11.1](https://fontawesome.com/) - 
6. [Heroku](https://heroku.com/) - This is a cloud based application platform that allows deployment of an application to the web and connection to the database.
7. [AWS S3](https://aws.amazon.com/s3/) - Amazon S3 is an object storage service that offers industry-leading scalability, data availability, security, and performance.
8. [StackOverflow](https://stackoverflow.com/) - Stack Overflow is a question and answer site for professional and enthusiast programmers.
9. [Mozilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) - I found Mozilla documentation for django very helpful when solving problems.
10. [favicon.io](https://favicon.io/) - I used favicon.io to generate my favicon.


### Programming Languages
1. [Python 3.8.2](https://www.python.org/) - Python is an interpreted, high-level and general-purpose programming language.
2. [Django 3.1.1](https://www.djangoproject.com/) - Django is designed to help developers take applications from concept to completion as quickly as possible.
3. [HTML5](https://en.wikipedia.org/wiki/HTML5) - HTML is the standard markup language for documents designed to be displayed in a web browser.
3. [CSS3](https://en.wikipedia.org/wiki/CSS) - CSS is a style language used for describing the presentation of a document.
4. [JavaScript](https://www.javascript.com/) - JavaScript (JS) is a lightweight, interpreted, or just-in-time compiled programming language with first-class functions.
5. [jQuery](https://jquery.com/) - jQuery is a JavaScript library designed to simplify HTML DOM tree traversal and manipulation, as well as event handling.
6. [Markdown](https://www.markdownguide.org/) - Markdown is a lightweight markup language with plain-text-formatting syntax.


### Django Extension and tools
1. [dj-database-url](https://pypi.org/project/dj-database-url/) - Allows use of environment variable for database connections
2. [django-crispy-forms](https://pypi.org/project/django-crispy-forms/) - Crispy forms where used to style most of my forms
3. [stripe](https://pypi.org/project/stripe/) - This libary allowed me to talk with stripes api
4. [gunicorn](https://pypi.org/project/gunicorn/) - Python WSGI HTTP Server for UNIX so you can host your application on heroku
5. Thease Database's where used to store all users information and models.
    * [SQLite](https://www.sqlite.org/index.html) I used SQLite for dev
    * [Postgres](https://www.postgresql.org/) DB as part of Heroku was used for production
6. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja is a modern and designer-friendly templating language for Python, modelled after Django’s templates.

### APIs
1. [Stripe](https://stripe.com/) - Stripes APIs allow you to accept credit cards, manage subscriptions, send money, run a marketplace.
2. [Disease.sh](https://disease.sh/docs/) - An open API for disease-related statistics
3. [HIGHCHARTS](https://www.highcharts.com/) - Highcharts where used to present the information from Disase.sh api to the user


## Testing
#### Styling
1. Check that all success buttons are styled the same.
2. I checked my css file to make sure that i removed use of px and replaced it with REM. :heavy_check_mark:
3. I check all html files for inline styling to see if i could move this styling into a bootstrap class. :heavy_check_mark:
4. I check that there was consistant use of buttons across the site. I navigated to each page to see if i was using the correct button classes on each page. :heavy_check_mark:
5. I checked each page for a consitant  color scheme. :heavy_check_mark:
 
#### Navbar
1. Check that all the links are working correctly. :heavy_check_mark:
2. Check that the navbar collapses into hamburger menu on mobile. :heavy_check_mark:
![https://gyazo.com/738fa482eabc49edf3a2b77884cc4127](/readmeimage/hamburgermenu.png)
3. 

### Sign up
1. Register account using sign up :heavy_check_mark:
    1. Go to django admin and check that user object was created with the email, first name and last name from sign up form :heavy_check_mark:
    2. Attempt to create a user if successful check that it redirects to login page. :heavy_check_mark:
2. Attempt to create a user with the same email address and check if it fails with a message. :heavy_check_mark:
3. Attempt to create a user with passwords that don't match. This should fail with a message. Check that it fails to create the user. :heavy_check_mark:
4. Attempt to create a user with a password less then 8 characters. This should fail with a message. Check that it fails to create the user. :heavy_check_mark:
5. Attempt to create a user with a password that is the same as the email. This should fail with a message.
Check that it fails to create the user. :heavy_check_mark:
6. Attempt to create a user with a password that is part of the email address. This should fail with a message.
Check that it fails to create the user. :heavy_check_mark:

### Login 
1. Attempt to login with an account that dose not exist. This should fail with a message. User stays on login page. :heavy_check_mark:
2. Attempt to login with an account that dose exist but using the wrong password. This should fail with a message. User stays on login page. :heavy_check_mark:
3. Check that the forgot password button navigates you to the password reset page. :heavy_check_mark:
4. On the password reset page enter an email address for user that dose not exist. Press the reset my password. This should fail with a message. :heavy_check_mark:
5. On the password reset page enter an email address for user that dose exist. Press the reset my password. This should redirect you to password reset done page and you should receive an email. :heavy_check_mark:
6. On the password reset done page check that the button to navigate to login page works. :heavy_check_mark:
7. Open email account and check that when you click the link in the email it redirects you the change password page. :heavy_check_mark:
8. Check that on the change password page if you enter passwords that don't match this should fail with a error message. :heavy_check_mark:
9. Attempt to change the password to less then 8 characters. This should fail with a message. Check that it fails to change password. :heavy_check_mark:
11. Attempt to change the password to be part of the email address. This should fail with a message. :heavy_check_mark:
12. Try to use the same password reset link a second time. This should fail telling the user its already been used. :heavy_check_mark:
13. On the password reset page enter a new valid password. This should redirect you to password reset done page. :heavy_check_mark:

### Home
#### Map 
1. Attempt to zoom in and out with mouse wheel. This should let the user zoom in and out. :heavy_check_mark:
2. Hover over countries. This should display a menu that has more information about each country. :heavy_check_mark:
3. Check that the full screen option in the hamburger menu works. This should take the user into a full screen view. :heavy_check_mark:
4. Check that print chart button works in the hamburger menu. This should take the user into a print window. :heavy_check_mark:
5. Check that download as PNG works in hamburger menu. This should download a image of the map in PNG format. :heavy_check_mark:
6. Check that download as JPEG works in the hamburger menu. This should download a image of the map in JPEG format. :heavy_check_mark:
7. Check that download as PDF works in the hamburger menu. This should download a PDF file with the map inside it. :heavy_check_mark:
8. Check that download as SVG vector image works in hamburger menu. This should download as a SVG file. :heavy_check_mark:
9. Check that the zoom in and out buttons work as intended. This should zoom the users view in/out. :heavy_check_mark:
10. Check that when the user clicks on a color on the legend all countries of that color disappear. :heavy_check_mark:
#### Products
1. Attempt to add product to basket. This should update the total amount in the basket on the navbar. :heavy_check_mark:
2. Attempt to add product to basket when quantity is greater then number in stock. This should show a message saying not enough in stock. :heavy_check_mark:
3. Attempt to put the quantity below 1. This should not allow the user to do so. :heavy_check_mark:
4. Hover over product image. This should display an alternative view of the image. :heavy_check_mark:
5. When the user is a admin they have the ability to click the update product button. Check that this button redirect to the update product page. :heavy_check_mark:

### Update Product - Admin user only
1. Attempt to update a new product with no product name. Form should tell the user that this field is required. :heavy_check_mark:
2. Attempt to update a new product with no color entered. Form should tell the user that this field is required. :heavy_check_mark:
3. Attempt to update a new product with no price entered. Form should tell the user that this field is required. :heavy_check_mark:
4. Attempt to update a new product with no supplier chosen. Form should tell the user that this field is required. :heavy_check_mark:
5. Attempt to update a new product with out number in stock filled out. Form should tell the user that this field is required. :heavy_check_mark:
6. Attempt to delete product by clicking the delete button. Sets the is_deleted boolean to True. Redirects the user to home page. :heavy_check_mark:


### Add Products - Admin user only
1. Attempt to add a new product with no product name. Form should tell the user that this field is required. :heavy_check_mark:
2. Attempt to add a new product with no color entered. Form should tell the user that this field is required. :heavy_check_mark:
3. Attempt to add a new product with no price entered. Form should tell the user that this field is required. :heavy_check_mark:
4. Attempt to add a new product with no supplier chosen. Form should tell the user that this field is required. :heavy_check_mark:
5. Attempt to add a new product with out number in stock filled out. Form should tell the user that this field is required. :heavy_check_mark:


### My Profile
1. Attempt to Update profile without First name. Form should tell the user the this field is required. :heavy_check_mark:
2. Attempt to Update profile without Last name. Form should tell the user the this field is required. :heavy_check_mark:
3. Attempt to Update profile without Phone number. Form should tell the user the this field is required. :heavy_check_mark:
4. Attempt to Update profile without Address line 1. Form should tell the user the this field is required. :heavy_check_mark:
5. Attempt to Update profile without Country. Form should tell the user the this field is required. :heavy_check_mark:
6. Click reset password button. Should redirects you to password reset page. :heavy_check_mark:


### Shopping Bag
1. Click on back to shopping button. Redirects the user back to the home page. :heavy_check_mark:
2. Click on the plus button to increment the quantity. quantity gets incremented. :heavy_check_mark:
3. Click on minus button to decrement the quantity. Quantity get decremented. :heavy_check_mark:
4. Check to see if quantity is equal to 0. If quantity is 0 hide minus button. :heavy_check_mark:
5. Check to see if quantity is equal to number in stock. If quantity is equal number in stock hide plus button. :heavy_check_mark:
6. Click remove button to. Removed the current product from shopping bag. :heavy_check_mark:
7. Attempt to proceed to checkout if all quantity's are 0. The proceed to checkout button wont show if grand total is 0. :heavy_check_mark:

### Checkout 
1. Attempting to submit the checkout form without filling out the required fields. The form will display a message saying this field is required. :heavy_check_mark:
2. Check to see if the card number is valid. If the card number is not valid an error message will be displayed under the card input. :heavy_check_mark:

#### Checkout while not registered
1. Check to see if the user can purchase item while not signed in. The user can complete the checkout process without having to be logged in or registered. :heavy_check_mark:
2. Check to see if the user can still view order history if they sign up at a later date. The user can see their order history when ever they choose to create an account. :heavy_check_mark:

#### Checkout while registered
1. Check to see if registered users can complete the checkout process. The user can complete the checkout process while being registered. :heavy_check_mark:
2. Check to see if the user can still purchase without being logged in while still being registered. The user can still complete the checkout process. :heavy_check_mark:
3. The users information should be filled when the proceed to checkout if they have made purchase before or have edited there profile. :heavy_check_mark:

#### Order history
1. Click place order again. The same order will be placed if the items are in stock. :heavy_check_mark:
2. Check that Order history page looks okay on mobile. :heavy_check_mark:



#### Order success
1. Click the Home button. The user will be redirected to the home page. :heavy_check_mark:
2. Click the edit profile button. the user will be redirect to the My profile page. :heavy_check_mark:


#### Responsive Testing
1. When i deployed the project to heroku i navigated to deployed url on my mobile and added the website as a app on my mobile. I checked that all pages where responsive on mobile and was a pleasant user experience. :heavy_check_mark:
2. I used chrome dev tools mobile view to check across different mobile devices but i found out this isn't always accurate. The dev tools showed some pages not being responsive yet on my mobile it looked okay. :heavy_check_mark:
3. When i was first checking out how it looked on mobile i realised that the user couldn't see there shopping bag unless they clicked the hamburger menu. So i took the shopping bag out of the hamburger menus and just displayed it on the navbar.


### Known Issues :small_red_triangle:
1. On the password reset done page there is a pop up that is being displayed by the messages framework that should be removed. :x:
2. In my database model i have the price set to the products price so if the price of a product changes then the orders price will to. to fix this i should copy the price to the OrderItem when the order is placed. 










## Deployment
#### To deploy the project to Github the following steps were taken:
1. created a master branch in Github repository
2. Committed files to the staging area using bash terminal commands: git status; git add (specify directory); git commit -m"add message"
3. Pushed files to the working environment using git push, which then updates the repository.
4. Published site from master branch using settings tab in the main page of the repository, select source as master branch, then save
5. git push -u origin master

6. The repository can be cloned by clicking Clone or Download on the main page of the repository
7. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
8. Open Git Bash Terminal
9. Type git clone, and then paste the URL, Press Enter. A local clone will be created.
10. git push -u origin master


#### Environment variables:
1. create a file named env.py in root of your project. use this file to define you environment variables
2. create a file name .gitignore add env.py to this file
3. in your env file we need to import os.
4. To assign your environment variables is easy its as simple as doing the following:
```python
    import os
    os.environ["Variable Name Here"] = "Value of Variable Goes Here"
```
5. Then we need to import the env file we do this by importing os.path then checking if "./covid_case/env.py" exists if it dose import it. Like in the following example:
```python
    import os.path
    if os.path.exists("./covid_case/env.py"):
        from . import env
```
#### Deploying to heroku:
1. I started by creating an account at [Heroku](https://signup.heroku.com/)
2. Then I created a package dependency file called requirements.txt by running the command "pip freeze > requirements.txt". This needs to be called requirements.txt and has to be in the root of the project for heroku to install the packages listed in the file.
3. I created a new app by navigating to dashboard.heroku.com/apps then clicking the new button.
4. Then I logged into the heroku CLI by typing heroku login into my terminal.
5. In order to  get the application up and running i had to create a Procfile. The Profile tells Heroku which file is the entry point. A Procfile looks something like this "web: gunicorn covid_case.wsgi" (process type: command).
6. To connect an existing repository from Github to Heroku use the following CLI syntax "heroku git:remote -a (followed by name of Heroku app)"
7. To push to Heroku Master Branch, then simply use "git push heroku master"
8. In order for our application to run on heroku we need to specify a few Config Vars in Heroku. To do this go to Settings tab > Config Variables followed by the various config variable needed.
9. I needed to add the following lines to my settings.py in order to tell heroku what database to access
```python
    import dj_database_url

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    db_from_env = dj_database_url.config(conn_max_age=600)
    DATABASES['default'].update(db_from_env)
```
10. I used Django-heroku in order to configure DATABASE_URL , ALLOWED_HOSTS, WhiteNoise (for static assets), Logging, and Heroku CI for my application. This was done as follows.
```python
    import django_heroku
    django_heroku.settings(locals())
```



## Credits
## Content


## Media
My product images and information were taken from Dunnes Stores website
Favicon was created using 

### Color Choice
For this project these where my choice of colors
![https://coolors.co/ffffff-bee0d3-179967-41b085-0c3c26](/readmeimage/covidCasesColorPallet.png)


## Acknowledgements
Id like to give a big thanks to the [code institute](https://codeinstitute.net/) team and the mentor they assigned me [Rhey Ann Magcalas]()
Id also like to give a big thanks to family and friends who have helped me with ideas for projects and styling tweaks that could be made.




![](/readmeimage/iphone6smobileimage2.png)
![](/readmeimage/iphone6smobileimage1.png)
![](/readmeimage/motog4.png)
