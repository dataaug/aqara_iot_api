import hashlib
import time
import json
from params import params
import os


class RequestAqara():
    def __init__(self) -> None:
        self.params = params

    def get_sign(self):
        string = ''
        if self.params['Accesstoken']:
            string += 'Accesstoken=' + self.params['Accesstoken'] + '&'

        string += 'Appid=' + self.params['Appid'] + '&'
        string += 'Keyid=' + self.params['Keyid'] + '&'
        string += 'Nonce=' + self.params['Nonce'] + '&'
        string += 'Time=' + self.params['Time']
        string += self.params['AppKey']
        print(string.lower())
        return hashlib.md5(string.lower().encode(encoding="UTF-8")).hexdigest()

    def request(self, body):

        self.params['Sign'] = self.get_sign()
        request_url = '''
                time curl -X POST -d '
                [body]
            '  -H 'Content-Type: application/json' -H 'Appid:[Appid]' -H 'Keyid:[Keyid]' -H 'Time:[Time]' -H 'Nonce:[Nonce]' -H 'Sign:[Sign]'  -H 'Accesstoken:[Accesstoken]' https://open-cn.aqara.com/v3.0/open/api
            '''
        request_url = request_url.replace('[body]', json.dumps(body))
        request_url = request_url.replace('[Appid]', params['Appid'])
        request_url = request_url.replace('[Keyid]', params['Keyid'])
        request_url = request_url.replace('[Time]', params['Time'])
        request_url = request_url.replace('[Sign]', params['Sign'])
        request_url = request_url.replace('[Nonce]', params['Nonce'])
        request_url = request_url.replace(
            '[Accesstoken]', params['Accesstoken'])

        result = os.popen(request_url).read()
        return result


if __name__ == '__main__':
    tool = RequestAqara()
    result = tool.request({
        "intent": "query.resource.value",
        "data": {
            "resources": [
                {
                    "subjectId": "lumi.54ef441000518b63",
                    "resourceIds": [
                        "3.51.85"
                    ]
                }
            ]
        }
    })
    print(result)
