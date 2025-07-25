from .responses import *
from chargebee import request, environment
from typing_extensions import TypedDict, Required, NotRequired
from typing import Dict, List, Any, cast
from enum import Enum


@dataclass
class PaymentReferenceNumber:

    env: environment.Environment

    class Type(Enum):
        KID = "kid"
        OCR = "ocr"
        FRN = "frn"
        FIK = "fik"
        SWISS_REFERENCE = "swiss_reference"

        def __str__(self):
            return self.value

    pass
