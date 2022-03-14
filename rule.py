import ftplib
import hasher
server = ftplib.FTP()
server.connect('192.168.0.0', 21)
server.login('user','password')
project_path = {'/public_html/alter_test':['index.php']}
object_start = hasher.Start()
#object_start.run('get',0,project_path,server)
object_start.run('compare','March 14, 2022',project_path,server)
