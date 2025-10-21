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
            
            
def selection_Sort(inputList):
    lenOfList = len(inputList)
    sortedList = []
    for value in range(lenOfList):
        smallestElement = inputList[0]
        for subvalue in range(lenOfList):
            newElement = inputList[subvalue]
            if smallestElement > newElement:
                smallestElement = newElement
                del inputList[subvalue]
        if smallestElement == inputList[0]:
            del inputList[0]
            
        sortedList.append(smallestElement)
    return sortedList

print(selection_Sort(testingData(100)))