import urlfetch
import socket
import requests
import pyChainedProxy as socks #import pyChainedProxy

# Enable debugging
def DEBUG(msg):
  print (msg)

socks.DEBUG = DEBUG
print ("Hell:  ",urlfetch.get('http://ip-api.com/json').content)   
# Configure a default chain
chain = [
  'tor://localhost:9050/', # First hop is Tor,
  'http://user:pass@proxy.example.com/' # ...and then auth to an HTTP proxy
]
socks.setdefaultproxy() # Clear the default chain
#adding hops with proxies
for hop in chain:
   socks.adddefaultproxy(*socks.parseproxy(hop))

#wrap a single module   
#socks.wrapmodule(urlfetch)   
res = urlfetch.get('http://ip-api.com/json')

# Configure alternate routes (No proxy for localhost)
socks.setproxy('localhost', socks.PROXY_TYPE_NONE)
socks.setproxy('127.0.0.1', socks.PROXY_TYPE_NONE)

# This would have set proxies using the standard environment variables:
#socks.usesystemdefaults()


# Monkey Patching whole socket class (everything will be proxified)
rawsocket = socket.socket
socket.socket = socks.socksocket
# Everything will be proxied!
print ("Hell:  ",urlfetch.get('http://ip-api.com/json').content)