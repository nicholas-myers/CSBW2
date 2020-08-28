def decodeString(s):
    decoded = ""
    entered_repeat, entered_string, temp_repeat, temp_string, get_num, char_num, inner_repeats, remaining_decodes = False, False, "", "", "", 0, 0, 0
    for c in s:
        if c == "[" and entered_repeat:
            inner_repeats += 1
            remaining_decodes += 1
        if c.isnumeric() and entered_repeat == False:
            entered_repeat = True
        if entered_repeat:
            temp_repeat += c
        if c.isnumeric():
            get_num += c
        if c == "]" and inner_repeats > 0:
            inner_repeats -= 1
        if c == "]" and inner_repeats == 0:
            decoded += temp_string * char_num
            entered_repeat, entered_string, char_num, get_num, temp_repeat, temp_string = False, False, 0, "", "", ""
        if c.isalpha() and entered_repeat == False:
            decoded+=c
        if entered_string:
            temp_string += c
        if c == "[" and entered_string == False:
            entered_string = True
            char_num = int(get_num)
    
    if remaining_decodes == 0:
        return decoded
    return decodeString(decoded)
            
decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")