from flask import Flask, jsonify, request
from src.model.agenda import ( get_agenda)
from scr.model.users import ( get_users)
#from Agenda import

app = Flask(__name__)

@app.route('/agenda', methods=['GET'])
def get_all_agenda_items():
    return get_agenda()

@app.route('/users', methods=['GET'])
def get_all_users():
    return get_users()

if __name__ == '__main__':
    app.run(debug=True) # debug=True para desenvolvimento