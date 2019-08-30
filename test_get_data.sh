#!/bin/sh

# The code shouldn't error out
./get_data.sh
./get_data.sh -s aapl
./get_data.sh -d 20190101
./get_data.sh -s aapl -d 20190101
./get_data.sh -s aapl tsla -d 20190101 20190601
