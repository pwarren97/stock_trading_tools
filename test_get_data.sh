#!/bin/sh

# For testing to see if the entire program runs correctly
# Test 1
printf "Test 1:\n"
echo "./get-data -s tsla -d 20190102 --close_only"
./get-data -s tsla -d 20190102 --close_only

# Test 2
printf "\nTest 2:\n"
echo "./get-data -s MSFT -d 20190102 20190104 --close_only"
./get-data -s MSFT -d 20190101 20190104 --close_only

# Test 3
printf "\nTest 3:\n"
echo "./get-data -s aapl msft -d 20190102 20190104 --close_only"
./get-data -s aapl msft -d 20190102 20190104 --close_only

# # test cases that should error out
# ./get-data
# ./get-data -s aapl
# ./get-data -d 20190101
#
# # test cases that shouldn't error out
# ./get-data -s aapl -d 20190101
# ./get-data -s aapl tsla -d 20190101 20190103
