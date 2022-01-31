import requests
def snippet(params):
    url = 'https://api.crabon.io/v1/snippet'
    path = 'i.png'
    response = requests.post('https://carbonara-42.herokuapp.com/api/cook', json=params)
    if response.status_code == 200:
        with open(path, 'wb') as f:
            for chunk in response:
                f.write(chunk)
    print(response.status_code)


code = '''
print("Hello World")
'''

params = {'code': code,
          "paddingVertical": "56px",
          "paddingHorizontal": "57px",
          "backgroundImage": None,
          "backgroundImageSelection": None,
          "backgroundMode": "color",
          "backgroundColor": "rgba(3,26,26,1)",
          "dropShadow": True,
          "dropShadowOffsetY": "7px",
          "dropShadowBlurRadius": "10px",
          "theme": "panda-syntax",
          "windowTheme": "bw",
          "language": "auto",
          "fontFamily": "Hack",
          "fontSize": "18px",
          "lineHeight": "250%",
          "windowControls": True,
          "widthAdjustment": True,
          "lineNumbers": True,
          "firstLineNumber": 1,
          "exportSize": "2x",
          "watermark": False,
          "squaredImage": False,
          "hiddenCharacters": True,
          "width": 680}


snippet(params)
