from src.entities.payload import Payload
import requests


class Status:
    # The user's id whose status will be updated.
    _userId: str

    # Every Slack workspace has to install this application for it
    # to work properly. With that said, this property contains that
    # token.
    _workspace_token: str

    # The status text that will be shown as the actual status.
    _text: str

    # A text version of an emoji. e.g., :mountain_railway:
    _emoji: str

    def __init__(self, user_id: str, workspace_token: str):
        self._userId = user_id
        self._workspace_token = workspace_token

    def with_text(self, text: str) -> 'Status':
        self._text = text
        return self

    def with_emoji(self, emoji: str) -> 'Status':
        self._emoji = emoji
        return self

    def change(self):
        payload = Payload(self._text, self._emoji, 0)
        response = requests.post(
            'https://slack.com/api/users.profile.set',
            json={
                'charset': 'utf-8',
                'token': self._workspace_token,
                'user': self._userId,
                'profile': payload.to_json(),
            },
            headers={
                'Content-type': 'application/json; charset=utf-8',
                'Authorization': f'Bearer {self._workspace_token}',
            }
        )

        print(response.text)
