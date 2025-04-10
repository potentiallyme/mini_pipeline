from faker import Faker
from colorama import Fore, Style
from .data_config import DataConfig
import random
import csv
import re
import logging

class CreateData:
    def __init__(self, required_keys={'first_name', 'last_name', 'email', 'phone_number', 'website', 'address', 'country'}, config=None):
        self.config = config or DataConfig()
        self.required_keys = {
                k: self.config.default_generators[k]
                for k in required_keys if k in self.config.default_generators
                }
        self.valid_data = []
        self.invalid_data = []
        self.dataset = []

    def _generate_data(self):
        return {key: generator() for key, generator in self.required_keys.items()}
    
    def _validate_data(self, data):
        if set(data.keys()) != set(self.required_keys.keys()):
            return False
        return True
    
    def _write_to_csv(self, filename, sort_key=None, mode='all'):
        if not self.dataset:
            logging.error(Fore.RED + "Error generating dataset | No dataset to write to CSV" + Style.RESET_ALL)
            return

        if mode == 'all':
            dataset = self.dataset
        elif mode == 'valid':
            dataset = self.valid_data
        elif mode == 'invalid':
            dataset = self.invalid_data

        if sort_key:
            to_write = sorted(dataset, key=lambda x: x[sort_key])
        else:
            to_write = dataset
        with open(filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.required_keys.keys())
            writer.writeheader()
            writer.writerows(to_write)

    def generate_dataset(self, n=100):
        self.dataset = [self._generate_data() for _ in range(n)]
        for data in self.dataset:
            (self.valid_data if self._validate_data(data) else self.invalid_data).append(data)
        return self.dataset

    def generate_csv(self, filename, n=100, sort_key=None, mode='all'):
        if mode not in ['all', 'valid', 'invalid', 'split']:
            logging.error(Fore.RED + f"Invalid MODE: {mode} | Options: all, valid, invalid, split" + Style.RESET_ALL)
            return
        if not self.dataset:
            self.generate_dataset(n)
        if mode == 'split':
            self._write_to_csv("valid_" + filename, sort_key=sort_key, mode='valid')
            self._write_to_csv("invalid_" + filename, sort_key=sort_key, mode='invalid')
        else:
            self._write_to_csv(filename, sort_key=sort_key, mode=mode)
