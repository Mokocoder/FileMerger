def split_file(file_name, num_parts):
    with open(file_name, 'rb') as f:
        content = f.read()

    part_len = len(content) // num_parts
    parts = [content[i*part_len:(i+1)*part_len] for i in range(num_parts)]
    parts[-1] += content[num_parts*part_len:]  # 마지막에 남은 부분을 마지막 파트에 추가
    
    for i, part in enumerate(parts):
        with open(f'{file_name}.part{i+1}', 'wb') as f:
            f.write(part)

split_file('원본.txt', 4)