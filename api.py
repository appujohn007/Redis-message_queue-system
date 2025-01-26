import redis

# Redis connection details
REDIS_URL = "redis://default:vi1zdXRYds3bjzaZijA3Jpbig8Qyr0cE@redis-15545.c11.us-east-1-2.ec2.redns.redis-cloud.com:15545"

def send_message(message: str):
    try:
        # Connect to Redis
        redis_client = redis.StrictRedis.from_url(REDIS_URL)
        
        # Publish the message to the "messages" channel
        redis_client.publish("messages", f"print: {message}")
        
        print(f"Message sent: {message}")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    # Input message to send
    message = input("Enter the message to send: ")
    send_message(message)
