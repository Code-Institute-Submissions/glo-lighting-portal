# ARCHIMANIC
TEMPLATE BUILT FROM GROUND UP...<br/>
See demo: https://glo-lighting.herokuapp.com/
<a href="http://www.gowild.nl/archimanic/designs.html" >
Click here to see the initial designs</a>

The original concept for this ecommerce website was named "glo lighting" however it was decided to change the name to "Archimanic" and incorperate other related categories. At present this project contains only lighting content but 
Furniture and Bathrooms has yet to be added to the products/model.py

Archimanic is a service providing a show case for the ***best brands from all around the world.*** 
The site is specifically built to facilitate the needs of interieur architects and designers
looking to find amazing products for high-end projects such as hotels restaurants hospitals schools public buildings etc. The landing pages display images of the products containing no name or price so that the designer is not swayed or distracted into choosing price above design. The designer must first fall in love with the product.

The user/designer/consumer should be able to browse easily and find image material to compile mood boards for client presentations. 
The price for each lamp is displayed after the user clicks on a lamp. Retail prices are displayed.
According to the users profession will be awarded various discounts for each brand.

Architects and interior architects can register their projects and recieve commission.

### Discount:

1. Architects max 10-20%
2. Interior architects max 10-50%
3. Instillators/electricions max 20-30%
4. Retailers max 10-50%
5. Consumers max 10%

Apply for discount form 

## Lighting Brands/Manufactures

The manufacturers/sellers can request a seller account. The admin will register them under the name of their brand after a contract has been signed. 

admin: Admin
password:Lamps69*^<br/>
username: Sandro password: lzfLamps69*^ 

A user name & password will then be forwarded to the new owner of the account. 
The seller will then be able to login write and edit text and product photos.
The company Archimanic offers a service to clients who do not accomadate the skills to do this,
Depending on the ammount of work envolved in publishing the clients products an extra fee will be charged accordingly. 

## The Ux experience
A simple and clean cut user interface provides ease in finding in this case decorative lamps
designers will be able to create mood boards and also purchase lamps directly.

## Existing Features
- One categorie available. "LIGHTING".
- Payment system via 'Stripe'.

- Payment is simplified by not having to fill in register forms except for at the Checkout, this encourages the buyer to complete the transaction.

- The clients payment details will not be retained.
    If a consumer closes the browser window and comes back the next day, their shopping basket will not have forgotten the product details in the shopping cart.

- search function. </li>
- jQuery lightbox Featherlight. has been integrated with the detail photos which means you can enlarge the thumbnail by clicking on it.

- Articles.(blog) Read the text in the footer to find out more.</li>

- Email.
- Register.
- Login.

## Features left to implement
- In the future this website will expand its contents to other catagories..
- A pop-up to enlarge detail images.<br>
The technologies applied in this project were: 

- [Python] (https://www.python.org/)
- [JQuery] (https://jquery.com)used to simplify image inzoom.
- [Django] (https://www.djangoproject.com/)immensely scalable!
- [Bootswatch] (https://getbootstrap.com/)
- [Javascript] (https://www.javascript.com/)
 
All other dependencies can be seen in requirements.txt.

The website has been extensively tested for the seller and the user.
At one point there was a bug in the deployed version, the checkout was returning "Payment unsucsessfull". Eventually a redeployment to the s3 bucket seemed to do the trick.
Other problems encountered were the type of error message returned when a user tried to create a product without being logged in.

## Deployment.
1. Clone or download github version
2. Register and login to AWS services account: https://s3.console.aws.amazon.com/s3/
3. Create a bucket and make a note of the AWSSecretKey and the AWSSecretKey.
4. In this bucket you will need to upload the static files from your local directory.
5. Register and login to Heroku, You can create an app there: https://dashboard.heroku.com/apps
6. Going back to your local files In CLI follow these instructions:
    A) type in: login heroku
    B) type in: heroku create "your_db" --region eu
    c) type in: heroku addons:create heroku-postgresql:hobby-dev
7. Next we need to register a payments account with stripe.
8. https://dashboard.stripe.com/account/apikeys copy your Publishable key and secret key. You find these keys by clicking on 'developers' on the left hand side of your dashboard.
9. Go back to Heroku https://dashboard.heroku.com/apps, open dashboard and then db.
10. Click on settings then on 'Reveal Config Vars' button. You can then copy the database url.
11. Go back to your local CLI and type sudo pip3 install dj_database_url
12. In CLI type the following pip3 install -r requirements.txt   ...this will install all dependencies
13. Inside top level file: bash.rc line 71 paiste your db url inbetween the ''.
14. Paiste in your AWS Keys in lines 66 to 68
15. Paiste in line 63 "ecommerce.settings.dev" without the quotes.
16. Paiste in lines 57 & 58 your stripe keys.

```
export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export SECRET_KEY=""

export DJANGO_SETTINGS_MODULE=""

export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_STORAGE_BUCKET_NAME=""

export DATABASE_URL="postgres://itpqvhstetc"
```

17. Ensure you have all of the above keys copied and paisted into the "Config Vars" in Heroku.
18. Whilst inside Heroku, go to menu item "deployment" and click on the github icon then specify your github repository using the search button, once this is included
when ever you push to Github from your local directory it will automatically push to Heroku. Use the following CLI commands:
    git status
    git add .
    git commit -m "The final push"
    git push 

19. Before anything will work you will have to migrate your db.sqlite using the following commands.
    
    python3 manage.py makemigrations<br/>
    python3 manage.py migrate

20. Inside Heroku-settings click "Open app" button on the top right hand side of the settings page.
21. It should now be running.

22. using CLI command python3 manage.py createsuperuser:
 	fill in username and password.Go into the CMS Admin 127.0.0.1:8000/admin.
23.Because your db is new it will also be empty, that means you won't see any products until you have added them. Once you are logged in as superuser you need to firstly add a brand. Doing this enables you to append a product.

22. If you want to run the app locally you will need to use the CLI command "python3 manage.py run" without the "" however it will still be pulling the data from your Heroku database and AWS-services
so you will need to un comment the following:

#### STATIC_URL = '/static/'
#### MEDIA_URL = '/media/'


#### TESTING:
<a href="https://gowild.nl/glolighting/tests.html" >Click here to see W3 tests carried out</a><br>

#### ISSUES:
The link to google font "Barlow" needed to have the " | " replaced with "%7C" to validate.

The Django framework has it's own built in automated test system, 
Each test can be found inside the app directories in tests.py. 
In order to run tests, 
Install and activate virtualenv before typing the following command "python3 manage.py accounts" this should run the tests for the accounts app.
Repeat this for other apps replacing the name of the after "python3 manage.py _______".

#### Apps included with this project

Home
The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#### accounts
This app outlines the permissions of each manufacturer to a brand 
there is a one to many relationship between brand and maufacturer

#### cart
The cart app shows us what we have in the cart including quantity
and a total ammount and from here we can check out

#### checkout
As the title says this app allows us to fill in our name address and credit card
so that we can pay for the goods.

#### products
In this app there are two templates which contain image and text data firstly
just the image of the product with no name or price.
#sendmail

#### search
This Search function is a filter which returns product items

#### Furniture
underconstruction

#### Bathrooms
underconstruction

#### Articles
Is actually a blog

Each app has an url.py file which is linked into the central nervous system of Django in the ecommerce/settings/urls.py file.
 <br/>
Each app/directory has a models.py and views.py file.
The models.py defines the field structure in the postgres database, when ever a "python3 manage.py makemigrations" followed buy "python3 manage.py migrate"  command a nieuw field will be added to the database.
The views.py file contains the functions which inject data into the template files between the {% block content %} tags.

#### Credits
Many thanks to Code Institute in particular Brian, Katie, Matt, Richard, not forgetting the backup team who were there after the course had finished.

The content material comes from Lzf the prices and information are fictitious.

The concept of this website was inspired by architonic.com


