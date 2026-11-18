
from flask import Flask, render_template, request, redirect, url_for
from pathlib import Path
import sqlite3

app = Flask(__name__)
app.config["DATABASE"] = str(Path(__file__).resolve().with_name("database.db"))

def get_db():
    conn = sqlite3.connect(app.config["DATABASE"])
    conn.row_factory = sqlite3.Row
    return conn


def create_table():
    conn = get_db()
    try:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                subject TEXT NOT NULL,
                due_date TEXT NOT NULL,
                priority TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Pending'
            )
        """)
        conn.commit()
    finally:
        conn.close()


@app.route("/")
def home():
    conn = get_db()
    try:
        tasks = conn.execute(
            "SELECT * FROM tasks ORDER BY id DESC"
        ).fetchall()
    finally:
        conn.close()

    total = len(tasks)
    completed = sum(1 for task in tasks if task["status"] == "Completed")
    pending = total - completed

    return render_template(
        "index.html",
        tasks=tasks,
        total=total,
        completed=completed,
        pending=pending
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    due_date = request.form.get("due_date", "").strip()
    priority = request.form.get("priority", "Medium")

    if not title or not subject or not due_date:
        return redirect(url_for("home"))

    conn = get_db()
    try:
        conn.execute("""
            INSERT INTO tasks (title, subject, due_date, priority)
            VALUES (?, ?, ?, ?)
        """, (title, subject, due_date, priority))
        conn.commit()
    finally:
        conn.close()

    return redirect(url_for("home"))


@app.route("/complete/<int:task_id>")
def complete_task(task_id):
    conn = get_db()
    try:
        conn.execute("""
            UPDATE tasks
            SET status = 'Completed'
            WHERE id = ?
        """, (task_id,))
        conn.commit()
    finally:
        conn.close()

    return redirect(url_for("home"))


@app.route("/delete/<int:task_id>")
def delete_task(task_id):
    conn = get_db()
    try:
        conn.execute(
            "DELETE FROM tasks WHERE id = ?",
            (task_id,)
        )
        conn.commit()
    finally:
        conn.close()

    return redirect(url_for("home"))


create_table()


if __name__ == "__main__":
    app.run()

