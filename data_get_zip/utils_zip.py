import os
import zipfile


def get_all_files_in_directory(directory):
    # 获取目录中的所有文件和文件夹
    files_and_folders = os.listdir(directory)
    # 只保留文件，并去除文件夹
    files = [f for f in files_and_folders if os.path.isfile(os.path.join(directory, f))]
    return files


def get_all_files_folders_in_directory(directory):
    # 获取目录中的所有文件和文件夹
    files_and_folders = os.listdir(directory)
    files = [f for f in files_and_folders if os.path.isfile(os.path.join(directory, f))]
    folders = [f for f in files_and_folders if os.path.isdir(os.path.join(directory, f))]

    return [files, folders]


def zip_directory_files(source_dir, target_dir, zip_name):
    # zip all dir and files
    zip_path = os.path.join(target_dir, zip_name)
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(source_dir):
            for file in files:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname=relative_path)


def zip_only_files(source_dir, target_dir, zip_name):
    # only zip files
    # 构造压缩文件的完整路径
    zip_path = os.path.join(target_dir, zip_name)
    # 创建一个 ZipFile 对象，用于写入压缩文件
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        # 遍历指定目录下的所有文件
        files_and_folders = os.listdir(source_dir)
        files = [f for f in files_and_folders if os.path.isfile(os.path.join(source_dir, f))]

        for file in files:
            file_path = os.path.join(source_dir, file)
            # 将文件写入压缩文件
            if os.path.isdir(file_path):
                continue
            zipf.write(file_path, arcname=os.path.relpath(file_path, source_dir))
