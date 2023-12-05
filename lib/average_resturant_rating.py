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

    def average_star_rating(self):
        if not self._reviews:
            return 0  # Default to 0 if there are no reviews
        total_ratings = sum(review.get_rating() for review in self._reviews)
        return total_ratings / len(self._reviews)


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
restaurant1 = Restaurant("Kempinski")

# Customer1 and Customer2 add reviews
review1 = customer1.add_review(restaurant1, rating=5)
review2 = customer2.add_review(restaurant1, rating=4)

# Access the average star rating for the restaurant
average_rating = restaurant1.average_star_rating()
print(f"Average star rating for {restaurant1.name}: {average_rating}")
