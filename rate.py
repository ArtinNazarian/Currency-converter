from forex_python.converter import CurrencyCodes

def cal_amount(amount, rate):
    result = amount * rate
    return round(result,2)

# def check_currency_code(from_code, to_code):
#     c=CurrencyCodes()
#     try:
#         c.get_symbol(from_code)
#         c.get_symbol(to_code)
#     except:
         
    
    
