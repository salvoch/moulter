from logging import raiseExceptions
import chevron
from pathlib import Path
import http.server
import socketserver
from functools import partial

class TokenMismatchError(Exception):
    pass

def check_tokens(filename, data):
    '''Check that the data has the keys in the filename'''
    template_path = Path("templates/")
    
    #Extract tokens
    with open(template_path / filename, 'r') as f:
        ft = f.read()
        tokens_tuple = chevron.tokenizer.tokenize(ft)
        tokens = [v[1] for v in tokens_tuple if v[0] == 'variable'] #Extract variable names
    
    #Check tokens == keys
    if set(data.keys()) != set(tokens):
        raise TokenMismatchError(f"Tokens do not match!\n\
        Data keys: {str(list(data.keys()))}, \n\
        Template variables: {str(tokens)}")

def render_template(filename, data):
    '''Render a template with given data. return rendered template.'''
    template_path = Path("templates/")
    check_tokens(filename, data) #Check tokens

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

