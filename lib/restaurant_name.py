class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self._name = name
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self._name

# Testing

# Creating instances of the Restaurant class
restaurant1 = Restaurant(name="Kempinski")
restaurant2 = Restaurant(name="Java House")

all_restaurants = Restaurant.all_restaurants

for restaurant in all_restaurants:
    print(restaurant.name())  # Corrected from get_name() to name()
