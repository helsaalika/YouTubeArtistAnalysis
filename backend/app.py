from flask import Flask, jsonify
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/YT-Analysis-Project'

try:
    mongo = MongoClient(app.config['MONGO_URI'])
    mongo.admin.command('ismaster')  # Check if MongoDB is available
    print("Database sudah terhubung")
except ConnectionFailure as e:
    print(f"Koneksi ke database gagal: {e}")

db = mongo['YT-Analysis-Project']  # Use dictionary-style notation to access the database

@app.route('/')
def index():
    data = {'message': 'Database Connected!'}
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
