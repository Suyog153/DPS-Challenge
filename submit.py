'''This code submits the solution to the DPS-Challenge server'''

#import requests
import pyotp
import base64

totp = pyotp.TOTP(base64.b32encode(bytearray("suyognmv@gmail.comDPSCHALLENGE", 'ascii')).decode('utf-8'), digits=10, digest='sha512', interval = 120)

body = {
        "github":"https://github.com/Suyog153/DPS-Challenge",
        "email":"suyognmv@gmail.com",
        "url":"https://dpschallenge2022.ew.r.appspot.com/prediction",
        "notes":"Please give values for first 9 months as 1, 2, 3, etc and not as 01, 02, 03 at test time"
        }

headers = {'Content-type': 'application/json', 'Authorization': 'Basic' + totp.now()}

req = requests.post("https://dps-challenge.netlify.app/.netlify/functions/api/challenge", headers = headers, json = body)

print(req.json())


