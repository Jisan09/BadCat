import re

import requests


def paste_text(text):
    asciich = ["*", "`", "_"]
    for i in asciich:
        text = re.sub(rf"\{i}", "", text)
    try:
        key = (
            requests.post("https://nekobin.com/api/documents", json={"content": text})
            .json()
            .get("result")
            .get("key")
        )
        link = f"https://nekobin.com/{key}"
    except:
        text = re.sub(r"•", ">>", text)
        kresult = requests.post(
            "https://del.dog/documents", data=text.encode("UTF-8")
        ).json()
        link = f"https://del.dog/{kresult['key']}"
    return link
