import pyotp
import sys

#########
class cloudflare:
    codename = None
    def __init__(self):
        self.authySecret = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # change your authysecret key
    def getAuthy(self):
        totp = pyotp.TOTP(self.authySecret)
        totp.digits = 7
        totp.interval = 10
        totp.issuer = "Cloudflare"
        return(totp.now())

c1 = cloudflare()
print("Authy token code : ",c1.getAuthy())
