from flask import Flask, jsonify, request

app = Flask(__name__)

# Dados de exemplo (pode ser substituído por um banco de dados)
items = [
        {"id": 1, "name": "Item A", "description": "Descrição do Item A"},
        {"id": 2, "name": "Item B", "description": "Descrição do Item B"},
]



# Rota para obter todos os itens
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)

# Rota para obter um item específico por ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.json
    if not new_item or 'name' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(items) + 1 
    items.append(new_item)
    return jsonify(new_item), 201


# Rota para atualizar um item existente
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item_data = request.json
    item = next((item for item in items if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para deletar um item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items # Permite modificar a lista global
    original_len = len(items)
    items = [item for item in items if item['id'] != item_id]
    if len(items) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404

# usuarios
# Dados de exemplo (pode ser substituído por um banco de dados)
listUsers = [
        {"id": 1, "login": "jose", "password": "123"},
        {"id": 2, "login": "maria", "password": "123"},
]

# Rota para obter todos os itens
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(listUsers)


# Rota para obter um item específico por ID
@app.route('/users/<int:item_id>', methods=['GET'])
def get_userid(item_id):
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
@app.route('/users', methods=['POST'])
def add_user():
    new_item = request.json
    if not new_item or 'login' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(listUsers) + 1 
    listUsers.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/users/<int:item_id>', methods=['PUT'])
def update_user(item_id):
    item_data = request.json
    item = next((item for item in listUsers if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para deletar um item
@app.route('/users/<int:item_id>', methods=['DELETE'])
def delete_user(item_id):
    global listUsers # Permite modificar a lista global
    original_len = len(listUsers)
    listUsers = [item for item in listUsers if item['id'] != item_id]
    if len(listUsers) < original_len:
        return jsonify({"message": "Item deletado com sucesso"}), 200
    return jsonify({"message": "Item não encontrado"}), 404

# agenda
# Dados de exemplo (pode ser substituído por um banco de dados)
listAgenda = [
        {"id": 1, "nome": "jose", "celular": "16 9991-1113"},
        {"id": 2, "nome": "maria", "celular": "16-88891-9952"},
]


# Rota para obter todos os itens
@app.route('/agenda', methods=['GET'])
def get_agenda():
    return jsonify(listAgenda)

# Rota para obter um item específico por ID
@app.route('/agenda/<int:item_id>', methods=['GET'])
def get_agendaid(item_id):
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item não encontrado"}), 404

# Rota para adicionar um novo item
@app.route('/agenda', methods=['POST'])
def add_agenda():
    new_item = request.json
    if not new_item or 'nome' not in new_item:
        return jsonify({"message": "Dados inválidos"}), 400
        
    # Atribui um novo ID (simples, para exemplo)
    new_item['id'] = len(listAgenda) + 1 
    listAgenda.append(new_item)
    return jsonify(new_item), 201

# Rota para atualizar um item existente
@app.route('/agenda/<int:item_id>', methods=['PUT'])
def update_agenda(item_id):
    item_data = request.json
    item = next((item for item in listAgenda if item['id'] == item_id), None)
    if item:
        item.update(item_data)
        return jsonify(item)
    return jsonify({"message": "Registro não encontrado"}), 404

# Rota para deletar um item
@app.route('/agenda/<int:item_id>', methods=['DELETE'])
def delete_agenda(item_id):
    global listAgenda # Permite modificar a lista global
    original_len = len(listAgenda)
    listAgenda = [item for item in listAgenda if item['id'] != item_id]
    if len(listAgenda) < original_len:
        return jsonify({"message": " registro deletado com sucesso"}), 200
    return jsonify({"message": "registro não encontrado"}), 404

if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento