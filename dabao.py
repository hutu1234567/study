#_*_ coding:utf-8 _*_
#pack.py
from distutils.core import setup
import py2exe
import sys

sys.argv.append('py2exe')

py2exe_options = {
  "dll_excludes": ["MSVCP90.dll",],
  "compressed": 1,
  "optimize": 2,
  "ascii": 0,
  "bundle_files": 1
}

setup(
  name = 'Demo',
  version = '1.0',
  windows = ['main.py',],
  zipfile = None,
  options = {'py2exe': py2exe_options}
)