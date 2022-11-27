import math
import time
start = time.time()
try:
    x = 0
    y = 1
    while True:
        x += 6 / y ** 2
        print(math.sqrt(x))
        y += 1
except KeyboardInterrupt:
    end = time.time()
    print(f"Time taken: {end - start} s")
    exit()
