import redis

# Connect to the Redis server
redis_client = redis.StrictRedis.from_url(
    "redis://default:vi1zdXRYds3bjzaZijA3Jpbig8Qyr0cE@redis-15545.c11.us-east-1-2.ec2.redns.redis-cloud.com:15545"
)

# Subscribe to a channel
pubsub = redis_client.pubsub()
pubsub.subscribe("messages")  # Replace "messages" with your preferred channel name

print("Listening for messages...")

# Continuously listen for messages
for message in pubsub.listen():
    if message["type"] == "message":
        content = message["data"].decode()
        if content.startswith("print:"):
            print(content.split("print:", 1)[1].strip())  # Print the text after "print:"
