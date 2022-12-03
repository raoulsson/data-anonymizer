from data_anonymizer.user.user_callback import UserCallback


def apply_user_callback(func):
    def wrapper(self, *args, **kwargs):
        column_type = None
        try:
            if isinstance(self.type_config_dict, dict):
                column_type = self.type_config_dict.get('type')
        except AttributeError:
            pass  # Don't choke if self.type_config_dict has not been set properly

        anonymized_value = func(self, *args, **kwargs)

        if len(args) > 2:
            if isinstance(args[2], UserCallback):
                user_callback = args[2]
            else:
                " We got a tuple with all the value, something to do with args and kwargs "
                user_callback = args[2][2]
            if user_callback is not None and isinstance(user_callback, UserCallback):
                anonymized_value = user_callback.handleResult(column_type, args[1], anonymized_value)
        return anonymized_value
    return wrapper
