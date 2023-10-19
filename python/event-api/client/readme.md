# EventClient

The `EventClient` is a Python class designed to facilitate the logging of events to an external service. This class is
particularly useful for applications that need to capture and record important events or errors during their execution.

## Prerequisites

Before using the `EventClient`, make sure you have the following dependencies installed in your Python environment:

- `requests`: This library is used to send HTTP POST requests to an external API.
- `dotenv`: It allows you to load environment variables from a `.env` file.
- `sentry_sdk`: This library is used for error tracking and reporting. It's optional but recommended for capturing and
  reporting exceptions.

You can install these dependencies using pip:

```bash
pip install -r requirements.txt
```

## Getting Started

1. **Import Required Libraries**

   Import the necessary libraries at the beginning of your Python script:

   ```python
   import os
   import datetime
   import requests
   from dotenv import load_dotenv
   from sentry_sdk import capture_event
   ```

2. **Load Environment Variables**

   Before using the `EventClient`, load your environment variables using `load_dotenv()` from the `dotenv` library.
   Ensure that you have a `.env` file containing the necessary configuration variables. In this example, the expected
   variables are `SERVICE_NAME` and `EVENT_API`.

   ```python
   load_dotenv()
   ```

3. **Initialize the EventClient**

   Create an instance of the `EventClient` class:

   ```python
   event_client = EventClient()
   ```

   The `EventClient` constructor will read the `SERVICE_NAME` and `EVENT_API` values from your environment variables.

4. **Logging Events**

   You can log events using the `send` method of the `EventClient` instance. Provide a `message` as a string, and
   optionally, you can provide `relation_info` as additional information related to the event:

   ```python
   event_client.send("This is a sample event message", relation_info={"key": "value"})
   ```

   The `send` method will send a POST request to the specified `EVENT_API` with the event data.

5. **Error Handling (Optional)**

   If an error occurs while sending the event, the `EventClient` will capture the error using `sentry_sdk` (if
   configured) and print the error to the console. You can customize the error handling logic to suit your needs.

   ```python
   except Exception as e:
       print(e)
       capture_event(e)
   ```

## Customization

You can customize the `EventClient` to fit your specific requirements. For example, you can modify the data sent in the
event payload or customize error handling behavior.

Feel free to adapt the `EventClient` to your project's needs and extend its functionality as necessary.

That's it! You now have a basic understanding of how to use the `EventClient` to log events in your Python application.
Customize it to suit your project's requirements and capture important events for monitoring and analysis.