def generate(numRows):
    # start at head node
    # each node
    # each row is a list
    # index 0 and -1 equal 1
    pt = []
    count = 1
    for row in range(numRows):
        pt.append([1] * count)
        count += 1
    # print(pt)
    prev_row = 1
    cur_row = 2
    # check the prev_row contents
    adding = True
    while adding:
        print(pt[prev_row])
        for i, n in enumerate(pt[prev_row]):
            if i < len(pt[prev_row]) - 1:
                pt[cur_row][i+1] = n + pt[prev_row][i+1]
        if cur_row + 1 < len(pt):
            prev_row = cur_row
            cur_row += 1
        else:
            adding = False
    return pt
generate(5)