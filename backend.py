from flask import Flask, flash, jsonify, redirect, render_template, request, url_for                            # Import all the neccesary modules/functions from flask
from PIL import Image


UPLOAD_FOLDER = 'static/uploads/'                                                                               # Set the upload folder for images
app = Flask(__name__)                                                                                           # Initiate Flask application
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER





@app.route("/")                                                                                                 # The default/main route, will render or show the main page, page.html
def main():
    return render_template("main.html")


@app.route("/", methods=['POST'])                                                                              # Upload_Image method/function, will be the method in charge of the logic of uploading an image
def upload_image():                                                                                            # Unfortunately not working, First time designing an API, I think I learned the fundamentals of api design with Flask, over the 48 h period.
    if request.method == 'POST':
        image_upl = request.files['image_upload']                                                              # The image uploaded, will be under the image_upload name, of the input in the html
        if image_upl.filename != "":
            image_upl.save(app.config['UPLOAD_FOLDER'] + image_upl.filename)                                   # As long as the file is not empty, the image will get saved in the location specified above, /static/uploads 
            flash('File uploaded succesfully')
        
    return render_template('main.html')                                                                        # Upon succesfull upload of the image, redirect to main page


@app.route("/list_images")                                                                                     # List images endpoint, will be responsible for displaying all of the uploaded images so far
def list_images():
    uploads = [{"img1": "/static/images/python.png"}]    #{"img2": "/static/images/minion.jpg"}                # Due to the first endpoint not working how it should, I set up a small test case to represent the image uploads 
    for img_uploads in uploads:                                                                                # The list of uploads is composed of, diccionaries where each dict contains, the image_id and the image url
        for image_id in img_uploads:                                                                            
            img_url = img_uploads[image_id]                                                                    # Image_url = the url of the image of the image_id within the list
            dot_index = img_url.index('.')
            img_extension = img_url[dot_index + 1:]                                                            # Retrieve the extension of the image url, for pretty visualization in the html
            if img_extension == "png":
                img_type = "/static/images/png.png"                                                            # if the image extension is png, associate the corresponding image in the images folder, /static/images 
            else:
                img_type = "/static/images/jpg.png"                                                            # Same for images with jpg extension, associate corresponding image

    return render_template('list_images.html', img_type = img_type, file_name = image_id + ': ' + img_url)     # Show the list_images.html file, with img_type = image url for corresponding extension, and file_name = string following the format, image_id + : + img_url as the 2 arguments/parameters

@app.route("/analyse_image/<image_id>")                                                                        # Analyse Images, recieves an image id, if the image id corresponds with an uploaded image, show uploaded image with that image id, ad sho the width and height of the image
def analyse_image(image_id):
    if image_id != 'img1':                                                                                     # If and image id does not exist, show message and 400 http status code, current implementation only focuses on a single uploaded image file
        return "Image Not Found", 400
    else:                                                                                                      # If the image_id is found within the list of uploaded files, display it 
        image_url = "static/images/python.png"                                                                 # The image url, would be the corresponding value of that image id
        image = Image.open(image_url)
        img_width, img_height = image.size                                                                      # Create a PIL Image object, to extract the width and the height of the image found
    return render_template("analyse_image.html", url="/" + image_url, image_width=img_width, image_height=img_height)
                                                                                                                # return 3 aruguments/parameters to the analyse_image page, adding a slash to the image url, to be able to open in html, with the image width and height included

# @app.route("/analyse_image/<image_id>")
# def analyse_image(image_id):
#     uploads = [
#     {
#         "img1": "static/images/cloud_computing.png"       
#     },
#     {
#         "img2": "static/images/python.png"
#     }
# ]
#     image_uploads = jsonify(results=uploads)
#     print(image_uploads)
#     if image_id not in image_uploads:
#         return 'Image Not Found', 400
#     else:
#         image_url = image_uploads[image_id]
#     return render_template('analyse_image.html', data=image_url)

app.run()