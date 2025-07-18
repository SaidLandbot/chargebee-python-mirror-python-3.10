from .responses import *
from chargebee import request, environment
from typing_extensions import TypedDict, Required, NotRequired
from typing import Dict, List, Any, cast


@dataclass
class ImpactedItem:

    env: environment.Environment

    class Download(TypedDict):
        download_url: Required[str]
        valid_till: Required[int]
        mime_type: NotRequired[str]

    pass
