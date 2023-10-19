from event_client import EventClient

client = EventClient()
client.send("Hello World!")

## With relation info
client.send("Hello World!", "relation info")
