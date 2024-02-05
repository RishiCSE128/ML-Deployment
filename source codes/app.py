from flask import Flask, request, render_template_string

app = Flask(__name__)

# HTML template for the file upload page
UPLOAD_PAGE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Upload File</title>
</head>
<body>
    <h2>Upload File</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" />
        <input type="submit" value="Upload" />
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(UPLOAD_PAGE)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        # Save the file to the server
        # You can process the file here as per your requirements
        file.save(file.filename)
        return 'File uploaded successfully'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
