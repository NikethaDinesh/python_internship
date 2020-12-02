import re

str = "i live in 60,street cross,pin code-6000987 ,from 506 left of rightshine ,building 6"
pattern = re.findall('[0-9]+', str)
print("nos are", pattern)


def pattern_match(pattern):
    if len(pattern) == 1 :
        return True
    elif len(pattern)==2:
        return True
    elif len(pattern)==3:
        return True
    else:
        return False


final_list = list(filter(pattern_match, pattern))
print(final_list)
