# Testing

## Contents

This site has been tested using the following testing procedures

* [Code Validation](#Code-validation)  

* [Lighthouse Testing](#Lighthouse-Testing)

* [Browser Compatibility](#Browser-Compatibility)

* [Automatic Testing](#Automatic-Testing)

* [Manual Testing](#Manual-Testing)

* [Bug Reporting](#Bug-Reporting)


## Code Validation    

The site has been run through [W3C](https://validator.w3.org/), [WC3 CSS](https://jigsaw.w3.org/css-validator/), [JSHint](https://www.jshint.com/) javascript validator and CI [PEP8 validator](https://pep8ci.herokuapp.com/) 

**HTML** 

![Image of validator testing](README-images/w3c-validator-ke.png "Optional title")  

- No errors were present during validation.  
- 9 Warnings were present, 7 of which were aria label errors in navbar.
   
**CSS**  

![Image of css validator testing](README-images/w3c-css.png "Optional title")  

- No errors were present during validation.  
- 16 errors present in bootstrap CSS but no errors in base.css.  


**Javascript**  

There were no errors when running javascript file through JShint validator.  

**Python**  

I had to correct some errors regarding characters exceeding 79 and 2 lines not present between dunctions. There are no errors when running python files through pep8 validator, There were also no errors present in the terminal or console.  

![Image of pep8 validator testing](README-images/pep8-py.png "Optional title")


## Lighthouse Testing  

All pages passed lighthouse testing scoring particularly highly throughout.  

**Home**  
Desktop lighthouse score [here](README-images/light-home-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-home-mobile.png "Optional title")  

**Products**  
Desktop lighthouse score [here](README-images/light-products-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-products-mobile.png "Optional title")  

**Product detail**  
Desktop lighthouse score [here](README-images/light-product-detail-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-product-detail-mobile.png "Optional title") 

**Reviews**  
Desktop lighthouse score [here](README-images/light-reviews-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-reviews-mobile.png "Optional title") 

**About us**  
Desktop lighthouse score [here](README-images/light-about-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-about-mobile.png "Optional title")  

**Basket**  
Desktop lighthouse score [here](README-images/light-basket-desktop.png "Optional title")  

Mobile lighthouse score [here](README-images/light-basket-mobile.png "Optional title")  

Pages that require authentication??


## Browser Compatibility 
  
**Desktop**  

| Browser            | Version                                               | Bugs  |
| -------------      |:-------------:                                        | -----:|
| Google Chrome      | Version 112.0.5615.138 (Official Build) (64-bit)      | None  |
| Microsoft Edge     | Version 112.0.1722.58 (Official build) (64-bit)       | None  |
| Firefox            | 112.0.1 (64-bit)                                      | None  |  


**Mobile**  

| Device                   | Operating system | Bugs  |
| -------------            |:-------------:   | -----:|
| iPhone 14                | iOS 16.6.1       | None  |
| iPhone 14 pro            | iOS 16.6.1       | None  |
| iPad 10                  | iOS 16.6         | None  |
| Samsung Galaxy S22 ultra | Android 14.0     | None  |
| HONOR Magic5 Pro         | Android 13.0     | None  |
| iPhone 13 pro            | iOS 16.6         | None  |

## Automated Testing   

Is this required??

**Sanity Testing**   

**Feature Testing**    

**Endpoint Testing**  

 

## Manual Testing  

During the manual testing, I tested the sites functionality, usability and responsiveness.  

I have kept the basic functionality of the site the same throughout the entire project. Initially leaning towards a note/review site, moving towards a social media site that allows users to create, edit and delete posts.  


#### Functionality

**Home**

 - Navbar links - The feature works as expected. 
 - Interactive image gallery - The feature works as expected.
 - Browse Products button -  The feature works as expected.
 - Search bar -  The feature works as expected. 
 

**Profile** 

- Update Default Delivery Information - The feature works as expected.
- Accessing order history -  The feature works as expected.
- Country dropdown/Django countries -  The feature works as expected. 

**Products**

- Product images have black border on hover - The feature works as expected.  
- Bootstrap breakpoints - The feature works as expected.
- Edit and Delete buttons -  The feature works as expected, present for superusers, not present for normal users.
- Toast messages - The feature works as expected, both for edit and delete buttons.

  **Product details**

- Model fields for the product - All product fields ar avilable for selection.
- Keep shopping/Add to basket - Buttons work as expected regarding styling and url.
- Product images have black border on hover - The feature works as expected.
- Edit/Delete buttons for superusers - Present for superusers but not for standard users.

**Reviews**  

- Add review button - The feature works as expected, users are taken to the add review page.
- Review container - Users can enter title, comment and star rating.
- Edit review - The feature works as expected.
- Error handling regarding character limit - Users are limited to the number of characters they can add to review.
- Time display - The feature works as expected, time is displayed as (time ago) rather than actual date.

**About** 

- Rotating logo - The feature works as expected.
- Contact us form - Users can add to contact form.
- send message button - Button submits form and displays toast message.

**Basket** 

- Product info displayed in basket - Product info is present.
- View embroidery text model - The feature works as expected.
- Quantity buttons - quantity is reflected by use of buttons.
- Update/remove buttons - The feature works as expected.
- Keep shopping/Secure checkout buttons - The feature works as expected, buttons take user to correct url.

**Checkout** 
- User details - The feature works as expected, form populates.
- Delivery details - The feature works as expected, form populates.
- payment details - The feature works as expected, form populates.
- order summary - Product info is present.

**Checkout Success** 
- Thank you message - The feature works as expected.
- order info - The feature works as expected, content is present.
- toast message - The feature works as expected.
- confirmation email - User recieves confirmation email.



**Usability**  

During testing;

- some users felt that the image carousel would be better on smaller devices instead of the interactive images.
- It was noted that the collapsible navbar wasnt very clear and needed to be a lighter colour.
- Some users felt that the collapsible navbar needed titles instead of just icons.
- Some users felt that the stars on the review page needed a background colour to enhance colour contrast.  


**Responsiveness**  

I used the following break points for responsiveness.  

- 500px  
- 768px  
- 992px
- 1090px
- 1264px
- 1492px

Generic bootstrap breakpoints were also used throughout the site.  

## Bug Reporting
Throughout the development phase of the site, I came across a variety of different bugs/errors that eventually overcame.  

**resolved**  
-	static files temporary fix followed by permanent fix, I added disable static to config vars. However, the introduction of AWS S3 bucket was more of a permanent solution.  
-	import issue with home.views
-	Allowed hosts added for local testing
-	Css folder not registering causing console error
-	404 error when logging user in
-	Application error when logging in user/superuser, hadn’t migrate local database.
-	Heroku migrations error




**Unresolved**




[Back to README.md](https://github.com/ojalaw/knockout-embroidery-MP4/blob/main/README.md)
