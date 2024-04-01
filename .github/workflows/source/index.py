import requests
import os
import time


def send_mgs():
    token = os.environ['TELEGRAM_BOT_TOKEN']
    user_id = os.environ['USER_ID']
    repository = os.environ['GITHUB_REPOSITORY']
    author = os.environ['GITHUB_EVENT_AUTHOR']
    date = time.ctime()
    baseUrl = "https://api.telegram.org"
    url = f"{baseUrl}/bot{token}/sendMessage"
    link = f"github.com/{repository}"

    msg = f"A Pushed 🚀 made by {author}✨ made on {date} \n \n feel free to edit it at {link}"
    payload = dict(chat_id=user_id, text=msg)
    requests.post(url=url, params=payload)


if __name__ == "__main__":
    send_mgs()
