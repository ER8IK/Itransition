from flask import Flask, request

app = Flask(__name__)

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    return abs(x * y) // gcd(x, y)

@app.route('/dedppoolbhfg@gmail.com', methods=['GET'])
def calculate_lcm():
    try:
        x_param = request.args.get('x')
        y_param = request.args.get('y')
        
        if x_param is None or y_param is None:
            return 'NaN'
        
        x = int(x_param)
        y = int(y_param)
        
        if x <= 0 or y <= 0:
            return 'NaN'
        
        result = lcm(x, y)
        
        return str(result)
        
    except (ValueError, TypeError):
        return 'NaN'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
