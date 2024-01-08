#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    response = "<h1>Python Operations with Flask Routing and Views</h1>"
    print(response)
    return response
@app.route("/print/<parameter>")
def print_string(parameter):
    response = f"{parameter}"
    print(response)
    return response

@app.route("/count/<parameter>")
def count(parameter):
    num_list = ""
    for number in range(int(parameter)):
        num_list += f"{number}\n"
        print(number)
    response = num_list
    print(response)
    return response

@app.route("/math/<num1>/<operation>/<num2>")
def math(num1, operation, num2):
    x = int(num1)
    y = int(num2)
    if operation == "+":
        print(f"{x + y}")
        return f"{x + y}"
    elif operation == "-":
        print(f"{x - y}")
        return f"{x - y}"
    elif operation == "*":
        print(f"{x * y}")
        return f"{x * y}"
    elif operation == "div":
        print(f"{x / y}")
        return f"{x / y}"
    elif operation == "%":
        print(f"{x % y}")
        return f"{x % y}"

if __name__ == '__main__':
    app.run(port=5555, debug=True)
