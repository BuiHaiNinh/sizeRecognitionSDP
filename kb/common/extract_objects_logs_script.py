# Using readlines()
file1 = open('../logs/extract_objects_logs', 'r')
lines = file1.readlines()

error_files = []
prev = None
for line in lines:
    if 'Error!' in line:
        error_files.append(prev)

    prev = line

with open('../logs/objects_extraction_error_files.txt', 'w') as f:
    for item in error_files:
        f.write("%s" % item)
