from . import BaseFieldType
from data_anonymizer.user.user_callback import UserCallback
from .decorators.apply_user_callback import apply_user_callback


class SafeHarborAge(BaseFieldType):

    @apply_user_callback
    def generate_obfuscated_value(self, key, value, *args, **kwargs):
        if int(value) >= 90:
            return 150
        return value
