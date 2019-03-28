from flask import Flask, jsonify, render_template, request
import json
import requests
from pprint import pprint

app = Flask(__name__)
tv_maze_url = 'http://api.tvmaze.com/singlesearch/shows?q={tv_show_name}'

all_tv_shows = [{
		"id": 4175,
		"url": "https://africamagic.dstv.com/show/my-flatmates",
		"name": "My Flatmates",
		"type": "Scripted",
		"language": "English",
		"genres": ["Drama"],
		"status": "Running",
		"runtime": 30,
		"premiered": "1995-10-23",
		"officialSite": "https://africamagic.dstv.com/show/my-flatmates",
		"schedule": {
			"time": "10:30",
			"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
		},
		"rating": {
			"average": "null"
		},
		"weight": 56,
		"network": {
			"id": 20,
			"name": "DSTV Showcase",
			"country": {
				"name": "Nigeria",
				"code": "NG",
				"timezone": "West Africa/Lagos"
			}
		},
		"webChannel": "null",
		"externals": {
			"tvrage": 1888,
			"thetvdb": 78006,
			"imdb": "tt0112004"
		},
		"image": {
			"medium": "http://static.tvmaze.com/uploads/images/medium_portrait/73/183727.jpg",
			"original": "http://static.tvmaze.com/uploads/images/original_untouched/73/183727.jpg"
		},
		"summary": "<p><b>Tinsel</b> is a situational comedy documenting the lives of four friends who share an apartment. All sorts of chaotic and hilarious things happen as they go about their daily escapades in pursuit of a better life for themselves.</p>",
		"updated": 1553265654,
		"_links": {
			"self": {
				"href": "http://api.tvmaze.com/shows/4175"
			},
			"previousepisode": {
				"href": "http://api.tvmaze.com/episodes/1623452"
			},
			"nextepisode": {
				"href": "http://api.tvmaze.com/episodes/1623453"
			}
		}
	},

	{
		"id": 4176,
		"url": "https://africamagic.dstv.com/show/tinsel",
		"name": "Tinsel",
		"type": "Scripted",
		"language": "English",
		"genres": ["Drama"],
		"status": "Running",
		"runtime": 30,
		"premiered": "2001-10-23",
		"officialSite": "https://africamagic.dstv.com/show/tinsel",
		"schedule": {
			"time": "18:30",
			"days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
		},
		"rating": {
			"average": "null"
		},
		"weight": 52,
		"network": {
			"id": 47,
			"name": "DSTV Showcase",
			"country": {
				"name": "Nigeria",
				"code": "NG",
				"timezone": "West Africa/Lagos"
			}
		},
		"webChannel": "null",
		"externals": {
			"tvrage": 1888,
			"thetvdb": 78006,
			"imdb": "tt0112004"
		},
		"image": {
			"medium": "http://static.tvmaze.com/uploads/images/medium_portrait/73/183727.jpg",
			"original": "http://static.tvmaze.com/uploads/images/original_untouched/73/183727.jpg"
		},
		"summary": "<p><b>Tinsel</b> is a Nigerian soap opera on Movie Magic DSTV Africa Magic showcase channel. This tale is a combination of drama, intrigue, romance, deception, betrayal as well as triumph.</p>",
		"updated": 1553265654,
		"_links": {
			"self": {
				"href": "http://api.tvmaze.com/shows/4175"
			},
			"previousepisode": {
				"href": "http://api.tvmaze.com/episodes/1623452"
			},
			"nextepisode": {
				"href": "http://api.tvmaze.com/episodes/1623453"
			}
		}

	}


]


##@app.route('/')
##def hello():
##	return "<h1>Hello, World!</h1>"

@app.route('/<name>')
def hello(name):
    # name = request.args.get("name")
    return('<h1>Hello, {}!</h1>'.format(name))

@app.route('/tvshow/<Show>')
def profile(Show):
    rows = session.execute( """Select * From tvshow.tvshow where Show = '{}'""".format(Show))

    for tvshow in rows:
        return('<h1>{} is {} show!</h1>'.format(Show,tvshow.type))
    return('<h1>That Show does not exist!</h1>')


@app.route('/tvshows/', methods=['GET'])
def tv_shows():
	return jsonify(all_tv_shows)

@app.route('/tvshows/single_show/', methods=['GET'])
def get_tvshow():
	response = [item['name'] for item in all_tv_shows]
	return jsonify(response)

@app.route('/tvshows/single_show/summary/', methods=['GET'])
def get_tvshow_summary(tv_show_name):
		response={tv_show_name:'Not Found!'}
		for item in tv_shows:
				if item["name"]==tv_show_name:
						response = [x["name"] for x in item["summary"]]
						break
		return jsonify(response)

##app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('welcome.html')

@app.route('/singlesearch/shows/', methods=['GET'])
def search_tvshows():
		response = [item['name'] for item in singlesearch]
		return jsonify(response)

@app.route('/schedule/full/', methods=['GET'])
def full_schedule():
		response = [item['name'] for item in full]
		return jsonify(response)

@app.route('/tv', methods=['POST','GET'])
def tvshow():
    tv_show_name = request.form['text']
    tv_show_name = request.args.get('tv_show_name', tv_show_name)
    tv_url = tv_maze_url.format(tv_show_name=tv_show_name)
    resp = requests.get(tv_url)
    a = resp.json()
    return render_template("tv.html",final=a)

if __name__ == '__main__':
	app.run(port=8080, debug=True)
