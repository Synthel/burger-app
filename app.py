
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "fronteiraBurger"

estoque = []
vendas = []
prod_id = 1

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", estoque=estoque)

@app.route("/vendas")
def vendas_view():
    return render_template("vendas.html", vendas=vendas)

@app.route("/nova-venda", methods=["GET", "POST"])
def nova_venda():
    global vendas
    if not estoque:
        flash("Cadastre ao menos um produto antes de registrar venda!", "warning")
        return redirect(url_for("produtos"))
    if request.method == "POST":
        produto = request.form["produto"]
        quantidade = int(request.form["quantidade"])
        for item in estoque:
            if item["nome"] == produto:
                if item["quantidade"] < quantidade:
                    flash("Estoque insuficiente!", "danger")
                    return redirect(url_for("nova_venda"))
                item["quantidade"] -= quantidade
                vendas.append({"produto": produto, "quantidade": quantidade})
                flash("Venda registrada!", "success")
                return redirect(url_for("vendas_view"))
    return render_template("nova_venda.html", estoque=estoque)

@app.route("/novo-produto", methods=["GET", "POST"])
def novo_produto():
    global estoque, prod_id
    if request.method == "POST":
        nome = request.form["nome"]
        quantidade = int(request.form["quantidade"])
        for item in estoque:
            if item["nome"].lower() == nome.lower():
                flash("Produto já cadastrado.", "danger")
                return redirect(url_for("novo_produto"))
        estoque.append({"id": prod_id, "nome": nome, "quantidade": quantidade})
        prod_id += 1
        flash("Produto cadastrado!", "success")
        return redirect(url_for("produtos"))
    return render_template("novo_produto.html")

if __name__ == "__main__":
    app.run(debug=True, port=3000)
