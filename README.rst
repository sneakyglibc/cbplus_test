Welcome to Cb plus test's documentation!
----------------------------------------


The test
========

- :download:`Cb plus test <files/test.pdf>`


`The production url of the project <https://cbplustest.herokuapp.com/index/>`_
==============================================================================


How to launch the project locally
=================================



Explanation of the project
==========================

In general the code will scale with no problem, if they are billions of row it can be a problem but in that case, I
don't think we need to return all the rows and maybe we have to use a history table in order to stock all the unused
rows. The evolution will depends a lot about the product and the use in the future.

Technically how the settings are handle in local, test or production has to be improved.

Model
*****

I created a django model with only the fields needed a creation date, a reference id and an expiry date.
The creation date will be used as a filter and to determine which model is the last distinct by the reference id.
As the creation date, the reference id and the expiry date will be used as filter by the api, they are index.

I added a validator for the reference id field in order to check if it has 13 digits for the creation.
The expiry date is a date field, it can be change to a datetime field if we need more precision.

Api
***

I choose to create a rest framework api because it allows me to separate the front and the back. If in the future we
have to change the front we can without the back affected. Also it is really simple to create a scalable and robust
back end with a lot of automatic feature.

I created one view with two endpoints:
    - A POST one in order to create stock reading objects, the serializer will automatically launch the check of the data.
    - A GET one in order to list all the stock reading objects, there are 3 filters reference_id, last (last stock readings distinct by reference id) and cursor (get all the stock readings after the uuid object date).

Test
****

All the back end feature is tested by django tests. They can be improved by using factory or mixer in order to create
a bulk of models instead of manually.

Front
*****

It's a html page where you can create a stock reading with a form and there is a list of the last stock readings.
The rows of the table are interactive if you click on it it will show you the previous stock readings of a reference id.

Sync with a mobile app
**********************

Sync a data with a mobile app is more complicated than with a browser because of the discontinuity of the internet
connection.

The solution that I propose is to use the http protocol in a secure way with a push notification system (kafka).

The mobile has not internet:
    - The mobile app can create stock readings in a temporary table and send them when he has a connection. The server will answer with an uuid for the objects and the mobile app can add the stock readings to his "real" table and erase the rows in the temporary table.
    - The mobile app retrieves internet and can ask the server all the missing stock readings with the uuid of the last stock readings receives from the server. If they are too much data a limit can be used in order to not get all the data at one and the mobile app will call the server until it has all the data.

The mobile has internet:
    - The mobile app receives notifications from the server each time there are new data created (by another mobile app).
    - The mobile app can ask the server all the missing stock readings with the uuid of the last stock readings receives from the server. If they are too much data a limit can be used in order to not get all the data at one and the mobile app will call the server until it has all the data.
