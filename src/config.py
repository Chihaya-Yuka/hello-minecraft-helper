import sys

def system_info() -> int:
    platform = sys.platform
    if platform == 'win32':
        return 1
    else:
        return 0

class config:
    VERSION = '3.0.1'
    COMPANY = 'Huanyu, Inc.'
    RUNTIME = 'Kivy 2.3.0'
    SYSTEM = system_info()
    FORUMURL = 'https://mcbbs.app/'
    ONLINEPLAY = 'https://online.mcbox.duowan.click/'