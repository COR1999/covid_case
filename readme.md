# Covid Case
## Overview
In this project I have planned that users can visually see the statistics for corona virus for each country. A simple threshold is used to identify which countries are on the green list.
The business part of the website is to sell facemasks and other corona virus related products such as hand sanitizers and visors.
The user has the ability to sign in and purchase.

## UX
In my user design I wish to create a application that is an intuitive shopping experience. The application navigation is very simple and easy to understand.
I selected products that minimized consumer decision making by using visual pictures of the products rather than lengthy descriptions.


# Features
## Existing Functionality
### Admin
1. **Nav Bar** When signed in as a admin the admin has the ability to add products by clicking the Add products link on the navbar 
2. **Home Page -** The admin has the ability to update and delete products from the home page.
### End User
* **Nav Bar -** for a user who isn't signed in contains the home page, sign up, login and view bag links.
* **Nav Bar Signed in -** When the user is signed in the user has the ability to view the home page, user profile, Orders, logout, and view bag 
* **Home Page -** On the home page the user can see the highcharts map with a world map with the countrys color coded if they are high or low on the covid-19 green list.
The user also has the ability to add products to thier bag and view the product images. the user can see clearly if the product is out of stock.

* Ability to reset password (Requires email server)
* The ability to view user profile
* Add products to cart, validates that product is in stock
* Edit products in the user cart
* Checkout functionality
* Overview of ordered products
* View order history!!!!!!!!!!!!
## Future Enhancements
1. Search/filter functionality would be a good addition
2. Customer reviews

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
vi. I installed the chrome Lighthouse plugin to use the audit feature to check Performance, progressive web app, Best practices, accessibility and SEO.
2. Application Testing !!CHANGE
i. I tested that everything worked okay when resizing the browser.
ii. I ran all my tests on localhost (root website) then pushed it onto github (where ran off the subdomain). Checked that all resources loaded properly off the root and subdomain.
iii. I checked on mobile to see that everything was working correctly.
iv. I ran into some problems trying to get blueprints to work and i solved this problem by changing how I initialised my DB.
v. I ran into some problems with basic html i solved them by googling.
Deployment
I used Live Server on my windows PC and once I was happy I committed to github to check that everything ran smoothly there as well.
I used XYZ to help me move my product from development into production x was used to help me do y and z 
Credits
Content
I used Bootstrap Version 4.4.1 grid system. I used StackOverflow to solve problems that I couldn't figure out. I used Favicon for my favicon
I used django’s documention a lot to figure out solutions to my problems 
I found Mozzilla documention very helpful https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django
Media
My product images and information were taken from Dunnes Stores website

Acknowledgements





## Color Choice
For this project these where my choice of colors
![https://coolors.co/ffffff-bee0d3-179967-41b085-0c3c26](/media/covidCasesColorPallet.png)
