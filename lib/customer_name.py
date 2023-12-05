class Customer:
    all_customers = []

    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.all_customers.append(self)

    def set_given_name(self, given_name):
        self._given_name = given_name

    def set_family_name(self, family_name):
        self._family_name = family_name

    def given_name(self):
        return self._given_name

    def family_name(self):
        return self._family_name

    def full_name(self):
        return self._given_name + '' + self._family_name

    @classmethod
    def all(cls):
        return cls.all_customers
    
customer_instance = Customer(given_name='Mary',family_name="Kirui")
customer_instance = Customer(given_name='Philip',family_name="Mutai")

all_customers = Customer.all()

for customer in all_customers:
    print(customer._given_name, customer._family_name)


