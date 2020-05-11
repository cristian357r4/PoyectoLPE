import datetime
import re
from datetime import date
date_str = '29/12/2017' # The date - 29 Dec 2017
format_str = '%d/%m/%Y' # The format

datetime_obj = datetime.datetime.strptime(date_str, format_str)
print(datetime_obj.date())

resultado = re.split("/", date_str)
#
print(resultado)

id =  ''.join(resultado)
print(id)



today = date.today()
print("Today's date:", today)


from datetime import date

today = date.today()

# dd/mm/YY
d1 = today.strftime("%d%m%Y")
print("d1 =", d1)

# Textual month, day and year
d2 = today.strftime("%B %d, %Y")
print("d2 =", d2)

# mm/dd/y
d3 = today.strftime("%m/%d/%y")
print("d3 =", d3)

# Month abbreviation, day and year
d4 = today.strftime("%b-%d-%Y")
print("d4 =", d4)
##################################

import re

txt = "Cristian"
x = re.findall("[^A-Za-z]", txt)

if	len(x) != 0:
	print("Entrada incorrecta porfavor digite son caracteres especiales o espacios")
else:
	print("Bienvendo "+txt)
