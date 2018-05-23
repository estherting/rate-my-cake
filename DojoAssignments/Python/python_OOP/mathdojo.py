# Part I
class MathDojo:
    def __init__(self):
        self.result = 0
        print(self.result)
    def add(self, *nums):
        for num in nums:
            self.result += num
        return self
    def subtract(self, *nums):
        for num in nums:
            self.result -= num
        return self


#md = MathDojo()
#print(md.add(2).add(2, 5).subtract(3, 2).result)


# Part II
class Mathdojo2:
    def __init__(self):
        self.result = 0
        print(self.result)
    def add(self, *nums):
        for num in nums:
            if isinstance(num, int):
                self.result += num
            else:
                for i in num:
                    self.result += i
        return self
    def subtract(self, *nums):
        for num in nums:
            if isinstance(num, int):
                self.result -= num
            else:
                for i in num:
                    self.result -= i
        return self
md2 = Mathdojo2()
print(md2.add([1], 3, 4).add([3,5,7,8], [2,4,3,1,25]).subtract(2, [2,3],[1,1,2,3]).result)
