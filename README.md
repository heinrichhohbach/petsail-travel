# Pet Vacation Ad Site Project - Code Academy Stream 3

You can view the project here: http://pet-sail.herokuapp.com


### Purpose and need of project

The project itself is to provide a platform that connects vacation goers with vacation providers. The Merchants on the site
can easily list their ads for the vacation goers to view and decide if they want to buy it. The Merchants have access to
a fully functional RichText editor that allows them to combine text with images which allows the ads to look good and gives
them the opportunity to easily structure their ads for the benefit of the user. The user can easily view the ads through the
site and once they decide which trip they want, they can purchase it using Stripe, ensuring that their credit card information
isn't stored anywhere and it's completely safe. The idea for the site came to me when I was looking for vacations that allowed
pets and I realised how little resources there are for that.


### Database Information

During development SQLite provided enough functionality to test the data connections and POST and GET features of the website.
Once the website was deployed however, MySQL became the host of the data instead of SQLite. This provided an online safe platform
for the data storage.

The Heroku MySQL database add on is called "ClearDB MySQL" and can easily be setup by adding the add-on in the resources section
of the app. Then you run the COMMAND NEEDED command and heroku local will push the models to ClearDB and create the database tables.
Once that is complete, the database is ready for use and if the POST and GET functions are correct, the database should easily allow
insert, edit, delete and read functions to be performed.


### Technologies Used
Technology Name | Description | How I used the Technology
------------ | ------------- | -------------
[ckeditor](https://ckeditor.com/) | CKEditor provides a RichText editor that easily integrates with django and gives a far more easily usable text editor that others. | I used CkEditor to create the editor for the ad creation feature of the Merchant dashboard
[Stripe](https://stripe.com/) | Stripe provides a payment platform to easily and safely process payments on django. | I used Stripe to setup the payment gateway for the vacation sales.
[Bootstrap](https://getbootstrap.com/) | Bootstrap gives the developer a grid like system to work with when using HTML. This allows for easier design and mobile compatibility. | I used Bootstrap to allow me to streamline the mobile and desktop designs and to ensure that they both were responsive no matter what device the user uses. |
[Google Fonts](https://fonts.google.com/) | Google Fonts provides the user with a wide variety of Fonts that anyone can use to customize their project more. | I used Google Fonts to give the website a bit personality, by not just using generic windows fonts. |
[Python](https://www.python.org/) | Python is a programming language that lets you work quickly and integrate systems more effectively. | I used Python for the backend of the website.
[SQLite](https://www.sqlite.org/index.html) | SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. SQLite is the most used database engine in the world. | I used SQLite during the development of the website.
[MySQL](https://www.mysql.com/) | MySQL is an open-source relational database management system. | I used MySql for the deployment database. This integrates well with Heroku and allows for Django Views to edit the data in the database.
[Django-forms-bootstrap](https://github.com/pinax/django-forms-bootstrap) | django-forms-bootstrap is a simple bootstrap filter for Django forms. Extracted from the bootstrap theme for Pinax. | I used Django-Forms-Bootstrap to create the bootstrap form design. This allows for the form to adjust according to the screensize and helps place the form into the bootstrap grid design.
[ClearDB MySQL](https://devcenter.heroku.com/articles/cleardb) | ClearDB is a powerful, fault tolerant database-as-a-service in the cloud for your MySQL powered applications. | ClearDB is the add-on Heroku uses to run MySQL databases. The add on easily generates tables from the Django Models setup in the project files.
[Django built in Password hashing](https://docs.djangoproject.com/en/2.0/topics/auth/passwords/) | Django provides a User class that integrates password hashing by itself. | Rather than building my own hashing methods, I used the Django hashing feature that's included in their User Model, because it's a safe method that already fulfills the need I had with password encryption.


### Project Detailed explanation

The Project has two sides to it:

The Merchant side of the site provides a ad creation, editing and deletion feature. The merchant has a profile where he/she
can see how many ads they currently have live and have the option to edit them or delete them. The Ads creator provides the
Merchant with a RichText editor as well as the option to set a Title, Description, Start of the vacation, End of the vacation
and price. This information is them displayed in a table and detailed ad view.

The customer side of the site provides a e-commerce experience for the user. The customer can easily browser the available holiday
ads that merchants created. Then the customer can see a full view of the ads and see the specifics the merchant put into the ad and decide if he/she wants to buy the holiday. There's an easy "buy now" button at the bottom of the detailed view, to allow the customer
to proceed with their purchase. Stripe then uses the input from the checkout fields the customer entered to validate the credit card
and take the payment charge. This ensures that there aren't any credit card data saved in the database.



### Deploying Application

The application was deployed using "Heroku". Heroku is an easy to use deployment platform that easily integrates with github respositories.

The application was deployed in this manner:
1. The project was setup with Github to create a repository online.
2. Then Heroku can be linked up with github.
3. I set up Heroku with the option that Github changes were directly pushed to the app to allow for an instant preview of the updated application.
4. I used ClearDB, a free MySQL add-on, to run the database for the application. The integration is easy and with the usage of the Django model setup, which allows for table creation directly from the models setup during development.
5. The dev version of the app includes a 'env' file that emulates a virtual machine. This is not needed with the Heroku application seeing as the "requirements" file handles the same function as the env.

NB: The Database setup can be found under the Database heading.


### Testing
Function Tested | How it was tested
------------ | -------------
Django Forms validation | I tested the Django forms on the website using the test.py files inside each app. This allowed me to test all the variations of errors that can happen on the forms easily and ensured that the tests were actually successful which can be difficult to test manually. 
Mobile and Desktop Layouts | I tested the mobile and Desktop layouts of the site using the Chrome Browser and their built in developer tools. This allowed me to ensure that the designs were fitting the screen sizes of mobile devices and the Desktop version itself. Once the layouts were correct, I tested the designs on an actual Android phone and iPhone to ensure that the website was as responsive as I wanted it to be. Using both these methods together helped me iron out any design flaws that might have been there.
Stripe Transaction | I used the Stripe API tool on the Stripe Dashboard to test if the Stripe transactions were successful. The API gives you enough information to see why payments failed. It alerted me of incorrect data types and failed authentication methods. Using the log files from the Stripe API, I was able to find the mistakes that were present and fix them accordingly


### External Influences

The general design of the dashboard was influenced by the dashboard example given during the course. The html skeleton
was modified to fit my charts and the layout I required.

The font used in the chart headers is called [Parry Hotter](http://www.1001fonts.com/parry-hotter-font.html) and is free
to use for non-commercial projects.

