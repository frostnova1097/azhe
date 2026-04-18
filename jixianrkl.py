import os
import shutil
import argparse

def split_files(src_folder, group_size):
    files = [f for f in os.listdir(src_folder) if os.path.isfile(os.path.join(src_folder, f))]
    total_files = len(files)
    print(f"总文件数: {total_files}")

    # 自动在源文件夹同级目录下创建output文件夹
    parent_dir = os.path.dirname(src_folder.rstrip("\\/"))
    dst_base_folder = os.path.join(parent_dir, "output")
    os.makedirs(dst_base_folder, exist_ok=True)

    for i in range(0, total_files, group_size):
        group_num = i // group_size + 1
        dst_folder = os.path.join(dst_base_folder, f"group_{group_num}")
        os.makedirs(dst_folder, exist_ok=True)
        for f in files[i:i+group_size]:
            shutil.move(os.path.join(src_folder, f), os.path.join(dst_folder, f))
        print(f"已移动 group_{group_num} 文件夹: {len(files[i:i+group_size])} 个文件")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="将文件夹内文件按指定数量分组到新文件夹")
    parser.add_argument("src_folder", help="源文件夹路径")
    parser.add_argument("--group_size", type=int, default=5000, help="每组文件数量，默认5000")
    args = parser.parse_args()
    split_files(args.src_folder, args.group_size)