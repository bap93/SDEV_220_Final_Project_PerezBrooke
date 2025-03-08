# SDEV_220_Final_Project_PerezBrooke
Final project for sdev 220 course

## Running the Project
```
python3 -m venv venv
. ./venv/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
**NOTE:** The name of your python interpreter may vary depending on your operating system.

## Changing the admin password
In order to access the admin page you will want to change the admin password. You can do that like so:
```
python manage.py changepassword admin
```


## Project Summary

This project allows for customers of the Made-up Lake Boathouse to easily make reservation requests and for the admin or employee to easily contact the customer via email or delete request.

## Project Layout

### Landing Page
This page gives information regrading boat reservation along with a button that when clicked will allow the user to submit a reservation request. The reservation request is a modal form that when submitted takes the user to the add_reservation_request_success page where the form is echoed back and they are presented with a success message. The boathouse logo on the top left can take the user back to the reservation_info page. The reservation_info page also include admin login via a button on the top right of page in the navbar. When clicked the user will be asked to login via a login page if they are not logged in. If they are already logged in the user will be presented with the admin_reservation_list page.
### Admin Page
The admin_reservation_list page allows for the user to easily access the reservation requests. The admin can see all the information about the reservation from the database. This information includes: first name, last name, age, email, phone number, party size, date of desired reservation, number of kayaks, number of canoes and numbers of paddle boards. The user can delete the request but do note that it is also deleted from the database. The user can email the customer with the use of the email button. On the top of the page is a logout button that logs the user out of the admin_reservation_list and redirects the user to the landing page reservation_info. 
