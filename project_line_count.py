import os

lines_count = 0
for roots, dirs, files in os.walk('.'):
    for file_name in files:
        # print os.path.join(roots, file_name)
        # print file_name[file_name.rfind('.'):]
        if file_name[file_name.rfind('.'):] == '.py':
            count = len(open(os.path.join(roots, file_name), "rU").readlines())
            lines_count += count

print ("all lines count:%d" % lines_count)
