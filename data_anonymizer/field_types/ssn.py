from . import BaseFieldType
from data_anonymizer.user.user_callback import UserCallback
from .decorators.apply_user_callback import apply_user_callback


class SSN(BaseFieldType):

    @apply_user_callback
    def generate_obfuscated_value(self, key, value, *args, **kwargs):
        self.seed_faker(key, value)
        return self.faker.ssn()
