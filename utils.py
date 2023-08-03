import os
import pickle
import shutil

from scipy.io import loadmat


def read_mat(mat_file_path):
    # 使用loadmat函数打开.mat文件
    data = loadmat(mat_file_path)
    temp = str(data['roi'].flatten()[0][-1][0])
    # print(temp, type(temp))
    return temp


def copy_file_tree(source_file):
    destination_file, temp = get_destination_file_path(source_file)
    # 定义目标目录路径
    destination_directory = r'E:\筛选后肝包虫图片'
    # 拼接目标文件夹路径
    destination_folder = os.path.join(destination_directory, os.path.dirname(temp))
    # 创建目标文件夹（如果不存在）
    os.makedirs(destination_folder, exist_ok=True)
    # 使用shutil库的copy函数复制文件
    try:
        shutil.copy(source_file, destination_file)
    except Exception as e:
        print(e)


def read_images_list():
    with open('./assets/images_list.pkl', 'rb') as f:
        images_list = pickle.load(f)
    return images_list


def read_included_list(path):
    with open(path, 'rb') as f:
        included_list = pickle.load(f)
    return included_list


def get_destination_file_path(source_file):
    # 定义目标目录路径
    destination_directory = r'E:\筛选后肝包虫图片'

    # 去除盘符
    temp = '\\'.join(source_file.split('\\')[1:])

    # 拼接目标文件路径
    destination_file = os.path.join(destination_directory, temp)
    return destination_file, temp


def get_current_index(index_file):
    with open('./assets/current_index_saved.pkl', 'rb') as f:
        current_index = pickle.load(f)
    return current_index
