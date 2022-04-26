import requests

url = 'https://api.fpt.ai/vision/idr/vnm'

files = {'image': open('CARD.png', 'rb').read()}
headers = {
    'api-key': 'RQpZ1ZDQvVUIGqC9vvdEavSZmAnYU8W0'
}

response = requests.post(url, files=files, headers=headers)

print(response.text)
