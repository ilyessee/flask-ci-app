from flask import Flask, jsonify, redirect, render_template, request, url_for

# In-memory database
items = []


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html", items=items)

    @app.route("/health")
    def health():
        return jsonify({"status": "ok"})

    @app.route("/add", methods=["POST"])
    def add_item():
        item = request.form.get("item")
        if item:
            items.append(item)
        return redirect(url_for("index"))

    @app.route("/delete/<int:index>")
    def delete_item(index):
        if index < len(items):
            items.pop(index)
        return redirect(url_for("index"))

    @app.route("/update/<int:index>", methods=["POST"])
    def update_item(index):
        if index < len(items):
            items[index] = request.form.get("new_item")
        return redirect(url_for("index"))

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)
