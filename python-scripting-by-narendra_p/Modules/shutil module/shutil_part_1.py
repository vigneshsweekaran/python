#!/usr/local/bin/python3
import shutil
#copy', 'copy2', 'copyfile', 'copyfileobj', 'copymode', 'copystat', 'copytree'

#copyfile-->copy --> copy2
#src="/home/Automation/working_with_remote_server.py"
src="/home/Automation/shutil_part_1.py"
dest="/home/Automation/working_with_remote_server.py_bkp"
#shutil.copyfile(src,dest)       # Copy the file with new timestamp and default permissions
#shutil.copy(src,dest)   # copy the file with src permissions
#shutil.copy2(src,dest)   # same metadata(permissions and timestamp) for dest as well
#shutil.copymode(src,dest)
#shutil.copystat(src,dest)

#f1=open('xyz.txt','r')
#f2=open('pqr.txt','w')
#shutil.copyfileobj(f1,f2)

#src="/home/Automation/tomcat7"
#shutil.copytree(src,'/tmp/tomcat')

shutil.rmtree('/tmp/tomcat')