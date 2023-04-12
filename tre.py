
from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd
dati = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep = ";")
    
@app.route('/')
def home():
    nomi_lingue = dati.drop_duplicates(subset=['Language'])
    return render_template('es3.html', list= list(nomi_lingue['Language']))

@app.route('/search', methods = ['GET'])
def search():
    lingua = request.args['lingua']
    risultato = dati[dati['Language']==lingua.capitalize()]
    if len(risultato) == 0:
        table = 'Regione non trovata'
    else:
        table = risultato.to_html()
    return render_template('table.html', tabella = table)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)