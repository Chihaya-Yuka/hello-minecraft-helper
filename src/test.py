import pytest
from kivy.config import Config
from kivy.tests.common import GraphicUnitTest
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.base import EventLoop
from unittest.mock import patch
from main import MinecraftHelperApp  # 替换为实际文件名

class TestMinecraftHelperApp(GraphicUnitTest):
    
    def test_app_launch(self):
        # 创建应用程序实例
        app = MinecraftHelperApp()

        # 构建应用程序的主窗口部件
        root_widget = app.build()

        # 检查主布局是否存在
        assert root_widget is not None

        # 检查标题标签是否设置正确
        header_label = root_widget.children[2].children[0].children[0]
        assert isinstance(header_label, Label)
        assert header_label.text == '多玩我的世界盒子'

        # 检查按钮是否创建并设置为深棕色
        for i, button_text in enumerate(["启动游戏", "模组下载", "资源下载", "多人游戏"]):
            button = root_widget.children[1].children[0].children[i]
            assert isinstance(button, Button)
            assert button.text == button_text
            assert button.background_color == [0.36, 0.25, 0.20, 1]

    @patch('app.config.SYSTEM', True)
    def test_launch_game_windows(self):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取启动游戏按钮
        launch_game_button = root_widget.children[1].children[0].children[3]

        with patch('os.system') as mock_system:
            launch_game_button.dispatch('on_press')
            mock_system.assert_called_once_with('start.py')

    @patch('app.config.SYSTEM', False)
    def test_launch_game_other_systems(self):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取启动游戏按钮
        launch_game_button = root_widget.children[1].children[0].children[3]

        # 模拟点击按钮
        launch_game_button.dispatch('on_press')

        # 获取弹出的 Popup 并验证内容
        popup = root_widget.children[0]
        assert isinstance(popup, Popup)
        assert popup.title == '警告'
        assert popup.content.children[1].text == '只有电脑端支持启动功能。'

    @patch('webbrowser.open')
    def test_manage_mods(self, mock_open):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取模组下载按钮
        mod_management_button = root_widget.children[1].children[0].children[2]

        # 模拟点击按钮
        mod_management_button.dispatch('on_press')
        mock_open.assert_called_once_with(app.config.FORUMURL)

    @patch('webbrowser.open')
    def test_manage_resource_packs(self, mock_open):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取资源下载按钮
        resource_pack_button = root_widget.children[1].children[0].children[1]

        # 模拟点击按钮
        resource_pack_button.dispatch('on_press')
        mock_open.assert_called_once_with(app.config.FORUMURL)

    @patch('webbrowser.open')
    def test_backup_saves(self, mock_open):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取多人游戏按钮
        save_backup_button = root_widget.children[1].children[0].children[0]

        # 模拟点击按钮
        save_backup_button.dispatch('on_press')
        mock_open.assert_called_once_with(app.config.ONLINEPLAY)

    def test_show_about(self):
        app = MinecraftHelperApp()
        root_widget = app.build()

        # 获取“关于”按钮
        about_button = root_widget.children[0].children[1]

        # 模拟点击按钮
        about_button.dispatch('on_press')

        # 获取弹出的 Popup 并验证内容
        popup = root_widget.children[0]
        assert isinstance(popup, Popup)
        assert popup.title == '关于'
        assert 'Version:' in popup.content.children[1].text

if __name__ == '__main__':
    pytest.main()
