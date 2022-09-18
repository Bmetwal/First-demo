import os
from datetime import datetime
import pprint
#print (dir (os))
print (os.getcwd())
#os.chdir('\Users\Badaw\PycharmProjects\infopro\venv\')

#print(os.listdir())
#os.mkdirs("os_demot\sub_dir_1")
#os.rmdir('')
#os.removedirs("")
#os.rename ("original.txt","new.txt")
#os.state("original.txt".st_mtime)  file status properties
#os.state("original.txt".size) file status properties
#mode_time= os.stat('original.txt').st_mtime
#print(datetime.fromtimestamp(mod_time))


for dirpath , dirnames , filenames in os.walk('/Users/Badaw/PycharmProjects/infopro/'):
    print ("current path " , dirpath)
    print ("Directory :", dirnames)
    print ("files :", filenames)
    print ()

#print(os.environ.get)

print(os.environ.get("COMPUTERNAME"))
print(os.environ.get('HOMEPATH'))

#file_path = os.path.join(os.environ.get('HOMEPATH'),'test.txt')
#print (file_path)

#print(os.path.basename('/tmp/test.txt'))
#os.path.exists
#os.path.isdir
#os.path.isfile
#os.path.splitext will split the file from the extenstion
#print (dir(os.path))
