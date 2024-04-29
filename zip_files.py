import os
import zipfile
from data_get_zip import *

if __name__ == "__main__":
## set up
    source_dir_c = '/lustre03/project/6008063/neurohub/HCP/HCPDevelopment/'
    hcp_dir_name = '1199770-HCPDevelopmentRec/'

    target_dir = "/lustre04/scratch/lianghe/lianghe/forzip/hcp_d/"
    zip_name = "developed_"

## zip
# zip only the files in the big dir
    source_dir_rest = source_dir_c + hcp_dir_name
    # get files and folders name
    [hcp_files, hcp_folders] = get_all_files_folders_in_directory(source_dir_rest)

    zip_name_rest = zip_name + 'rest_files.zip'
    if len(hcp_files) > 0:
        zip_only_files(source_dir_rest, target_dir, zip_name_rest)

    print(f"finish rest, compressed as {os.path.join(target_dir, zip_name_rest)}")

# zip experiments files
    source_dir_exp = source_dir_c + hcp_dir_name + 'experiments/'
    zip_name_exp = zip_name + 'experiments.zip'
    zip_directory_files(source_dir_exp, target_dir, zip_name_exp)

    print(f"finish experiments, compressed as {os.path.join(target_dir, zip_name_rest)}")

# zip fmri
    # rest part
    source_dir_fmri = source_dir_c + hcp_dir_name + 'fmriresults01/'
    zip_name_fmri = zip_name + 'fmri_files.zip'
    [hcp_files_fmri, hcp_folders_fmri]= get_all_files_folders_in_directory(source_dir_fmri)
    # for any files
    if len(hcp_files_fmri) > 0:
        zip_only_files(source_dir_fmri, target_dir, zip_name_fmri)

    print(f"finish rest fMRI, compressed as {os.path.join(target_dir, zip_name_rest)}")
    # subject level

    # 检查目标路径是否存在，不存在时创建
    target_dir_subjects = target_dir + 'subjects/'
    if not os.path.exists(target_dir_subjects):
        os.makedirs(target_dir_subjects)

    for hcp_folder_sub in hcp_folders_fmri:
        source_dir_subjects = source_dir_fmri + hcp_folder_sub + '/'
        zip_name_subjects = 'fMRI_' + hcp_folder_sub + '.zip'
        zip_directory_files(source_dir_subjects, target_dir_subjects, zip_name_subjects)
        print(f"finish subjects fMRI: **** {hcp_folder_sub} ****, compressed as {os.path.join(target_dir, zip_name_rest)}")
