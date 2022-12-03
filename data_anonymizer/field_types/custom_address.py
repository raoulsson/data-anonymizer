from . import BaseFieldType
from .decorators import apply_formatting_options
from data_anonymizer.user.user_callback import UserCallback
from .decorators.apply_user_callback import apply_user_callback


class CustomAddress(BaseFieldType):
    def __init__(self, type_config_dict):
        super().__init__(type_config_dict)
        self.format_string = type_config_dict.get('format')

    @apply_formatting_options
    @apply_user_callback
    def generate_obfuscated_value(self, key, value, *args, **kwargs):
        self.seed_faker(key, value)
        if not self.format_string:
            return self.faker.address()
        else:
            return_value = self.format_string.replace('$STREET', self.faker.street_address())
            return_value = return_value.replace('$CITY', self.faker.city())
            return_value = return_value.replace('$ZIP', self.faker.postcode())
            return_value = return_value.replace('$STATE_ABBR', self.faker.state_abbr())
            return_value = return_value.replace('$STATE_FULL', self.faker.state())
            return_value = self.faker.bothify(return_value)
            return return_value
