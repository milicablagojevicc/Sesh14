from latam import china
from latam.china import cook as china_cook
from japan import cook as japan_cook, is_prime
from latam.peru import cook as peru_cook

def cook():
    print("we are spanish, we are making paella")

print(china.greet)
japan_cook()
china_cook()
cook()

print(f"1027 is prime: {is_prime(1027)}")

peru_cook()