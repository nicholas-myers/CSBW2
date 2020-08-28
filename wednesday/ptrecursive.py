def generate(numRows):
    
    pt = []
    count = 1
    for row in range(numRows):
        pt.append([1] * count)
        count += 1
    print(pt)
    if numRows <= 2:
        return pt
    prev_row = 1
    cur_row = 2
    # check the prev_row contents
    def add(prev_row, cur_row):
        for i, n in enumerate(pt[prev_row]):
            if i < len(pt[prev_row]) - 1:
                pt[cur_row][i+1] = n + pt[prev_row][i+1]
        if cur_row + 1 < len(pt):
            prev_row = cur_row
            cur_row += 1
            add(prev_row, cur_row)
    add(prev_row, cur_row)
    # print(pt)
    return pt
generate(5)