import cv2
import pytesseract


class OCRProcessor:
    def __init__(self):
        # Your OCR initialization code here
        pass

    def perform_ocr(self,img_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        img = cv2.imread(img_path)
        # Read image from which text needs to be extracted
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # Convert the image to gray scale

        # Denoise the image using Gaussian blur
        gray = cv2.GaussianBlur(gray, (5, 5), 0)

        # Performing adaptive thresholding for better binarization
        thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

        # Specify structure shape and kernel size for morphological operations
        rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

        # Applying dilation on the threshold image
        dilation = cv2.dilate(thresh, rect_kernel, iterations=1)

        # Finding contours
        contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

        # Creating a copy of the image
        im2 = img.copy()

        # A text file is created and flushed
        file = open("recognized.txt", "w+")
        file.write("")
        file.close()

        # Looping through the identified contours
        # Then rectangular part is cropped and passed on
        # to pytesseract for extracting text from it
        # Extracted text is then written into the text file
        for cnt in contours:
            x, y, w, h = cv2.boundingRect(cnt)

            # Drawing a rectangle on the copied image
            rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Cropping the text block for giving input to OCR
            cropped = im2[y:y + h, x:x + w]

            # Open the file in append mode
            file = open("recognized.txt", "a")

            # Apply OCR on the cropped image
            text = pytesseract.image_to_string(cropped)

            # Appending the text into the file
            file.write(text)
            file.write("\n")

            # Close the file
            file.close()

        # Output a message when processing is complete
        print("Text extraction complete. The extracted text is saved in 'recognized.txt'")
        return text

