import hashlib
import os
import json
from datetime import date
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'
    CEND = '\033[0m'
class Start:
    def run(self,process_name,file_name,project_path,server):
        obj1 = Hash()
        option = process_name
        if(str(option) == 'get'):
            obj1.get_sum(project_path,server)
        if(str(option) == 'compare'):
            obj1.check_sum(file_name,project_path,server)
class Hash:
    def check_sum(self,file_name,project_path,server):
        data_file=file_name
        f = open(data_file)
        data_json = json.load(f)
        for y in project_path:
            server.cwd(y)
            file_list = project_path[y]
            print("[*] Checking "+str(y))
            for x in file_list :
                filename = x
                file_path = str(y)+"/"+str(x)
                with open(filename, "wb") as file:
                    server.retrbinary(f"RETR {filename}", file.write)
                hash_value = hashlib.md5(open(filename,'rb').read()).hexdigest()
                print(style.YELLOW  +"[+] "+str(file_path)+" : "+str(hash_value)+" Old hash ("+data_json[file_path]+")"+style.CEND)
                if(str(hash_value) == str(data_json[file_path])):
                    print(style.GREEN  +"[+] "+str(file_path)+" is safe"+style.CEND)
                else:
                    print(style.RED  + "[-] "+str(file_path)+" is Modified"+style.CEND)
                os.remove(filename)
            print("[*] Checking "+str(y)+" is completed")
    def get_sum(self,project_path,server):
        json_data = {}
        for y in project_path:
            server.cwd(y)
            file_list = project_path[y]
            print("[+] ------"+str(y)+"------")
            for x in file_list :
                filename = x
                file_path = str(y)+"/"+str(x)
                with open(filename, "wb") as file:
                    server.retrbinary(f"RETR {filename}", file.write)
                hash_value = hashlib.md5(open(filename,'rb').read()).hexdigest()
                print("[+] "+str(file_path)+" : "+str(hash_value))
                json_data[file_path] = hash_value
                os.remove(filename)
        file_name_json = today = date.today()
        file_name_json_last = today.strftime("%B %d, %Y")
        with open(str(file_name_json_last), 'w') as outfile:
            json.dump(json_data, outfile)
