from flask import Flask, flash, redirect, render_template, request, url_for


UPLOAD_FOLDER = 'uploads/'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER




@app.route("/")
def main():
    return render_template("frontend.html")

# @app.route("/", methods=['POST'])
# def upload_image():
#     if request.method == 'POST':
#         image_upl = request.files['image_upload']
#         if image_upl.filename != "":
#             image_upl.save(app.config['UPLOAD_FOLDER'] + image_upl.filename)
#             flash('File uploaded succesfully')
        
#     return render_template('frontend.html')


@app.route("/list_images")
def list_images():
    return "<h1> Prueba</h1>"

@app.route("/analyse_image")
def analyse_image():
    return "<h1> Prueba</h1>"

app.run()