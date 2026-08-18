from datetime import datetime 
from pydantic import BaseModel, Field
from typing import Literal, Union, Annotated
import uuid

class Event(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4) 
    tickers: set[str]
    event_time: datetime 
    received_time: datetime 

class TradeEvent(Event):
    kind: Literal["trade"] = "trade"
    price: float 
    exchange: str  
    size: float 

class FilingEvent(Event):
    kind: Literal["filing"] = "filing"
    filing_type: Literal["10-Q", "8-K"] 

class NewsEvent(Event):
    kind: Literal["news"] = "news" 
    source: str 
    named_entities: list[str]

AnyEvent = Annotated[ 
    Union[TradeEvent, FilingEvent, NewsEvent],
    Field(discriminator="kind"),
]
