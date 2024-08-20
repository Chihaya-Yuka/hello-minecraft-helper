import os
import sys

commands = [
  'python -m pip install --upgrade pip wheel setuptools',
  'python -m pip install docutils pygments pypiwin32 kivy.deps.sdl2 kivy.deps.glew',
  'python -m pip install kivy.deps.gstreamer --extra-index-url https://kivy.org/downloads/packages/simple/',
  'python -m pip install kivy',
]
for command in commands:
  os.system(command)
if sys.platform == 'win32':
  os.system('set PATH=%PATH%;%cd%\share\sdl2\bin;%cd%\share\glew\bin')

os.system('python main.py')
