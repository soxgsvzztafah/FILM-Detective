#Modified By DARK DEVIL
import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    START_TXT = """π·π΄π»π»πΎ {} π±ππΎπ,
πΌπ π½π°πΌπ΄ πΈπ <a href=https://t.me/{}>{}</a>, πΈ π²π°π½ πΏππΎππΈπ³π΄ πΌπΎππΈπ΄π, πΉπππ π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ π°π½π³ πΌπ°πΊπ΄ πΌπ΄ π°π³πΌπΈπ½ πΈπ½ ππ·π΄ πΆππΎππΏ. ππ·π΄π½ ππΎπ ππΈπ»π» ππ΄π΄ πΌπ πΏπΎππ΄ππ... π"""
    HELP_TXT = """π·πΎπ π°ππ΄ ππΎπ {} π±ππΎπ
π·π΄ππ΄ πΈπ ππ·π΄ π·π΄π»πΏ π΅πΎπ πΌπ π²πΎπΌπΌπ°π½π³π. π±ππ ππΎπ π²π°π½ π½πΎπ πππ΄ π°π³πΌπΈπ½ π²πΎπΌπΌπ°π½π³π\n\nπΌπ π³π΄ππ΄π»πΎπΏπ΄π πΈπ <a href=https://t.me/DARKDevilV2>πΌπ°π»πΈπ½π³π π½πΈπΌππ°ππ°</a> """
    ABOUT_TXT = """ π€‘ πΈ ππ <a href=https://t.me/Film_Detective_Bot>π΅πΈπ»πΌ π³π΄ππ΄π²ππΈππ΄</a>
π π²ππ΄π°ππΎπ: <a href=https://t.me/TeamDarkDevil>ππ΄π°πΌ π³π°ππΊ π³π΄ππΈπ»</a>
π₯ π»πΈπ±ππ°ππ: πΏπππΎπΆππ°πΌ
π₯ π»π°π½πΆππ°πΆπ΄: πΏπππ·πΎπ½ πΉ
π₯ π³π°ππ° π±π°ππ΄: πΌπΎπ½πΆπΎ π³π± π΅ππ΄π΄ πππΈπ°π»
ποΈ π±πΎπ ππ΄πππ΄π: ππΏπ
π  οΈπ±ππΈπ»π³ πππ°πππ: v1.0 [ π±π΄ππ° ]
π¨βπ» πΌπ π³π΄ππ΄π»πΎπΏπ΄π πΈπ <a href=https://t.me/DARKDevilV2>πΌπ°π»πΈπ½π³π π½πΈπΌππ°ππ°</a>"""
    SOURCE_TXT = """<b>NOTE:</b>
- This is a privat edition. 
- Source - lockedπ

<b>π¨βπ»DEVELOPERSπ©βπ»:</b>
- <a href=https://t.me/DarkDevilBotz>α΄α΄Κα΄ α΄α΄α΄ ΙͺΚ Κα΄α΄α΄’</a>"""
    MANUELFILTER_TXT = """π·π΄π»πΏ: <b>π΅πΈπ»ππ΄ππ</b>

- Filter is the feature were users can set automated replies for a particular keyword and film-detective will respond whenever a keyword is found the message

<b>NOTE:</b>
1. film detective should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
β’ /filter - <code>add a filter in chat</code>
β’ /filters - <code>list all the filters of a chat</code>
β’ /del - <code>delete a specific filter in chat</code>
β’ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """π·π΄π»πΏ: <b>π±ππππΎπ½π</b>

- Film Detective Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. film detective supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/film_detective_bot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """π·π΄π»πΏ: <b>π°πππΎ π΅πΈπ»ππ΄π</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """π·π΄π»πΏ: <b>π²πΎπ½π½π΄π²ππΈπΎπ½π</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
β’ /connect  - <code>connect a particular chat to your PM</code>
β’ /disconnect  - <code>disconnect from a chat</code>
β’ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """π·π΄π»πΏ: <b>π΄ππππ° πΌπΎπ³ππ»π΄π</b>

<b>NOTE:</b>
these are the extra features of Film Detective

<b>Commands and Usage:</b>
β’ /id - <code>get id of a specified user.</code>
β’ /info  - <code>get information about a user.</code>
β’ /imdb  - <code>get the film information from IMDB source.</code>
β’ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """π·π΄π»πΏ: <b>π°π³πΌπΈπ½ πΌπΎπ³π</b>

<b>NOTE:</b>
This module only works for my admins

<b>Commands and Usage:</b>
β’ /logs - <code>to get the rescent errors</code>
β’ /stats - <code>to get status of files in db.</code>
β’ /delete - <code>to delete a specific file from db.</code>
β’ /users - <code>to get list of my users and ids.</code>
β’ /chats - <code>to get list of the my chats and ids </code>
β’ /leave  - <code>to leave from a chat.</code>
β’ /disable  -  <code>do disable a chat.</code>
β’ /ban  - <code>to ban a user.</code>
β’ /unban  - <code>to unban a user.</code>
β’ /channel - <code>to get list of total connected channels</code>
β’ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """π₯οΈ ππΎππ°π» π΅πΈπ»π΄π ππ°ππ΄π³: <code>{}</code>
π΅οΈ ππΎππ°π» πππ΄ππ: <code>{}</code>
π ππΎππ°π» π²π·π°ππ: <code>{}</code>
βοΈ πππ΄π³ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±
π§? π΅ππ΄π΄ πππΎππ°πΆπ΄: <code>{}</code> πΌππ±"""
    LOG_TEXT_G = """π‘ππͺ ππ₯π’π¨π£
βοΈπΆππΎππΏ = {}(<code>{}</code>)
π°ππΎππ°π» πΌπ΄πΌπ±π΄ππ= <code>{}</code>
π½π°π³π³π΄π³ π±π - {}
Β©οΈπ³π°ππΊ π³π΄ππΈπ» π±πΎππ
"""
    LOG_TEXT_P = """π‘ππͺ π ππ πππ₯
ππΈπ³ - <code>{}</code>
π‘π½π°πΌπ΄ - {}
Β©οΈπ³π°ππΊ π³π΄ππΈπ» π±πΎππ
"""
