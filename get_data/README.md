# get_data program


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

[ sources/installer_scripts/ Directory ]
get_data/sources/installer_scripts/
  The scripts inside here are the installer scripts for all python modules necessary and the corresponding versioning needed.

  iex_finance.sh
    Installer script for iexcloud related python modules.
