import typing
from src.dictonaries.payload import Payload as PayloadDictionary


class Payload:
    # The status text that will be shown as the actual status.
    _text: str

    # A text version of an emoji. e.g., :mountain_railway:
    _emoji: typing.Optional[str]

    _expiry: typing.Optional[int]

    def __init__(self, text: str, emoji: str = None, expiry: int = None):
        self._text = text
        self._emoji = emoji
        self._expiry = expiry

    def to_json(self) -> PayloadDictionary:
        payload = { 'status_text': self._text }

        if self._emoji is not None:
            payload['status_emoji'] = self._emoji
        if self._expiry is not None:
            payload['status_expiration'] = self._expiry

        return payload
