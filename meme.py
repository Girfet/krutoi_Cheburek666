from PIL import Image, ImageDraw, ImageFont
image = Image.open('jabloko.jpg')
width, height = image.size 
top_text = input('Введите верхний текст: ')
bottom_text = input('Введите нижний текст: ')
font = ImageFont.truetype('impact.ttf', float(input('Введите размер шрифта: ')) )
#первое поле для рисования
text = draw.textbbox((0,0), top_text, font)
text_width = text[2]
top_draw = ImageDraw.Draw(image)
top_draw.text(((width - text_width) / 2, 10),top_text, 'white', font)
text = draw.textbbox((0,0), bottom_text, font)
text_width = text[2]
text_height = text[3]
bottom_draw = ImageDraw.Draw(image)
bottom_draw.text(((width - text_width) / 2, height - text_height - 10), bottom_text, 'white', font)
image.save('mem1.jpg')