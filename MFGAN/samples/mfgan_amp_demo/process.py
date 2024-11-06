import re

# 定义输入和输出文件路径
input_file_path = 'sampled_1_preds.txt'
output_file_path = 'processed_sampled__preds.txt'

# 打开输入文件和输出文件
with open(input_file_path, 'r') as infile, open(output_file_path, 'w') as outfile:
    # 逐行读取文件
    for line_number, line in enumerate(infile, start=1):
        # 删除所有的'P'和数字
        cleaned_line = re.sub('[P\d]', '', line)

        # 在行前添加行号标记
        marked_line = f'>s{line_number} {cleaned_line}'

        # 写入到输出文件
        outfile.write(marked_line)

print('文件处理完成，结果已保存到:', output_file_path)