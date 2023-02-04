from flask import Flask, render_template, jsonify
from numerize.numerize import numerize
import requests
import random

Channels = {
    'datasciencewithsaify':'UCZ0lqWahpHE2ctzVh9mhncQ',
    'cleverprogrammer':'UCqrILQNl5Ed9Dz6CGMyvMTQ',
    'arshad':'UCrs6J5y7Dc08BRg9RXx2QrQ',
    'fraz':'UC81Q2wnuk5KqOFVgAbq4nUw',
    'namanahkapoor':'UCLpovxJVLBZrXJGCymB6LYw'  
}

app = Flask(__name__)

@app.route('/')
def home():
    
    url = "https://youtube138.p.rapidapi.com/channel/videos/"

    querystring = {"id":random.choice([Channels[i] for i in Channels]),"hl":"en","gl":"US"}

    headers = {
	"X-RapidAPI-Key": "626e1dde0emsh1fbae465cb4970cp14b1cbjsnd0ac795c2422",
	"X-RapidAPI-Host": "youtube138.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    
    contents = data['contents']
    videos = [video['video'] for video in contents if video['video']['publishedTimeText']]
    video = videos[0]
    return render_template('index.html', video = video, videos = videos)

# adding filter to numerzie our views
@app.template_filter()
def numberize(views):
    return numerize(views, 1)

app.run()

