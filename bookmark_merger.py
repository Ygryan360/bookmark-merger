import io
from bookmark_helper import *

first_file_name = input('Enter first file name, including extension: ')
second_file_name = input('Enter second file name, including extension: ')

first_file  = open(first_file_name, 'r')
second_file = open(second_file_name, 'r')

first_file_header  = first_file.readline()
second_file_header = second_file.readline()

if not test_header(first_file_header) or not test_header(second_file_header):
    print('Files are not bookmark files')
    exit()

f_list = list(first_file)
s_list = list(second_file)

first_file.close()
second_file.close()

first_bookmarks, first_folders   = create_list(f_list)
second_bookmarks, second_folders = create_list(s_list)

all_bookmarks = first_bookmarks + second_bookmarks
all_folders = first_folders + second_folders

# Deduplicate bookmarks
bookmark_dict = {}
for bm in all_bookmarks:
    if bm.url not in bookmark_dict or bm.date > bookmark_dict[bm.url].date:
        bookmark_dict[bm.url] = bm

deduplicated_bookmarks = list(bookmark_dict.values())

folder_set = set(all_folders)

ordered_bookmark_list = sorted(deduplicated_bookmarks, key=get_date)

separated_by_folders = []

for folder in folder_set:
    separated_by_folders.append('    <DT><H3>' + folder + '</H3>\n')
    folder_bookmarks = [bm.line for bm in ordered_bookmark_list if bm.folder == folder]
    separated_by_folders.extend(folder_bookmarks)

new_file = open('merged_bookmarks.html', 'w')
new_file.write(header)

for line in separated_by_folders:
    new_file.write(line)

new_file.close()
exit()
