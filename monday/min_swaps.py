
def minimumSwap(self, s1: str, s2: str) -> int:
    # count the number of x's and y's
    # fin len() of strings
    # the number of x's and y's has to be equal
    count = {
        x: 0,
        y: 0
    }
    for xy in s1:
        count[xy] += 1
    if count[x] != count[y]:
        return -1

txt = 'Hello, welcome to my world.'

str1 = "xxyyxyxyxx"
str2 = "xxyyxyxyxx"
minimumSwap(str1, str2)