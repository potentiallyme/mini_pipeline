from generate_data.data_generator import CreateData

required_keys = {'name', 'category', 'price', 'stock', 'sku', 'description', 'rating', 'release_date', 'manufacturer', 'color', 'weight', 'dimensions'}
generator = CreateData(required_keys=required_keys)
generator.generate_csv("fake_data.csv", 1000, 'name', 'valid')

