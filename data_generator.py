from faker import Faker
import random
import csv

def write_to_file(filename, products):
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=products[0].keys())
        writer.writeheader()
        writer.writerows(products)

def process_products(products):
    valid_products = []
    invalid_products = []

    for product in products:
        if validate_product(product):
            valid_products.append(product)
        else:
            invalid_products.append(product)

    if valid_products:
        write_to_file('processed_products.csv', valid_products)
    if invalid_products:
        write_to_file('invalid_products.csv', invalid_products)

products = generate_fake_products(1000)
required_keys = {'name', 'category', 'price', 'stock', 'sku'}
sorted_products = sort_products(products, 'price')
write_to_file('test1.csv', sorted_products)

self.default_generators = {
    'name': self.fake.catch_phrase,
    'category': lambda: random.choice(self.categories),
    'price': lambda: round(random.uniform(5, 500), 2),
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
    'availability': lambda: random.choice(['In Stock', 'Out of Stock', 'Pre-order', 'Discontinued']),
    'created_date': self.fake.date_time_this_year,
    'updated_date': self.fake.date_time_this_year,
    'product_id': lambda: self.fake.unique.uuid4(),
    'review_count': lambda: random.randint(0, 5000),
    'currency': lambda: random.choice(['USD', 'EUR', 'GBP']),
    'zip_code': self.fake.zipcode,
    'region': self.fake.state
}

class FakeProductPipeline:
    def __init__(self, n=100, required_keys=None, categories=None):
        self.n = n
        self.fake = Faker()
        self.categories = categories or ['Electronics', 'Books', 'Clothing', 'Home', 'Toys']
        self.default_generators = {
            'name': self.fake.catch_phrase,
            'category': lambda: random.choice(self.categories),
            'price': lambda: round(random.uniform(5, 500), 2),
            'stock': lambda: random.randint(0, 100),
            'sku': lambda: self.fake.ean(length=13)
            'description': self.fake.text,
            'rating': lambda: round(random.uniform(1.0, 5.0), 1),
            'release_date': self.fake.date,
            'manufacturer': self.fake.company,
            'color': self.fake.color_name,
            'weight': lambda: round(random.uniform(0.5, 10.0), 2),
            'dimensions': lambda: self.fake.lexify(text='??x??x?? cm')
        }
        if required_keys is None:
            self.required_keys = self.default_generators
        else:
            self.required_keys{
                k: self.default_generators[k]
                for k in required_keys if k in self.default_generators
            }
        self.valid_products = []
        self.invalid_products = []

    def generate_product(self):
        return {key: generator() for key, generator in self.required_keys.items()}

    def generate_products
