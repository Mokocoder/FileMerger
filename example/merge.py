def merge_files(file_name, save_file_name):
    i = 1
    with open(save_file_name, 'wb') as f:
        while True:
            try:
                with open(file_name + '.part' + str(i), 'rb') as chunk_file:
                    chunk = chunk_file.read()
                    f.write(chunk)
                i += 1
            except FileNotFoundError:
                break

merge_files('원본.txt','복구본.txt')