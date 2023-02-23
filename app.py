from flask import Flask, request, render_template, redirect, flash
from forex_python.converter import CurrencyRates, CurrencyCodes
import requests
from rate import cal_amount

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

api_url = "https://api.exchangerate.host/convert"


@app.route('/')
def home():   
    return render_template('index.html')


@app.route('/exchange_rate', methods=["POST"])
def exchange():
    from_currency = request.form['from-currency']
    to_currency = request.form['to-currency']
    amount = request.form['amount']
    c=CurrencyCodes()
    r=CurrencyRates()
    
    try:
        amount = float(amount)
    except ValueError:
        flash('Amount needs to be a number')
        return redirect('/')

    try:
        r.get_rates(from_currency)             
    except Exception:
        flash(f"{from_currency} is not a valid currency code")        
        return redirect('/')

    try:
        r.get_rates(to_currency)        
    except Exception:        
        flash(f"{to_currency} is not valid currency code")
        return redirect('/')

    params ={'from':from_currency, 'to':to_currency}
    response = requests.get(api_url,params)
    
    data = response.json()  
    rate = data['info']['rate']  
    
    exchange_amount = cal_amount(amount,rate)    
    symbol = c.get_symbol(to_currency)
    msg = f"The result is {symbol} {exchange_amount}"   
   
    return render_template('rate.html', msg=msg)

