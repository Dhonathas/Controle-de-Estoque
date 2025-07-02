from flask import Blueprint, request, jsonify
from models.item import Item
from database import db

item_bp = Blueprint('item_bp', __name__, url_prefix='/itens')

@item_bp.route('', methods=['GET'])
def get_itens():
    itens = Item.query.all()
    return jsonify([item.to_dict() for item in itens])

@item_bp.route('', methods=['POST'])
def create_item():
    data = request.get_json()
    if not data or "nome" not in data or "quantidade" not in data:
        return jsonify({"error": "Campos 'nome' e 'quantidade' são obrigatórios."}), 400

    item = Item(
        nome=data["nome"],
        quantidade=data.get("quantidade", 0),
        descricao=data.get("descricao")
    )
    db.session.add(item)
    db.session.commit()
    return jsonify(item.to_dict()), 201

@item_bp.route('/<int:id>', methods=['PUT'])
def update_item(id):
    item = Item.query.get(id)
    if not item:
        return jsonify({'error': 'Item não encontrado'}), 404

    data = request.get_json()
    item.nome = data.get('nome', item.nome)
    item.quantidade = data.get('quantidade', item.quantidade)
    item.descricao = data.get('descricao', item.descricao)
    db.session.commit()
    return jsonify(item.to_dict())

@item_bp.route('/<int:id>', methods=['DELETE'])
def delete_item(id):
    item = Item.query.get(id)
    if item:
        db.session.delete(item)
        db.session.commit()
        return jsonify({'message': 'Item removido'}), 200
    return jsonify({'message': 'Item não encontrado'}), 404
