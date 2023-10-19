from slack_client import SlackClient

print("Fetching new data")
client = SlackClient()
client.send("test", "cron-jobs")
