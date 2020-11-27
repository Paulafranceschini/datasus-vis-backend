from app import app
import os
from flask import Flask, jsonify, json;

if __name__ == "__main__":
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=8080, debug=True)
