import os
from PIL import Image
from fpdf import FPDF

# Путь к директории с изображениями
#Path to the image directory
image_dir = 'C:\\Users\\...'

# Получаем список файлов в директории
# Getting a list of files in a directory
filenames = os.listdir(image_dir)

# Отфильтровываем только файлы с расширением jpg
# Filter only files with jpg extension
filenames = [f for f in filenames if f.endswith('.jpg')]

# Создаем объект PDF
# Create a PDF object
pdf = FPDF()

# Добавляем изображения в PDF
# Adding images to PDF
for filename in filenames:
    try:
        # Пытаемся открыть изображение
        # Trying to open an image
        image = Image.open(os.path.join(image_dir, filename))

        # Добавляем новую страницу в PDF
        # Adding a new page to PDF
        pdf.add_page() 
        width, height = image.size
        # Растягиваем изображение на всю страницу
        #Stretching an image to fill the page
        pdf.image(os.path.join(image_dir, filename), 0, 0, 210, 297)
    except Exception as e:
        print(f'Error converting image {filename}: {e}')
pdf.output('result.pdf', 'F')
