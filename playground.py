
from forex_python.bitcoin import BtcConverter
b = BtcConverter() # force_decimal=True to get Decimal rates
val = "{:,.2f}".format(b.get_latest_price('USD'))
print(val)