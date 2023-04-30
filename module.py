def search_str(substr, string):
    if substr.lower() in string.lower():
        return("bingo")
    else:
        return("no way")