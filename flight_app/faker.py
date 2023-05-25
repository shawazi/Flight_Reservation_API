'''
    # https://faker.readthedocs.io/en/master/
    $ pip install faker # install faker module
    python manage.py flush # delete all exists data from db. dont forget: createsuperuser
    python manage.py shell
    from flight_app.faker import run
    run()
    exit()
'''


from .models import Flight
import random
from django.utils import timezone
from datetime import datetime
from faker import Faker

def run():
    airlines = [("Spirit", "NK"), ("Frontier", "F9"), ("American", "AA"), ("United", "UA")]
    cities = ["New York", "Miami", "Boston", "Chicago", "Los Angles", "Dallas", "Denver"]

    fake = Faker() 
    for _ in range(200):
        flight = Flight()
        number = random.randint(100,999)
        airline = random.choice(airlines)
        flight.airlines = airline[0]
        flight.flight_number = airline[1] + str(number)
        places = random.sample(cities,2)
        flight.departure_city = places[0]
        flight.arrival_city = places[1]
        flight.date = fake.date_between(start_date=datetime(2023,3,1), end_date=datetime(2023,7,31))
        flight.time = fake.time()
        flight.save()

    print('Flights created')