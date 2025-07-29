import bpy

from .stretch_vertex import MYADDON_OT_stretch_vertex
from .my_menu import TOPBAR_MT_my_menu
from .create_ioc_sphere import MYADDON_OT_create_ico_sphere
from .export_scene import MYADDON_OT_export_scene
from .import_scene import MYADDON_OT_import_scene
from .add_filename import MYADDON_OT_add_filename
from .add_collider import MYADDON_OT_add_collider
from .collider import MYADDON_OT_add_collider
from .object_file_name import OBJECT_PT_file_name
from .object_collider import OBJECT_PT_collider

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

# Blenderに登録するクラスリスト
classes = (
    MYADDON_OT_stretch_vertex,
    MYADDON_OT_create_ico_sphere,
    MYADDON_OT_export_scene,
    MYADDON_OT_import_scene,
    TOPBAR_MT_my_menu,
    MYADDON_OT_add_filename,
    OBJECT_PT_file_name,
    MYADDON_OT_add_collider,
    OBJECT_PT_collider,
)

# メニュー項目描画
def draw_menu_manual(self, context):
    #self : 呼び出し元のクラスインスタンス。
    # context : カーソルを合わせた時のポップアップのカスタマイズなどに使用

    # トップバーの「エディターメニュー」に項目（オペレータ）を追加
    self.layout.menu(TOPBAR_MT_my_menu.bl_idname)

# アドオン有効化時コールバック
def register():
    # Blenderにクラスを登録
    for cls in classes:
        bpy.utils.register_class(cls)

    # メニューに項目を追加
    bpy.types.TOPBAR_MT_editor_menus.append(draw_menu_manual)
    # 3Dビューに描画関数を追加
    DrawCollider.handle = bpy.types.SpaceView3D.draw_handler_add(DrawCollider.draw_collider, (), "WINDOW", "POST_VIEW")
    print("レベルエディタが有効化されました。")

#アドオン無効化時コールバック
def unregister():
    # メニューから項目を削除
    bpy.types.TOPBAR_MT_editor_menus.remove(draw_menu_manual)
    # 3Dビューに描画関数を追加
    bpy.types.SpaceView3D.draw_handler_remove(DrawCollider.handle, "WINDOW")

    # Blenderからクラスを削除
    for cls in classes:
        bpy.utils.unregister_class(cls)
    print("レベルエディタが無効化されました。")

# テスト実行用コード
if __name__ == "__main__":
    register()