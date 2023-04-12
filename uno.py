from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def home():
   import pandas as pd
   dati = pd.read_csv('https://raw.githubusercontent.com/wtitze/3E/main/2010.csv', sep = ";")
   table = dati[dati["Language"] == "English"] 
   tabella = table.to_html()
   return render_template('table.html', tabella = tabella)


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)