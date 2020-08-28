def decodeString(s):
    cache = {}
    
    def getInner(checks):
        entered_repeat = False
        getnum = ""
        repeat = ""
        string = ""
        for c in checks:
            if c.isnumeric() and entered_repeat == False:
                getnum += c
            if c.isnumeric() and entered_repeat:
                getnum = ""
                getnum += c
                # print(getnum)
            if c == "[" and entered_repeat == False:
                entered_repeat = True
            if entered_repeat:
                if c != "[" and c != "]":
                    repeat += c
            if c == "]":
                entered_repeat = False
                decoder = getnum + repeat
                cache[decoder] = int(getnum) * repeat
                print(cache)
                return cache[decoder]
        
    return getInner(s)        
decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")