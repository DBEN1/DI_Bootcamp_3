import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bike_store.settings')

import django
django.setup()
from rent.models import Customer, Address, RentalStation, Vehicle, VehicleType, VehicleSize
from faker import Faker

fake = Faker()
def create_vehicles(number):
    vehicle_types = VehicleType.objects.all()
    vehicle_sizes = VehicleSize.objects.all()

    for _ in range(number):
        vehicle = Vehicle(
            vehicle_type=fake.random_choice(vehicle_types),
            date_created=fake.date_this_decade(),
            real_cost=fake.decimal(l_digits=4, r_digits=2, positive=True),
            size=fake.random_choice(vehicle_sizes)
        )
        vehicle.save()

    print(f"CREATED {number} Vehicles")

if __name__ == '__main__':
    create_vehicle_types_and_sizes()
    create_rental_stations(10)  # for example, create 10 rental stations
    create_vehicles(50)  # for example, create 50 vehicles
    create_customers(100)  # as you've already provided
