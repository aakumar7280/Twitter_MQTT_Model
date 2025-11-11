from tkinter import Tk, Label, Entry, Button, Text, END
import paho.mqtt.client as mqtt
import config

class PublisherApp:
    def __init__(self, master):
        self.master = master
        master.title("Tweet Publisher")

        self.username_label = Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = Entry(master)
        self.username_entry.pack()

        self.tweet_label = Label(master, text="Tweet Message:")
        self.tweet_label.pack()

        self.tweet_entry = Text(master, height=5, width=30)
        self.tweet_entry.pack()

        self.hashtag_label = Label(master, text="Hashtag (Topic):")
        self.hashtag_label.pack()

        self.hashtag_entry = Entry(master)
        self.hashtag_entry.pack()

        self.publish_button = Button(master, text="Publish Tweet", command=self.publish_tweet)
        self.publish_button.pack()

        self.client = mqtt.Client()
        self.client.connect(config.BROKER_ADDRESS, config.BROKER_PORT)

    def publish_tweet(self):
        username = self.username_entry.get()
        tweet_message = self.tweet_entry.get("1.0", END).strip()
        hashtag = self.hashtag_entry.get()

        if username and tweet_message and hashtag:
            message = f"{username}: {tweet_message}"
            self.client.publish(hashtag, message)
            self.tweet_entry.delete("1.0", END)  # Clear the tweet entry after publishing

if __name__ == "__main__":
    root = Tk()
    app = PublisherApp(root)
    root.mainloop()