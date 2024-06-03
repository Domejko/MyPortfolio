from jinja2 import Template

from settings.settings import BASE_DIR


def render_css(url: str):
    with open(f'{BASE_DIR}/frontend/static/css/template.css', 'r') as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_css = template.render(background_image_url=url)

    with open(f'{BASE_DIR}/frontend/static/css/style.css', 'w') as file:
        file.write(rendered_css)
