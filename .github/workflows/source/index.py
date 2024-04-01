import requests


def send_mgs():
    token = "bot${{secrets.TELEGRAM_BOT_TOKEN}}"
    url = f"https://api.telegram.org/{token}/sendMessage"
    user_id = int("${{secrets.FITZ_ID}}")
    msg = "A ${{github.event.type}} made by ${{github.event.author}}  ,  fille free to edit it at ${{github.repository.html_url}}"
    payload = dict(chat_id=user_id, text=msg)
    requests.post(url=url, params=payload)


if __name__ == "__main__":
    send_mgs()
