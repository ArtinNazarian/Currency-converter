from app import app 
from unittest import TestCase
from rate import cal_amount

class CurrencyExchange(TestCase):
    def test_form(self):
       with app.test_client() as client:
        res = client.get('/')
        html = res.get_data(as_text=True)
        
        self.assertEqual(res.status_code, 200)
        self.assertIn('<form action="/exchange_rate" class="exchange-form" method="POST">',html)


    def test_form_input(self):
        with app.test_client() as client:
            res = client.post('/exchange_rate', data={'from-currency': 'USD', 'to-currency':'USD', 'amount':'20'})
            html = res.get_data(as_text=True)            
            self.assertEqual(res.status_code, 200)

    def test_cal_amount(self):
        result = cal_amount(100,.5)
        self.assertEqual(result, 50.00)
