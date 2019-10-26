from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')

def request_image(): 
    print(render_template('webpage.html'))
    return render_template('webpage.html')

app.route('/', methods=['POST'])

def send_image():
    photo = request.file.get('webpage.html', '')
    return render_template('pass.html', photo)

if __name__ == '__main__':
    while True:
        app.run()