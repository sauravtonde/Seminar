from flask import Flask, render_template, request
from backend import OCRProcessor

app = Flask(__name__)

ocr_processor = OCRProcessor()


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if the 'image' file is in the request
        if 'image' in request.files:
            image = request.files['image']

            # Save the uploaded image to a temporary location
            image_path = 'temp_image.jpg'
            image.save(image_path)

            # Perform OCR using the backend module
            text = ocr_processor.perform_ocr(image_path)

            # Pass the OCR output to the template
            return render_template('index2.html', text=text)

        # Render the initial form
    return render_template('index2.html')


if __name__ == '__main__':
    app.run(debug=True)
