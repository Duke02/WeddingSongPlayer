import typing as tp

from pydantic import BaseModel


class Ack(BaseModel):
    """
    Acknowledgement to make sure people know we actually did something, we promise.
    """
    acknowledged: bool = True