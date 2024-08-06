import os
from flask import Flask, render_template, send_from_directory, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/images/<filename>')
def serve_image(filename):
    return send_from_directory('images', filename)

@app.route('/images')
def list_images():
    image_folder = 'images'
    image_files = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return jsonify(image_files)

if __name__ == '__main__':
    app.run(debug=True)






#####Previous Code

'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
'''