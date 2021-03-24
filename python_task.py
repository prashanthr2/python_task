#/usr/bin/python
def predictdata(stockData, queries):
    result = [] #list to save the result , that is the days on which the stock price is less than days givem by player 1
    
    for day in queries: # loop through each day given by player 1
        flag=0 # flag variable to indicate if the found a match , that is a day where stock price is less than current day
        day_value = stockData[day-1] #getting the value of current day, since list in python starts from 0. doing day-1
        for i in range(day-1,-1,-1): # this for loop is to parse the stockData from current day to start of the list
            if stockData[i] < day_value: #getting the stock price here and comparing it with the stock price on the day given by player1.
                result.append(i+1) # the day on which the stock price is less than current day will be appended to the result list. using +1 as list in python starts with 0
                flag+=1 #incrementing flag here in order to stop parsing the remaining of the StockData list
                break
        if flag!=1: #checking if the flag value is already set, if set then we dont need to parse the remaining list as we found the day on which the stock is less than current day
            
            for i in range(day,len(stockData),1): #if no match is found for the days previous to current day, we will parse the stockData list for the days after the current day ( Parsing list from current value to till the end of the list)
                if stockData[i] < day_value: # Same as before, we are checking the value of any days is less than current day
                    result.append(i+1) #saving the value to result list
                    flag+=1 #incrementing flag here , and we use it next to decide on what to do next
                    break
                    
        if flag!=1: #if flag value is not sent any where, then we didnt find a match, hence append -1
            result.append(-1)
    
    print(result)     



stockData = [5, 6, 8, 4, 9, 10, 8, 3, 6, 4]
queries = [6,5,4,10,8,1]

predictdata(stockData,queries)
