import os
from flask import Flask
import random
app = Flask(__name__)


@app.route('/')
def index():
    return (pingvar)


@app.route('/about')
def about():
    return "About page"


pingvar = "string"

  
ip_list = ['8.8.8.8']
for ip in ip_list:
    response = os.popen(f"ping {ip}").read()
    if "Received = 4" in response:
        pingvar = "UP {ip} Ping Successful"
      
    else:
        pingvar = "DOWN {ip} Ping Unsuccessful"

print(pingvar)




if __name__ == "__main__":
  app.run(
		host='0.0.0.0',
		port=random.randint(2000,9000)
  )
