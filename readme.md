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
 !!!
 

## Future Enhancements
1. Search/filter functionality would be a good addition
2. Customer reviews
3. List of all orders received that admins can see
4.

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














1. I used Chrome Dev Tools for debug Testing. !!REVIEW
i. I used the inspect feature to check different elements on my page.
ii. I used the coverage tab to check my css was being used on the given page.
iii. I used the network tab to see what was taking a long time to load and what wasn't loading.
iv. I used the computed tab to see the final state of a given element.
v. I used the device toolbar to check that my website was rendered in a responsive manner on all device's.
vi. I installed the chrome Lighthouse plugin to use the audit feature to check Performance, progressive web app, Best practices, accessibility and SEO.
2. Application Testing !!CHANGE
i. I tested that everything worked okay when resizing the browser.
ii. I ran all my tests on localhost (root website) then pushed it onto github (where ran off the subdomain). Checked that all resources loaded properly off the root and subdomain.
iii. I checked on mobile to see that everything was working correctly.
iv. I ran into some problems trying to get blueprints to work and i solved this problem by changing how I initialised my DB.
v. I ran into some problems with basic html i solved them by googling.
## Deployment
#### To deploy the project to Github the following steps were taken:
1. created a master branch in Github repository
2. Committed files to the staging area using bash terminal commands: git status; git add (specify directory); git commit -m"add message"
3. Pushed files to the working environment using git push, which then updates the repository.
4. Published site from master branch using settings tab in the main page of the repository, select source as master branch, then save
5. The repository can be cloned by clicking Clone or Download on the main page of the repository
6. In the Clone with HTTPs section, click the clipboard icon to copy the clone URL for the repository
7. Open Git Bash Terminal
8. Type git clone, and then paste the URL, Press Enter. A local clone will be created.
9. 

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

![](/readmeimage/database_schema.png)
