import os
import sys
import subprocess

class Setup:
    def __init__(self):
        self.is_first_open = os.path.exists('First Open')
        self.commands = [
            'python -m pip install --upgrade pip wheel setuptools',
            'python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew',
            'python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/',
            'python -m pip install kivy'
        ]

    def run_commands(self):
        for command in self.commands:
            subprocess.run(command, shell=True, check=True)

    def update_path(self):
        if sys.platform == 'win32' and self.is_first_open:
            new_path = f"{os.environ['PATH']};{os.getcwd()}\\share\\sdl2\\bin;{os.getcwd()}\\share\\glew\\bin"
            os.environ['PATH'] = new_path
            with open('First Open','w') as file: pass

    def setup_environment(self):
        self.run_commands()
        self.update_path()

if __name__ == "__main__":
    print('请稍后，正在启动中......')
    setup = Setup()
    setup.setup_environment()
    subprocess.run(['python', 'main.py'])
