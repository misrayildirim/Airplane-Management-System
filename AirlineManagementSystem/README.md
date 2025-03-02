# Airline Management Sytsem

## Project Description
This project is a backend web application developed using Django REST Framework (DRF) to help an airline company manage its aircraft, flights, and passenger reservations. The system provides APIs for managing airplanes, flights, and reservations while ensuring data integrity through necessary validations.

## Technologies Used
-Django & Django REST Framework (DRF)
-SQLite for local development

## Setup instructions
### 1-Clone the Repository

--If we download the project directly to the computer
-cd C:\Users\Username\Masaüstü
-mkdir Airplane Management System  # Proje klasörünü oluştur
-cd AirlineManagementSystem 

### 2-Create Virtual Environment & Install Dependencies
-python -m venv venv
-source venv/Scripts/activate 
-pip install -r requirements.txt

### 3-Apply Migration 
python manage.py makemigrations
python manage.py migrate      

### 4-Run the Server
python manage.py runserver    

### API will be available at http://127.0.0.1:8000/

## Usage

## Airline API

| Method | Endpoint                    | Description                                   |
|--------|-----------------------------|-----------------------------------------------|
| GET    | /airplanes/                 | List all airplanes                            |
| POST   | /airplanes/                 | Create a new airplane                         |
| GET    | /airplanes/{id}/            | Retrieve an airplane by ID                    |
| PATCH  | /airplanes/{id}/            | Update an airplane by ID                      |
| DELETE | /airplanes/{id}/            | Delete an airplane by ID                      |
| GET    | /airplanes/{id}/flights/    | List all flights of an airplane by airplane ID|

## Flight API

| Method | Endpoint                    | Description                                      |
|--------|-----------------------------|--------------------------------------------------|
| GET    | /flights/                   | List all flights                                 |
| POST   | /flights/                   | Create a new flight                              |
| GET    | /flights/{id}/              | Retrieve a flight by ID                          |
| PATCH  | /flights/{id}/              | Update a flight by ID                            |
| DELETE | /flights/{id}/              | Delete a flight by ID                            |
| GET    | /flights/{id}/reservations/ | List all reservations of a flight by flight ID   |

## Reservation API

| Method | Endpoint                   | Description                              |
|--------|----------------------------|------------------------------------------|
| GET    | /reservations/              | List all reservations                   |
| POST   | /reservations/              | Create a new reservation                |
| GET    | /reservations/{id}/         | Retrieve a reservation by ID            |
| PATCH  | /reservations/{id}/         | Update a reservation by ID              |
| DELETE | /reservations/{id}/         | Delete a reservation by ID              |

## Validations:

* Ensure that there is at least a 1-hour difference between flights of the same aircraft.
* Ensure that flight times do not conflict.
* Ensure that the departure and destination locations are not the same.
* Ensure that the departure time is not in the past.
* Ensure that the flight capacity is not exceeded when making a reservation.


## Why Class-Based Views (CBV) over Function-Based Views (FBV)?

* Code Reusability: CBVs allow the creation of reusable components, making the codebase more maintainable and reducing duplication.
* Modularity: CBVs provide a modular approach to building views, making it easier to extend and customize views.
* Built-in Generic Views: Django's built-in generic views handle common tasks, reducing the need for boilerplate code.
* Separation of Concerns: CBVs organize code into methods, making the code more readable and understandable.
* Professionalism: CBVs offer a more structured and professional approach, which is beneficial for larger projects.
While FBVs are simpler, CBVs offer greater flexibility and scalability, making them a better fit for larger projects.* 