from flask import Flask, request, redirect, render_template, send_file
from pydub import AudioSegment
import os
from werkzeug.utils import secure_filename




app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        audio_file = request.files['file']
        if audio_file:
            # Save the uploaded audio file
            
            f = request.files['file']

            basepath = os.path.dirname(__file__)
            audio_path = os.path.join(
                basepath, 'uploads', secure_filename(f.filename))
            
            f.save(audio_path)
            
            # Convert audio to desired format
            output_format = request.form.get('format')
            output_path = os.path.join(
                basepath, 'hasil', audio_file.filename.replace(audio_file.filename.split('.')[-1], output_format))
            AudioSegment.from_file(audio_path).export(output_path, format=output_format)
            
            # Provide the download link to the converted audio file
            return send_file(output_path, as_attachment=True)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
