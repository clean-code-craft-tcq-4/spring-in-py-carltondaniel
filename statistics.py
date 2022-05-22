import math
def calculateStats(numbers):
    num_dict={}
    if numbers:
    	total=sum(numbers)
    	count=len(numbers)
    	average=total/count
    	num_dict["avg"]=average
    	num_dict["max"]=max(numbers)
    	num_dict["min"]=min(numbers)
    else:
        num_dict["avg"]=str(math.nan)
        num_dict["max"]=str(math.nan)
        num_dict["min"]=str(math.nan)
	
    

    return num_dict



class EmailAlert:
    emailSent=False


class LEDAlert:
    ledGlows=False


class StatsAlerter:

    def __init__(self,maxThreshold,AlertObjects):
        self.maxThreshold=maxThreshold
        self.AlertObjects=AlertObjects

    def checkAndAlert(self,checkList):
        self.checkList=checkList
        for ele in self.checkList:
            if ele > self.maxThreshold:
                self.AlertObjects[0].emailSent=True
                self.AlertObjects[1].ledGlows=True
                
                


        

        
