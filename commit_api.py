import requests
from urllib import request
import lizard
from utils.utils import Utils
import os

merge_file = []
commit_file_data = []
counter = 0
changed_lines = 0
file_dict_critical = {}
file_dict1_non_critical = {}
config = Utils().get_config_file('config.ini')
user_id = config.get('GithubCredential', 'user_id', raw=True)
password = config.get('GithubCredential', 'password')
#user_id = config.get('GithubCredential', 'user_id1', raw=True)
#password = config.get('GithubCredential', 'password1')
requests_commit = config.get('commit_api', 'commit_url')
requests_merged = config.get('merge_api', 'merge_url')
res_commit_api = requests.get(requests_commit, auth=(user_id, password)).json()
res_merge_files = requests.get(requests_merged, auth=(user_id, password))
temp_dir_complexity = config.get('temp_directory', 'temp_dir')


class commit:
    def commit_files(self, file_name1, count, filename=None):
        # print (file_name1)
        for j in res_commit_api['files']:
            if j['filename'] == file_name1:
                raw_url = ((j['raw_url']))
                response = request.urlopen(raw_url)
                data_file = (response.read())
                data_file = data_file.decode()
                commit_file_data.append(data_file)
                self.lines_data = commit_file_data[count].rsplit('\n')

    def lizard(self, file_name1):
        print(file_name1)
        for j in res_commit_api['files']:
            if j['filename'] == file_name1:
                x = ((j['raw_url']))
                filename, file_extension = os.path.splitext(x)
                # print(filename +' '+ file_extension)
                response = request.urlopen(x)
                html = response.read()
                html = html.decode()
                full_path = temp_dir_complexity + file_extension
                with open(full_path, 'w') as f:
                    print(html, file=f)
                i = lizard.analyze_file(full_path)
                print(i.__dict__)
        try:
            self.temp1 = i.function_list
            os.remove(full_path)
        except:
            print('Code not generic so no complexity')
            pass

    def repo_files(self, file_name1):
        res2 = requests.get(requests_merged + "/" + file_name1, auth=(user_id, password))
        for j in res2:
            merge_file.append(j.decode())
        self.merge_file_lines = merge_file[0].rsplit('\n')

    def cmp_file(self, file):
        nonchanged_lines = 0
        if len(self.lines_data) < len(self.merge_file_lines):
            i = len(self.lines_data)
        else:
            i = len(self.merge_file_lines)

        for j in self.lines_data:
            for i in self.merge_file_lines:
                if j == i:
                    if j == '' or i == '':
                        pass
                    else:
                        nonchanged_lines += 1
                else:
                    pass
        perc_change_files = ((len(self.lines_data) - nonchanged_lines)/(len(self.merge_file_lines) - nonchanged_lines))*100
        del self.lines_data[:]
        if perc_change_files > 50:
            ret_val = []
            ret_val.append("critical")
            ret_val.append(self.temp1)
            file_dict_critical[file] = ret_val
        else:
            file_dict1_non_critical[file] = "Not-Critical"
            file_dict_critical[file] = self.temp1


class api_call(commit):
    file_names = []
    count = 0

    def postman(self):
        #print ("hi")
        for j in res_commit_api['files']:
            self.file_names.append(j['filename'])
        class_obj = commit()
        for j in self.file_names:
            class_obj.commit_files(j, self.count)
            self.count += 1
            class_obj.repo_files(j)
            class_obj.lizard(j)
            class_obj.cmp_file(j)

    def critical_files(self):
        print(file_dict_critical)
        return (file_dict_critical)

if __name__ == "__main__":

    apicall_obj = api_call()
    apicall_obj.postman()
    apicall_obj.critical_files()
