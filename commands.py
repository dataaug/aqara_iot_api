import copy
action_light_up = {
    "intent": "write.resource.device",
    "data": [
        {
            "subjectId": "lumi.54ef4410003fead8",
            "resources": [
                {
                    "resourceId": "4.1.85",
                    "value": "1"
                }
            ]
        }
    ]
}

action_light_down = copy.deepcopy(action_light_up)
action_light_down['data'][0]['resources'][0]['value'] = 0

action_light_intensity = copy.deepcopy(action_light_up)
action_light_intensity['data'][0]['resources'][0]['resourceId'] = '1.7.85'
action_light_intensity['data'][0]['resources'][0]['value'] = 0 # 灯光强度默认为1

action_light_temperature = copy.deepcopy(action_light_up)
action_light_temperature['data'][0]['resources'][0]['resourceId'] = '1.9.85'
action_light_temperature['data'][0]['resources'][0]['value'] = 370