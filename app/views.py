from app import app
from app import generator
from flask import render_template
from flask import request
from flask import send_from_directory

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == "POST":
        url = request.form["url"]
        img_name = "result"

        generator.generate_qr(url)

        return render_template(
            "index.html", url=url, img_name=img_name, path=app.config["IMAGES"]
        )

    return render_template(
        "index.html", url="", img_name="example", path=app.config["IMAGES"]
    )

@app.route('/download/<path:img_name>', methods=["GET"])
def download(img_name):

    filename = f"{img_name}.png"

    try:
        return send_from_directory(
            app.config["IMAGES"], filename, as_attachment=True
        )
    except FileNotFoundError:
        abort(404)