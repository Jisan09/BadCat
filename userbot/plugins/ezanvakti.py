# ported from
# https://github.com/muhammedfurkan/UniBorg/blob/master/stdplugins/ezanvakti.py
import json
import logging
import requests
from .. import LOGS
from ..utils import admin_cmd, sudo_cmd, edit_or_reply

logging.basicConfig(
    format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
    level=logging.WARNING)
TEMPAT = ''


@borg.on(admin_cmd(pattern=("ezanvakti ?(.*)")))
@borg.on(sudo_cmd(pattern="ezanvakti ?(.*)", allow_sudo=True))
async def get_adzan(adzan):
    if not adzan.pattern_match.group(1):
        LOKASI = TEMPAT
        if not LOKASI:
            await edit_or_reply(adzan, "Please specify a city or a state.")
            return
    else:
        LOKASI = adzan.pattern_match.group(1)
    url = f'http://muslimsalat.com/{LOKASI}.json?key=bd099c5825cbedb9aa934e255a81a5fc'
    request = requests.get(url)
    LOGS.info(request.text)
    result = json.loads((request.text))
    if request.status_code != 200:
        await edit_or_reply(adzan, f"{result['status_description']}")
        return
    tanggal = result["items"][0]["date_for"]
    lokasi = result["query"]
    lokasi2 = result["country"]
    lokasi3 = result["address"]
    lokasi4 = result["state"]
    subuh = result["items"][0]["fajr"]
    syuruk = result["items"][0]["shurooq"]
    zuhur = result["items"][0]["dhuhr"]
    ashar = result["items"][0]["asr"]
    maghrib = result["items"][0]["maghrib"]
    isya = result["items"][0]["isha"]
    textkirim = (f"⏱  **Tarih ** `{tanggal}`:\n" +
                 f"`{lokasi} | {lokasi2} | {lokasi3} | {lokasi4}`\n\n" +
                 f"**Güneş :** `{subuh}`\n" +
                 f"**İmsak :** `{syuruk}`\n" +
                 f"**Öğle :** `{zuhur}`\n" +
                 f"**İkindi :** `{ashar}`\n" +
                 f"**Akşam :** `{maghrib}`\n" +
                 f"**Yatsı :** `{isya}`\n")
    await edit_or_reply(adzan, textkirim)
