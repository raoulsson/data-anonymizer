from . import BaseFieldType


class UserType(BaseFieldType):

    def __init__(self, type_config_dict, user_type_method):
        super().__init__(type_config_dict)
        self.__method = user_type_method

    def generate_obfuscated_value(self, key, value):
        self.seed_faker(key, value)
        func = getattr(self.faker, self.__method)
        return func()
