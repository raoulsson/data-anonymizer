from abc import abstractmethod


class UserCallback:

    def __init__(self, *args, **kwargs):
        pass

    @abstractmethod
    def handleResult(self, column_type: str, supplied_value: str, anonymized_value: str) -> str:
        """ Called after obfuscation. Log or tweak the value, but you must give it back """
        pass
