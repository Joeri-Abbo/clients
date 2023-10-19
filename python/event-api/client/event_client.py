import os
import datetime

import requests
from dotenv import load_dotenv
from sentry_sdk import capture_event

load_dotenv()


class EventClient:

    def __init__(self):
        self.service = os.getenv("SERVICE_NAME", "UNKNOWN")
        self.api = os.getenv("EVENT_API")

    def _send(self, data):
        data["service"] = self.service
        current_time = datetime.datetime.now()
        data["occurred_at"] = current_time.strftime("%Y-%m-%d %H:%M:%S")

        try:
            response = requests.post(
                self.api,
                json=data
            )
            if not response.status_code == 200:
                raise "Event could not be logged!"
        except Exception as e:
            print(e)
            capture_event(e)

    def send(self, message, relation_info=None):
        data = {
            "message": message
        }

        if relation_info:
            data["relation_info"] = relation_info
        self._send(data)
