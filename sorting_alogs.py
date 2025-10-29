#Sorting Algorithms

from random import randint

rando = [260270, 169997, 62169, 695794, 879504, 73144, 63660, 237331, 343755, 824442, 715001, 325279, 
         189993, 7480, 579878, 53241, 215362, 670813, 330152, 47598, 317921, 540424, 225138, 774704, 
         623452, 650614, 877691, 115393, 865900, 663667, 108906, 598711, 891573, 438624, 484341, 778480, 
         120942, 879346, 820578, 734685, 601225, 270847, 726717, 260700, 269145, 167696, 681761, 766696, 
         306422, 349839, 32072, 57835, 990460, 831597, 847624, 369734, 36274, 778269, 346087, 779120, 8550, 
         966841, 272877, 715622, 206448, 934151, 560004, 279911, 834465, 423693, 472494, 43290, 226041, 
         121216, 679386, 314704, 630557, 153915, 318366, 559864, 522430, 706975, 431361, 137660, 226697, 
         389673, 19772, 47518, 962145, 111598, 30615, 410322, 779258, 40597, 439903, 675677, 51150, 815971, 
         904937, 660269]

rando_huge = [randint(0,1000000) for i in range(0,10000000)]
def deep_copy(my_list):
    new_list = []
    for i in range(0,len(my_list)):
        new_list.append(my_list[i])
    return new_list
    
def insertion_sort(my_list):

    for i in range(1,len(my_list)):

        for k in range(i-1,-1,-1):
            if my_list[k]<my_list[k+1]:
                break
            else:
                temp = my_list[k+1]
                my_list[k+1] = my_list[k]
                my_list[k] = temp
    return my_list
    
def bubble_sort(my_list):
    for i in range(len(my_list)):
        for k in range(0,len(my_list)-i-1):
            if my_list[k]>my_list[k+1]:
                current = my_list[k]
                my_list[k] = my_list[k+1]
                my_list[k+1] = current
    print(my_list)

def merge(first_half,second_half):
    ind = 0
    merged_list = []
    for item in first_half:
        remove_items = []
        for item2 in second_half:
            if item2<item:
                merged_list.append(item2)
                remove_items.append(item2)
        for rem in remove_items:
            second_half.remove(rem)
        merged_list.append(item)
    for item2 in second_half:
        merged_list.append(item2)
    return merged_list
    
def merge_sort(my_list, l, r):
    #merged_array = []
    if r>l:
        middle = l + (r-1)//2
        first_half = merge_sort(my_list,l,middle)
        second_half = merge_sort(my_list,middle+1,r)
        my_list = merge(first_half,second_half)
        test = ""
        #merged_array = merge_sort(merged_array)
   
    return my_list


def partition(my_list,low,high):
    pivot = my_list[high]

    i = low - 1
    for k in range(low,high):
        if my_list[k] <= pivot:
            i = i+1
            (my_list[i],my_list[k]) = (my_list[k],my_list[i])
    (my_list[i+1],my_list[high]) = (my_list[high],my_list[i+1])
    return i+1

def quick_sort(my_list,low,high):
    if low<high:
        part = partition(my_list,low,high)
        quick_sort(my_list,low,part-1)
        quick_sort(my_list,part+1,high)
    print(my_list)

def selection_sort(my_list):
    sorted_arrray=[]
    remaining_array = deep_copy(my_list)
    while len(remaining_array)>0:
        lowest_val = 9**10
        for i in range(len(remaining_array)):
            if remaining_array[i]<lowest_val:
                lowest_val=remaining_array[i]
        for i in range(len(remaining_array)):
            if remaining_array[i]==lowest_val:
                add_val = remaining_array.pop(i)
                break
        sorted_arrray.append(add_val)
    print(sorted_arrray)
