# chatty_web_app

## Installation and Running the Server

To install dependencies from requirements.txt
```pip install -r requirements.txt```

If you would like to run the server on multiple browsers/devices, change 'localhost' to your machines IP address in app.py line 69:
```socketio.run(app, host="your_IP_address", port=5000)```

To run the server:
```python3 app.py```