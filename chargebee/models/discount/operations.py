from .responses import *
from chargebee import request, environment
from typing_extensions import TypedDict, Required, NotRequired
from typing import Dict, List, Any, cast
from enum import Enum


@dataclass
class Discount:

    env: environment.Environment

    class Type(Enum):
        FIXED_AMOUNT = "fixed_amount"
        PERCENTAGE = "percentage"

        def __str__(self):
            return self.value

    pass
