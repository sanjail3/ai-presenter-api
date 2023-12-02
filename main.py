from flask import Flask, send_file,jsonify
from presentation import  get_presentation
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
import base64




@app.route('/generate_presentation/<topic>' ,methods=['GET'])
def generate_presentation(topic):
    # ppt_bytes = get_presentation(topic)
    # return send_file(ppt_bytes, download_name=f'{topic}_presentation.pptx', as_attachment=True)
    ppt_content = get_presentation(topic)

    # Assuming ppt_content is a BytesIO object
    ppt_content.seek(0)  # Reset the position to the beginning
    ppt_content_bytes = ppt_content.read()

    # Encode the presentation content to Base64
    ppt_base64 = base64.b64encode(ppt_content_bytes).decode('utf-8')

    return jsonify({'presentation': ppt_base64})


if __name__ == '__main__':
    app.run(host = '0.0.0.0')
