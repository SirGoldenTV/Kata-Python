def solution(text, ending):
    long_ending = len(ending)
    index = text.rfind(ending)
    if (index >= 0):
        return index == (len(text) - long_ending)
    else:
        return False