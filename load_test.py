import requests
import threading
import time

URL = "http://3.80.175.17:5000/apidocs/"
THREADS = 1000
DURATION = 600

print(URL)

end_time = time.time() + DURATION
threads = []

for _ in range(THREADS):
    t = threading.Thread(target=load_test)
    t.start()
    threads.append(t)

for t in threads:
    t.join()


def load_test():
    while time.time() < end_time:
        try:
            requests.get(URL, timeout=2)
        except Exception:
            pass

print("Finished loading test")

