from fastapi import FastAPI
import redis

app = FastAPI()

# Connect to Redis
redis_client = redis.StrictRedis.from_url(
    "redis://default:vi1zdXRYds3bjzaZijA3Jpbig8Qyr0cE@redis-15545.c11.us-east-1-2.ec2.redns.redis-cloud.com:15545"
)

@app.get("/text")
async def send_message(msg: str):
    """
    Push a message to Redis. The message will be in the format 'print: <msg>'.
    """
    message = f"print: {msg}"
    redis_client.publish("messages", message)  # Publish the message to the 'messages' channel
    return {"status": "Message sent", "message": msg}

