from wsgiref.simple_server import make_server
import requests
import json

def weather(smth, response):
    status = '200 OK'
    headers = [('Content-type', 'text/html;charset = utf-8')]
    # api.openweathermap.org/data/2.5/weather?q=London&appid=b6b92ff090fb41e4a9f51762c5100f11
    url = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s' % ('Moscow','b6b92ff090fb41e4a9f51762c5100f11')
    print(json.loads(requests.get(url).text))
    response(status, headers)
    return [b'HELLO WORLD']

server = make_server('', 8000, weather)
server.serve_forever()