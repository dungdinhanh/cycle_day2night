import os, shutil, glob, random

def get_list_images(folder, num):
    list_images = glob.glob(os.path.join(folder, "*.png"))
    random.shuffle(list_images)
    return list_images[0:num]

def copy_files(src, dest, num=3000):
    dest_traina = os.path.join(dest, "trainA")
    dest_trainb = os.path.join(dest, "trainB")
    src_traina = os.path.join(src, "trainA")
    src_trainb = os.path.join(src, "trainB")


    os.makedirs(dest_traina, exist_ok=True)
    os.makedirs(dest_trainb, exist_ok=True)

    list_traina = get_list_images(src_traina, num)
    list_trainb = get_list_images(src_trainb, num)

    for file in list_traina:
        shutil.copy(file, dest_traina)
    for file in list_trainb:
        shutil.copy(file, dest_trainb)

def copy_test_files(src, dest):
    dest_traina = os.path.join(dest, "testA")
    dest_trainb = os.path.join(dest, "testB")
    src_traina = os.path.join(src, "testA")
    src_trainb = os.path.join(src, "testB")

    os.makedirs(dest_traina, exist_ok=True)
    os.makedirs(dest_trainb, exist_ok=True)

    list_traina = get_list_images(src_traina, 10000)
    list_trainb = get_list_images(src_trainb, 10000)

    for file in list_traina:
        shutil.copy(file, dest_traina)
    for file in list_trainb:
        shutil.copy(file, dest_trainb)

if __name__ == '__main__':
    data_folder = "data"
    src_folder = os.path.join(data_folder, "combinedata/kaist")
    dist_folder = os.path.join(data_folder, "combinedata")
    copy_files(src_folder, dist_folder, 1000)

