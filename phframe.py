import os, random, shutil

srcdir = '/data/pframe'
dstdir = '/media/B466-0C4E'

def main():
    files = os.listdir(srcdir)
    random.shuffle(files)
    for file in files:
        print file
        src = os.path.join(srcdir, file)
        dst = os.path.join(dstdir, file)
        shutil.copyfile(src, dst)

if __name__ == '__main__':
    main()

