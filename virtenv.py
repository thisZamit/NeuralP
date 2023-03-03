import subprocess
import sys
from flask import Flask
print('hellow')


try:
    import pandas as pd
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pandas'])
finally:
    import pandas as pd

app = Flask(__name__)

@app.route("/")
def hello():
    return "hey amit"

if __name__ == '__main__':
    app.run(debug=True)

