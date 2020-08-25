
def minimumSwap(s1, s2) -> int:
    # count the number of x's and y's
    # find len() of strings
    # the number of x's and y's has to be equal
    count = {
        "x": 0,
        "y": 0
    }
    swap = {
        "x": "y",
        "y": "x"
    }
    str1 = []
    str2 = []
    for xy in s1:
        count[xy] += 1
        str1.append(xy)
    for xy in s2:
        count[xy] += 1
        str2.append(xy)
    if count["x"] != count["y"]:
        return -1
    ideal_str = "x"
    for c in range(len(s1)):
        if c > 0:
            if ideal_str[c - 1] == "x":
                ideal_str += "y"
            else:
                ideal_str += "x"
    ideal_list = []
    for c in ideal_str:
        ideal_list.append(c)
        
    steps = 0
    str1_index = 0
    str1_steps = 0
    str2_index = 0
    str2_steps = 0
    while str1 != ideal_list and str2 != ideal_list:
        if str1[str1_index] != ideal_list[str1_index]:
            str1[str1_index] = swap[str1[str1_index]]
            str1_steps += 1
            str1_index += 1
        else:
            str1_index += 1
        if str2[str2_index] != ideal_list[str2_index]:
            str2[str2_index] = swap[str2[str2_index]]
            str2_steps += 1
            str2_index += 1
        else:
            str2_index += 1
    
            if steps < str1_steps and steps < str2_steps:
                steps += 1
        
    return steps            

txt = 'Hello, welcome to my world.'

str1 = "xxyyxyxyxx"
str2 = "xyyxyxxxyx"
minimumSwap(str1, str2)

"xxyyxyxyxx"
"xyyxyxxxyx"
