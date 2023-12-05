class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name = name
        self._reviews = []
        Restaurant.all_restaurants.append(self)

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        return list({review.customer for review in self._reviews})


class Review:
    all_reviews = []

    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating
        Review.all_reviews.append(self)
        restaurant.add_review(self)

    def get_rating(self):
        return self.rating

    @classmethod
    def all(cls):
        return cls.all_reviews


class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
        self._reviews = []
        Customer.all_customers.append(self)

    def num_reviews(self):
        return len(self._reviews)

    @classmethod
    def find_by_name(cls, name):
        for customer in cls.all_customers:
            if customer.full_name() == name:
                return customer
        return None

    @classmethod
    def find_all_by_given_name(cls, name):
        return [customer for customer in cls.all_customers if customer.given_name == name]

    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    def add_review(self, restaurant, rating):
        new_review = Review(self, restaurant, rating)
        self._reviews.append(new_review)
        return new_review

# Example Usage:

# Create instances of Customer, Restaurant, and Review
customer1 = Customer("Mary", "Kirui")
customer2 = Customer("Philip", "Mutai")
customer3 = Customer("Mary", "Wangari")
restaurant1 = Restaurant("Kempinski")

# Customer1 adds reviews
review1 = customer1.add_review(restaurant1, rating=5)
review2 = customer1.add_review(restaurant1, rating=4)

# Customer2 adds reviews
review3 = customer2.add_review(restaurant1, rating=3)

# Access the number of reviews authored by a customer
print(f"{customer1.given_name} has authored {customer1.num_reviews()} reviews.")
print(f"{customer2.given_name} has authored {customer2.num_reviews()} reviews.")

# Find a customer by full name
found_customer = Customer.find_by_name("Philip Mutai")
print(f"Found customer: {found_customer.given_name} {found_customer.family_name}")

# Find all customers by given name
customers_with_given_name = Customer.find_all_by_given_name("Mary")
print(f"Customers with given name 'Mary': {[customer.full_name() for customer in customers_with_given_name]}")


