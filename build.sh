#!/bin/bash
if [[ $1 == "" ]]; then
	echo "Please use ./build.sh [OPTION] where OPTION={debug,release}"
	exit
fi
#RELEASE - equationBuddy.py should be the main file instead of the current kivyGUITest.py.
#cp equationBuddy.py main.py
cp kivyGUITest.py main.py
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

