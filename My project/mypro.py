from pathlib import Path

text = """MOBILEMART HOMEPAGE - BEGINNER HTML NOTES
=============================================

1. HEAD SECTION
---------------
The <head> section contains information about the webpage that is not directly displayed on the page.

<title>Homepage</title>
Sets the title displayed on the browser tab.

<link rel="stylesheet" ...>
Used to connect CSS files to the HTML page.

Bootstrap CSS:
The Bootstrap CDN link connects Bootstrap to the webpage.
Bootstrap provides ready-made buttons, navigation bars, cards, containers, forms, spacing and responsive layouts.

<link rel="stylesheet" href="homepage.css">
Connects our own custom CSS file called homepage.css.

------------------------------------------------------------

2. BODY SECTION
---------------
<body>
Contains everything visible on the webpage.

Examples:
- Navigation bar
- Images
- Text
- Buttons
- Products
- About section
- Contact section
- Footer

------------------------------------------------------------

3. NAVIGATION BAR
-----------------
<nav class="navbar navbar-expand-lg navbar-dark bg-dark sticky-top">

navbar
Indicates that this is a Bootstrap navigation bar.

navbar-expand-lg
The navigation expands on large screens and can collapse on smaller screens.

navbar-dark
Makes the navigation text suitable for a dark background.

bg-dark
Gives the navigation bar a dark background.

sticky-top
Keeps the navigation bar at the top while scrolling.

------------------------------------------------------------

4. CONTAINER-FLUID
------------------
<div class="container-fluid">

container-fluid uses almost the entire width of the screen.

container provides a responsive maximum width.
container-fluid uses the full available width.

------------------------------------------------------------

5. WEBSITE LOGO AND NAME
------------------------
<a class="navbar-brand fw-bold" href="#">

navbar-brand
Styles the website brand.

fw-bold
Makes the text bold.

href="#"
Links to the top/default location of the page.

------------------------------------------------------------

6. LOGO IMAGE
------------
<img src="sk logo.png" class="logo-img me-2">

<img>
Used to display an image.

src
Specifies the image location/name.

class="logo-img"
Custom CSS class used to control the logo design.

me-2
Bootstrap margin-end class. It adds space after the logo.

------------------------------------------------------------

7. NAVIGATION LINKS
-------------------
Example:

<li class="nav-item">
    <a class="nav-link" href="#products">Products</a>
</li>

<li>
Represents one item in a list.

nav-item
Bootstrap class for a navigation item.

<a>
Creates a hyperlink.

nav-link
Bootstrap styling for navigation links.

href="#products"
Moves the page to the element having id="products".

Example:
<a href="#products">Products</a>
connects to:
<section id="products">

------------------------------------------------------------

8. ACTIVE LINK
--------------
<a class="nav-link active" aria-current="page" href="#banner">Home</a>

active
Shows that Home is the active navigation link.

aria-current="page"
Helps accessibility tools understand the current page/location.

------------------------------------------------------------

9. SEARCH FORM
--------------
<form class="d-flex me-3" role="search">

<form
Creates a form.

d-flex
Uses Bootstrap Flexbox.

me-3
Adds margin at the end.

role="search"
Indicates that the form is used for searching.

------------------------------------------------------------

10. SEARCH INPUT
----------------
<input class="form-control me-2"
       type="search"
       placeholder="Search mobiles"
       aria-label="Search">

type="search"
Creates a search input.

placeholder
Displays temporary text inside the input.

form-control
Bootstrap styling for form inputs.

------------------------------------------------------------

11. SEARCH BUTTON
-----------------
<button class="btn btn-outline-light" type="submit">Search</button>

btn
Basic Bootstrap button class.

btn-outline-light
Creates a light outlined button.

type="submit"
Submits the form.

------------------------------------------------------------

12. LOGOUT BUTTON
-----------------
<a href="loginpage.html" class="btn btn-outline-danger">Logout</a>

This creates the Logout button.

btn
Bootstrap button styling.

btn-outline-danger
Creates a red outlined button.

IMPORTANT:
For a website, it is better to use a relative path such as:

href="loginpage.html"

instead of a Windows path such as:

D:\\Krishna Documents\\FULL STACK DEVELOPMENT\\Frontend\\loginpage.html

------------------------------------------------------------

13. BANNER SECTION
------------------
<header id="banner">

The <header> contains the main introductory area of the website.

id="banner"
Gives the section a unique ID.

This allows a navigation link such as:
href="#banner"
to move to this section.

------------------------------------------------------------

14. BANNER OVERLAY
------------------
<div class="banner-overlay text-center text-white">

banner-overlay
Custom CSS class used for the banner design/overlay.

text-center
Centers the text.

text-white
Makes the text white.

------------------------------------------------------------

15. MAIN HEADING
----------------
<h1 class="display-4 fw-bold">Grab the Best Mobile Deals</h1>

<h1>
Largest and most important heading.

display-4
Bootstrap display heading size.

fw-bold
Makes the text bold.

------------------------------------------------------------

16. PARAGRAPH
-------------
<p class="lead">...</p>

<p>
Creates a paragraph.

lead
Bootstrap class that makes the paragraph larger and more noticeable.

------------------------------------------------------------

17. SHOP NOW BUTTON
-------------------
<a href="#products" class="btn btn-danger btn-lg mt-3">Shop Now</a>

href="#products"
Moves the user to the Products section.

btn
Bootstrap button style.

btn-danger
Creates a red Bootstrap button.

btn-lg
Creates a large button.

mt-3
Adds margin above the button.

------------------------------------------------------------

18. PRODUCTS SECTION
--------------------
<section id="products">

Contains the mobile products.

The navigation link:
<a href="#products">
moves the page to this section.

------------------------------------------------------------

19. CONTAINER
-------------
<div class="container">

Bootstrap container keeps the content properly aligned and responsive.

------------------------------------------------------------

20. PRODUCTS HEADING
--------------------
<h2 class="text-center mb-4">Mobiles</h2>

<h2>
Second-level heading.

text-center
Centers the heading.

mb-4
Adds bottom margin.

------------------------------------------------------------

21. ROW
-------
<div class="row g-4 justify-content-center product-grid">

row
Bootstrap row used to arrange columns.

g-4
Adds spacing/gap between columns.

justify-content-center
Centers the columns horizontally.

product-grid
Custom CSS class for product grid styling.

------------------------------------------------------------

22. PRODUCT COLUMN
------------------
<div class="col-6 col-md-4 col-lg-3">

This controls how much space each product takes.

col-6
On small screens, a product takes 6 out of 12 columns.
Therefore, 2 products can appear in one row.

col-md-4
On medium screens, a product takes 4 out of 12 columns.
Therefore, 3 products can appear in one row.

col-lg-3
On large screens, a product takes 3 out of 12 columns.
Therefore, 4 products can appear in one row.

This is called RESPONSIVE DESIGN.

------------------------------------------------------------

23. PRODUCT CARD
----------------
<div class="card product-card h-100 shadow-sm">

card
Bootstrap component used to create a card.

product-card
Custom CSS class.

h-100
Makes the card use 100% of the available height.

shadow-sm
Adds a small shadow.

------------------------------------------------------------

24. PRODUCT IMAGE
-----------------
<img src="iPhone 14 Pro.jpg"
     class="card-img-top product-img"
     alt="iPhone 15">

card-img-top
Bootstrap class for an image at the top of a card.

product-img
Custom CSS class for controlling image size.

alt
Alternative text for the image.

IMPORTANT:
It is better to use a relative path:
src="iPhone 14 Pro.jpg"

if the image is stored in the same folder as the HTML file.

------------------------------------------------------------

25. PRODUCT CARD BODY
---------------------
<div class="card-body d-flex flex-column text-center">

card-body
Contains the main content of the card.

d-flex
Uses Flexbox.

flex-column
Places items vertically.

text-center
Centers the text.

------------------------------------------------------------

26. PRODUCT NAME
----------------
<h5 class="card-title">iPhone 15</h5>

card-title
Bootstrap styling for a card title.

------------------------------------------------------------

27. PRODUCT PRICE
-----------------
<p class="price mb-2">₹65,000</p>

price
Custom CSS class.

It can be used to change font size, weight, color and spacing.

mb-2
Adds bottom margin.

------------------------------------------------------------

28. BUY NOW BUTTON
------------------
<button class="btn btn-primary buy-btn mt-auto"
        data-name="iPhone 15"
        data-price="65000">
    Buy Now
</button>

btn
Bootstrap button styling.

btn-primary
Usually creates a blue button.

buy-btn
Custom CSS/JavaScript class.

mt-auto
Automatically pushes the button toward the bottom when Flexbox is used.

------------------------------------------------------------

29. DATA ATTRIBUTES
-------------------
data-name="iPhone 15"
data-price="65000"

These are custom HTML data attributes.

They can be accessed using JavaScript.

Example:
button.dataset.name
returns:
iPhone 15

button.dataset.price
returns:
65000

These are useful for creating a shopping cart.

------------------------------------------------------------

30. ABOUT SECTION
-----------------
<section id="about" class="bg-light">

id="about"
Used for navigation.

bg-light
Bootstrap class that gives a light background.

------------------------------------------------------------

31. mx-auto AND col-lg-8
------------------------
<p class="mx-auto col-lg-8">

mx-auto
Adds automatic left and right margins and helps center the element.

col-lg-8
On large screens, the paragraph uses 8 out of 12 columns.
This prevents the paragraph from becoming too wide.

------------------------------------------------------------

32. CONTACT SECTION
-------------------
<section id="contact">

Contains contact information.

The navigation link:
<a href="#contact">Contact</a>
moves the page to this section.

------------------------------------------------------------

33. MAILTO
----------
<a href="mailto:support@skmobilemart.com">

mailto:
Opens the user's default email application.

The user can then send an email to:
support@skmobilemart.com

------------------------------------------------------------

34. TOAST
---------
A Toast is a small notification that appears on the screen.

Example:
Item added to cart!

The following code creates a Bootstrap Toast:

<div id="cartToast" class="toast ...">

It can be shown after the user clicks Buy Now.

------------------------------------------------------------

35. TOAST MESSAGE
-----------------
<div class="toast-body" id="toastMessage">
    Item added to cart!
</div>

toast-body
Bootstrap styling for the Toast message.

id="toastMessage"
Gives the message a unique ID.

JavaScript can change the message.

Example:
"iPhone 15 added to cart!"

------------------------------------------------------------

36. CLOSE BUTTON
----------------
<button type="button"
        class="btn-close btn-close-white me-2 m-auto"
        data-bs-dismiss="toast"
        aria-label="Close">

btn-close
Bootstrap close button.

btn-close-white
Makes the close icon white.

data-bs-dismiss="toast"
Tells Bootstrap that clicking the button should close the Toast.

------------------------------------------------------------

37. FOOTER
----------
<footer>

The footer is the bottom section of the website.

Example:
© 2026 SKMobileMart. All rights reserved.

------------------------------------------------------------

38. IMPORTANT HTML ATTRIBUTES
-----------------------------

id
--
Provides a unique name to an element.

Example:
<section id="products">

Used with:
href="#products"

class
-----
Used to apply CSS or Bootstrap styles.

Example:
class="btn btn-primary"

href
----
Specifies where a link should go.

Example:
href="#about"

src
---
Specifies the location of an image.

Example:
src="sk logo.png"

alt
---
Provides alternative text for an image.

Example:
alt="iPhone 15"

data-name
---------
Stores custom data in an HTML element.

data-price
----------
Stores the product price.

------------------------------------------------------------

39. BOOTSTRAP CLASSES USED IN THIS PROJECT
------------------------------------------

navbar
navbar-expand-lg
navbar-dark
bg-dark
sticky-top
container-fluid
navbar-brand
fw-bold
navbar-nav
me-auto
mb-2
mb-lg-0
nav-item
nav-link
active
d-flex
me-3
form-control
me-2
btn
btn-outline-light
btn-outline-danger
text-center
text-white
display-4
lead
btn-danger
btn-lg
mt-3
container
mb-4
row
g-4
justify-content-center
col-6
col-md-4
col-lg-3
card
h-100
shadow-sm
card-img-top
card-body
flex-column
card-title
mb-2
btn-primary
mt-auto
bg-light
mx-auto
col-lg-8
toast-container
position-fixed
bottom-0
end-0
p-3
toast
text-bg-success
border-0
align-items-center
btn-close
btn-close-white
m-auto
mb-0

------------------------------------------------------------

40. CUSTOM CLASSES USED
-----------------------

These classes are probably defined in homepage.css:

logo-img
banner-overlay
product-grid
product-card
product-img
price
buy-btn

Bootstrap provides the general design.
homepage.css provides your custom design.

------------------------------------------------------------

41. RESPONSIVE DESIGN
---------------------

Bootstrap makes the webpage responsive.

For example:

col-6 col-md-4 col-lg-3

means:

Small screen:
2 products per row

Medium screen:
3 products per row

Large screen:
4 products per row

This helps the website work on:
- Mobile phones
- Tablets
- Laptops
- Desktop computers

------------------------------------------------------------

42. OVERALL PAGE STRUCTURE
--------------------------

HTML
 |
 +-- HEAD
 |    |
 |    +-- Title
 |    +-- Bootstrap CSS
 |    +-- Homepage CSS
 |
 +-- BODY
      |
      +-- NAVBAR
      |    +-- Logo
      |    +-- Home
      |    +-- Products
      |    +-- About
      |    +-- Contact
      |    +-- Search
      |    +-- Logout
      |
      +-- BANNER
      |    +-- Heading
      |    +-- Description
      |    +-- Shop Now
      |
      +-- PRODUCTS
      |    +-- iPhone 15
      |    +-- Samsung Galaxy S24
      |    +-- OnePlus 12
      |
      +-- ABOUT
      |
      +-- CONTACT
      |
      +-- CART TOAST
      |
      +-- FOOTER

------------------------------------------------------------

43. SIMPLE EXPLANATION OF THE WEBSITE
--------------------------------------

This HTML creates a mobile shopping website called:

SK MobileMart

The website contains:

1. Navigation bar
2. SK logo and MobileMart name
3. Home link
4. Products link
5. About link
6. Contact link
7. Search box
8. Logout button
9. Promotional banner
10. Shop Now button
11. Mobile product cards
12. Product prices
13. Buy Now buttons
14. About Us section
15. Contact information
16. Cart notification Toast
17. Footer

Bootstrap is used to make the webpage responsive and attractive.

homepage.css is used for custom styling.

JavaScript can later be added to make features such as:
- Search
- Buy Now
- Cart
- Login/logout
- Product filtering
- Toast notifications

interactive.

------------------------------------------------------------

44. BEGINNER KEY POINTS TO REMEMBER
------------------------------------

HTML = Structure of the webpage

CSS = Design and appearance

Bootstrap = Ready-made CSS components/classes

JavaScript = Makes the webpage interactive

<header> = Header/banner area

<nav> = Navigation bar

<section> = Separate content section

<div> = General container/group

<a> = Link

<img> = Image

<h1>, <h2>, <h5> = Headings

<p> = Paragraph

<button> = Button

<form> = Form

<footer> = Bottom section

id = Unique identifier

class = Styling/group identifier

href = Link destination

src = Image/file location

alt = Alternative image text

data-* = Custom data stored in HTML

------------------------------------------------------------

45. IMPORTANT NOTE ABOUT YOUR CODE
-----------------------------------

Your HTML is good for a beginner Bootstrap project.

However, avoid Windows absolute paths such as:

D:\\Krishna Documents\\FULL STACK DEVELOPMENT\\Frontend\\loginpage.html

and:

d:\\Krishna Documents\\FULL STACK DEVELOPMENT\\Frontend\\iPhone 14 Pro.jpg

Use relative paths when possible.

For example:

href="loginpage.html"

src="iPhone 14 Pro.jpg"

This makes your project easier to move to another computer and upload to GitHub.

============================================================
END OF NOTES
============================================================
"""

path = Path("/mnt/data/MobileMart_Beginner_HTML_Notes.txt")
path.write_text(text, encoding="utf-8")
print(path)
