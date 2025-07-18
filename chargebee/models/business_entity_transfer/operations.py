from .responses import *
from chargebee import request, environment
from typing_extensions import TypedDict, Required, NotRequired
from typing import Dict, List, Any, cast
from enum import Enum


@dataclass
class BusinessEntityTransfer:

    env: environment.Environment

    class ResourceType(Enum):
        CUSTOMER = "customer"
        SUBSCRIPTION = "subscription"

        def __str__(self):
            return self.value

    class ReasonCode(Enum):
        CORRECTION = "correction"

        def __str__(self):
            return self.value

    pass
