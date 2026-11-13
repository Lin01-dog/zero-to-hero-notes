import json
import base64
import os
import re

# 获取当前脚本所在的绝对路径，确保万无一失
script_dir = os.path.dirname(os.path.abspath(__file__))
notebook_path = os.path.join(script_dir, 'practice.ipynb')
output_img_dir = os.path.join(script_dir, 'images')

print(f"正在读取文件: {notebook_path}")

if not os.path.exists(output_img_dir):
    os.makedirs(output_img_dir)

with open(notebook_path, 'r', encoding='utf-8') as f:
    nb_data = json.load(f)

image_counter = 1

def save_image(b64_data, ext='png'):
    global image_counter
    # 清理多余空格和换行
    b64_data = re.sub(r'\s+', '', b64_data)
    
    img_filename = f"img_{image_counter}.{ext}"
    img_path = os.path.join(output_img_dir, img_filename)
    
    try:
        img_bytes = base64.b64decode(b64_data)
        with open(img_path, 'wb') as f:
            f.write(img_bytes)
        print(f"✅ [成功提取图片 {image_counter}] 保存至: images/{img_filename}")
        image_counter += 1
        return f"./images/{img_filename}"
    except Exception as e:
        print(f"❌ 解码图片 {image_counter} 失败: {e}")
        return None

cells_processed = 0

for cell in nb_data.get('cells', []):
    cell_type = cell.get('cell_type')
    
    # 1. 扫描 Markdown 单元格
    if cell_type == 'markdown':
        source = "".join(cell.get('source', []))
        
        # 兼容匹配各种 data:image 格式 (png, jpeg, jpg, webp, svg 等)
        pattern = r'!\[(.*?)\]\(data:image\/(png|jpeg|jpg|webp|svg\+xml);base64,([A-Za-z0-9+\/=\s]+)\)'
        
        def repl(match):
            alt_text = match.group(1) or "image"
            ext = match.group(2).replace('svg+xml', 'svg')
            b64_str = match.group(3)
            new_rel_path = save_image(b64_str, ext)
            if new_rel_path:
                return f"![{alt_text}]({new_rel_path})"
            return match.group(0)

        new_source = re.sub(pattern, repl, source)
        cell['source'] = [new_source]

    # 2. 扫描 attachments 类型的附件图片
    if 'attachments' in cell:
        for att_key, att_val in list(cell['attachments'].items()):
            for mime_type, base64_data in att_val.items():
                if 'image' in mime_type:
                    ext = mime_type.split('/')[-1].replace('svg+xml', 'svg')
                    if isinstance(base64_data, list):
                        base64_data = "".join(base64_data)
                    
                    new_rel_path = save_image(base64_data, ext)
                    if new_rel_path and cell_type == 'markdown':
                        source_text = "".join(cell.get('source', []))
                        source_text = source_text.replace(f"attachment:{att_key}", new_rel_path)
                        cell['source'] = [source_text]
        del cell['attachments']
    
    cells_processed += 1

# 保存修改后的 Notebook
cleaned_notebook_path = os.path.join(script_dir, 'practice_cleaned.ipynb')
with open(cleaned_notebook_path, 'w', encoding='utf-8') as f:
    json.dump(nb_data, f, ensure_ascii=False, indent=2)

print("\n-------------------------------------------")
if image_counter > 1:
    print(f"🎉 瘦身大成功！共提取了 {image_counter - 1} 张图片到 images 文件夹。")
    print(f"📁 瘦身后的新文件已生成: practice_cleaned.ipynb")
else:
    print("⚠️ 提示：未在当前文件中找到 Base64 格式的图片，请检查图片是否是其他嵌套方式。")
print("-------------------------------------------")