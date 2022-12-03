from . import BaseFieldType
from data_anonymizer.user.user_callback import UserCallback
from .decorators.apply_user_callback import apply_user_callback


class UserType(BaseFieldType):

    def __init__(self, type_config_dict):
        super().__init__(type_config_dict)
        self.__method = type_config_dict.get('type')

    @apply_user_callback
    def generate_obfuscated_value(self, key, value, *args, **kwargs):
        self.seed_faker(key, value)
        func = getattr(self.faker, self.__method)
        return func()
