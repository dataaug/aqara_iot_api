import hashlib
import time
import json
from params import params
import os
from commands import action_light_up, action_light_down, action_light_intensity, action_light_temperature
import time


class RequestAqara():
    def __init__(self) -> None:
        self.params = params

    def get_sign(self, time_now):
        string = ''
        if self.params['Accesstoken']:
            string += 'Accesstoken=' + self.params['Accesstoken'] + '&'

        string += 'Appid=' + self.params['Appid'] + '&'
        string += 'Keyid=' + self.params['Keyid'] + '&'
        # self.time_now = str(int(time.time() * 1000))
        string += 'Nonce=' + time_now + '&'
        string += 'Time=' + time_now
        string += self.params['AppKey']
        print(string.lower())
        return hashlib.md5(string.lower().encode(encoding="UTF-8")).hexdigest()

    def request(self, body):
        time_now = str(int(time.time() * 1000))
        self.params['Sign'] = self.get_sign(time_now)
        request_url = '''
                time curl -X POST -d '
                [body]
            '  -H 'Content-Type: application/json' -H 'Appid:[Appid]' -H 'Keyid:[Keyid]' -H 'Time:[Time]' -H 'Nonce:[Nonce]' -H 'Sign:[Sign]'  -H 'Accesstoken:[Accesstoken]' https://open-cn.aqara.com/v3.0/open/api
            '''
        request_url = request_url.replace('[body]', json.dumps(body))
        request_url = request_url.replace('[Appid]', params['Appid'])
        request_url = request_url.replace('[Keyid]', params['Keyid'])
        request_url = request_url.replace('[Time]', time_now)
        request_url = request_url.replace('[Sign]', params['Sign'])
        request_url = request_url.replace('[Nonce]', time_now)
        request_url = request_url.replace(
            '[Accesstoken]', params['Accesstoken'])

        result = os.popen(request_url).read()
        return result

def light_up(tool = None):
    if not tool:
        tool = RequestAqara()
    result = tool.request(action_light_up)

def light_down(tool = None):
    if not tool:
        tool = RequestAqara()
    result = tool.request(action_light_down)

def wink():
    tool = RequestAqara()
    # result = action(action_light_up)
    # print('action_light_down:', action_light_down)
    # time.sleep(10)
    # result = action(action_light_up)
    # result = tool.request(action_light_up)
    light_up(tool)
    time.sleep(0.1)
    light_down(tool)
    # print(action_light_down)
    # result = tool.request(action_light_down)
    return result

def light_adjust(intensity, temperature = 0, tool = None): # 色温最低2700 最高6500
    if not tool:
        tool = RequestAqara()
    action_light_intensity['data'][0]['resources'][0]['value'] = intensity
    result = tool.request(action_light_intensity)

    if temperature >= 2700 and temperature <= 6500:
        action_light_temperature['data'][0]['resources'][0]['value'] = int(1000000 / temperature)
        result = tool.request(action_light_temperature)
        # print(result)



if __name__ == '__main__':
    tool = RequestAqara()
    # tool = RequestAqara()
    # # result = action(action_light_up)
    # # print('action_light_down:', action_light_down)
    # # time.sleep(10)
    # result = action(action_light_up)
    # result = tool.request(action_light_up)
    
    # time.sleep(0.3)
    # # print(action_light_down)
    # result = tool.request(action_light_down)

    # result = wink()
    # light_down()
    time.sleep(1)
    light_adjust(1, 2700)
    # print(result)
