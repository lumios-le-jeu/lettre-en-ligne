from flask import Flask, render_template, request, send_file
import os
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from io import BytesIO

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""
    filename = None

    if request.method == 'POST':
        text = request.form['text']
        filename = generate_image(text)

    return render_template('index.html', text=text, image_url=filename)

def generate_image(word):
    """Générer une image du texte."""
    font_path = os.path.join(BASE_DIR, "fonts", "GRAPHECRIT.OTF")  # Mettez ici votre police préférée
    graphecrit_font = FontProperties(fname=font_path, size=112)

    fig, ax = plt.subplots(figsize=(6, 2))
    ax.text(0.5, 0.5, word, fontproperties=graphecrit_font, va='baseline', ha='center', color='black')

    ax.axis('off')
    plt.tight_layout()

    # Sauvegarder l'image temporairement
    img_path = os.path.join(BASE_DIR, "static", "output_image.png")
    plt.savefig(img_path, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return "static/output_image.png"

@app.route('/download')
def download():
    """Téléchargez l'image générée."""
    path = os.path.join(BASE_DIR, "static", "output_image.png")
    return send_file(path, as_attachment=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
