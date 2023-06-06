import gzip

def compress_file(input_path, output_path):
    with open(input_path, 'rb') as file_in:
        with gzip.open(output_path, 'wb') as file_out:
            file_out.writelines(file_in)

# Example usage
input_file_path = 'D:\\offline-translator\\translation_models\\en_ja\\model\\model.bin'
compressed_file_path = 'D:\\offline-translator\\translation_models\\en_ja\\model\\compressed_model.bin.gz'

compress_file(input_file_path, compressed_file_path)
