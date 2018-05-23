import random
def randInt(min=0, max=100):
    return int(random.random()*max + min)

print randInt()
print randInt(max=50)
print randInt(min = 50)
print randInt(min=50, max=500)
