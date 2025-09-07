import json
import os

class Transport:
    def __init__(self, model, speed):
        self.model = model
        self.speed = speed

    def info(self):
        return f"Model: {self.model}, Speed: {self.speed} km/h"
    


class Car(Transport):
    def __init__(self, model, speed, fuel_type):
        super().__init__(model, speed)
        self.fuel_type = fuel_type

    def info(self):
        base_info = super().info()
        return f"{base_info}, Fuel Type: {self.fuel_type}"
    
class Bicycle(Transport):
    def __init__(self, model, speed, bike_type):
        super().__init__(model, speed)
        self.bike_type = bike_type

    def info(self):
        base_info = super().info()
        return f"{base_info}, Bike Type: {self.bike_type}"
    

class TransportSystem():
    def __init__(self):
        if os.path.exists("transports.json"):
            with open("transports.json", "r") as f:
                data = json.load(f)
                self.transports = [Car(**item) if item.get("fuel_type") else Bicycle(**item) for item in data]
        else:
            self.transports = []

    def save(self):
        with open("transports.json", "w") as f:
            json.dump([t.__dict__ for t in self.transports], f)

    

    def add_transport(self, transport):
        if not transport:
            print("Invalid transport.")
            return
        self.transports.append(transport)
        self.save()
        print(f"Added: {transport.info()}")

        
    def show_all(self):
        if not self.transports:
            print("No transports available.")
            return
        for i, t in enumerate(self.transports):
            print(f"{i + 1}. {t.info()}")





def menu():
    system = TransportSystem()
    while True:
        print("\nMenu:")
        print("1. Add Car")
        print("2. Add Bicycle")
        print("3. Show All Transports")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            model = input("Enter car model: ")
            if not model:
                print("Model cannot be empty.")
                continue
            try:
                speed = int(input("Enter car speed: "))
                if speed <= 0:
                    print("Speed must be positive.")
                    continue
                
            except ValueError:
                print("Invalid speed. Please enter a number.")
                continue
            fuel_type = input("Enter car fuel type: ")
            if not fuel_type:
                print("Fuel type cannot be empty.")
                continue
            transport = Car(model, speed, fuel_type)
            system.add_transport(transport)
        elif choice == "2":
            model = input("Enter bicycle model: ")
            if not model:
                print("Model cannot be empty.")
                continue
            try:
                speed = int(input("Enter bicycle speed: "))
                if speed <= 0:
                    print("Speed must be positive.")
                    continue
            except ValueError:
                print("Invalid speed. Please enter a number.")
                continue
            bike_type = input("Enter bicycle type: ")
            if not bike_type:
                print("Bicycle type cannot be empty.")
                continue
            transport = Bicycle(model, speed, bike_type)
            system.add_transport(transport)
        elif choice == "3":
            system.show_all()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

menu()