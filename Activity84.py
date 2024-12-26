#Write a Python program to create a class that will find the numbers in the tuple that add up to a sum and return the position of elements. The value of the sum can be taken as input from the user. Tuple - (10,20,30,40,50,60,70)
class tulips:
    
    def twoSum(self,nums,target):
        lookup={}
        for a ,num in enumerate(nums):
            if target-num in lookup:
                return(lookup[target-num],a)
            lookup[num]=a
value = int(input('Enter the numbers you wanna search'))
print('index1 =%d, index2=%d'%tulips().twoSum((10,20,30,40,50,60,70),value))
            
            
                                                                                                                                   