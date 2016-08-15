import time
import urllib3
from multiprocessing.dummy import Pool as ThreadPool


def main(host):
    http = urllib3.PoolManager()
    url = http.request('GET', host)
    print(url.status)

pool = ThreadPool(4)

hosts = ["http://yahoo.com", "http://google.com", "http://amazon.com",
         "http://ibm.com", "http://apple.com", "http://gameover.com.ua"]

start = time.time()

pool.map(main, hosts)
pool.close()
pool.join()

print("Elapsed Time: {}" .format(time.time() - start))
