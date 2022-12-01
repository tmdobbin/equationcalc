#!/usr/bin/sh
pip3 install kivy
pip3 install --user --upgrade buildozer
pip3 install cpython
buildozer init
buildozer -v android ios debug

