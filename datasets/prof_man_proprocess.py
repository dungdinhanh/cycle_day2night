import cv2
import os
import glob

if __name__ == '__main__':
    folder = "data/grass_day"
    new_folder = "data/pm_preprocessed"
    os.makedirs(new_folder, exist_ok=True)
    files_name = glob.glob(os.path.join(folder, "*.jpg"))
    for file in list(files_name):
        image = cv2.imread(file)
        # image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        base_name = os.path.basename(file)
        cv2.imwrite(file, image)

