from flask import *
import RPi.GPIO as GPIO
import time
from os.path import expanduser
import io
import subprocess
import sqlite3
from contextlib import closing

app = Flask(__name__)

@app.route("/flask/myhome/")
def myhome():
    SOUNDER = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SOUNDER, GPIO.OUT, initial = GPIO.LOW)
    Hz = 25
    p = GPIO.PWM(SOUNDER, 1)
    p.start(70)
    p.ChangeFrequency(880)
    time.sleep(5)
    #gochiusa(p)
    #p.start(50)
    #for i in range(1, 500) :
    #    p.ChangeFrequency(i * Hz)
    #    time.sleep(0.2)
    p.stop()
    GPIO.cleanup()
    return render_template('myhome.html')

@app.route('/flask/myhome/googlehome', methods=['GET'])
def googlehome():
    m = request.args.get('m', 'メッセージの内容がありません。')
    subprocess.run(['node', 'message.js', m], cwd=expanduser('~/google/google-home-notifier/'))
    with closing(sqlite3.connect('downloads/test.db')) as conn:
        c = conn.cursor()
        c.execute(
            "insert into test(time, msg) values(datetime('now', 'localtime'), ?)",
            [m]
        )
        conn.commit()
    return escape(m)

def gochiusa(p):
    p.ChangeFrequency(392)
    time.sleep(0.2)
    p.ChangeFrequency(415)
    time.sleep(0.2)
    p.ChangeFrequency(466)
    time.sleep(0.2)
    p.ChangeFrequency(523)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(523)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(523)
    time.sleep(0.2)
    p.ChangeFrequency(523)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(466)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(466)
    time.sleep(0.2)
    p.ChangeFrequency(415)
    time.sleep(0.2)
    p.ChangeFrequency(415)
    time.sleep(0.2)
    p.ChangeFrequency(392)
    time.sleep(0.2)
    p.ChangeFrequency(415)
    time.sleep(0.2)
    p.ChangeFrequency(392)
    time.sleep(0.2)
    p.ChangeFrequency(349)
    time.sleep(0.2)
    p.ChangeFrequency(311)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(466)
    time.sleep(0.2)
    time.sleep(0.2)
    p.ChangeFrequency(311)
    time.sleep(0.2)
    time.sleep(0.2)


if __name__ == "__main__":
    app.run(debug=True)
