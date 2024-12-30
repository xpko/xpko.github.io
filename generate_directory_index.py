import os
import urllib.parse

def read_blogignore(dir_path):
    """
    从指定目录下读取 .blogignore 文件，返回需要排除的文件或目录名称列表。
    - 忽略空行和以 '#' 开头的注释行
    """
    blogignore_path = os.path.join(dir_path, '.blogignore')
    if not os.path.isfile(blogignore_path):
        return []

    ignore_list = []
    with open(blogignore_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            # 跳过空行与注释行
            if not line or line.startswith('#'):
                continue
            ignore_list.append(line)
    return ignore_list

def has_readme(directory):
    """检查目录中是否存在 README.md（不区分大小写）"""
    for item in os.listdir(directory):
        if item.lower() == 'readme.md':
            return True
    return False

def is_markdown_file(filename):
    """检查文件是否为 Markdown 文件（不区分大小写）"""
    return filename.lower().endswith('.md')

def generate_markdown_index(
    base_path,
    current_path='.',
    level=0,
    exclude_dirs=None,
    exclude_files=None
):
    """
    递归生成 Markdown 目录索引，包含：
    - 仅包含 README.md 的目录，链接指向目录本身；
    - 其他 Markdown 文件，链接指向文件本身，链接文本为文件名（不含 .md）；
    - 同时可排除指定目录和指定文件；
    - 若当前目录下存在 .blogignore 文件，则读取其中指定的排除目标（可以是文件或目录）。
    """
    # 默认的全局排除目录
    if exclude_dirs is None:
        exclude_dirs = ['.git', '.github', 'node_modules', '__pycache__']
    # 默认的全局排除文件
    if exclude_files is None:
        exclude_files = []

    markdown = ""
    full_path = os.path.join(base_path, current_path)

    # 1. 读取当前目录下的 .blogignore 文件
    local_ignores = read_blogignore(full_path)

    # 2. 将 .blogignore 中的条目分别加入排除列表（可能是文件也可能是文件夹）
    combined_exclude_dirs = set(exclude_dirs)     # 用集合来合并
    combined_exclude_files = set(exclude_files)

    for item in local_ignores:
        item_path = os.path.join(full_path, item)
        if os.path.isdir(item_path):
            combined_exclude_dirs.add(item)
        else:
            combined_exclude_files.add(item)

    # 开始读取目录内容
    try:
        items = sorted(os.listdir(full_path))
    except PermissionError:
        return markdown

    for item in items:
        item_path = os.path.join(full_path, item)
        relative_path = os.path.join(current_path, item).replace('\\', '/')

        # 如果命中了目录排除，直接跳过
        if item in combined_exclude_dirs and os.path.isdir(item_path):
            continue

        # 如果是子目录（并且不在排除名单中）
        if os.path.isdir(item_path) and item not in combined_exclude_dirs:
            if has_readme(item_path):
                indent = '  ' * level
                # 确保目录路径以 '/' 结尾，并进行 URL 编码
                dir_link = urllib.parse.quote(relative_path.rstrip('/') + '/')
                markdown += f"{indent}- 📁 [{item}/]({dir_link})\n"
                # 递归查找子目录
                markdown += generate_markdown_index(
                    base_path,
                    relative_path,
                    level + 1,
                    exclude_dirs=combined_exclude_dirs,
                    exclude_files=combined_exclude_files
                )
            else:
                # 没有 README.md 的目录，如果递归下仍有内容，才显示该目录名称
                indent = '  ' * level
                sub = generate_markdown_index(
                    base_path,
                    relative_path,
                    level + 1,
                    exclude_dirs=combined_exclude_dirs,
                    exclude_files=combined_exclude_files
                )
                if sub.strip():
                    markdown += f"{indent}- 📁 {item}/\n"
                    markdown += sub

        # 如果是文件，并且是 Markdown 文件，且未被排除
        elif os.path.isfile(item_path):
            # 如果命中了文件排除，直接跳过
            if item in combined_exclude_files:
                continue

            if is_markdown_file(item) and item.lower() != 'readme.md':
                indent = '  ' * level
                file_name = os.path.splitext(item)[0]
                file_link = urllib.parse.quote(relative_path)
                markdown += f"{indent}- 📄 [{file_name}]({file_link})\n"

    return markdown

def main():
    base_path = '.'  # 仓库根目录

    # 全局排除的目录和文件（可自行按需设置）
    exclude_dirs = ['.git', '.github', 'node_modules', '__pycache__']
    exclude_files = []  # 如需全局排除特定文件，可在此添加

    start_marker = '<!-- DIRECTORY INDEX START -->'
    end_marker = '<!-- DIRECTORY INDEX END -->'

    directory_index = generate_markdown_index(
        base_path=base_path,
        current_path='.',
        level=0,
        exclude_dirs=exclude_dirs,
        exclude_files=exclude_files
    )

    directory_section = f"{start_marker}\n{directory_index}{end_marker}\n"

    readme_path = 'README.md'

    # 读取现有 README.md 内容
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
    else:
        readme_content = ''

    # 替换或添加目录索引部分
    if start_marker in readme_content and end_marker in readme_content:
        # 替换现有的目录索引
        parts = readme_content.split(start_marker)
        if len(parts) > 1:
            before = parts[0]
            after_part = parts[1]
            if end_marker in after_part:
                after = after_part.split(end_marker, 1)[1]
            else:
                after = ''
            new_readme = before + directory_section + after
        else:
            new_readme = readme_content + "\n" + directory_section
    else:
        # 如果 README.md 中还没有这两个标记，则直接加到文件末尾
        new_readme = readme_content + "\n" + directory_section

    # 写回 README.md
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_readme)

    print("README.md 已更新目录索引。")

if __name__ == "__main__":
    main()
