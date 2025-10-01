from flask import jsonify, request
from sqlalchemy import text 
from src.db import database

db_connect - database.get_db_connection()
tableName = "users"

def get():
    try:
        # recebe uma conexão com o banco
        conexao = db_connect.connect()
        query_text = text( f"SELECT * FROM {tableName} ORDER BY id DESC")
        # data recebe o resultado da consulta
        data = db.execute(query_text)
        # mapeia os resultados para uma lista de dicionários
        result = [dict(zip(data.keys(), row)) for row in data]
        return jsonify(result), 200
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def getBy(value):
    try:
       # recebe uma conexão com o banco
        conexao = db_connect.connect()
        query_text = text( f"SELECT * FROM {tableName} WHERE id = :id ORDER BY id DESC")
        # data recebe o resultado da consulta
        data = db.execute(query_text, ["id": value])
        # mapeia os resultados para uma lista de dicionários
        result = [dict(zip(data.keys(), row)) for row in data]
        if not result:
            return jsonify("error": f"Registro com ID {value} não encontrado"), 404
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def delete(value):
    try:
       # recebe uma conexão com o banco
        conexao = db_connect.connect()
        query_text = text( f"DELETE FROM {tableName} WHERE id = :id")
        # data recebe o resultado da consulta
        data = db.execute(query_text, ["id": value])
        db.commit
        if date.rowcont == 0 :
            return jsonify("error": f"Registro com ID {value} não encontrado"), 404
        
            return jsonify("sucesso": f"Registro apagado com sucesso"), 204
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
def post():
    try:
       # recebe uma conexão com o banco
        conexao = db_connect.connect()
        payload = request.get_json(force = true)
        
        login = payload.get('login')
        password = payload.get('password')
        name = payload.get('name') 
        
        query_text = text( f"""INSERT INTO {tableName} ( login, password, name ) 
                          VALUES ( :login, :password, :name)
                        """)
        # data recebe o resultado da consulta
        data = db.execute(query_text, {"login": login , "password": password,  "name": name} )
        db.commit
    
        if date.rowcont == 0 :
            return jsonify("error": f"Registro com ID {value} não encontrado"), 404
        
            return jsonify("sucesso": f"Registro criado com sucesso"), 201
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def put(value):
    try:
       # recebe uma conexão com o banco
        conexao = db_connect.connect()
        payload = request.get_json(force = true)
        
        login = payload.get('login')
        password = payload.get('password')
        name = payload.get('name') 
        active = payload.get('active')
        
        query_text = text( f"""UPDATE {tableName} 
                          SET login = :login, password = :password, name = :name, active = :active 
                          WHERE ID = :id
                        """)
        # data recebe o resultado da consulta
        data = db.execute(query_text, {"login": login , "password": password,  "name": name, "id": id, "active": active} )
        db.commit
        if date.rowcont == 0 :
            return jsonify("error": f"Registro com ID {value} não encontrado para atualização"), 404
        
            return jsonify("message": f"Registro com ID {value} atualizado com sucesso"), 201
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



# def get():
#     try:
#           Código metodo
#         return
#     except Exception as e
#         return jsonify({"error": str(e)}), 500














# Rota para obter um item específico por ID
#@app.route('/users/<int:item_id>', methods=['GET'])
def getBy(item_id):
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
#@app.route('/users', methods=['POST'])
def post():
    new_item = request.json
    if not new_item or 'login' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(listUsers) + 1 
    listUsers.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
#@app.route('/users/<int:item_id>', methods=['PUT'])
def put(item_id):
    item_data = request.json
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para deletar um item
#@app.route('/users/<int:item_id>', methods=['DELETE'])
def delete(item_id):
    global listUsers # Permite modificar a lista global
    original_len = len(listUsers)
    listUsers = [item for item in listUsers if item['id'] != item_id]
    if len(listUsers) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404