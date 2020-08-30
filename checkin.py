import requests, json

# server酱开关，填0不开启(默认)，填1只开启cookie失效通知，填2同时开启cookie失效通知和签到成功通知
sever = '0'
# 填写server酱sckey,不开启server酱则不用填
sckey = 'SCU89402Tf98b7f01ca3394b9ce9aa5e2ed1abbae5e6ca42999999'
# 填入glados账号对应cookie
cookie = '__cfduid=db79479eaddb227c9ee91b229b62d896b1598747991; _ga=GA1.2.2047428545.1598747984; _gid=GA1.2.1075437917.1598747984; koa:sess=eyJ1c2VySWQiOjQ3NzEzLCJfZXhwaXJlIjoxNjI0NjY4MTY3ODM2LCJfbWF4QWdlIjoyNTkyMDAwMDAwMH0=; koa:sess.sig=Rd8M0wv_tYTfniG0MUVw97I5pPE'
referer = 'https://glados.rocks/console/checkin'

def start():
    url= "https://glados.rocks/api/user/checkin"
    url2= "https://glados.rocks/api/user/status"
    checkin = requests.post(url,headers={'cookie': cookie ,'referer': referer })
    state =  requests.get(url2,headers={'cookie': cookie ,'referer': referer})
   # print(res)

    if 'message' in checkin.text:
        mess = checkin.json()['message']
        time = state.json()['data']['leftDays']
        time = time.split('.')[0]
        #print(time)
        if sever == '2':
            requests.get('https://sc.ftqq.com/' + sckey + '.send?text='+mess+',xms，you have '+time+' days left')
    else:
        requests.get('https://sc.ftqq.com/' + sckey + '.send?text=cookie过期')

def main_handler(event, context):
  return start()

if __name__ == '__main__':
  start()
