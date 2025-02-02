import json
from http.server import BaseHTTPRequestHandler
import urllib.parse

# Static data (since reading a file won't work on Vercel)
DATA = [{"name":"6ip","marks":53},{"name":"JybhUqp","marks":51},{"name":"mdHvDs7tNj","marks":84},{"name":"WD","marks":20},{"name":"jA4","marks":55},{"name":"H","marks":57},{"name":"uRhBlq3I","marks":39},{"name":"tokP","marks":79},{"name":"22M","marks":40},{"name":"y5Ly","marks":0},{"name":"Yn69q","marks":31},{"name":"Bg","marks":81},{"name":"duGpfW","marks":76},{"name":"xRMZKPVclM","marks":87},{"name":"l7539","marks":69},{"name":"b9","marks":74},{"name":"SmK9lxw6","marks":23},{"name":"P4ZLrXy","marks":64},{"name":"YnP","marks":77},{"name":"z0PhtFs","marks":45},{"name":"zx7835","marks":56},{"name":"NI","marks":69},{"name":"SdHK7","marks":49},{"name":"eSypT8J","marks":96},{"name":"tfVnww","marks":77},{"name":"1p","marks":28},{"name":"Jjl","marks":66},{"name":"j2Eo","marks":93},{"name":"MF","marks":6},{"name":"r","marks":98},{"name":"11KkF4DBzg","marks":91},{"name":"MF5X9r","marks":63},{"name":"1c","marks":51},{"name":"6UtiL9qXt","marks":23},{"name":"OaUZyhQod3","marks":90},{"name":"8BnvPM","marks":85},{"name":"xXZEon","marks":62},{"name":"FxQIVCR","marks":91},{"name":"8FG9BLE","marks":87},{"name":"mm3G","marks":48},{"name":"9mPw5EUl7","marks":67},{"name":"UH6p","marks":33},{"name":"U","marks":47},{"name":"wuYdEub","marks":39},{"name":"4o","marks":87},{"name":"FmeEc4kyBz","marks":12},{"name":"ivZnV8sDPW","marks":34},{"name":"7BUZxUK","marks":99},{"name":"wEJcv7arAk","marks":85},{"name":"9l8S","marks":12},{"name":"rkP","marks":37},{"name":"5b","marks":6},{"name":"w","marks":45},{"name":"vgnB9ZClP","marks":30},{"name":"jsiU47rzO","marks":4},{"name":"7u0hN","marks":16},{"name":"Jw8yb","marks":44},{"name":"Qww","marks":29},{"name":"Wjzx7hdhI","marks":68},{"name":"ZZrVkHyi","marks":88},{"name":"y","marks":16},{"name":"Bp","marks":27},{"name":"2cFYp2n6DA","marks":86},{"name":"j0","marks":10},{"name":"MeUfWCy3oX","marks":70},{"name":"AgexbAo","marks":70},{"name":"BHxaa4Z","marks":37},{"name":"Si5b","marks":33},{"name":"t9","marks":38},{"name":"5e1KGX","marks":74},{"name":"GyjZ","marks":53},{"name":"awe","marks":74},{"name":"N2k","marks":43},{"name":"7LQdrZ","marks":24},{"name":"cV","marks":38},{"name":"V9VjMOUf","marks":32},{"name":"VqN7mXuC","marks":54},{"name":"q","marks":21},{"name":"VOf","marks":68},{"name":"lBIodS9AX","marks":61},{"name":"3xqMamac9t","marks":36},{"name":"2N1GHqtalR","marks":59},{"name":"aEJYhk7","marks":73},{"name":"nWo9Lhi","marks":68},{"name":"HRKwvYCiR","marks":49},{"name":"hjl0dpgist","marks":0},{"name":"SQ4","marks":90},{"name":"esfw25","marks":22},{"name":"GZDg8Xj","marks":3},{"name":"uPkdYdbb","marks":21},{"name":"zFBgySSUq","marks":17},{"name":"CcTVb","marks":63},{"name":"ozLDD","marks":84},{"name":"Q","marks":87},{"name":"jlG6J","marks":98},{"name":"xwqjPQ","marks":17},{"name":"D8Ls","marks":44},{"name":"YD","marks":99},{"name":"QCD","marks":68},{"name":"OX","marks":3}]

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse query parameters
        query = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
        names = query.get('name', [])

        # Prepare the result
        result = {"marks": []}
        for name in names:
            for entry in DATA:
                if entry["name"].lower() == name.lower():  # Case-insensitive match
                    result["marks"].append(entry["marks"])

        # Send response
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(result).encode('utf-8'))
