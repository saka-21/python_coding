# # JSON

# import json

# j = {
#     "employee":
#     [
#         {"id": 111, "name": "Mike"},
#         {"id": 222, "name": "Nancy"}
#     ]
# }
# print(j)
# print("--------------")
# print(json.dumps(j))

# with open('test.json', 'w') as f:
#     json.dump(j, f)

# print('aaa')

from flask import Flask
from flask import g
from flask import render_template
from flask import request
from flask import Response

app = Flask(__name__)

@app.route('/', methods=[''])
def hello_world():
    return 'hello world'

def main():
    app.debug = True
    app.run()


if __name__ == '__main__':
    main()
