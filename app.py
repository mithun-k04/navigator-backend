from flask import Flask, request, jsonify
import urllib.parse

app = Flask(__name__)

@app.route('/get-directions', methods=['POST'])
def get_directions():
    data = request.get_json()
    origin_lat = data['origin']['lat']
    origin_lng = data['origin']['lng']
    destination = urllib.parse.quote(data['destination'])  

    map_url = f"https://www.google.com/maps/dir/?api=1&origin={origin_lat},{origin_lng}&destination={destination}&travelmode=driving"

    return jsonify({'url': map_url})

if __name__ == '__main__':
    app.run()
