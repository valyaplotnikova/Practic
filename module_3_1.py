calls = 0


def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    len_string = len(string)
    up_string = string.upper()
    low_string = string.lower()
    return len_string, up_string, low_string


def is_contains(string, list_to_search):
    count_calls()
    flag = True
    for st in list_to_search:
        if string.lower() == st.lower():
            flag = True
            break
        else:
            flag = False
    return flag


print(string_info('Vacation'))
print(string_info('hometown'))
print(is_contains('Son', ['sunshine', 'sOn', 'Json']))
print(is_contains('club', ['clubs', 'cluBbing']))
print(string_info('homework'))
print(calls)
