from . import BaseFieldType
from data_anonymizer.user.user_callback import UserCallback
from .decorators.apply_user_callback import apply_user_callback


class FloatRange(BaseFieldType):

    @apply_user_callback
    def generate_obfuscated_value(self, key, value, *args, **kwargs):
        self.seed_faker(key, value)
        if self.type_config_dict.get('start') is None:
            raise ValueError('"start" must be defined in config for FloatRange column types.')
        if self.type_config_dict.get('end') is None:
            raise ValueError('"end" must be defined in config for FloatRange column types.')
        start = int(self.type_config_dict.get('start'))
        end = int(self.type_config_dict.get('end'))
        result = self.faker.random.uniform(start, end)
        if self.type_config_dict.get('precision'):
            precision = int(self.type_config_dict.get('precision'))
            return round(float(result), precision)
        return result
