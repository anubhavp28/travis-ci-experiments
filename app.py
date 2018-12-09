from flask import Flask, jsonify
import requests as req

app = Flask(__name__)

@app.route('/series/current', methods=['GET'])
def current_series():
    try:
        r = req.get('https://cricbuzz.com/api/match/current')
        matches = r.json()
    except ValueError:
        return jsonify({
            "error" : "Invalid json response received from cricbuzz servers. Cricbuzz might have changed their internal API."
        })
    except req.RequestException:
        return jsonify({
            "error" : "Unable to get a response from cricbuzz servers. Cricbuzz might have changed their internal API."
        })
    uniques = set()
    series = []
    for match in matches:
        if 'series' in match:
            if match['series']['id'] not in uniques:
                uniques.add(match['series']['id'])
                series.append(match['series'])

    return jsonify(series)

#@app.route('/match/current', methods=['GET'])
#def current_match():
