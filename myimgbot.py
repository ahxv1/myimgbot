import time,requests

time_user = int(input("Enter time in second : "))

while True:
    for x in range(time_user,0,-1):
        sacond = int(x%60)
        print(f'00:00:{sacond}',end='\r')
        time.sleep(1)

    req = requests.get(url='https://random.responsiveimages.io/v1/docs')
    with open('jj.jpg','wb') as d:
        d.write(req.content)
    files = {f'photo':open(f'jj.jpg','rb')}

    tlg = (f'''https://api.telegram.org/bot5587578988:AAGqPKBMqRvCzJUCDVTrGMX_adfwLhPzNpE/sendPhoto?chat_id=-1001670680818''')
    i = requests.post(tlg,files=files)


