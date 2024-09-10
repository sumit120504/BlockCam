from flask import Flask, render_template, jsonify,  request, redirect, url_for
from web3 import Web3

app = Flask(__name__)


w3 = Web3(Web3.HTTPProvider(''))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_balance/<address>')
def get_balance(address):
    balance = w3.eth.get_balance(address)
    eth_balance = w3.fromWei(balance, 'ether')
    return jsonify({'balance': eth_balance})

@app.route("/dashboard")
def dashboard():
    return render_template("dash.html")

@app.route("/ai-models")
def ai():
    return render_template("ai.html")

@app.route("/abc")
def video():
    return render_template("video.html")

@app.route("/plans")
def plans():
    return render_template("plans.html")

@app.route("/check-footage")
def check_footage():
    return render_template("preview.html")

@app.route('/video', methods=['POST'])
def submit():
    camera_url = request.form.get('cameraUrl')
    return redirect(url_for('live', url=camera_url))


# @app.route('/dashboard')
# def submit():
#     camera_url = request.form.get('url','')
#     return render_template(url_for('live', url=camera_url))

@app.route('/live-footage')
def live():
    camera_url = request.args.get('url', '') 
    return render_template('live.html', camera_url="https://www.youtube.com/embed/"+camera_url+"?autoplay=1&mute=0")
if __name__ == '__main__':
    app.run(debug=True, port = 8000)
