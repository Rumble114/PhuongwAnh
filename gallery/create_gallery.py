import os
import urllib.parse  # Import thư viện urllib để mã hóa URL

# Đường dẫn đến thư mục chứa ảnh
image_folder = 'images_gallery/'

# Lấy danh sách tất cả các file trong thư mục
images = os.listdir(image_folder)

# Tạo file gallery.html
with open('gallery.html', 'w', encoding='utf-8') as f:
    f.write('<!DOCTYPE html>\n<html lang="en">\n<head>\n')
    f.write('<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    f.write('<title>Kho ảnh bé iu nè</title>\n')
    f.write('<link rel="stylesheet" href="gallery.css"> <!-- Liên kết với file CSS -->\n')
    f.write('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css" integrity="sha512-iecdLmaskl7CVkqkXNQ/ZH/XLlvWZOJyj7Yy7tcenmpD1ypASozpmT/E0iPtmFIB46ZmdtAc9eNBvH0H/ZpiBw==" crossorigin="anonymous" referrerpolicy="no-referrer" />\n')
    f.write('</head>\n<body>\n')

    # Bắt đầu tạo gallery
    f.write('<div class="gallery">\n')
    f.write('    <div class="slide">\n')

    # Tạo từng item trong slide từ danh sách ảnh
    for image in images:
        # Kiểm tra xem file có phải là ảnh không
        if image.endswith(('.jpg', '.jpeg', '.png', '.gif')):
            # Mã hóa URL để xử lý các ký tự đặc biệt (bao gồm cả dấu cách)
            encoded_image_url = urllib.parse.quote(f'{image_folder}{image}')
            
            f.write(f'        <div class="item" style="background-image: url({encoded_image_url});">\n')
            f.write('            <div class="content">\n')
            f.write('                <div class="name">yêu em</div>\n')  # Hiển thị "yêu em"
            f.write('            </div>\n')
            f.write('        </div>\n')

    f.write('    </div>\n')
    f.write('<div class="button">\n')
    f.write('    <button class="prev"><i class="fa-solid fa-arrow-left"></i></button>\n')
    f.write('    <button class="return" onclick="window.location.href=\'../index.html\'"><i class="fa-solid fa-xmark"></i></button>\n')
    f.write('    <button class="next"><i class="fa-solid fa-arrow-right"></i></button>\n')
    f.write('</div>\n')
    f.write('<script src="gallery.js"></script>\n')
    f.write('</div>\n</body>\n</html>\n')
