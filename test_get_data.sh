#!/bin/sh

# For testing to see if the entire program runs correctly
<<<<<<< HEAD
./get_data.sh -s aapl -d 20190102 20190104 --close_only
=======
# Test 1
printf "Test 1:\n"
echo "./get_data.sh -s tsla -d 20190102 --close_only"
./get_data.sh -s tsla -d 20190102 --close_only

# Test 2
printf "\nTest 2:\n"
echo "./get_data.sh -s aapl msft -d 20190102 20190104 --close_only"
./get_data.sh -s aapl msft -d 20190102 20190104 --close_only


# Test 3
printf "\nTest 3:\n"
echo "./get_data.sh -s MSFT -d 20190102 20190104 --close_only"
./get_data.sh -s MSFT -d 20190101 20190104 --close_only

>>>>>>> eaa1828904b755910e4ca65f10a3bd8d78cac66a

# # test cases that should error out
# ./get_data.sh
# ./get_data.sh -s aapl
# ./get_data.sh -d 20190101
#
# # test cases that shouldn't error out
# ./get_data.sh -s aapl -d 20190101
# ./get_data.sh -s aapl tsla -d 20190101 20190103
