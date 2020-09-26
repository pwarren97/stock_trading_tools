import stt_lib

def import_source():
    if stt_lib.conf.DATA_SOURCE == "iex":
        from stt_lib.sources.iex import IEXCloud as source
    return source
