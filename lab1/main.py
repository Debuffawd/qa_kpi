# -*- coding: utf-8 -*-


from directory import Directory

from binary_file import BinaryFile

from log_text_file import LogTextFile

from buffer_file import BufferFile




root = Directory('root', 100)

child_dir1 = Directory('child_dir1', 10, root)

child_dir2 = Directory('child_dir2', 5, child_dir1)




bin_file1 = BinaryFile(child_dir2, 'file1', 'text info')

bin_file2 = BinaryFile(root, 'file2', 'another text info')




log_file1 = LogTextFile(child_dir1, 'file3', 'first line')

log_file2 = LogTextFile(child_dir2, 'file4', 'foo')

log_file1.append_line('second line')

print(log_file1.read())




buf_file1 = BufferFile(root, 10, 'file5')

buf_file2 = BufferFile(child_dir1, 20, 'file6')




buf_file2.move(child_dir2)




print(root.list_elems())

