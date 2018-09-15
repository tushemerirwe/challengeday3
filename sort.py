def listsort(mylist):
    listEvenNumbers = [number for number in mylist if isinstance(number, int) and number % 2 == 0]
    listOddnumbers = [number for number in mylist if isinstance(number, int) and  number % 2 != 0]
    listChars = [element for element in mylist if isinstance(element, str) ]

    listEvenNumbers.sort()
    listOddnumbers.sort()
    listChars.sort()

    return {
        "even": listEvenNumbers,
        "odd": listOddnumbers,
        "chars": listChars,
    }
    
print(listsort([2,0,6,5,1,7,"z","a"]))