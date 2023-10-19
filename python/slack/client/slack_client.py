import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()


class SlackClient:

    def __init__(self):
        self.token = os.getenv("SLACK_TOKEN", "https://api.courier.com/")

    def send(self, text, channel, blocks=None):
        return requests.post('https://slack.com/api/chat.postMessage', {
            'token': self.token,
            'channel': channel,
            'text': text,
            'blocks': json.dumps(blocks) if blocks else None
        }).json()


if __name__ == '__main__':
    exit()
