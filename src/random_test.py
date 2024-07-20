import random

def random2asd(n):
    for i in range(6,n):
        for j in range(0,5):
            ans = 0
            for k in range(0, i):
                ans*=10
                ans+=int(random.random()*10)
            print(ans)

random.seed()
random2asd(18)
