import requests
from threading import Thread


def test():
    url = 'https://school33.centerstart.ru/news?page=3'
    i = 0
    while True:
        response1 = requests.get(url)
        response2 = requests.post(url)
        i += 1
        print(i, response1)
        i += 1
        print(i, response2)


print('main')
thrnon = 1
test()
# for i in range(int(thrnon)):
#     thr = Thread(target=test)
#     thr.start()
