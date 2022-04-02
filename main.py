
import os
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import shutil

if __name__ == '__main__':

    file_names = os.listdir('files')

    file_names.sort()
    #print(len(file_names))

    count = 5580
    #os.rename('files/a.txt', 'b.kml')
    for i in range(45):
        for each_file in file_names:
            path_with_name = 'files/'+each_file
            print(path_with_name)
            new_name = 'files_all/frame_' + str(count) + '.png'
            print(new_name)
            count = count - 1

            shutil.copy(path_with_name, new_name)
    print(file_names)