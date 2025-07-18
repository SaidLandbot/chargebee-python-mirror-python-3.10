from .responses import *
from chargebee import request, environment
from typing_extensions import TypedDict, Required, NotRequired
from typing import Dict, List, Any, cast


@dataclass
class ThirdPartyPaymentMethod:

    env: environment.Environment

    pass
