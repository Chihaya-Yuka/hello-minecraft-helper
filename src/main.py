import os
import kivy
import subprocess
import webview  # 新增的导入
from kivy.app import App
from config import config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.core.text import LabelBase

kivy.require('2.3.0')

# 注册字体
LabelBase.register(name='Roboto', fn_regular='fonts/OPPOSans-Medium.ttf')

# 自定义颜色和尺寸常量
BACKGROUND_COLOR = [0.96, 0.87, 0.70, 1]
HEADER_COLOR = [0.20, 0.50, 0.20, 1]
BUTTON_COLOR = [0.36, 0.25, 0.20, 1]
NAVBAR_COLOR = [0.15, 0.15, 0.15, 1]
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
            if config.SYSTEM:
                os.system('start start.py')
            else:
                show_popup("警告", "只有电脑端支持启动功能。")

        def open_webview_window(url, title="WebView"):
            # 使用 pywebview 创建一个新窗口加载网页
            webview.create_window(title, url)
            webview.start()

        def manage_mods(instance):
            open_webview_window(config.FORUMURL, "模组下载")

        def manage_resource_packs(instance):
            open_webview_window(config.FORUMURL, "资源下载")

        def backup_saves(instance):
            open_webview_window(config.ONLINEPLAY, "多人游戏")

        def toolkit(instance):
            if config.SYSTEM:
                folder_path = '{}\\tools'.format(os.getcwd())
                subprocess.Popen(f'explorer "{folder_path}"')
            else:
                show_popup("警告", "只有电脑端支持工具箱功能。")

        def mcbbs(instance):
            open_webview_window(config.FORUMURL, "m社")

        def show_popup(title, text):
            content = BoxLayout(orientation='vertical', padding=10)
            content.add_widget(Label(text=text, font_size='20sp'))
            close_button = Button(text='关闭', size_hint_y=None, height=BUTTON_HEIGHT, font_name='Roboto')
            content.add_widget(close_button)
            popup = Popup(title=title, content=content, size_hint=(None, None), size=(300, 200))
            close_button.bind(on_press=popup.dismiss)
            popup.open()

        launch_game_button = Button(text="启动游戏", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        launch_game_button.bind(on_press=launch_game)

        mod_management_button = Button(text="模组下载", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        mod_management_button.bind(on_press=manage_mods)

        resource_pack_button = Button(text="资源下载", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        resource_pack_button.bind(on_press=manage_resource_packs)

        backup_button = Button(text="多人游戏", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        backup_button.bind(on_press=backup_saves)

        toolkit_button = Button(text="工具箱", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        toolkit_button.bind(on_press=toolkit)

        mcbbs_button = Button(text="m社", size_hint=(1, None), height=BUTTON_HEIGHT, font_name='Roboto')
        mcbbs_button.bind(on_press=mcbbs)

        for button in [launch_game_button, mod_management_button, resource_pack_button, backup_button, toolkit_button, mcbbs_button]:
            button.background_normal = ''
            button.background_color = BUTTON_COLOR

        function_layout.add_widget(launch_game_button)
        function_layout.add_widget(mod_management_button)
        function_layout.add_widget(resource_pack_button)
        function_layout.add_widget(backup_button)
        function_layout.add_widget(toolkit_button)
        function_layout.add_widget(mcbbs_button)

        middle_anchor = AnchorLayout(anchor_x='center', anchor_y='center')
        middle_anchor.add_widget(function_layout)
        main_layout.add_widget(middle_anchor)

        navbar = ColoredBoxLayout(size_hint_y=None, height=60, spacing=10, padding=[20, 10, 20, 10], color=NAVBAR_COLOR)

        def null(instance):
            pass
        
        def show_about(instance):
            show_popup('关于', 'Version:{}\n{}\n'.format(config.VERSION, config.RUNTIME))

        nav_buttons = [
            ("主页", null),
            ("关于", show_about)
        ]

        for button_text, callback in nav_buttons:
            nav_button = Button(text=button_text, size_hint=(None, 1), width=100, font_name='Roboto')
            nav_button.background_normal = ''
            nav_button.background_color = NAVBAR_COLOR
            nav_button.color = [1, 1, 1, 1]
            nav_button.bind(on_press=callback)
            navbar.add_widget(nav_button)

        main_layout.add_widget(navbar)

        return main_layout

if __name__ == '__main__':
    MinecraftHelperApp().run()
