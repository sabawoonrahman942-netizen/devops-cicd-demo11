import os
import sqlite3

from flask import Flask, g, jsonify, request, send_from_directory

app = Flask(__name__)
app.config["DATABASE"] = os.path.join(app.instance_path, "tasks.sqlite3")
os.makedirs(app.instance_path, exist_ok=True)


def get_db():
    """Bu istek için SQLite bağlantısını alır veya oluşturur."""
    if "db" not in g:
        g.db = sqlite3.connect(app.config["DATABASE"])
        g.db.row_factory = sqlite3.Row
    return g.db


@app.teardown_appcontext
def close_db(_error=None):
    """İstek bittiğinde açık veritabanı bağlantısını kapatır."""
    db = g.pop("db", None)
    if db is not None:
        db.close()


def init_db():
    """Görev tablosu henüz yoksa oluşturur."""
    db = get_db()
    db.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0,
            created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    db.commit()


with app.app_context():
    init_db()


def task_to_dict(row):
    return {
        "id": row["id"],
        "title": row["title"],
        "completed": bool(row["completed"]),
        "created_at": row["created_at"],
    }


@app.get("/")
def home():
    return send_from_directory(app.root_path, "index.html")


@app.get("/styles.css")
def styles():
    return send_from_directory(app.root_path, "styles.css")


@app.get("/app.js")
def frontend_script():
    return send_from_directory(app.root_path, "app.js")


@app.get("/api/tasks")
def list_tasks():
    rows = get_db().execute(
        "SELECT id, title, completed, created_at FROM tasks ORDER BY id DESC"
    ).fetchall()
    return jsonify(tasks=[task_to_dict(row) for row in rows])


@app.post("/api/tasks")
def create_task():
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict):
        return jsonify(error="JSON gövdesi gerekli."), 400

    title = payload.get("title")
    if not isinstance(title, str):
        return jsonify(error="Görev başlığı metin olmalı."), 400

    title = title.strip()
    if not title:
        return jsonify(error="Görev başlığı boş olamaz."), 400
    if len(title) > 120:
        return jsonify(error="Görev başlığı en fazla 120 karakter olabilir."), 400

    db = get_db()
    cursor = db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    db.commit()
    row = db.execute(
        "SELECT id, title, completed, created_at FROM tasks WHERE id = ?",
        (cursor.lastrowid,),
    ).fetchone()
    return jsonify(task=task_to_dict(row)), 201


@app.patch("/api/tasks/<int:task_id>")
def update_task(task_id):
    payload = request.get_json(silent=True)
    if not isinstance(payload, dict) or type(payload.get("completed")) is not bool:
        return jsonify(error="'completed' alanı true veya false olmalı."), 400

    db = get_db()
    cursor = db.execute(
        "UPDATE tasks SET completed = ? WHERE id = ?",
        (int(payload["completed"]), task_id),
    )
    if cursor.rowcount == 0:
        return jsonify(error="Görev bulunamadı."), 404

    db.commit()
    row = db.execute(
        "SELECT id, title, completed, created_at FROM tasks WHERE id = ?",
        (task_id,),
    ).fetchone()
    return jsonify(task=task_to_dict(row))


@app.delete("/api/tasks/<int:task_id>")
def delete_task(task_id):
    db = get_db()
    cursor = db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        return jsonify(error="Görev bulunamadı."), 404

    db.commit()
    return jsonify(message="Görev silindi.")


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000)
