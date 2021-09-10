#Plugin made for Catuserbot by t.me/@VinuXD. Kang with credits :)
 
import random

from userbot import catub

from ..core.managers import edit_or_reply

plugin_category = "extra"


PICKUP_LINES = [
"Do you believe in love at first sight, or should I walk by again?",
"Are you sure you’re not tired? You’ve been running through my mind all day.",
"Aside from being sexy, what do you do for a living?",
"Hey, you’re pretty and I’m cute.",
"Together we’d be Pretty Cute.",
"Is your name Google? Because you have everything I’ve been searching for.",
"[Why?] Because when I looked at you, I dropped mine.",
"You don’t need keys to drive me crazy.",
"If nothing lasts forever, will you be my nothing",
"Are you a dictionary? Cause you’re adding meaning to my life.",
"Can I borrow your cell phone? I want to call my mother and tell her I just met the girl of my dreams.",
"Is your name Wi-Fi? Because I am really started to feel a connection.",
"If looks could kill, you’d be a weapon of mass destruction.",
"Like a broken pencil, life without you is pointless.",
"If I had four quarters to give to the four prettiest girls in the world, you would have a dollar.",
"You’re so beautiful you made me forget my pickup line.",
"Do you have a tan or do you always like this hot?",
"Do you have a name, or can I just call you mine?",
"You are hotter than the bottom of my laptop.",
"I wish I was cross-eyed so I could see you twice.",
"You must be debt, because my interest in you is growing.",
 "On a scale of 1 to 10, you are a 9, and I’m the 1 you need.",
"If I were a stop light, I’d turn red every time you passed by just so I could stare at you a little bit longer.",
"Was your father a thief? Because someone stole the stars from the sky and put them in your eyes.",
"Kissme and kissyou are on a boat if kissyou falls off who remains on the boat?",
"Are you a camera? Because every time I see you I smile",
"Do you know what material is my shirt made of? Boyfriend material!",
"Roses are red, Violets are fine. I'll be the 6, If you be the 9",
"Are you a time traveller coz I can see u in my future",
"If kisses were raindrops, I'd give you showers and if hugs were minutes, I'd give you hours!",
"Are you a magician? Because every time I look at you, everyone else disappears.",
"Are you chocolate pudding? 'Cause i want to spoon you.",
"Are you my assignment? Cause I'm not doing you but I definitely should be",
"Your kids will be really pretty but 'Y' is silent.",
"Kiss me if I'm wrong, but you wanna kiss me, right?",
"My love for you is like diarrhea, I can't hold it in.",
"Are you http? because I'm ://  without you",
"Therapy is expensive so I watch you smile.",
"Tired of being an adult? Then by my baby",
"Are you cryptocurrency? Coz I wanna hold you for so long.",
"Are your parents bakers? Cause you are a cutiepie",
"i wanna c_ddle and k_ss. But u and i aren't together",
]

@catub.cat_cmd(
    pattern="pickup$",
    command=("pickup", plugin_category),
    info={
        "header": "Use at your own risk. It can change your life upside down or downside up ¯\_(ツ)_/¯. Pickup lines by @VinuXD",
        "usage": "{tr}pickup",
    },
)
async def pickup(e):
    "pickup"
    txt = random.choice(PICKUP_LINES)
    await edit_or_reply(e, txt)
