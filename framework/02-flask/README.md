## Flask

### Activate virtual environment
```
python3 -m venv learn
source learn/bin/activate
```

### Install dependencies
```
pip install flask
```

### To run the flask application
```
flask run
or
python -m flask run
```

### To expose the application to outside
```
flask run --host=0.0.0.0
```

### Check the response with curl
```
curl http://127.0.0.1:5000/hello
curl http://127.0.0.1:5000/info
```