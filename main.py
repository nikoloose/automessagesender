import http.client
import json
import random
import time

header_data = {
    "Content-Type": "application/json",
    "User-Agent": "DiscordBot",
    "Authorization": ""
}

def get_connection():
    return http.client.HTTPSConnection("discord.com", 443)

def send_message(conn, channel_id, message_data):
    try:
        conn.request("POST", f"/api/v10/channels/{channel_id}/messages", message_data, header_data)
        resp = conn.getresponse()

        if 199 < resp.status < 300:
            print(f"Message Sent to channel {channel_id}.")
        else:
            print(f"HTTP {resp.status}: {resp.reason}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    with open('./config.json', encoding='utf-8') as f:
        config_data = json.load(f)
        token = config_data['Config'][0]['token']
        header_data["Authorization"] = token
        channels = config_data['Config'][0]['channels']

    for channel in channels:
        channel_id = channel['channelid']
        messages = channel['messages']
        message = random.choice(messages)

        message_data = {
            "content": message,
            "tts": False
        }

        conn = get_connection()
        send_message(conn, channel_id, json.dumps(message_data))
        conn.close()

if __name__ == '__main__':
    while True:
        main()
        time.sleep(3600)  # this means it will send a message in all the channels every 1 hour.                        

                    # change the number to choose how long u want to send the messages again
