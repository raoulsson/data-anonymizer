import os
from abc import ABC

from data_anonymizer.user.user_callback import UserCallback


class StripNewlinesCallBack(UserCallback, ABC):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def handleResult(self, column_type: str, supplied_value: str, anonymized_value: str) -> str:
        return anonymized_value.replace("\r", "").replace(os.linesep, "")
