import json 

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
            
            
# This is less memory and time efficent, instead of swaping the elements, we have 2 list that we keep track of
            
def selection_sort(inputList):
    sortedList = []
    for value in range(len(inputList)):
        smallestIndex = 0
        for subvalue in range(len(inputList)):
            if inputList[smallestIndex] > inputList[subvalue]:
                smallestIndex = subvalue
            
        sortedList.append(inputList[smallestIndex])
        del inputList[smallestIndex]
        
    return sortedList

# print(selection_Sort(testingData(100)))
# Done

def bubble_sort(inputList):
    change = True
    listLen = len(inputList) -1
    while change: 
        change = False
        for elementIndex in range(listLen):
            if inputList[elementIndex] > inputList[elementIndex + 1]:
                change = True
                inputList[elementIndex], inputList[elementIndex + 1 ] = inputList[elementIndex + 1 ], inputList[elementIndex]
                
        listLen -= 1 
    
    return inputList

# I do call len() many times, could be better if you just stored it as a var 
# each pass the largest is at the end, so I can always reduce that

# print(bubble_sort(testing_data(100)))
# Done


# "Binding the list to a local name means assigning the parameter to a short local variable (e.g. a = inputList) and caching any frequently used values (like length or a method) before entering a tight loop. This reduces repeated lookups and function calls inside the loop, which is a small but measurable speed win in CPython because accessing local variables is faster than repeated attribute/global lookups or repeated calls to len()."
def quick_sort(inputList):
    a = inputList
    
    def _partition(b):
        
        p = b[0]
        s = []
        if len(b) == 1: 
            return
        for i in b:
            if p >= b:
                s.insert(0, b)
            else:
                s.append(b)
        return _partition
    
    
# using letters as var is much easier to type, might be hard to read or confusing
#this is hard

def insertion_sort(inputList):
    
    def _sorting(inputList, index):
        a = inputList
        if index == len(a) - 1:
            return a
        s = True
        p = index
        while s:
            s = False
            if p > 0: 
                if a[p-1] > a[p]:
                    s = True
                    a[p], a[p-1] = a[p-1], a[p]
            p -= 1
        return _sorting(a, index + 1 )
    
    return _sorting(inputList, 1)
# should avoid recursion to avoid recursion errors and coud be faster

print(insertion_sort(testing_data(100)))