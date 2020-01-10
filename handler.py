import json
import datetime
import numpy as np

def hello(event, context):
    current_time = datetime.datetime.now().time()
    a = np.arange(15).reshape(3, 5)
    print("Your numpy array:")
    print(a)
    body = {
        "message": "Hello, the current time is " + str(current_time),
        # "input": event
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response
