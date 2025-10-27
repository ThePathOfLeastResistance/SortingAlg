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


    


# using letters as var is much easier to type, might be hard to read or confusing
#this is hard

def insertion_sort(inputList):
    a = inputList
    n = len(a)
    # dont forget this section here 
    if n < 2:
        return a
    
    for i in range(1, n):
        key = a[i]
        e = i - 1
        
        while e >= 0 and a[e] > key:
            a[e +1] = a[e]
            e -= 1
            
        a[e + 1] = key
    return a 
        
        
    
# should avoid recursion to avoid recursion errors and coud be faster
#it is much easier to type everyting when the var are just letters
# print(insertion_sort([3,2,4,2,5,6,3]))
# Done

