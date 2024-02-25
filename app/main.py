from datetime import datetime
import requests
from pyscript import display

now = datetime.now()
display(now.strftime("%m/%d/%Y, %H:%M:%S"))