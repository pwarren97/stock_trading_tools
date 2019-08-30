[ root ]
get_data/
  Base directory of the whole program. Start with python get_data or the get_data.sh file.
  conf.py
    All configuration information should be defined here.
  __main__.py
    File is what gets run when you pass get_data/ to python.


[ sources/ Directory ]
get_data/sources/
  The sources folders contains a python file for each source you can download information from.

  iex.py
    used for trading with iexcloud.
  iex.md
    explains dependencies required for iex.py
  sources_information.md
    Explains the template for all of the sources all in one place. After importing
    each source, the functions should all match that template and work the same.
