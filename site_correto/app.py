from flask import Flask, render_template, request

app = Flask(__name__)

times_cadastrados = []
matriculas_cadastradas = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["POST"])
def register():
    nome_time  = request.form.get("nome_time")
    matricula1 = request.form.get("primeiro_int")
    matricula2 = request.form.get("segundo_int")
    matricula3 = request.form.get("terceiro_int")
    nivel_time = request.form.get("nivel")

    if nome_time in times_cadastrados:
        return render_template("index.html", resultado="Time " + nome_time + " já cadastrado. Escolha outro nome para seu time",cor="#990000")
    elif nome_time.isspace():
        return render_template("index.html", resultado="Nome do time não pode conter apenas caracteres do tipo espaço",cor="#990000")
    elif matricula1 in matriculas_cadastradas:
        return render_template("index.html", resultado=str(matricula1) + " já participa de um time",cor="#990000")
    elif matricula2 in matriculas_cadastradas:
        return render_template("index.html", resultado=str(matricula2) + " já participa de um time",cor="#990000")
    elif matricula3 in matriculas_cadastradas:
        return render_template("index.html", resultado=str(matricula3) + " já participa de um time",cor="#990000")
    elif matricula1 == matricula2 or matricula1 == matricula3 or matricula2 == matricula3:
        return render_template("index.html", resultado="Matrículas iguais: o time deve possuir três integrantes distintos",cor="#990000")
    else:
        times_cadastrados.append(nome_time)
        matriculas_cadastradas.append(matricula1)
        matriculas_cadastradas.append(matricula2)
        matriculas_cadastradas.append(matricula3)
        return render_template("index.html", resultado="Time " + nome_time + " inscrito com sucesso no nível " + nivel_time + "!",cor="rgb(0, 180, 0)")