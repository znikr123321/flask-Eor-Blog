
def summon(begin, end):
    if begin == end:
        return begin
    if begin > end:
        return print('NaN')
    if begin < end:
        return begin + summon(begin+1, end)


print(summon(1, 5))