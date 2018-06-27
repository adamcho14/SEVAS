import http.server  # https://docs.python.org/3/library/http.server.html
import cgitb

# https://cit.uniba.sk/wiki/doku.php?id=public/jas/cosign
# https://www.piware.de/2011/01/creating-an-https-server-in-python/

cgitb.enable()

address = ""
port = 8000

handler = http.server.CGIHTTPRequestHandler
handler.cgi_directories = ["/", "/administration"]
autServer = http.server.HTTPServer((address, port), handler)

print("Serving at port", port)
print("Test voting by typing this to your browser: localhost:" + str(port) + "/test_index.py")
print("Access real voting by typing this to your browser (Cosign must be configured on your server): localhost:" + str(port) + "/index.py")
print("If you want to access paper voting management, type: localhost:" + str(port) + "/administration/login.py")
autServer.serve_forever()

