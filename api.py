from flask import Flask
import scipy.stats as stats
app = Flask(__name__)

@app.route('/')
def hello_world():
   valor_min = 0
   valor_max = 100
   media = 0
   desvio_padrao = 1
   dist = stats.truncnorm((valor_min - media) / desvio_padrao, (valor_max - media) / desvio_padrao, loc=media, scale=desvio_padrao)
   values = dist.rvs(1)
   return str(values[0])
