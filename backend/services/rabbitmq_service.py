import pika
from dotenv import load_dotenv
import os

load_dotenv()

class RabbitMQService:
    def __init__(self):
        self.connection = self._connect()
        self.channel = self.connection.channel()
    
    def _connect(self):
        credentials = pika.PlainCredentials(
            os.getenv("RABBITMQ_USER"), 
            os.getenv("RABBITMQ_PASSWORD")
        )
        return pika.BlockingConnection(
            pika.ConnectionParameters(
                host=os.getenv("RABBITMQ_SERVER"),
                port=int(os.getenv("RABBITMQ_PORT")),
                virtual_host=os.getenv("RABBITMQ_VIRTUAL_HOST"),
                credentials=credentials
            )
        )
    
    def send_message(self, queue_name: str, message: str):
        self.channel.queue_declare(queue=queue_name, durable=True)
        self.channel.basic_publish(
            exchange="",
            routing_key=queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,  # Persistent
            )
        )
