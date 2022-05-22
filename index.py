from nturl2path import url2pathname
from bs4 import BeautifulSoup
import requests
from flask import request
import json
import flask

app =  flask.Flask(__name__)

@app.route('/v1/vimeo')
def index():
    id = request.args.get('id',type = int)
    youtube_url = f"https://player.vimeo.com/video/{id}/config"
    response = requests.request("GET", youtube_url)
    soup = BeautifulSoup(response.text, "html.parser")
    result = json.loads(soup.text)
    result = result['request']['files']['progressive']

    qualities = []
    url = []
    for i in result:
        qualities.append(i['quality'])
        url.append(i['url'])

    data = {}
    for key in qualities:
        for value in url:
            data[key] = value
            url.remove(value)
            break  

    json_data = json.dumps(data, indent = 4) 

    return json_data

if __name__ == '__main__':
    app.run()


