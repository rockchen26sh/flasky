from flask import Flask,render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

def dataSet():
    months = ['Jan','Feb','Mar','Apl','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    weather = {
        'Jan':{'min':38,'max':47,'rain':6.14},
        'Feb':{'min':38,'max':51,'rain':4.79},
        'Mar':{'min':41,'max':56,'rain':4.5},
        'Apl':{'min':44,'max':61,'rain':3.4},
        'May':{'min':49,'max':67,'rain':2.55},
        'Jun':{'min':53,'max':73,'rain':1.69},
        'Jul':{'min':57,'max':80,'rain':0.59},
        'Aug':{'min':58,'max':80,'rain':0.71},
        'Sep':{'min':54,'max':75,'rain':1.54},
        'Oct':{'min':48,'max':63,'rain':3.42},
        'Nov':{'min':41,'max':52,'rain':6.74},
        'Dec':{'min':36,'max':45,'rain':6.94},
    }
    highlight = {'min':40,'max':80,'rain':5}
    return (months,weather,highlight)

@app.route('/')
def index():
    months, weather, highlight = dataSet()
    return render_template('index.html',city = 'Portland,OR',months=months,
                           weather = weather, highlight = highlight)

if __name__ == '__main__':
    app.run(debug=True)
