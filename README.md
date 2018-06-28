# dockPond Sample EBOs

[dockPond](https://github.com/rmetcalf9/dockPond) is a application that will create a data lake based on data models it reads from git. This is a sample repository with some data models for it to read.


## Code to test a model

Go into the model directory and run the following in a python REPL
```
from flask_restplus import Api
import model
flaskRestPlusAPIObject = Api(None, version='UNSET', title='Dummy Test', description='Dummy', doc='/', default_mediatype='application/json')
aa = model.getModel(flaskRestPlusAPIObject)
```