# Stock Trading Tools application suite
This application suite was made to be used for stock trading. Each program is designed to be able to be run on a separate computer.

## get-data
"get-data" is a program designed to pull data from the internet and put it in the database. If you want to use a different data source or database, you can implement your own model for that. The data source model is located under get_data/sources and the database model is located under stt_global_items/dbms.

## calc-indicators
"calc-indicators" is a program designed for calculating the indicators that you want to use.

## stt_lib
Used as the backend of all the wrapper programs mentioned above.

### *conf.py*
The file conf.py contains the configuration information and can be changed to use a different database or data source that already has an implemented model.

:tada: :fireworks:
