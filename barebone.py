import os

store_dir = './dist/files'
with os.scandir(store_dir) as files:
    for file in files:
        path = os.path.join(file)
        os.system("lowriter -p %s" % path)
        os.remove(path)
