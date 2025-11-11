import paho.mqtt.client as mqtt
import tkinter as tk
from tkinter import messagebox, scrolledtext
from config import BROKER_ADDRESS, BROKER_PORT

class SubscriberApp:
    def __init__(self, master):
        self.master = master
        master.title("Twitter Hashtag Subscriber")

        self.hashtag_label = tk.Label(master, text="Hashtag:")
        self.hashtag_label.pack()

        self.hashtag_entry = tk.Entry(master)
        self.hashtag_entry.pack()

        self.subscribe_button = tk.Button(master, text="Subscribe", command=self.subscribe)
        self.subscribe_button.pack()

        self.unsubscribe_button = tk.Button(master, text="Unsubscribe", command=self.unsubscribe)
        self.unsubscribe_button.pack()

        self.tweet_display = scrolledtext.ScrolledText(master, wrap=tk.WORD, height=15, width=50)
        self.tweet_display.pack()

        # Initialize MQTT client and connect to broker
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.connect(BROKER_ADDRESS, BROKER_PORT, 60)
        self.client.loop_start()

    def subscribe(self):
        hashtag = self.hashtag_entry.get()
        if hashtag:
            self.client.subscribe(hashtag)
            self.tweet_display.insert(tk.END, f"Subscribed to: {hashtag}\n")
        else:
            messagebox.showwarning("Input Error", "Please enter a hashtag.")

    def unsubscribe(self):
        hashtag = self.hashtag_entry.get()
        if hashtag:
            self.client.unsubscribe(hashtag)
            self.tweet_display.insert(tk.END, f"Unsubscribed from: {hashtag}\n")
        else:
            messagebox.showwarning("Input Error", "Please enter a hashtag.")

    def on_message(self, client, userdata, message):
        tweet = message.payload.decode()
        self.tweet_display.insert(tk.END, f"{tweet}\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = SubscriberApp(root)
    root.mainloop()