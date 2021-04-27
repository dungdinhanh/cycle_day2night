import cv2
import os
import glob
import random


def video_to_images(mp4_file, base_name, s_folder):
    cam = cv2.VideoCapture(mp4_file)

    currentframe = 0
    os.makedirs(s_folder, exist_ok=True)
    while(True):
        ret, frame = cam.read()

        if ret:
            name = base_name + "_f"  +str(currentframe) + ".jpg"
            # print(name)
            image_path = os.path.join(s_folder, name)
            rotated = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite(image_path, rotated)
            currentframe += 1
        else:
            break
    pass

def get_list_removed_images(folder, num):
    list_images = glob.glob(os.path.join(folder, "*.jpg"))
    random.shuffle(list_images)
    n = len(list_images)
    return list_images[0: (n - num)]

if __name__ == '__main__':
    main_folder = "data/collected_data"
    save_folder = "data/expo_video"
    mp4_files = glob.glob(os.path.join(main_folder, "*.mp4"))
    for mp4_file in list(mp4_files):
        file_name = os.path.basename(mp4_file)
        # print(file_name)
        file_name_woext = file_name.split(".")[0]
        sf = save_folder + file_name_woext
        # print(file_name_woext)
        video_to_images(mp4_file, file_name_woext, sf)


        # list of removed images
        rm_images = get_list_removed_images(sf, 700)
        for img in rm_images:
            os.remove(img)



