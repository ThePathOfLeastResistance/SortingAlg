from sorting_alogs import insertion_sort, bubble_sort, merge_sort, selection_sort, quick_sort
import tracemalloc
import json 
import time 
import unittest


testList = [100, 1000, 10000, 100000, 1000000]
funcList = [insertion_sort, bubble_sort, merge_sort, selection_sort,quick_sort]


def testing_data(index):
    file = ''
    match index:
        case 100:
            file = "inputTest100.txt"
        case 1000:
            file = "inputTest1000.txt"
        case 10000:
            file = "inputTest10000.txt"
        case 100000:
            file = "inputTest100000.txt"
        case 1000000:
            file = "inputTest1000000.txt"
           
    with open(f'Testing Data/{file}', 'r') as file:
        output = file.readline().strip()
        outputList = json.loads(output)
        
        if len(outputList) == index:
            return outputList
        else:
            print('Something is wrong with the reading thing') 
            return
    
# testData = [4,2,1,5,3]
# answerData = [1,2,3,4,5]
# for f in funcList:
    # assert f(testData) if f != merge_sort and f != quick_sort else f(testData, 0, len(testData)) == answerData
# print('All functions Passed')

for i in testList:
    for f in funcList:
        
        start = time.time()
        tracemalloc.start()
        f(testing_data(i)) if f != merge_sort and f != quick_sort else f(testing_data(i), 0, len(testing_data(i)))
        memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        end = time.time()
        timeTaken = end - start
        
        with open("Testing Results", "a") as file:
            file.write(f'function: {f.__name__},\n Data Size: {i},\n Memory: {memory},\n Time: {timeTaken}')
            file.write("\n\n ")
