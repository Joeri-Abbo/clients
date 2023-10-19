# CourierClient

The `CourierClient` is a Python class designed to interact with the Courier API, a notification service. This class is
intended to help you retrieve notification templates from the Courier API and store them locally for later use. It also
provides a mechanism for updating fallback templates in case there are issues fetching templates from the API.

## Prerequisites

Before using the `CourierClient`, make sure you have the following dependencies installed in your Python environment:

- `requests`: This library is used to send HTTP requests to the Courier API.
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
   import json
   import os
   import requests
   from dotenv import load_dotenv
   from sentry_sdk import capture_exception
   ```

2. **Load Environment Variables**

   Before using the `CourierClient`, load your environment variables using `load_dotenv()` from the `dotenv` library.
   Ensure that you have a `.env` file containing the necessary configuration variables. In this example, the expected
   variable is `COURIER_BEARER_TOKEN`.

   ```python
   load_dotenv()
   ```

3. **Initialize the CourierClient**

   Create an instance of the `CourierClient` class:

   ```python
   courier_client = CourierClient()
   ```

   The `CourierClient` constructor will read the `COURIER_BEARER_TOKEN` and `COURIER_URL` (optional) values from your
   environment variables. If the `COURIER_URL` is not provided, it will default to `https://api.courier.com/`.

4. **Retrieve Templates**

   You can retrieve notification templates from the Courier API using the `_get_templates` method. If the templates are
   not available locally (stored in `storage/templates.json`), the method will make a request to the API and store the
   templates in the file.

   ```python
   templates = courier_client._get_templates()
   ```

   The templates are returned as a list of template IDs.

5. **Update Fallback Templates**

   If you want to update the fallback templates manually, you can use the `update_fallback_templates` method. This
   method will fetch the templates from the API and overwrite the existing fallback templates
   in `storage/fallback-templates.json`.

   ```python
   courier_client.update_fallback_templates()
   ```

6. **Error Handling (Optional)**

   If an error occurs during API requests, the `CourierClient` will capture the exception using `sentry_sdk` (if
   configured) and continue execution. You can customize the error handling logic to suit your needs.

   ```python
   except Exception as e:
       capture_exception(e)
   ```

7. **Sending Notifications (Placeholder)**

   The `CourierClient` includes a `send` method, which you can customize to send notifications using the retrieved
   templates. You would need to implement this method according to your specific use case.

   ```python
   def send(self):
       # Implement notification sending logic here
       pass
   ```

## Customization

You can customize the `CourierClient` to fit your specific requirements. For example, you can modify the file paths for
storing templates, implement notification sending logic, or extend its functionality as necessary.

Feel free to adapt the `CourierClient` to your project's needs and leverage it for working with Courier notifications in
your Python application.

That's it! You now have a basic understanding of how to use the `CourierClient` to interact with the Courier API and
manage notification templates. Customize it to suit your project's requirements and streamline your notification
workflows.