from flask import Flask
from threading import Thread

app = Flask('')


@app.route('/')
def home():
  return "Stay with me."


def run():
  app.run(host='0.0.0.0', port=8080)


def stay_alive():
  s = Thread(target=run)
  s.start()
