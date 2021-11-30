def mergeFiles(fileSizes):
    fileSizes.sort()
    total_time = 0
    while len(fileSizes)!=1:
        first_minimum_size = min(fileSizes)
        fileSizes = fileSizes[1:]
        second_minimum_size = min(fileSizes)
        fileSizes = fileSizes[1:]
        sub_merge = first_minimum_size + second_minimum_size
        fileSizes.append(sub_merge)
        fileSizes.sort()
        total_time += sub_merge
    return total_time


# print(mergeFiles([20,4,8,2]))

def mergeFiles1(fileSizes):
    # [2,2,2,2,2,2,2,2,2,2]
    # [10,8,12]
    sub_merge = 0
    total_time = 0
    h_map={}
    for idx, i in enumerate(fileSizes):
        h_map[i] = i

    while len(h_map)!=0:
        min_1 = min(h_map)
        if h_map[min_1]==0:
            h_map.pop(min_1)
            continue
        else: h_map[min_1] -=1
        min_2 = min(h_map)
        if h_map[min_2] == 0:
            h_map.pop(min_2)
            continue
        else: h_map[min_2] -= 1

        merge = min_1+min_2
        total_time+=merge
        if merge not in h_map:
            h_map[merge] = 1
        else:
            h_map[merge] +=1
    return total_time


# lst1 = [2,2,2,2,2,2,2,2,2,2]
lst = [20,4,8,2]
# print(mergeFiles(lst))



def app_pair(capacity, lst1, lst2):
    out = [[]]
    h_map = {}
    for foreground_lst in lst1:
        for background_lst in lst2:
            if foreground_lst[1]+background_lst[1] < capacity:
                h_map[(foreground_lst[0], background_lst[0])] = [foreground_lst, background_lst]
    max_num = 0
    for id, memory in h_map.items():
        temp = max_num
        max_num = max(max_num, memory[0][1]+memory[1][1])
        if max_num > temp:
            out[0] = list(id)
    return out


lst1 = [[1,2], [2,4], [3,6]]
lst2 = [[1,2]]
# print(app_pair(7,lst1, lst2))


def minimumDivisor(arr, threshold):
    total_sum = sum(arr)
    minimum_divisor = 1

    while total_sum>threshold:
        temp = [((i // minimum_divisor) + 1) if type(i) != i else i // minimum_divisor for i in arr]
        total_sum = sum(temp)
        if total_sum<=threshold:
            break
        minimum_divisor+=1

    return minimum_divisor

print(minimumDivisor([1,5,7], 8))




