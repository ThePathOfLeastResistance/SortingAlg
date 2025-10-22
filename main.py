import json 

def testingData(index):
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
            
def selection_Sort(inputList):
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

def bubble_Sort(inputList):
    change = True
    while change: 
        change = False
        for elementIndex in range(len(inputList) - 1):
            if inputList[elementIndex] > inputList[elementIndex + 1]:
                change = True
                inputList[elementIndex], inputList[elementIndex + 1 ] = inputList[elementIndex + 1 ], inputList[elementIndex]
    return inputList

print(bubble_Sort(testingData(100)))