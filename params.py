from email.quoprimime import body_check
import time

params = {}
params['Accesstoken'] = 'xxx'
params['Appid'] = 'xxx'
params['Keyid'] = 'xxx'
params['AppKey'] = 'xxx'
params['Nonce'] = str(int(time.time() * 1000))
params['Time'] = str(int(time.time() * 1000))  # 时间 ms
