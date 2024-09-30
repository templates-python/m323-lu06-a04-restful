from flask import Flask, jsonify, request
from todoItem import TodoItem
from todoDao import TodoDao


# Flask App initialisieren und TodoDao-Objekt erstellen
app = ...
dao = ...
dao.create_table()


def add_todo():
    # TODO: Implementiere das Hinzufügen eines neuen ToDo-Elements
    return jsonify({"message": "Not implemented yet"}), 501


def get_all_todos():
    # TODO: Implementiere das Abrufen aller ToDo-Elemente
    return jsonify({"message": "Not implemented yet"}), 501


def get_todo(item_id):
    # TODO: Implementiere das Abrufen eines einzelnen ToDo-Elements
    return jsonify({"message": "Not implemented yet"}), 501


def update_todo(item_id):
    # TODO: Implementiere das Aktualisieren eines ToDo-Elements
    return jsonify({"message": "Not implemented yet"}), 501


def delete_todo(item_id):
    # TODO: Implementiere das Löschen eines ToDo-Elements
    return jsonify({"message": "Not implemented yet"}), 501


if __name__ == "__main__":
    app.run(debug=True)
