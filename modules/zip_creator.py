import zipfile
import pathlib

def make_zip(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, 'compressed.zip')
    with zipfile.ZipFile(dest_path, 'w') as zip:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            zip.write(filepath, arcname=filepath.name)

if __name__ == '__main__':
    make_zip(filepaths=[
        'C:/Users/mrnrz/Desktop/photo/Austria/IMG_20171005_110040.jpg',
        'C:/Users/mrnrz/Desktop/photo/Austria/IMG_20171005_110719.jpg',
        'C:/Users/mrnrz/Desktop/photo/Austria/IMG_20171005_115239.jpg'],
             dest_dir='C:/Users/mrnrz/Desktop/photo')