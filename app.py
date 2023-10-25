from flask import Flask, render_template, request
from GetDirections import *

api_key = 'AIzaSyA6cXymaX959J3CYjXTcNhCTBFTt9qi6pM'

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    '''The `index()` function retrieves route data based on user input, extracts relevant information from
    the data, and renders an HTML template with the extracted information.

    Returns
    -------
        The function `index()` returns a rendered template called 'index.html' with various variables
    passed to it. The variables include `start`, `end`, `api_key`, `start_lat`, `start_long`, `end_lat`,
    `end_long`, `stop1_lat`, `stop1_long`, `stop1_address`, `stop2_lat`, `stop2_long`, and
    `stop2_address

    '''
    if request.method == 'POST':
        return render_template('index.html', api_key=api_key)
    return render_template('index.html', api_key=api_key)


@app.route('/receive_location_data', methods=['GET'])
def receive_location_data():
    '''The function receives latitude and longitude data of the user, uses an API key to get the corresponding address,
    and returns the address.

    Returns
    -------
        The address of the current location of the user corresponding to the latitude and longitude provided.
    
    '''
    lat = request.args.get('latitude')
    long = request.args.get('longitude')
    address = get_address_from_lat_lng(lat, long, api_key)
    return address


if __name__ == '__main__':
    app.run(debug=True)
