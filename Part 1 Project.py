
from bs4 import BeautifulSoup
from tqdm.notebook import tqdm as tqdm
import requests
import time

session_requests = requests.session()


header = {"user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36"}


URL = "https://www.planespotters.net/user/login"
page1 = session_requests.get(URL, headers = header)
doc1 = BeautifulSoup(page1.content, 'html.parser')

cookies1 = session_requests.cookies.get_dict()

input1 = doc1.find("input", id = 'csrf')
input2 = doc1.find("input", id = 'rid')


csrf = input1.get("value")
rid = input2.get("value")
rid = ""


time.sleep(5)

res = session_requests.post(URL, data = {"username":"hello555","password":"hello123","csrf": csrf,"rid":rid},timeout = 15, cookies = cookies1, headers = header)


cookies2 = res.cookies.get_dict()


cookies = dict(cookies1,**cookies2)
URL = "https://www.planespotters.net/member/profile"


page2 = session_requests.get(URL, cookies=cookies, headers = header)
doc2 = BeautifulSoup(page2.content, 'html.parser')


print("Entire Document:", doc2)
print("Combined Cookies: ", cookies)

if doc2.find(text = 'hello555'):
    print('True')
else:
    print('False')    

