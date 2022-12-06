#!/bin/bash
if [[ $1 == "" ]]; then
	echo "Please use ./build.sh [OPTION] where OPTION={debug,release}"
	exit
fi
pip3 install kivy
pip3 install --user --upgrade buildozer
pip3 install cpython
cp equationBuddy.py main.py
buildozer init
echo "Building in $1 mode"

if [[ $1 == "" ]]; then
	echo ""
fi

if [[ "$OSTYPE" == "darwin"* ]]; then
	pip3 install kivy-ios
	echo "OSTYPE is Darwin. Attempting to build for iOS."
	buildozer  ios $1
else
	buildozer android $1
fi
#FOR RELEASE ONLY
#buildozer -v android release
#buildozer -v ios release

