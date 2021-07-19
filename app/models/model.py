def tip(num, tip):
    answer = num*(tip/100)
    answer = str(round(answer, 2))
    # if answer[len(answer)-1] == "0":
    #     return answer+"0"
    return answer
    
def totalBill(num,tip):
    answer= num*(1+(tip/100))
    answer = str(round(answer, 2))
    # if answer[len(answer)-1] == "0":
    #     return answer+"0"
    return answer
    
def split(num, tip, people):
    answer = (num*(1+(tip/100)))/people
    answer = str(round(answer, 2))
    # if answer[len(answer)-1] == "0":
    #     return answer+"0"
    return answer
    
    
    