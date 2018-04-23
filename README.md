# Pet Vacation Ad Site Project - Code Academy Stream 3

You can view the project here: LINK NOT YET AVAILABLE


### Purpose and need of project

The project itself is to provide a platform that connects vacation goers with vacation providers. The Merchants on the site
can easily list their ads for the vacation goers to view and decide if they want to buy it. The Merchants have access to
a fully functional RichText editor that allows them to combine text with images which allows the ads to look good and gives
them the opportunity to easily structure their ads for the benefit of the user. The user can easily view the ads through the
site and once they decide which trip they want, they can purchase it using Stripe, ensuring that their credit card information
isn't stored anywhere and it's completely safe. The idea for the site came to me when I was looking for vacations that allowed
pets and I realised how little resources there are for that.


### Database Information

TBA


### Technologies Used
Technology Name | Description
------------ | -------------
[ckeditor](https://ckeditor.com/) | CKEditor provides a RichText editor that easily integrates with django and gives a far more easily usable text editor that others. | I used CkEditor to create the editor for the ad creation feature of the Merchant dashboard
[Stripe](https://stripe.com/) | Stripe provides a payment platform to easily and safely process payments on django. | I used Stripe to setup the payment gateway for the vacation sales.
[Bootstrap](https://getbootstrap.com/) | Bootstrap gives the developer a grid like system to work with when using HTML. This allows for easier design and mobile compatibility. | I used Bootstrap to allow me to streamline the mobile and desktop designs and to ensure that they both were responsive no matter what device the user uses. |
[Google Fonts](https://fonts.google.com/) | Google Fonts provides the user with a wide variety of Fonts that anyone can use to customize their project more. | I used Google Fonts to give the website a bit personality, by not just using generic windows fonts. |
[Python](https://www.python.org/) | Python is a programming language that lets you work quickly and integrate systems more effectively. | I used Python for the backend of the website.
[SQLite](https://www.sqlite.org/index.html) | SQLite is a self-contained, high-reliability, embedded, full-featured, public-domain, SQL database engine. SQLite is the most used database engine in the world. | I used SQLite during the development of the website.


### Project Detailed explanation

The Project has two sides to it:

The Merchant side of the site provides a ad creation, editing and deletion feature. The merchant has a profile where he/she
can see how many ads they currently have live and have the option to edit them or delete them. The Ads creator provides the
Merchant with a RichText editor as well as the option to set a Title, Description, Start of the vacation, End of the vacation
and price. This information is them displayed in a table and detailed ad view.



### Deploying Application

The application was deployed using "Heroku". Heroku is an easy to use deployment platform that easily integrates with github respositories.

The application was deployed in this manner:
1. The project was setup with Github to create a repository online.
2. Then Heroku can be linked up with github.
3. I set up Heroku with the option that Github changes were directly pushed to the app to allow for an instant preview of the updated application.
4. I used mLab, a free MongoDB add-on, to run the database for the application. The integration is easy and with the usage of Flask it's very efficient.
5. The dev version of the app includes a 'env' file that emulates a virtual machine. This is not needed with the Heroku application seeing as the "requirements" file handles the same function as the env.


### Testing
Function Tested | How it was tested
------------ | -------------
Start Tour button | The start tour button launches the introjs javascript. The feature was tested using the Chrome developer tools. The Chrome developer tools let me see the button on different device screens and ensure that it works regardless of the device. Once it worked perfectly on chrome, I tested the website on an iPhone and Android device to ensure that it worked on Desktop and mobile devices.
Reset Charts button | The reset Charts button was tested using Chrome Developer tools. I used the Chrome browser to test that it reset the charts and that it didn't create any errors in the process. I could see that through the console that's part of the Chrome Browser. Once it worked on Chrome, I again tested the feature on an iPhone and an Android device, to ensure that it worked on Desktop and Mobile.
Interactive Charts | The interactive Charts were tested using the Chrome browser. I used the console feature of the developer tools to catch any errors that the script would output and fix them as they happened. I then proceeded to have friends of mine visit the website from their Desktop or Mobile devices and try the website out. They then let me know what errors they found and I had them re-create the errors for me and then fixed the problem. This method of testing worked well, because it gave me outside insight of the dashboard and the appearance of it.
HTML Dashboard | The Dashboard uses Bootstrap to create the grid system. I used Chrome Developer tools to test the design of the site on different sizes of screens. Chrome allows you to test any size of device screen which helped me ensure that the dashboard is compatible with Desktop and mobile devices.



### External Influences

The general design of the dashboard was influenced by the dashboard example given during the course. The html skeleton
was modified to fit my charts and the layout I required.

The font used in the chart headers is called [Parry Hotter](http://www.1001fonts.com/parry-hotter-font.html) and is free
to use for non-commercial projects.

