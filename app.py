from flask import Flask, request, jsonify

app = Flask(__name__)

# Rota para obter todos os itens
@app.route('/test', methods=['GET'])
def get_items():
    return jsonify({"message": "ola mundo"})

if __name__ == '__main__':
    app.run(debug=True)