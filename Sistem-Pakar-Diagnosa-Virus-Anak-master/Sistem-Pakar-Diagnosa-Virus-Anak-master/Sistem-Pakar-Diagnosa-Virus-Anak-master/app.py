from flask import Flask, render_template, request
from inference import Inference

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    
    if request.method=='POST':
        gejala = request.form.getlist('list_checkbox')
        Inference.Result = gejala

        knowledgeBaseFile = "./data/virus_anak/knowledge.json"
        clauseBaseFile = "./data/virus_anak/clause.json"

        inferenceEngine = Inference()
        inferenceEngine.startEngine(knowledgeBaseFile,
                            clauseBaseFile,
                            verbose=True,
                            method=inferenceEngine.FORWARD)
        
        iv = Inference.Virus[1]
        return render_template('new_hasil.html', inferensi="Aku rasa kamu mengalami berberapa gejala "+iv)
    return render_template('index.html')
    
if __name__ == '__main__':
    app.run(debug=True)