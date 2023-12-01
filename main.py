from flask import Flask, send_file
from presentation import  get_presentation
app = Flask(__name__)



@app.route('/generate_presentation/<topic>' ,methods=['GET'])
def generate_presentation(topic):
    ppt_bytes = get_presentation(topic)
    return send_file(ppt_bytes, download_name=f'{topic}_presentation.pptx', as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
