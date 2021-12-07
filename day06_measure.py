import time
import day06
import day06_02

start = time.time()
day06.main()
p1 = time.time()
day06_02.main()
p2 = time.time()

print((p1 - start) * 1000)
print((p2 - p1) * 1000)