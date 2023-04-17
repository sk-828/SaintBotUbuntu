import numpy as np
import requests


res = requests.get("https://script.google.com/macros/s/AKfycbyJLkB5dbYGurJsjbgJjJLJkKhh9rWp1I-dc-RVt47GexRtCIG3Y2iGgv2ncyREQCihXg/exec?row=10")
tarotComment=np.array(res.json())
tarotComment=tarotComment[1:23,2:5]