import chevron
from pathlib import Path

def render_template(filename, data):
    '''Render a template with given data. return rendered template. No error checking'''
    template_path = Path("templates/")
    with open(template_path / filename, 'r') as f:
        temp_render = chevron.render(f, data)

    return temp_render

def save_render(filename, render):
    '''save render to a file'''
    template_path = Path("site/")
    template_path.mkdir(exist_ok=True) #Create directory if it doesn't exist
    with open(template_path / filename, 'w') as f:
        f.write(render)

if __name__ == '__main__':
    #quick test
    testdata = {'title': 'shi-title', 'header-one': 'shi-header', 'body': 'shi-bod'}
    render = render_template('test1.html', testdata)
    save_render('shi.html', render)

