@@ -0,0 +1,29 @@


## Setup

1. Clone the repository
2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  
Copy3. Install dependencies:
pip install -r requirements.txt
Copy4. Set up your MySQL database and update the `DATABASES` configuration in `settings.py`
5. Apply migrations:
python manage.py migrate
Copy6. Create a superuser:
python manage.py createsuperuser
Copy
## Running the server
python manage.py runserver
Copy
The server will start at `http://localhost:8000`.

## API Endpoints

- `/api/users/register/`: Register a new user
- `/api/users/login/`: Login and get an auth token
- `/api/trains/`: CRUD operations for trains (admin only)
- `/api/availability/check_availability/`: Check seat availability
- `/api/bookings/book_seat/`: Book a seat
- `/api/bookings/<id>/`: Get booking details
