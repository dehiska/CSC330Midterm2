from flask import Flask

app = Flask(__name__)

@app.route('/add/<num1>/<num2>')
def add_nums(num1, num2):
    return f'<h1>{(num1)+(num2)} = {str(int(num1)+int(num2))}</h1>'

@app.route('/subtract/<num1></num2>')
def subtract_nums(num1, num2):
    return f'<h1>{(num1)-(num2)} = {str(int(num1)-int(num2))}</h1>'

@app.route('/multiply/<num1></num2>')
def multiply_nums(num1, num2):
    return f'<h1>{(num1)*(num2)} = {str(int(num1)*int(num2))}</h1>'

@app.route('/divide/<num1></num2>')
def divide_nums(num1, num2):
    return f'<h1>{(num1)/(num2)} = {str(float(int(num1)+int(num2)))}</h1>'

