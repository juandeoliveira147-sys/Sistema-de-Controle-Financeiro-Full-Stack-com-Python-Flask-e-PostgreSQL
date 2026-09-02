from flask import Flask , redirect , request , url_for , render_template 
from banco_de_dados import conectar , encerrar_conexao
import re
import datetime
app = Flask(__name__)



@app.route("/")
def home():
    return render_template('index.html')


@app.route("/receita")
def receita():
    return render_template('receita.html')

@app.route("/sucesso")
def sucesso():
    return render_template('sucesso.html')



@app.route("/salvar_receita", methods=['POST'])
def salvar_receita():
    valor = request.form.get('receita')
    descricao = request.form.get('descricao')
    if not descricao:
        descricao = 'Sem descrição!'
    if valor:
        converter = re.sub(r'\D', '', valor)
        numeros = float(converter) / 100
        conexao = conectar()
        cursor = conexao.cursor()
        agora = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        query = "INSERT INTO controlefinanceiro(tipo,valor,horario,descricao) values ('receita',%s,%s,%s)"
        cursor.execute(query, (numeros, agora, descricao))
        conexao.commit()
        encerrar_conexao(conexao)
        
        print(f"Valor enviado para o banco de dados: {numeros}")

        return redirect("/sucesso")

@app.route("/despesa")
def despesa():
    return render_template('despesa.html')


@app.route("/salvar_despesa", methods=['POST'])
def salvar_despesa():
    valor = request.form.get('despesa')
    descricao = request.form.get('descricao')
    if not descricao:
        descricao = 'Sem descrição!'
    if valor:
        converter = re.sub(r'\D', '', valor)
        numeros = float(converter) / 100
        conexao = conectar()
        cursor = conexao.cursor()
        agora = datetime.datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        query = "INSERT INTO controlefinanceiro(tipo,valor,horario,descricao) values ('despesa',%s,%s,%s)"
        cursor.execute(query, (numeros, agora, descricao))
        conexao.commit()
        encerrar_conexao(conexao)
        
        print(f"Valor enviado para o banco de dados: {numeros}")

        return redirect("/sucesso")



@app.route("/extrato")
def extrato():
    conexao = conectar()
    cursor = conexao.cursor()
    cursor.execute(f"select * from controlefinanceiro ORDER BY id ;")
    dados_extrato = cursor.fetchall()
    conexao.commit()
    encerrar_conexao(conexao)

    saldo_total = 0.0
    for transacao in dados_extrato:
        tipo = transacao[1]
        valor = transacao[2]
        if tipo == "receita":
            saldo_total += valor
        elif tipo == "despesa":
            saldo_total -= valor
    
    return render_template('extrato.html',transacoes=dados_extrato , saldo=saldo_total)

@app.route("/alteracoes")
def alteracoes():
    return render_template('alteracoes.html')

@app.route("/salvar_alteracoes", methods=['POST'])
def salvar_alteracoes():
    id_recebido = request.form.get('id')
    while True:
        if id_recebido:
            id_recebido = int(id_recebido)
            conexao = conectar()
            cursor = conexao.cursor()
            cursor.execute(f"select * from controlefinanceiro WHERE id={id_recebido}")
            temid = cursor.fetchall()
            conexao.commit()
            encerrar_conexao(conexao)
            if temid:
                break
            else:
                return render_template('id_nao_encontrado.html')


    alteracao_descricao = request.form.get('nova_descricao')
    alteracao_valor = request.form.get('novo_valor')
    alteracao_tipo = request.form.get('novo_tipo')
    if alteracao_descricao:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "UPDATE controlefinanceiro SET descricao=%s WHERE id=%s"
        cursor.execute(query, (alteracao_descricao, id_recebido))
        conexao.commit()
        encerrar_conexao(conexao)
    if alteracao_valor:
        converter = re.sub(r'\D', '', alteracao_valor)
        numeros = float(converter) / 100
        conexao = conectar()
        cursor = conexao.cursor()
        query = "UPDATE controlefinanceiro SET valor=%s WHERE id=%s"
        cursor.execute(query, (numeros, id_recebido))
        conexao.commit()
        encerrar_conexao(conexao)
    if alteracao_tipo:
        conexao = conectar()
        cursor = conexao.cursor()
        query = "UPDATE controlefinanceiro SET tipo=%s WHERE id=%s"
        cursor.execute(query, (alteracao_tipo, id_recebido))
        conexao.commit()
        encerrar_conexao(conexao)

    return redirect("/extrato")

@app.route("/excluir")
def excluir():
    return render_template('excluir_movimentacao.html')

@app.route("/excluir_movimentacao", methods=['POST'])
def excluir_movimentacao():
    id_recebido = request.form.get('excluir_id')
    conexao = conectar()
    cursor = conexao.cursor()
    query = "SELECT * FROM controlefinanceiro WHERE id=%s"
    cursor.execute(query, (id_recebido,))
    temid = cursor.fetchall()
    conexao.commit()
    encerrar_conexao(conexao)

    if id_recebido and temid:
        id_recebido = int(id_recebido)
        conexao = conectar()
        cursor = conexao.cursor()
        cursor.execute(f"DELETE FROM controlefinanceiro WHERE id={id_recebido}")
        conexao.commit()
        encerrar_conexao(conexao)
        return redirect("/excluido")
    else:
        return render_template('id_nao_encontrado.html')
    

@app.route("/excluido")
def excluido():
    return render_template('excluido.html')





@app.route("/admin")
def admin():
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)


