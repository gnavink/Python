file_sizes = {name: os.path.getsize(name) for name in os.listdir(".")
if os.path.isfile(name)}