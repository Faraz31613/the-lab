import json
from urllib.parse import parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler

from file_manager import FileManager


class MessageHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # First, send a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        menu_number = self.path[1:]

        data_string = ""
        with FileManager('info_about_lunch.txt', 'r') as lunch_details_file:
            data_string=lunch_details_file.read()

        data_dictionary=json.loads(data_string)

        lunch_according_day = data_dictionary[menu_number]
        lunch_according_day_list=lunch_according_day.split("-")
        menu_u_selected="The day You selected is "+lunch_according_day_list[0]+" and the lunch today is "+ lunch_according_day_list[1]+"\n"
        self.wfile.write(menu_u_selected.encode())

    def do_POST(self):
        # 1. How long was the message? (Use the Content-Length header.)
        length = int(self.headers.get('Content-length', 0))

        # 2. Read the correct amount of data from the request.
        data = self.rfile.read(length).decode()

        # 3. Extract the "message" field from the request data.
        menu_number = parse_qs(data)["menu_number"][0]

        # Send the "message" field back as the response.
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
      

        data_string = ""
        with FileManager('info_about_lunch.txt', 'r') as lunch_details_file:
            data_string=lunch_details_file.read()

        data_dictionary=json.loads(data_string)

        lunch_according_day = data_dictionary[menu_number]
        lunch_according_day_list=lunch_according_day.split("-")
        menu_u_selected="The day You selected is "+lunch_according_day_list[0]+" and the lunch today is "+ lunch_according_day_list[1]+"\n"
        self.wfile.write(menu_u_selected.encode())


if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MessageHandler)
    httpd.serve_forever()
    