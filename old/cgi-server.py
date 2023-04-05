from http.server import HTTPServer, BaseHTTPRequestHandler
import cgi


class WebServerHandler(BaseHTTPRequestHandler):
    form_html = \
        '''
        <form method='POST' enctype='multipart/form-data' action='/hello'>
        <h2>What would you like me to say?</h2>
        <input name="message" type="text"><input type="submit" value="Submit" >
        </form>
         '''

    def do_GET(self):
        try:
            if self.path.endswith("/hello"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = ""
                output += "<html>" \
                          " <body>" \
                          "     Hello!<br>" + self.form_html + \
                          " </body>" \
                          "</html>"
                self.wfile.write(output.encode())
                print(output)

            if self.path.endswith("/hola"):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

                output = "<html>" \
                         "    <body>" \
                         "      &#161;Hola! <br>" + self.form_html + \
                         "      <a href='/hello'>Back Home</a>" \
                         "    </body>" \
                         "</html>"
                self.wfile.write(output.encode())
                print(output)

        except IOError:
            self.send_error(404, "File Not Found {}".format(self.path))

    def do_POST(self):
        try:
            self.send_response(301)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # HEADERS are now in dict/json style container
            ctype, pdict = cgi.parse_header(
                self.headers['content-type'])

            # boundary data needs to be encoded in a binary format
            pdict['boundary'] = bytes(pdict['boundary'], "utf-8")

            if ctype == 'multipart/form-data':
                fields = cgi.parse_multipart(self.rfile, pdict)
                messagecontent = fields.get('message')

            output = ""
            output += "<html><body>"
            output += " <h2> Okay, how about this: </h2>"
            # decode it back into a string rather than byte string(b'stuff')
            output += "<h1> {} </h1>".format(messagecontent[0].decode())
            output += self.form_html
            output += "</body></html>"
            self.wfile.write(output.encode())
            print(output)

        except:
            raise


def main():
    try:
        port = 80
        server = HTTPServer(('', port), WebServerHandler)
        print("Web server is running on port {}".format(port))
        server.serve_forever()

    except KeyboardInterrupt:
        print("^C entered, stopping web server...")

    finally:
        if server:
            server.socket.close()


if __name__ == '__main__':
    main()