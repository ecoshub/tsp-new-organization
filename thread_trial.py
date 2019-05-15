import queue
import threading
import urllib3

# called by each thread




def find_min(it):
    min_val = float('-inf')
    for i in it:
        if i > min_val:
            min_val = i
    return min_val


theurls = iter(range(100))

q = queue.Queue()

for u in theurls:
    t = threading.Thread(target=find_min, args=(theurls, ))
    t.daemon = True
    t.start()

s = q.get()
print(s)
