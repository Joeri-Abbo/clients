from courier_client import CourierClient

print("Fetching new data")
client = CourierClient()
print("Creating new file")
client.update_fallback_templates()
print("Finished!")
