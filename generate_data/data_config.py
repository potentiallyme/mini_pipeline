from faker import Faker
import random

class DataConfig:
    def __init__(self, categories=None, availabilities=None, currencies=None):
        self.fake = Faker()

        self.default_availabilities = availabilities or ['In Stock', 'Out of Stock', 'Pre-order', 'Discontinued']
        self.default_categories = categories or ['Electronics', 'Books', 'Clothing', 'Home', 'Toys']

        self.default_generators = {
            'name': self.fake.catch_phrase,
            'category': lambda: random.choice(self.default_categories),
            'price': lambda: round(random.uniform(5, 500), 2),
            'stock': lambda: random.randint(0, 100),
            'sku': lambda: self.fake.ean(length=13),
            'description': self.fake.text,
            'rating': lambda: round(random.uniform(1.0, 5.0), 1),
            'release_date': self.fake.date,
            'manufacturer': self.fake.company,
            'color': self.fake.color_name,
            'weight': lambda: round(random.uniform(0.5, 10.0), 2),
            'dimensions': lambda: self.fake.lexify(text='??x??x?? cm'),
            'first_name': self.fake.first_name,
            'last_name': self.fake.last_name,
            'email': self.fake.email,
            'phone_number': self.fake.phone_number,
            'address': self.fake.address,
            'date_of_birth': self.fake.date_of_birth,
            'website': self.fake.url,
            'discount': lambda: round(random.uniform(0, 50), 2),
            'inventory_location': self.fake.city,
            'availability': lambda: random.choice(self.default_availabilities),
            'created_date': self.fake.date_time_this_year,
            'updated_date': self.fake.date_time_this_year,
            'data_id': lambda: self.fake.unique.uuid4(),
            'review_count': lambda: random.randint(0, 5000),
            'currency': self.fake.currency_code,
            'zip_code': self.fake.postcode,
            'city': self.fake.city,
            'region': self.fake.state,
            'country': self.fake.country
        } 

        def update_categories(self, categories):
            self.default_categories = categories
        
        def update_availabilities(self, availabilities):
            self.default_availabilities = availabilities

        def update_currencies(self, currencies):
            self.default_currencies = currencies


