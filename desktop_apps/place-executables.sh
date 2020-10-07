#!/bin/sh

EXECLOC=/usr/local/bin
# LIBLOC=~/.pyenv/versions/3.8.5/lib/python3.8
# cp -r ./get_data/ $EXECLOC
cp ./get-data $EXECLOC
# cp -r ./calc_indicators/ $EXECLOC
cp ./calc-indicators $EXECLOC
# cp -r ./stt_lib $LIBLOC

chmod +x $EXECLOC/get-data
chmod +x $EXECLOC/calc-indicators
