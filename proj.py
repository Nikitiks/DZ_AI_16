import cv2
import sys
import os
from PIL import Image, ExifTags

# image_path = "./images/image.png"

# image = cv2.imread(image_path, cv2.IMREAD_COLOR)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# threshold_value = 150

# _, binary = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)

# cv2.imshow("",binary)

# # saved = cv2.imwrite("./save_image1.png", image)


### Task 2
# Напишіть скрипт для створення аватарки: програма має взяти зображення, вирізати з нього строго центральний квадрат, зменшити його розмір до 250х250 пікселів та повернути у правильну орієнтацію, якщо фото зроблене боком.

# def get_exif_orient(path:str):
#     try:
#         img = Image.open(path)
#         exif = img.getexif()
#         if not exif:
#             return 1

#         orient_key = None
#         for tag, name in ExifTags.TAGS.items():
#             if name == "Orientation":
#                 orient_key = tag
#                 break

#         if orient_key and orient_key in exif:
#             return exif[orient_key]
#         return 1
#     except Exception as ex:
#         print(f"Read error: {ex}")
#         return 1

# image2_path = "./images/image2_copy.jpg"

# orientation = get_exif_orient(image2_path)
# print(f"Orientation {orientation}")

# image2 = cv2.imread(image2_path, cv2.IMREAD_COLOR)

# if orientation == 2:
#     image2 = cv2.flip(image2, 1)          
# elif orientation == 3:
#     image2 = cv2.rotate(image2, cv2.ROTATE_180)
# elif orientation == 4:
#     image2 = cv2.flip(image2, 0)          
# elif orientation == 5:
#     image2 = cv2.flip(cv2.rotate(image2, cv2.ROTATE_90_CLOCKWISE), 1)
# elif orientation == 6:
#     image2 = cv2.rotate(image2, cv2.ROTATE_90_COUNTERCLOCKWISE)
# elif orientation == 7:
#     image2 = cv2.flip(cv2.rotate(image2, cv2.ROTATE_90_CLOCKWISE), 1)
# elif orientation == 8:
#     image2 = cv2.rotate(image2, cv2.ROTATE_90_CLOCKWISE)

# h, w = image2.shape[:2]
# size = min(h,w)
# crop = image2[0 : 3*h//8, w//3 : 3*w//5]

# start_y = (h - size) // 2
# start_x = (w - size) // 2

# center = image2[start_y: start_y + size, start_x : start_x + size]
# small = cv2.resize(center, (250, 250), interpolation=cv2.INTER_AREA)
# cv2.imshow("",small)


## Task 3
# Створіть утиліту для перевірки відповідності зображення технічним вимогам. Програма має перевіряти, чи зображення має 3 канали та чи його роздільна здатність не менша за 800х600. Якщо умови виконано, збережіть його у папку processed, інакше виведіть помилку в консоль.

image3_path = "./images/image2_copy.jpg"
image3 = cv2.imread(image3_path, cv2.IMREAD_COLOR)

def is_correct_image(image):
    h,w = image.shape[:2]
    if h < 800 or w < 600:
        return f"image have incorrect size H = {h} W = {w}"

    channels = image.shape[2] if len(image.shape) == 3 else 1

    if channels != 3:
        return f"image have less canals than 3, shape = {channels}"

dir = "./processed"
err = is_correct_image(image3)

if err is not None:
    print(err)
else:

    output_dir = "./processed"
    os.makedirs(dir, exist_ok=True)

    path = os.path.join(dir,"image3_save.png")
    cv2.imwrite(path, image3)
    

cv2.waitKey(0)
cv2.destroyAllWindows()

