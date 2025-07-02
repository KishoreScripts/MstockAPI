# MstockAPI
Developing for Mstock API towards Scalping 

******Login and Access Token Generation**
******First open Notepad**
Paste Login.py Code There
save it as Login.py and save type as "all Files"

**Do Save in C:Users/Username for directly running it in CMD

Open CDM and Type:
Python login.py

- Prompts you for your username, password, and API key
- Triggers OTP and asks you to enter it
- Uses the official tradingapi_a SDK from GitHub
- Generates the access token
- Saves it in a JSON file for later us
 It’ll save the access token in session_data/token.json

In CMD, It asks For 
C:\Users\ganta>python login.py
👤 Username: MA2XXXX08
🔒 Password: OnXXXXXX3@
🔑 API Key: CFuFXXXXXXXXXXXP4Ps+0=
✅ OTP sent to your mobile number.
📲 Enter OTP: 2X8
🔓 Token saved successfully to session_data/token.json

**Install the python and official Mstock SDK **
 pip install mStock-TradingApi-A

**For Rest all packages I am Using Use**
pip install -r requirements.txt

Thats it we have now our access token in Session Data Folder
------------

Run Also Below Packages Further for Option Chain:

pip install pyOpenSSL

python -m pip install pyOpenSSL

pip install service_identity

python -m pip install service_identity

pip install xlwings

pip show xlwings



------------







