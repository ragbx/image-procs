#!/bin/sh

read -p "Enter tex filename [Ex. myfile] no extension: " texfile
latex "${texfile}.tex"
dvisvgm -e --no-merge "${texfile}.dvi"
mv "${texfile}.svg" ../image/

