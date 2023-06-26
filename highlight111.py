from io import BytesIO
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import ImageFormatter
from PIL import Image


def highlight_to_image(code, filename, lan):
    lexer = get_lexer_by_name(lan, stripall=True)
    formatter = ImageFormatter(font_name="Consolas", font_size=16, line_numbers=True)
    image_data = highlight(code, lexer, formatter)
    image = Image.open(BytesIO(image_data))

    image.save(filename)


# if __name__ == '__main__':
#     code1 = """
#     def highlight_to_image(code):
#     lexer = get_lexer_by_name("python", stripall=True)
#     formatter = ImageFormatter(font_name="DejaVu Sans Mono", font_size=16, line_numbers=True)
#     image_data = highlight(code, lexer, formatter)
#     image = Image.open(BytesIO(image_data))
#     return image
#     """
#     highlight_to_image(code1, "highlight_output.png")
