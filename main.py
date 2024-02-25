from datetime import datetime
from pyscript import display

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))