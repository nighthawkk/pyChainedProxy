# pyChainedProxy #

This is a modified version of socksipy module, which supports chaining of
proxy servers and various modes of TLS/SSL encryption.

https://pypi.org/project/pyChainedProxy/

Chaining of Proxy 
===========================
Client <--> Proxy(1) <--> Proxy(2) <--> ... <--> Proxy(n) <--> Web Server

Proxies can be Http, Socks4, Socks5, etc. 

## Install ##

```
pip install pyChainedProxy
```
## Usage ##

```
import socket
import pyChainedProxy as socks #import pyChainedProxy

# Enable debugging
def DEBUG(msg):
  print (msg)

socks.DEBUG = DEBUG


print ("Check IP w/o proxyfying:  ",urlfetch.get('http://ip-api.com/json').content)   

# Configure a default chain
chain = [
  'socks5://localhost:9050/', # First hop is Tor,
  'http://user1:pass@example.com/' # ...and then auth to an HTTP proxy
]
socks.setdefaultproxy() # Clear the default chain
#adding hops with proxies
for hop in chain:
   socks.adddefaultproxy(*socks.parseproxy(hop))

#wrap a single module   
#socks.wrapmodule(urlfetch)   

# Configure alternate routes (No proxy for localhost)
socks.setproxy('localhost', socks.PROXY_TYPE_NONE)
socks.setproxy('127.0.0.1', socks.PROXY_TYPE_NONE)

# This would have set proxies using the standard environment variables:
#socks.usesystemdefaults()


# Monkey Patching whole socket class (everything will be proxified)
rawsocket = socket.socket
socket.socket = socks.socksocket
# Everything will be proxied!

print ("Check IP After proxyfying:  ",urlfetch.get('http://ip-api.com/json').content)
```
## Example ##
You can edit and use `test.py` according to your config.

-------------------------------------------------------------------------------
# Original README #

<pre>
SocksiPy version 1.00
A Python SOCKS module.
(C) 2006 Dan-Haim. All rights reserved.
See LICENSE file for details.


WHAT IS A SOCKS PROXY?
A SOCKS proxy is a proxy server at the TCP level. In other words, it acts as
a tunnel, relaying all traffic going through it without modifying it.
SOCKS proxies can be used to relay traffic using any network protocol that
uses TCP.

WHAT IS SOCKSIPY?
This Python module allows you to create TCP connections through a SOCKS
proxy without any special effort.

PROXY COMPATIBILITY
SocksiPy is compatible with three different types of proxies:
1. SOCKS Version 4 (Socks4), including the Socks4a extension.
2. SOCKS Version 5 (Socks5).
3. HTTP Proxies which support tunneling using the CONNECT method.

SYSTEM REQUIREMENTS
Being written in Python, SocksiPy can run on any platform that has a Python
interpreter and TCP/IP support.
This module has been tested with Python 2.3 and should work with greater versions
just as well.


INSTALLATION
-------------

Simply copy the file "socks.py" to your Python's lib/site-packages directory,
and you're ready to go.


USAGE
------

First load the socks module with the command:

>>> import socks
>>>

The socks module provides a class called "socksocket", which is the base to
all of the module's functionality.
The socksocket object has the same initialization parameters as the normal socket
object to ensure maximal compatibility, however it should be noted that socksocket
will only function with family being AF_INET and type being SOCK_STREAM.
Generally, it is best to initialize the socksocket object with no parameters

>>> s = socks.socksocket()
>>>

The socksocket object has an interface which is very similar  to socket's (in fact
the socksocket class is derived from socket) with a few extra methods.
To select the proxy server you would like to use, use the setproxy method, whose
syntax is:

setproxy(proxytype, addr[, port[, rdns[, username[, password]]]])

Explaination of the parameters:

proxytype - The type of the proxy server. This can be one of three possible
choices: PROXY_TYPE_SOCKS4, PROXY_TYPE_SOCKS5 and PROXY_TYPE_HTTP for Socks4,
Socks5 and HTTP servers respectively.

addr - The IP address or DNS name of the proxy server.

port - The port of the proxy server. Defaults to 1080 for socks and 8080 for http.

rdns - This is a boolean flag than modifies the behavior regarding DNS resolving.
If it is set to True, DNS resolving will be preformed remotely, on the server.
If it is set to False, DNS resolving will be preformed locally. Please note that
setting this to True with Socks4 servers actually use an extension to the protocol,
called Socks4a, which may not be supported on all servers (Socks5 and http servers
always support DNS). The default is True.

username - For Socks5 servers, this allows simple username / password authentication
with the server. For Socks4 servers, this parameter will be sent as the userid.
This parameter is ignored if an HTTP server is being used. If it is not provided,
authentication will not be used (servers may accept unauthentication requests).

password - This parameter is valid only for Socks5 servers and specifies the
respective password for the username provided.

Example of usage:

>>> s.setproxy(socks.PROXY_TYPE_SOCKS5,"socks.example.com")
>>>

After the setproxy method has been called, simply call the connect method with the
traditional parameters to establish a connection through the proxy:

>>> s.connect(("www.sourceforge.net",80))
>>>

Connection will take a bit longer to allow negotiation with the proxy server.
Please note that calling connect without calling setproxy earlier will connect
without a proxy (just like a regular socket).

Errors: Any errors in the connection process will trigger exceptions. The exception
may either be generated by the underlying socket layer or may be custom module
exceptions, whose details follow:

class ProxyError - This is a base exception class. It is not raised directly but
rather all other exception classes raised by this module are derived from it.
This allows an easy way to catch all proxy-related errors.

class GeneralProxyError - When thrown, it indicates a problem which does not fall
into another category. The parameter is a tuple containing an error code and a
description of the error, from the following list:
1 - invalid data - This error means that unexpected data has been received from
the server. The most common reason is that the server specified as the proxy is
not really a Socks4/Socks5/HTTP proxy, or maybe the proxy type specified is wrong.
4 - bad proxy type - This will be raised if the type of the proxy supplied to the
setproxy function was not PROXY_TYPE_SOCKS4/PROXY_TYPE_SOCKS5/PROXY_TYPE_HTTP.
5 - bad input - This will be raised if the connect method is called with bad input
parameters.

class Socks5AuthError - This indicates that the connection through a Socks5 server
failed due to an authentication problem. The parameter is a tuple containing a
code and a description message according to the following list:

1 - authentication is required - This will happen if you use a Socks5 server which
requires authentication without providing a username / password at all.
2 - all offered authentication methods were rejected - This will happen if the proxy
requires a special authentication method which is not supported by this module.
3 - unknown username or invalid password - Self descriptive.

class Socks5Error - This will be raised for Socks5 errors which are not related to
authentication. The parameter is a tuple containing a code and a description of the
error, as given by the server. The possible errors, according to the RFC are:

1 - General SOCKS server failure - If for any reason the proxy server is unable to
fulfill your request (internal server error).
2 - connection not allowed by ruleset - If the address you're trying to connect to
is blacklisted on the server or requires authentication.
3 - Network unreachable - The target could not be contacted. A router on the network
had replied with a destination net unreachable error.
4 - Host unreachable - The target could not be contacted. A router on the network
had replied with a destination host unreachable error.
5 - Connection refused - The target server has actively refused the connection
(the requested port is closed).
6 - TTL expired - The TTL value of the SYN packet from the proxy to the target server
has expired. This usually means that there are network problems causing the packet
to be caught in a router-to-router "ping-pong".
7 - Command not supported - The client has issued an invalid command. When using this
module, this error should not occur.
8 - Address type not supported - The client has provided an invalid address type.
When using this module, this error should not occur.

class Socks4Error - This will be raised for Socks4 errors. The parameter is a tuple
containing a code and a description of the error, as given by the server. The
possible error, according to the specification are:

1 - Request rejected or failed - Will be raised in the event of an failure for any
reason other then the two mentioned next.
2 - request rejected because SOCKS server cannot connect to identd on the client -
The Socks server had tried an ident lookup on your computer and has failed. In this
case you should run an identd server and/or configure your firewall to allow incoming
connections to local port 113 from the remote server.
3 - request rejected because the client program and identd report different user-ids -
The Socks server had performed an ident lookup on your computer and has received a
different userid than the one you have provided. Change your userid (through the
username parameter of the setproxy method) to match and try again.

class HTTPError - This will be raised for HTTP errors. The parameter is a tuple
containing the HTTP status code and the description of the server.


After establishing the connection, the object behaves like a standard socket.
Call the close method to close the connection.

In addition to the socksocket class, an additional function worth mentioning is the
setdefaultproxy function. The parameters are the same as the setproxy method.
This function will set default proxy settings for newly created socksocket objects,
in which the proxy settings haven't been changed via the setproxy method.
This is quite useful if you wish to force 3rd party modules to use a socks proxy,
by overriding the socket object.
For example:

>>> socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"socks.example.com")
>>> socket.socket = socks.socksocket
>>> urllib.urlopen("http://www.sourceforge.net/")


</pre>
