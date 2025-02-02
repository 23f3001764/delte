import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Static data (replace this with a database if needed)
DATA = {
    "6ip": 53, "JybhUqp": 51, "mdHvDs7tNj": 84, "WD": 20, "jA4": 55,
    "H": 57, "uRhBlq3I": 39, "tokP": 79, "22M": 40, "y5Ly": 0,
    "Yn69q": 31, "Bg": 81, "duGpfW": 76, "xRMZKPVclM": 87, "l7539": 69,
    "b9": 74, "SmK9lxw6": 23, "P4ZLrXy": 64, "YnP": 77, "z0PhtFs": 45,
    "zx7835": 56, "NI": 69, "SdHK7": 49, "eSypT8J": 96, "tfVnww": 77,
    "1p": 28, "Jjl": 66, "j2Eo": 93, "MF": 6, "r": 98, "11KkF4DBzg": 91,
    "MF5X9r": 63, "1c": 51, "6UtiL9qXt": 23, "OaUZyhQod3": 90, "8BnvPM": 85,
    "xXZEon": 62, "FxQIVCR": 91, "8FG9BLE": 87, "mm3G": 48, "9mPw5EUl7": 67,
    "UH6p": 33, "U": 47, "wuYdEub": 39, "4o": 87, "FmeEc4kyBz": 12,
    "ivZnV8sDPW": 34, "7BUZxUK": 99, "wEJcv7arAk": 85, "9l8S": 12, "rkP": 37,
    "5b": 6, "w": 45, "vgnB9ZClP": 30, "jsiU47rzO": 4, "7u0hN": 16, "Jw8yb": 44,
    "Qww": 29, "Wjzx7hdhI": 68, "ZZrVkHyi": 88, "y": 16, "Bp": 27, "2cFYp2n6DA": 86,
    "j0": 10, "MeUfWCy3oX": 70, "AgexbAo": 70, "BHxaa4Z": 37, "Si5b": 33, "t9": 38,
    "5e1KGX": 74, "GyjZ": 53, "awe": 74, "N2k": 43, "7LQdrZ": 24, "cV": 38,
    "V9VjMOUf": 32, "VqN7mXuC": 54, "q": 21, "VOf": 68, "lBIodS9AX": 61,
    "3xqMamac9t": 36, "2N1GHqtalR": 59, "aEJYhk7": 73, "nWo9Lhi": 68, "HRKwvYCiR": 49,
    "hjl0dpgist": 0, "SQ4": 90, "esfw25": 22, "GZDg8Xj": 3, "uPkdYdbb": 21,
    "zFBgySSUq": 17, "CcTVb": 63, "ozLDD": 84, "Q": 87, "jlG6J": 98, "xwqjPQ": 17,
    "D8Ls": 44, "YD": 99, "QCD": 68, "OX": 3
}

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query.get('name', [])

        # Prepare the result
        if not names:
            # If no names are provided, return all data
            result = { "marks": list(DATA.values()) }
        else:
            # If names are provided, return marks for those names
            marks = [DATA.get(name, None) for name in names]  # Returns None if name not found
            result = { "marks": marks }

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')  # Enable CORS
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))