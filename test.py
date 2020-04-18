import urlfetch

# Import SocksiPy
import main as socks

res = urlfetch.get('http://ip-api.com/json')
print (res.content)
# Set the proxy information
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, '192.168.0.156', 9050)
#socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, 'klaki.net', 18080)

# Route an HTTP request through the SOCKS proxy 
socks.wrapmodule(urlfetch)
res = urlfetch.get('http://ip-api.com/json')
print (res.content)
