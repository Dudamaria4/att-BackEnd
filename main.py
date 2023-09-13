import uuid
from flask import Flask, request, jsonify

app = Flask(__name__)

pessoas_db = {}

@app.post('/pessoas')
def criar_pessoa():
    data = request.json
    pessoa_id = str(uuid.uuid4())
    data['id'] = pessoa_id
    pessoas_db[pessoa_id] = data
    return jsonify({"mensagem":"Pessoa criada com sucesso", "id":pessoa_id}),201

@app.get('/pessoas/<string:pessoa_id>')
def consultar_pessoa(pessoa_id):
    if pessoa_id in pessoas_db:
        return jsonify(pessoas_db[pessoa_id])
    else:
        return jsonify({"error":"Pessoa não encontrada"}), 404
    

@app.get('/pessoa')
def buscar_pessoas():
    termo_buscar:
    resultado = []
    for pessoa_id, pessoa_data in pessoas_db.items():
        if termo_buscar.lower() in pessoa_data['nome'].lower():
            resultados.append(pessoa_data)
            return jsonify(resultados)
        else:
            return jsonify(list(pessoas_db.values()))
        
@app.get('/contagem-pessoas')
def contar_pessoas():
    return jsonify ({"contagem": len(pessoas_db)})

if_name_ == '__main__':
app.run(debug=True)