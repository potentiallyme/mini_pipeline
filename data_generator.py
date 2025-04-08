from faker import Faker
import random
import csv
import re

class dataConfig:
    def __init__(self, categories=None, availabilities=None, currencies=None):
        self.fake = Faker()

        self.default_currencies = categories or ['USD', 'EUR', 'GBP', 'JPY', 'AUD', 'CAD', 'CHF', 'CNY', 'SEK', 'NZD']
        self.default_availabilities = availabilities or ['In Stock', 'Out of Stock', 'Pre-order', 'Discontinued']
        self.default_categories = categories or ['Electronics', 'Books', 'Clothing', 'Home', 'Toys']

        self.default_generators = {
            'name': self.fake.catch_phrase,
            'category': lambda: random.choice(self.default_categories),
            'price': lambda: round(random.uniform(-10, 500), 2),
            'stock': lambda: random.randint(0, 100),
            'sku': lambda: self.fake.ean(length=13),
            'description': self.fake.text,
            'rating': lambda: round(random.uniform(1.0, 5.0), 1),
            'release_date': self.fake.date,
            'manufacturer': self.fake.company,
            'color': self.fake.color_name,
            'weight': lambda: round(random.uniform(0.5, 10.0), 2),
            'dimensions': self.fake.lexify(text='??x??x?? cm'),
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
            'currency': lambda: random.choice(self.default_currencies),
            'zip_code': self.fake.zipcode,
            'region': self.fake.state
        } 

        def update_categories(self, categories):
            self.default_categories = categories
        
        def update_availabilities(self, availabilities):
            self.default_availabilities = availabilities

        def update_currencies(self, currencies):
            self.default_currencies = currencies

class FakeDataPipeline:
    def __init__(self, required_keys=None, config=None):
        self.config = config or dataConfig()
        self.required_keys = {
            k: self.config.default_generators[k]
            for k in required_keys if k in self.config.default_generators
        }
        self.valid_data = []
        self.invalid_data = []

    def generate_data(self):
        return {key: generator() for key, generator in self.required_keys.items()}

    def generate_dataset(self, n=100):
        return [self.generate_data() for _ in range(n)]

    def validate_data(self, data):
        if set(data.keys()) != set(self.required_keys.keys()):
            return False

        if 'email' in data:
            email_pattern = r"(^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"
            if not re.match(email_pattern, data['email']):
                return False
        if 'price' in data:
            if data['price'] <= 0:
                return False

        return True
    
    def write_to_csv(self, filename, dataset, sort_key=None):
        if not dataset:
            return
        if sort_key:
            sorted_data = sorted(dataset, key=lambda x: x[sort_key])
        else:
            sorted_data = dataset
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.required_keys.keys())
            writer.writeheader()
            writer.writerows(sorted_data)

    def filter_valid_invalid(self, dataset):
        for data in dataset:
            (self.valid_data if self.validate_data(data) else self.invalid_data).append(data)


required_keys = {'name', 'category', 'price', 'stock'}
pipeline = FakeDataPipeline(required_keys=required_keys)
products = pipeline.generate_dataset(n=50)
pipeline.filter_valid_invalid(products)
print("Valid Products:")
for product in pipeline.valid_data:
    print(product)
print("\nInvalid Products:")
for product in pipeline.invalid_data:
    print(product)
pipeline.write_to_csv('valid.csv', pipeline.valid_data, 'name')
