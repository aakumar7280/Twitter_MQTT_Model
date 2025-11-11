def connect_to_broker(broker_address, broker_port):
    import paho.mqtt.client as mqtt

    client = mqtt.Client()
    
    def on_connect(client, userdata, flags, rc):
        print(f"Connected to broker: {broker_address}:{broker_port} with result code {rc}")

    client.on_connect = on_connect
    client.connect(broker_address, broker_port, 60)
    
    return client

def publish_message(client, topic, message):
    result = client.publish(topic, message)
    if result.rc == 0:
        print(f"Message published to {topic}: {message}")
    else:
        print(f"Failed to publish message to {topic}")

def subscribe_to_topic(client, topic, on_message_callback):
    client.subscribe(topic)
    client.on_message = on_message_callback

def start_loop(client):
    client.loop_start()

def stop_loop(client):
    client.loop_stop()