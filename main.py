import chevron
from pathlib import Path
import http.server
import socketserver
from functools import partial

def render_template(filename, data):
    '''Render a template with given data. return rendered template. No error checking'''
    template_path = Path("templates/")
    with open(template_path / filename, 'r') as f:
        temp_render = chevron.render(f, data)

    return temp_render

def save_render(filename, render):
    '''save render to a file'''
    render_path = Path("site/")
    render_path.mkdir(exist_ok=True) #Create directory if it doesn't exist
    with open(render_path / filename, 'w') as f:
        f.write(render)

def host_site_test(sitename, path="site", PORT = 8080):
    '''host site port 8080'''
    handler = partial(http.server.SimpleHTTPRequestHandler, directory=path)
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"serving at: http://localhost:{str(PORT)}/{sitename}")
        httpd.serve_forever()

if __name__ == '__main__':
    #quick test
    testdata = {'title': 'shi-title', 'header-one': 'shi-header', 'body': 'shi-boddy'}
    render = render_template('test1.html', testdata)
    save_render('shi.html', render)
    host_site_test('shi.html')

