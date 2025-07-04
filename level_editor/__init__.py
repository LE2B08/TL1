# ブレンダーに登録するアドオン
bl_info = {
    "name": "レベルエディタ",
    "author": "Taro Kamata",
    "version": (1, 0),
    "blender": (3, 3, 1),
    "location": "",
    "description": "レベルエディタ",
    "warning": "",
    #"support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Object"
}

# main.pyにregister/unregister処理をまとめておくと便利
from .main import register, unregister