# def jump(A):
#     jump_array = [0]*(len(A))
    
#     for index, element in enumerate(A):
#         #import ipdb;ipdb.set÷_trace()

#         try:
#             if jump_array[index]:
#                 jump_array[index] = min(jump_array[index-1] + 1, jump_array[index])
#             else:
#                 if index > 0: 
#                     jump_array[index] = jump_array[index-1] + 1
        
#         except:
#             pass

#         if index + element > index:
#             try:
#                 if jump_array[index + element]:
#                     if index + element < len(A) -1 : 
#                         jump_array[index + element] = min(jump_array[index + element], jump_array[index] + 1)
#                     else:
#                         if jump_array[len(A)-1]:
#                             jump_array[len(A)-1] = min(jump_array[len(A)-1], jump_array[index] +1)
#                         else:
#                             jump_array[len(A)-1]  = jump_array[index] + 1
#                 else:
#                     jump_array[index + element] = jump_array[index] + 1
                    
#             except: 
#                 pass
    
#     # for index, key in enumerate(jump_array):
#     #     print(index,"    ",  key, "    ", A[index])
#     return jump_array[len(A)-1]


def jump(nums):
    length = len(nums)
    jump_array = [0]*length
    index_reached = 1
    if length == 1:
        return 0

    for index, element in enumerate(nums):
        try:
            if jump_array[index]:
                jump_array[index] = min(jump_array[index-1] + 1, jump_array[index])
            else:
                if index > 0: 
                    jump_array[index] = jump_array[index-1] + 1
        except:
            pass
            
        try:
            for i in range(index_reached, index+element+1):
                if jump_array[i]:
                        jump_array[i] = min(jump_array[i], jump_array[index] + 1)
                else:
                    jump_array[i] = jump_array[index] + 1
            index_reached = max(index + element, index_reached)    
        except: 
            pass
    
    for index, key in enumerate(jump_array):
        print(index,"    ",  key, "    ", nums[index])
    if not jump_array[length-1]:
        return -1
    return jump_array[length-1]
if __name__ == "__main__":
    # print(jump( [ 33, 21, 50, 0, 0, 46, 34, 3, 0, 12, 33, 0, 31, 37, 15, 17, 34, 18, 0, 4, 12, 41, 18, 35, 37, 34, 0, 47, 0, 39, 32, 49, 5, 41, 46, 26, 0, 2, 49, 35, 4, 19, 2, 27, 23, 49, 19, 38, 0, 33, 47, 1, 21, 36, 18, 33, 0, 1, 0, 39, 0, 22, 0, 9, 36, 45, 31, 4, 14, 48, 2, 33, 0, 39, 0, 37, 48, 44, 0, 11, 24, 16, 10, 23, 22, 41, 32, 14, 22, 16, 23, 38, 42, 16, 15, 0, 39, 23, 0, 42, 15, 25, 0, 41, 2, 48, 28 ]))
    print(jump([2,3,1,1,4]))
    # print(jump([1,2,3,4,5]))
    # print(jump([ 0, 46, 46, 0, 2, 47, 1, 24, 45, 0, 0, 24, 18, 29, 27, 11, 0, 0, 40, 12, 4, 0, 0, 0, 49, 42, 13, 5, 12, 45, 10, 0, 29, 11, 22, 15, 17, 41, 34, 23, 11, 35, 0, 18, 47, 0, 38, 37, 3, 37, 0, 43, 50, 0, 25, 12, 0, 38, 28, 37, 5, 4, 12, 23, 31, 9, 26, 19, 11, 21, 0, 0, 40, 18, 44, 0, 0, 0, 0, 30, 26, 37, 0, 26, 39, 10, 1, 0, 0, 3, 50, 46, 1, 38, 38, 7, 6, 38, 27, 7, 25, 30, 0, 0, 36, 37, 6, 39, 40, 32, 41, 12, 3, 44, 44, 39, 2, 26, 40, 36, 35, 21, 14, 41, 48, 50, 21, 0, 0, 23, 49, 21, 11, 27, 40, 47, 49 ]))
    # print(jump([20,1,1,1]))