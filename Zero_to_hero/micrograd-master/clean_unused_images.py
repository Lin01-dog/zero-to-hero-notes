import os
import re
import urllib.parse

def clean_unused_images():
    # 1. 获取当前脚本所在目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    img_dir = os.path.join(script_dir, 'images')

    if not os.path.exists(img_dir):
        print("❌ 错误：未找到 images 文件夹！")
        return

    # 2. 读取当前目录下所有 .ipynb 和 .md 笔记的内容
    notebook_files = [f for f in os.listdir(script_dir) if f.endswith(('.ipynb', '.md'))]
    
    if not notebook_files:
        print("❌ 错误：当前目录下没有找到任何 .ipynb 或 .md 笔记文件！")
        return

    combined_content = ""
    for file in notebook_files:
        file_path = os.path.join(script_dir, file)
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                combined_content += f.read() + "\n"
        except Exception as e:
            print(f"⚠️ 读取文件 {file} 失败: {e}")

    # 3. 获取 images 文件夹下的所有物理图片
    all_images = set(os.listdir(img_dir))

    # 4. 正则匹配笔记中引用的所有图片（包含 urlDecode 解析，处理空格/特殊字符）
    # 匹配模式覆盖: ./images/xxx.png, images/xxx.png, src="images/xxx.png" 等
    raw_matches = re.findall(r'images/([^\s\)\"\'>]+)', combined_content)
    referenced_images = set()
    
    for match in raw_matches:
        # 解码 URL 编码（例如将 %20 还原为空格）
        clean_name = urllib.parse.unquote(match)
        # 去除可能的 Query 参数（如 xxx.png?v=1）
        clean_name = clean_name.split('?')[0]
        referenced_images.add(clean_name)

    # 5. 计算未被任何笔记引用的冗余图片
    unused_images = sorted(list(all_images - referenced_images))

    # 6. 执行清理操作
    if unused_images:
        print(f"🔍 扫描了 {len(notebook_files)} 个笔记文件，发现 {len(unused_images)} 张冗余图片：\n")
        for img_name in unused_images:
            print(f"  - images/{img_name}")
        
        # 安全确认
        confirm = input("\n⚠️ 是否确认将上述图片永久删除？(y/N): ").strip().lower()
        if confirm == 'y':
            deleted_count = 0
            for img_name in unused_images:
                img_path = os.path.join(img_dir, img_name)
                try:
                    os.remove(img_path)
                    deleted_count += 1
                except Exception as e:
                    print(f"❌ 删除失败 {img_name}: {e}")
            print(f"\n✨ 清理完成！成功删除了 {deleted_count} 张无用图片。")
        else:
            print("\n🚫 操作已取消，未删除任何图片。")
    else:
        print("✅ 扫描完成：所有图片均被正常引用，没有发现无用冗余图片！")

if __name__ == '__main__':
    clean_unused_images()