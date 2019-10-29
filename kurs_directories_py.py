import os.path
os.chdir("/home/alex/Downloads/")

for current_dir, dirs, files in os.walk("main"):
    for file in files:
        if file[-3:] == ".py":
            print(current_dir)
            break

