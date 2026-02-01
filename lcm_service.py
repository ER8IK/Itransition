from flask import Flask, request

app = Flask(__name__)

def gcd(a, b):
    """Вычисление НОД через алгоритм Евклида"""
    while b:
        a, b = b, a % b
    return a

def lcm(x, y):
    """Вычисление НОК"""
    return abs(x * y) // gcd(x, y)

@app.route('/dedppoolbhfg_gmail_com', methods=['GET'])  # ← ИСПРАВЛЕНО: @ заменено на _
def calculate_lcm():
    """
    Веб-метод для вычисления НОК двух натуральных чисел.
    """
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
    import os
    # ← ИСПРАВЛЕНО: Динамический порт для Render
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)