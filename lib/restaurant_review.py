class Restaurant:
    def __init__(self, name):
        self.name = name
        self._reviews = []

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
    def __init__(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name


# Example Usage:

# Create instances of Customer and Restaurant
customer1 = Customer("Mary", "Kirui")
customer2 = Customer("Philip", "Mutai")
customer3 = Customer("Brian", "Korir")
customer4 = Customer("Diana", "Joy")
restaurant1 = Restaurant("Kempinski")

# Create reviews
review1 = Review(customer1, restaurant1, rating=5)
review2 = Review(customer2, restaurant1, rating=4)
review3 = Review(customer3, restaurant1, rating=6)
review4 = Review(customer4, restaurant1, rating=8)

# Access reviews for a restaurant
restaurant1_reviews = restaurant1.reviews()
for review in restaurant1_reviews:
    print(f"Rating by {review.customer.given_name}: {review.get_rating()}")

# Access unique customers who have reviewed the restaurant
restaurant1_customers = restaurant1.customers()
print("Customers who have reviewed the restaurant:", [customer.given_name for customer in restaurant1_customers])
