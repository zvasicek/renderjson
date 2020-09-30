import json, uuid
from IPython.display import display_javascript, display_html, display

class RenderJSON(object):
    def __init__(self, json_data, bg_color="#303030",text_color="#888"):
        if isinstance(json_data, dict):
            self.json_str = json.dumps(json_data)
        else:
            self.json_str = json_data
        self.uuid = str(uuid.uuid4())
        self.bg_color = bg_color
        self.text_color = text_color

    def _ipython_display_(self):
        display_html("""<style>
                        .renderjson {background:%s;padding:10px;color:%s}
                        .renderjson a              { color:lightblue; text-decoration: none; }
                        .renderjson .disclosure    { color: crimson; font-size: 80%%; }
                        .xrenderjson .syntax        { color: blue; }
                        .renderjson .string        { color: #90a959; }
                        .renderjson .number        { color: plum; }
                        .renderjson .boolean       { color: #d28445; }
                        .renderjson .key           { color: #90a959; }
                        .renderjson .keyword       { color: #d28445; }
                        .xrenderjson .object.syntax { color: #ddd; }
                        .renderjson .array.syntax  { color: #fff; }
                        </style>
                        <div id="%s" style="width:100%%;"></div>""" % (self.bg_color, self.text_color, self.uuid), raw=True)
        
        display_javascript("""
        require(["https://rawgit.com/caldwell/renderjson/master/renderjson.js"], function(r) {
            var node = document.getElementById('%s');
            node.innerHTML = ''; // vola se 2x neznamo proc
            node.appendChild(renderjson.set_icons('\u25BA', '\u25BC')(%s));
            return true;
        });
        """ % (self.uuid, self.json_str), raw=True)
