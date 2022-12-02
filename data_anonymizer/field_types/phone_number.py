from . import BaseFieldType
from .decorators import apply_formatting_options


class PhoneNumber(BaseFieldType):
    @apply_formatting_options
    def generate_obfuscated_value(self, key, value):
        self.seed_faker(key, value)
        return self.faker.phone_number()
