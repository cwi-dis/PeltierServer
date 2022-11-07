# Peltier server

Quick and dirty web server that forwards temperatures to an Arduino board driving a peltier element.

## Installation and running

```
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
flask run
```

## Usage

Let's assume the server is running on `mylaptop.local`. Then you can send (from anywhere on the local wifi network) an HTTP GET request to `http://mylaptop.local:5000/peltier/37.3`.

The server will print a message `Temperature: 37.3` and forward the request to the Arduino board over a USB serial connection.