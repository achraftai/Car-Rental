# Car Rental


## This project uses Flask to connect an SQLite database to a Car Rental Website.  

**HTML and CSS:**
The website is comprised of HTML and CSS. On the main page, a table of bookings is displayed. The page also contains buttons that take users to separate pages to add new customers, vehicles, and bookings.

**Flask:**
Flask is used to read information from and add information to the SQLite database.

**SQLite Database:** 
The database consists of 3 tables (Customer, Vehicle, Booking). The Vehicle and Customer tables are linked to the Booking table via foreign key relationships. 

## Important SQL queries:


### The following query joins the 3 tables so that the relevant columns from each table can be displayed on the website's main page. 

*SELECT booking.id, booking.start_date, booking.end_date, customer.first, customer.last, customer.phone_number, customer.email, vehicle.make, vehicle.model*

*FROM booking*

*INNER JOIN vehicle ON booking.vin = vehicle.vin* 

*INNER JOIN  customer ON booking.license_number = customer.license_number;*


### The following query is used to count the number of rows in the Booking table so that we can use that information to set the Booking ID when we add a new record.

*SELECT COUNT ( * ) as row_count FROM booking;*



### The following query is used to insert new vehicle information recorded on the website into the Vehicle table using Flask. A customized version of this query is used to add records to the other 2 tables.

*INSERT INTO vehicle (vin, type, make, model, year) VALUES (?, ?, ?, ?, ?)', (vin, type, make, model, year);*





