# Covid Case
## Overview
In this project users can visually see the statistics for coronavirus for each country. Simple thresholds are used to determine the safety level of each country, displayed using a traffic light system (green, orange, red).
The website's business function is to sell facemasks and other coronavirus-related products, such as hand sanitizers and visors.
The user has the ability to sign in and purchase these items.

## UX
The user design aims to create an application that is an intuitive shopping experience.
The web design links the need to purchase masks with the number of COVID-19 cases per country. The interactive map gives you more information about each country when you hover over it and there are a number of related items available to purchase underneath it. Hovering over the product will give you another view of the item.

The application navigation is very simple and easy to understand. The consumer decision making is simplified by using visual pictures of the products rather than lengthy descriptions. The customer does not need to have an account to view and purchase the products. If they don't already have an account when they place an order, they can sign up at a later date and still see their order history.

# Features
## Existing Functionality

### Nav Bar
* The nav bar is used to navigate throughout the website pages. There is different functionality depending on the user's access level.
* Before a user is logged in, they can navigate to the home page, can log in or sign up and can see their shopping basket.
* When a user is signed in, they can also reach their profile through "My Profile" and view their order history through "My Orders".
* When logged in as an admin, the user has additional privileges to add products.

### Home Page
* The home page contains the world map and the products users can buy.
* You can zoom in on the Highcharts world map to find the number of cases, deaths and number recovered for each country. You can also print or export the map in different formats.
* Underneath this is a gallery of the different products for sale, each containing a picture, description, price, quantity and buttons to interact with it. This also clearly shows if any products are out of stock.
* All users can choose "Add to Bag" to place the item in their checkout basket.
* Admins can also click "Update" to be taken to the "Update Product" page.

### Update Product
* Here they can update the product fields such as name, price, colour, number in stock etc.
* They can also delete products.

### Add Products
* Admins can find the "Add Products" page in the nav bar.
* Here they add a product and define all of the features related to the product, which will then get added to the home page.
* They also can see a preview of the image they uploaded.

### My Profile
* The user has the ability to view the current information associated with their profile.
* They can also edit this information here.
* The user can also reset their password from this page.

### My Orders
* The user can see their full order history, and have the ability to add this order to their bag (if the product is still in stock).

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
### Programming Languages
1. [Django framework](https://www.djangoproject.com/)
    1.
    2.
    3.
    4.
    5.
    6.
2. [HTML5](https://en.wikipedia.org/wiki/HTML5)
    1. I used HTML for the basic structure of the website.
3. [CSS3](https://en.wikipedia.org/wiki/CSS)
    1. CSS was used to style the HTML.
    2. The style sheet was mostly kept separate from the html.
4. [JQuery](https://jquery.com/)
    1.
5. [Python](https://www.python.org/)
    1.
6. [Markdown](https://www.markdownguide.org/)
    1. Documentation within the readme was generated using markdown
 


### Django Extension and tools
1. [dj-database-url](https://pypi.org/project/dj-database-url/)
    1.  allows use of environment variable for database connections
2. [django-crispy-forms](https://pypi.org/project/django-crispy-forms/)
    1. Crispy forms where used to style most of my forms
3. [stripe](https://pypi.org/project/stripe/)
    1. This libary allowed me to talk with strips api
4. [gunicorn](https://pypi.org/project/gunicorn/)
    1. Python WSGI HTTP Server for UNIX so you can host your application on heroku
5. [Bootstrap Version 4.4.1](https://getbootstrap.com/)
    1. Bootstrap components such as grid, card, button, table, navbar where used in my project to simplify creating responsive web application.
6. Database
    1. DB was used to store all users information and models.
    2. [SQLite](https://www.sqlite.org/index.html) for dev
    3. [Postgres](https://www.postgresql.org/) DB as part of Heroku was used for production
7. [VSCODE](https://code.visualstudio.com/)
    1. VSCODE was used as the development environment.
8. [Github](https://github.com/)
    1. Github was used for my version control in the project.
9. [Font-awesome Version 5.11.1](https://fontawesome.com/)
    1. Font-awesome was used to get some icons.
10. [Heroku](https://heroku.com/)
    1. I used heroku to host my application on a public URL

### APIs
1. [Stripe](https://stripe.com/en-ie)
    1.
2. [Disease.sh](https://disease.sh/docs/)
    1.
3. [HIGHCHARTS](https://www.highcharts.com/)
    1. Highcharts where used to present the information from Disase.sh api to the user
4.

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
8. Type git clone, and then paste the URL
9. Press Enter. A local clone will be created.

#### Env variables:
1. create a file named env.py in root of your project. use this file to define you environment variables
2. create a file name .gitignore add env.py to this file
3. in your env file we need to import os.
4. a signing you enviorment variables is easy its as simple as doing the following:<br/>
    os.environ["Variable Name Here"] = "Value of Variable Goes Here"
5. Then we need to import the env file we do this by first adding<br/>from os import path<br/> 
Then we check if the path exists <br/>
if path.exists("env.py"):<br/>
    import env



## Credits
## Content
I used Bootstrap Version 4.4.1 grid system. I used StackOverflow to solve problems that I couldn't figure out. I used Favicon for my favicon
I used django’s documention a lot to figure out solutions to my problems
I found [Mozzilla](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django) documention very helpful
## Media
My product images and information were taken from Dunnes Stores website

## Color Choice
For this project these where my choice of colors
![https://coolors.co/ffffff-bee0d3-179967-41b085-0c3c26](/readmeimage/covidCasesColorPallet.png)


Acknowledgements





![](/readmeimage/iphone6smobileimage2.png)
![](/readmeimage/iphone6smobileimage1.png)
![](/readmeimage/motog4.png)
![](/readmeimage/database_schema.png)
