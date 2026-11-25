from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        total = None
        descuento = None
        total_con_desc = None
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        cant_tarros = int(request.form['cant_tarros'])
        VALOR_TARRO = 9000
        if 18 <= edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0
        total = VALOR_TARRO*cant_tarros
        total_con_desc = total*(1 - descuento)
        descontado = total*descuento

        return render_template('ejercicio1.html', nombre=nombre, total=total,
                        descontado=descontado, total_con_desc=total_con_desc)
    return render_template('ejercicio1.html')

if __name__ == '__main__':
    app.run(debug=True)
