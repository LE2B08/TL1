import bpy

# トップバーの拡張メニュー（サブメニュークラス）
class TOPBAR_MT_my_menu(bpy.types.Menu):
    # Blenderがクラスを識別するための固有の文字列
    bl_idname = "TOPBAR_MT_my_menu"
    # メニューのラベルとして表示される文字列
    bl_label = "MyMenu"
    # 著者表示用の文字列
    bl_description = "拡張メニュー by " + bl_info["author"]

    # サブメニューの描画
    def draw(self, context):
        # トップバーの「エディターメニュー 」に項目（オペレータ）を追加
        self.layout.operator(MYADDON_OT_stretch_vertex.bl_idname, text = MYADDON_OT_stretch_vertex.bl_label)
        self.layout.operator(MYADDON_OT_create_ioc_sphere.bl_idname, text = MYADDON_OT_create_ioc_sphere.bl_label)
        self.layout.operator(MYADDON_OT_export_scene.bl_idname, text = MYADDON_OT_export_scene.bl_label)
        self.layout.operator(MYADDON_OT_import_scene.bl_idname, text = MYADDON_OT_import_scene.bl_label)
        
        # 区切り線
        self.layout.separator()
        self.layout.operator("wm.url_open_preset", text = "Manual", icon = 'HELP')

    # 既存のメニューにサブメニューを追加
    def submenu(self, context):
        # ID指定でサブメニューを追加
        self.layout.menu(TOPBAR_MT_my_menu.bl_idname)
