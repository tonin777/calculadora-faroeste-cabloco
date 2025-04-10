from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    resultado = None
    if request.method == 'POST':
        try:
            anos = int(request.form.get('anos', 0))
            meses = int(request.form.get('meses', 0))
            dias = int(request.form.get('dias', 0))
            horas = int(request.form.get('horas', 0))
            minutos = int(request.form.get('minutos', 0))
            segundos = int(request.form.get('segundos', 0))

            total_segundos = (
                segundos +
                minutos * 60 +
                horas * 3600 +
                dias * 86400 +
                meses * 2629800 +  # Média de segundos em um mês
                anos * 31557600    # Média de segundos em um ano
            )

            duracao_faroeste = 543  # Duração em segundos
            qtd_faroestes = total_segundos // duracao_faroeste
            sobra_segundos = total_segundos % duracao_faroeste

            resultado = {
                'qtd_faroestes': int(qtd_faroestes),
                'sobra_segundos': sobra_segundos
            }
        except ValueError:
            resultado = {'erro': 'Por favor, insira valores numéricos válidos.'}

    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
