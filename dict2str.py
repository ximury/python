import json

di = {
  '_id': '8102',
  'configData': {
    'Name': 'org.ukui.watermark',
    'Path': '/org/ukui/watermark',
    'Interfaces': 'org.ukui.watermark',
    'ukui-watermark': [
      {
        'name': '默认策略水印',
        'visible': 'false',
        'userNameVisible': 'true',
        'timeStampVisible': 'true',
        'textVisible': 'true',
        'setWindowOpacity': 0.1,
        'textContent': '默认策略',
        'textSize': 24,
        'density': [
          10,
          10
        ],
        'position': [
          50,
          50,
          100,
          100
        ],
        'rotate': 45
      }
    ]
  },
  'hash': '1e86d4a898813d1ad8aa350b0e0e89af',
  'server_local': 'watermark/8102.json',
  'strategy_id': '8000'
}
di = {
"Name": 'com.kylin.kysdk.systemsettings',
    "Path": '/com/kylin/kysdk/screensaver',
    "Interfaces": 'com.kylin.kysdk.screensaver',
    "params": {
      "Enable": [
        True
      ],
      "AutoLockEnable": [
        True
      ],
      "AutoLockTime": [
        600
      ]
    }
}
st = json.dumps(di)
print(st)
with open('dict_to_json.json', 'w') as f:
    f.write(st)
f.close()
