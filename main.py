"""from car import Car

# create Instances
car1 = Car("BMW", 2024, "Black", False)  
car2 = Car("BMW", 2024, "Red", False)
car3 = Car("BMW", 2024, "White", True)

car1.drive()

l = [0,0,1,1,1,2,2,3,3,4]

s = []

for i in l:
   if i in s:
      l.remove(i)
   else:
      s.append(i)
   
print(s,l)

class Animals:
    def __init__(self, name):
        self.name = name
    def sleep (self):
        print(f'{self.name}  is sleeping')

class Dog(Animals): 
    pass
dog = Dog('snoopy')

print( dog.sleep())    #numbers_list = [0,1,1,2,4]
                          #output_list = [0,1,2,4]


class remove_duplicate :
    def __init__(self, nums):
        self.numbers_list = nums
        self.output_list = []
    
    def remover(self):
        for i in self.numbers_list[:]:
            if i in self.output_list:
                self.numbers_list.remove(i)
            else:
                self.output_list.append(i)
        return self.output_list
    
# exemple

nums = remove_duplicate([0,1,1,2,4])

output = nums.remover()

print(output)



class not_equal_element:
   
    def __init__(self, nums, val):   #  [3,2,2,3]
        self.nums = nums 
        self.val = val               #  3
        self.good_element = []

    def not_equal(self):
        for i in self.nums[:]:
            if i != self.val:
                self.good_element.append(i)     # [2,2]

    def rerrange(self):   # [2,2,_,_]
        
        k = len(self.good_element)
        for i in range(k):
            self.nums[i] = self.good_element[i]
        return k 
    
nums = [2, 3, 3, 2]
val = 3

not_equal_prob = not_equal_element(nums, val)
not_equal_prob.not_equal()
k = not_equal_prob.rerrange()

print(k)
print(nums)"""


class shuffle:
    def __init__(self, nums):
        self.nums = nums 
        self.output = []
    
    def shuffling(self):
       middle_index = len(self.nums)//2
       

       for i in range(middle_index):
           self.output.append(self.nums[i])
           self.output.append(self.nums[middle_index +i])

       return self.output

nums = [1,5,7,9,0,1]

shuf = shuffle(nums)
k = shuf.shuffling() 
print(k)
