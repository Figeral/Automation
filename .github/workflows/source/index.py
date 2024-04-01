import requests


def send_mgs():
    token = "bot6544277286:AAHSPQdHgM8YIKVQM0fGJzXXN04iudE3pNg"
    url = f"https://api.telegram.org/{token}/sendMessage"
    user_id = 5429946779
    msg = "A ${{github.event.type}} made by ${{github.event.sender.login}}  ,  fille free to edit it at ${{github.repository.html_url}}"
    payload = dict(chat_id=user_id, text=msg)
    requests.post(url=url, params=payload)


if __name__ == "__main__":
    send_mgs()
