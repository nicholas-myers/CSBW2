def decodeString(s):
    decoded = ""
    repeats = {}
    entered_repeat = False
    entered_string = False
    temp_repeat = ""
    temp_string = ""
    char_num = 0
    get_num = ""
    inner_repeats = 0
    for i, c in enumerate(s):
        
        if c == "[" and entered_repeat:
            inner_repeats += 1
            
        if c.isnumeric() and entered_repeat == False:
            entered_repeat = True
        if entered_repeat:
            temp_repeat += c
        if c.isnumeric():
            get_num += c
        if c == "]" and inner_repeats > 0:
            inner_repeats -= 1
        if c == "]" and inner_repeats == 0:
            repeats[temp_repeat] = temp_string
            entered_string = False
            entered_repeat = False
            decoded += temp_string * char_num
            repeats = {}
            entered_repeat = False
            entered_string = False
            temp_repeat = ""
            temp_string = ""
            char_num = 0
            get_num = ""
            inner_repeats = 0
        if c.isalpha() and entered_repeat == False:
            decoded+=c
        if entered_string:
            temp_string += c
        if c == "[" and entered_string == False:
            entered_string = True
            char_num = int(get_num)
            get_num = ""
    print(decoded)
    count = 0
    for c in decoded:
        if c.isnumeric():
            count += 1
    if count == 0:
        return decoded
    return decodeString(decoded)
            
decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")