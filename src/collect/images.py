import os


def is_picture(path: str) -> bool:
    return path.endswith('.png') or path.endswith('.jpg') or path.endswith('.jpeg')


def list_images(path: str) -> list:
    file_list = os.listdir(path)
    filtered_list = filter(is_picture, file_list)
    return list(filtered_list)
