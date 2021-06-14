from ..core.managers import edit_or_reply

pawn = [
    "nsfw",
    "nsfw_gifs",
    "nsfw_gif",
    "60fpsporn",
    "porn",
    "porn_gifs",
    "porninfifteenseconds",
    "CuteModeSlutMode",
    "NSFW_HTML5",
    "the_best_nsfw_gifs",
    "verticalgifs",
    "besthqporngifs",
    "boobs",
    "pussy",
    "jigglefuck",
    "broslikeus",
    "gangbang",
    "passionx",
    "titfuck",
    "HappyEmbarrassedGirls",
    "suicidegirls",
    "porninaminute",
    "SexInFrontOfOthers",
    "tiktoknsfw",
    "tiktokporn",
    "TikThots",
    "NSFWFunny",
    "GWNerdy",
    "WatchItForThePlot",
    "HoldTheMoan",
    "OnOff",
    "TittyDrop",
    "extramile",
    "Exxxtras",
    "adorableporn",
]

hemtai = [
    "feet",
    "yuri",
    "trap",
    "futanari",
    "hololewd",
    "lewdkemo",
    "solog",
    "feetg",
    "cum",
    "erokemo",
    "les",
    "wallpaper",
    "lewdk",
    "ngif",
    "tickle",
    "lewd",
    "feed",
    "gecg",
    "eroyuri",
    "eron",
    "cum_jpg",
    "bj",
    "nsfw_neko_gif",
    "solo",
    "kemonomimi",
    "nsfw_avatar",
    "gasm",
    "poke",
    "anal",
    "slap",
    "hentai",
    "avatar",
    "erofeet",
    "holo",
    "keta",
    "blowjob",
    "pussy",
    "tits",
    "holoero",
    "lizard",
    "pussy_jpg",
    "pwankg",
    "classic",
    "kuni",
    "waifu",
    "pat",
    "8ball",
    "kiss",
    "femdom",
    "neko",
    "spank",
    "cuddle",
    "erok",
    "fox_girl",
    "boobs",
    "random_hentai_gif",
    "smallboobs",
    "hug",
    "ero",
    "smug",
    "goose",
    "baka",
    "woof",
]


async def importent(event):
    cat = ["-1001199597035", "-1001459701099", "-1001436155389", "-1001321431101"]
    if str(event.chat_id) in cat:
        await edit_or_reply(event, "**Yes I'm GAY**")
        await event.client.kick_participant(event.chat_id, "me")
        return True
    return False


def nsfw(catagory):
    catagory.sort(key=str.casefold)
    horny = "**Catagory :** "
    for i in catagory:
        horny += f" `{i.lower()}` ||"
    return horny


API = "https://weaverbottest.herokuapp.com/gimme"
