from PIL import Image
from random import randint
import StringIO

def main():

    width=128
    height=224

    my_list = []

    for x in range(width * height):
        my_list.append((0,randint(63,127),randint(0,255))) 

    img = Image.new('RGB', (width, height))
    img.putdata(my_list)

    output = StringIO.StringIO()

    img.save(output, 'png')

    return output.getvalue()

if __name__ == '__main__':
        main()
