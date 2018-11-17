# GloLighting
See demo: https://glo-lighting.herokuapp.com/

Glolighting is a service providing a show case for the best lighting brands from all around the world. 
The site is specifically built to facilitate the needs of interieur architects and designers
looking to find amazing lamps for high-end projects such as hotels restaurants hospitals schools public buildings etc.
The user/designer/consumer should be able to browse easily and find image material to compile mood baords for client presentations. 
The user can see the retail prices displayed. however according to the users profession will be awarded varius discounts for each brand. 

## Brands
The Lighting brands/manufacturers/sellers can request an account with which they
will be able to login to upload their product images and all other relavent infos related to the product. 
The company Glo Lighting offers a service to clients who do not accomadate the skills to do this,
Depending on the ammount of work envolved in publishing the clients product an extra fee will be charge accordingly. 

## The Ux experience
A simple and clean cut user interface provides ease in finding decorative lamps
designers will be able to create mood boards and also purchase lamps directly.


## Existing Features
Consumer can add products to their shopping cart and aquire them using the payment system 'Stripe' this is all made easy not having to login and only having to fill out Name and Address after clicking Checkout, the clients payment details will not be retained. If a consumer closes the browser window and comes back the next day, their shopping basket will not have forgotten the product detail in the shopping cart.

## Features left to implement
In the future this website will expand to other catagories which will include other interior subjects: bathrooms, kitchens, floors, furniture, ceilings, curtains, wall paper, ceramics etc.

When a lighting manufacturer adds their product they will be given a standard list of 
information fields. Not all of the fields will be necessary to be filled in. Only Article No, type
and price. Custom fields can be added on request to Glo lighting.

The technologies applied in this project were: 

- [Python] (https://www.python.org/)
- [JQuery] (https://jquery.com)used to simplify image inzoom.
- [Django] (https://www.djangoproject.com/)immensely scalable!
- [Bootswatch] (https://getbootstrap.com/)
- [Javascript] (https://www.javascript.com/)
 
All other dependencies can be seen in requirements.txt.

The website has been extensively tested for the seller and the user.
At one point there was a bug in the deployed version, the checkout was returning "Payment unsucsessfull". Eventually a redeployment to the s3 bucket seemed to do the trick.
Other problems encountered were the type of error message returned when a user tried
to create a product without being logged in.

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
11.Go back to your local CLI and type sudo pip3 install dj_database_url
12.In CLI type the following pip3 install -r requirements.txt   ...this will install all dependencies
13.Inside top level file: bash.rc line 71 paiste your db url inbetween the ''.
14.Paiste in your AWS Keys in lines 66 to 68
15.Paiste in line 63 "ecommerce.settings.dev" without the quotes.
16.Paiste in lines 57 & 58 your stripe keys.

```
export STRIPE_PUBLISHABLE_KEY=''
export STRIPE_SECRET_KEY=''

export SECRET_KEY=""

export DJANGO_SETTINGS_MODULE=""

export AWS_ACCESS_KEY_ID=""
export AWS_SECRET_ACCESS_KEY=""
export AWS_STORAGE_BUCKET_NAME=""

export DATABASE_URL="postgres://itpqvhstgtdkua:53ea12f0aa7ce5f20e4eae4512742a23c243f0ec956e9b1f2e4daffe4500eb76@ec2-46-51-184-229.eu-west-1.compute.amazonaws.com:5432/d7qo7lufr7qd5u"
```

17. Ensure that you have all of the above keys copied and paisted into the "Config Vars" in Heroku.
18. Whilst inside Heroku, go to menu item "deployment" and click on the github icon then specify your github repository using the search button, once this is included
when ever you push to Github from your lopcal directory it will automatically push to Heroku. Use the following CLI commands:
    git status
    git add .
    git commit -m "The final push"
    git push 

19. Before anything will work you will have to migrate your db.sqlite using the following commands.
    python3 manage.py migrate
    python3 makemigrations

20. Inside Heroku-settings click "Open app" button on the top right hand side of the settings page.
21. It should now be running.

##Into the CMS Admin 127.0.0.1:8000/admin
22. using CLI command create a Super user:
    python3 manage.py createsuperuser
 	fill in username and password
23.Because your db is new it will also be empty so you won't see any products until you have added then yourself. Once you are logged in as superuser you need to firstly add a brand otherwise you will not be able to append a product.

22. If you want to run the app locally you will need to use the CLI command "python3 manage.py run" without the "" however it will still be pulling the data from your Heroku database and AWS-services
so you will need to un comment out the following:

# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'


TESTING:
The Checkout form has been manually checked.
If user does not fill in the fields he or she will be prompted to do so.
The email form recognizes if the email is correctly filled in.
--------------------------------------
Can a manufacturer edit his products.
Correct outcome YES
--------------------------------------
Can a maufacturer edit another brand which is not his own
in correct outcome YES.
if out come is YES This can be fixed
--------------------------------------
Does contact work correctly.
Correct outcome YES.
--------------------------------------
Can product be entered without all fields being entered
Correct outcome YES.
--------------------------------------
If product has no Article ref. and Price can it still be pulished.
Correct outcome NO.
--------------------------------------
Forgotten email address sent to user:



##Apps included with this project

Home
The Home App renders the index.html template, which in turn calls the base.html template to present a full webpage with navbar, content and footer.

#accounts
This app outlines the permissions of each manufacturer to a brand 
there is a one to many relationship between brand and maufacturer

#cart
The cart app shows us what we have in the cart including quantity
and a total ammount and from here we can check out

#checkout
As the title says this app allows us to fill in our name address and credit card
so that we can pay for the goods.

#products
In this app there are two templates which contain image and text data firstly
just the image of the product with no name or price.
#sendmail

Each app has a url.py file which is linked into the central nervous system of Django
in the ecommerce/settings/urls.py file.
in each app there is also a models.py and views.py file.
The models.py defines the field structure in the sqlite database, when ever we do a makemigration command any nieuw field will be added to the database.
The views.py holds the data formatted within a html cms presentation.
 
appears inbetween the block tags in the files which reside in the templates directory.

**Credits
Many thanks to Code Instutute in partular Brian, Katie, Matt, Richard, not forgetting the backup team who who were there after the course ended to help us on our way to finding solutions in solving code problems and last but not least my wife for having to put up with me with my late friday night
fellow student drinking sessions with Stein, Daan, Katie, Gijs, Dimitar and Gi.

The content material comes from Lzf the prices and information may not be completely accurate.

The concept of this website was inspired by architonic.com


