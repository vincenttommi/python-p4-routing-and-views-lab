#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)



@app.route('/')
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'



@app.route('/<string:flask>')
def fas(flask):
    return f'<h1>title for {flask}</h1>'

if __name__ == '__main__':
    app.run(port=5567)
    
    
@app.route('/count/<int:parameter>/')
def count(parameter):
    numbers = range(parameter + 1)
    output =    '\n'.join(str(num) for num  in numbers)
    return output


@app.route('/math/<float:num1><string:operation><float:num2>/')
def  math(num1,operation,num2):
    if operation == '+':
        result = num1 + num2
    elif operation  == '-':
        result = num1 - num2
    elif operation ==  '*':
        result = num1 * num2
    elif operation  == 'div':
        if num2  == 0:
            return "Division by Zero is not allowed."
        result = num1 / num2
    elif operation  == '%':
        result = num1 % num2
    else:
        return "Invalid operation. Supported operations are +, -, *, div, and %."
    
    return  str(result)


if __name__ == '__main__':
    app.run()

            
    
         
        
        

    