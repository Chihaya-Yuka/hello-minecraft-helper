import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.graphics import Color, Rectangle
from kivy.core.text import LabelBase

kivy.require('2.3.0')
LabelBase.register(name='Roboto', fn_regular='fonts/OPPOSans-Medium.ttf') 
BACKGROUND_COLOR = [0.96, 0.87, 0.70, 1]  # 浅棕色（偏蜂蜜黄）
HEADER_COLOR = [0.20, 0.50, 0.20, 1]  # 树叶绿色
BUTTON_COLOR = [0.36, 0.25, 0.20, 1]  # 深棕色
NAVBAR_COLOR = [0.15, 0.15, 0.15, 1]  # 深灰色
BUTTON_HEIGHT = 50

class ColoredBoxLayout(BoxLayout):
    def __init__(self, **kwargs):
        self.color = kwargs.pop('color', [1, 1, 1, 1])
        super(ColoredBoxLayout, self).__init__(**kwargs)
        with self.canvas.before:
            Color(rgba=self.color)
            self.rect = Rectangle(size=self.size, pos=self.pos)
        self.bind(size=self._update_rect, pos=self._update_rect)

    def _update_rect(self, *args):
        self.rect.size = self.size
        self.rect.pos = self.pos

class MinecraftHelperApp(App):
    def build(self):
        main_layout = ColoredBoxLayout(orientation='vertical', color=BACKGROUND_COLOR)
        header = ColoredBoxLayout(size_hint_y=None, height=80, padding=[10, 10, 10, 10], color=HEADER_COLOR)
        header_label = Label(text='多玩我的世界盒子', font_size='24sp', color=[1, 1, 1, 1], size_hint_x=None, width=200, font_name='Roboto')
        header.add_widget(header_label)
        main_layout.add_widget(header)
        function_layout = GridLayout(cols=1, row_default_height=BUTTON_HEIGHT, padding=[20, 20, 20, 20], spacing=20, size_hint_y=None)
        function_layout.bind(minimum_height=function_layout.setter('height'))

        def launch_game(instance):
            print("启动游戏按钮被按下")

        def manage_mods(instance):
            print("模组管理按钮被按下")

        def manage_resource_packs(instance):
            print("资源包管理按钮被按下")

        def backup_saves(instance):
            print("存档备份按钮被按下")

        launch_game_button = Button(text="启动游戏", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        launch_game_button.bind(on_press=launch_game)

        mod_management_button = Button(text="模组管理", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        mod_management_button.bind(on_press=manage_mods)

        resource_pack_button = Button(text="资源包管理", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        resource_pack_button.bind(on_press=manage_resource_packs)

        save_backup_button = Button(text="存档备份", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        save_backup_button.bind(on_press=backup_saves)

        for button in [launch_game_button, mod_management_button, resource_pack_button, save_backup_button]:
            button.background_normal = ''
            button.background_color = BUTTON_COLOR

        function_layout.add_widget(launch_game_button)
        function_layout.add_widget(mod_management_button)
        function_layout.add_widget(resource_pack_button)
        function_layout.add_widget(save_backup_button)
        middle_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        middle_anchor.add_widget(function_layout)
        main_layout.add_widget(middle_anchor)

        navbar = ColoredBoxLayout(size_hint_y=None, height=60, spacing=10, padding=[20, 10, 20, 10], color=NAVBAR_COLOR)

        def go_home(instance):
            print("主页按钮被按下")

        def open_settings(instance):
            print("设置按钮被按下")

        def open_help(instance):
            print("帮助按钮被按下")

        nav_buttons = [
            ("主页", go_home),
            ("设置", open_settings),
            ("帮助", open_help)
        ]

        for button_text, callback in nav_buttons:
            nav_button = Button(text=button_text, size_hint=(None, 1), width=100, font_name='Roboto')
            nav_button.background_normal = ''
            nav_button.background_color = NAVBAR_COLOR
            nav_button.color = [1, 1, 1, 1]
            nav_button.bind(on_press=callback)  # 绑定回调函数
            navbar.add_widget(nav_button)

        main_layout.add_widget(navbar)

        return main_layout

if __name__ == '__main__':
    MinecraftHelperApp().run()
