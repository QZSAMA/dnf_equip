import pytesseract
from PIL import Image,ImageDraw

# 把图片分割成若干个单独材料图片
def cropIntoPieces(image):
    pass
# 把图片的上部分分割出来for OCR
def cropTopPart(image):
    pass

def main():
    #打开图片
    image = Image.open(r"D:\Users\QZhao\Desktop\hea\OCR\1200_1.png")
 
    #将图片转换成灰度图片
    image = image.convert("L")
 
    #保存图片
    image.save(r"D:\Users\QZhao\Desktop\hea\OCR\1200(1).png")
    code = pytesseract.image_to_string(image)
    print(code)
 
if __name__ == '__main__':
    main()
