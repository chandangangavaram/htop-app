from flask import Flask
import getpass
import subprocess
import datetime
import pytz

app = Flask(_name_)

@app.route('/htop')
def htop():
   
    name = "Gangavaram Venkata Sai Chandan"

    username = getpass.getuser()

    ist = pytz.timezone('Asia/Kolkata')
    server_time = datetime.datetime.now(ist).strftime("%Y-%m-%d %H:%M:%S")

    top_output = subprocess.getoutput("top -b -n 1 | head -15")

    return f"""
    <h2>Name: {name}</h2>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <pre>{top_output}</pre>
    """

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
