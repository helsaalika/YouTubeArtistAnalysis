from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/YT-Analysis-Project'
mongo = MongoClient(app.config['MONGO_URI'])
db = mongo['YT-Analysis-Project']  # Use dictionary-style notation to access the database

@app.route('/')
def index():
    # Contoh: Dapatkan data dari koleksi 'artistchannels' dan 'datavideos'
    data_artist = db.artistchannels.find()
    data_video = db.datavideos.find()

    # Kirim kedua set data ke template
    return render_template('index.html', data_artist=data_artist, data_video=data_video)

if __name__ == '__main__':
    app.run(debug=True)
