# def isPossible(a, b, c, d):
#     result = []
#     def helper(a,b,c,d, result):
#         if a==c and b==d:
#             result.append(True)
#             return True
#         elif a > c or b>d:
#             return False
#         elif a<c:
#             helper(a+b, b,c,d, result)
#         elif b<d:
#             helper(a,b+a,c,d, result)
#     helper(a, b, c, d, result)
#     return 'Yes' if any(result) else 'No'
#
# print(isPossible(1,4,62,45))

def countPairs(numbers, k):
    valid_pairs = 0
    pairs = []
    for index in range(len(numbers)):
        for index1 in range(len(numbers)):
            pair = (numbers[index], numbers[index1])
            if pair not in pairs:
                pairs.append(pair)
    for pair in pairs:
        if pair[0]+k==pair[1]:
            valid_pairs+=1
    return valid_pairs

countPairs([1,2,3,4,5,6,2], 2)