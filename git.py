import sys
import os
import subprocess

repo_url = 'https://github.com/%s/%s'

class Git:

    def __init__(self, boj):
        self.user_id = None
        self.repo_name = None
        self.pipe = subprocess.PIPE
        self.mkdir = ''
        self.boj = boj
        self.file_path = ''
        self.problem_number = ''
        self.file_name = ''
    
    def load_user_data(self):
        with open('./.data/user_git.dat', 'r') as f:
            data = f.readline().split()
            if len(data) != 2:
                with open('./.data/user_git.dat', 'w') as f:
                    id_s = input("\nUser Github ID: ")
                    repo_name = input("repo name: ")
                    f.write(id_s + ' ' + repo_name)
                    self.user_id = id_s
                    self.repo_name = repo_name
            else:
                self.user_id = data[0]
                self.repo_name = data[1]
    
    def set_mkdir(self):
        self.mkdir = self.boj.file_info['dir']
        self.problem_number = self.boj.file_info['problem_number']
        self.file_name = self.boj.file_info['problem_number']+self.boj.file_info['language']
    
    def clone(self):

        if os.path.isdir(self.repo_name):
            return False, "Repository '%s' already exists." % (self.repo_name)
        
        url = repo_url % (self.user_id, self.repo_name)
        command = ['git', 'clone', url]

        proc = subprocess.Popen(command, stdout=self.pipe, stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'
    
    def pull(self):
        url = repo_url % (self.user_id, self.repo_name)
        cwd = self.repo_name
        command = ['git','pull']

        proc = subprocess.Popen(command, cwd=cwd, stdout=self.pipe, stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'
    
    def add(self):
        cwd = self.repo_name
        command = ['git','add','.']

        proc = subprocess.Popen(command, cwd=cwd, stdout=self.pipe, stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'
    
    def commit(self):
        cwd = self.repo_name
        command = ['git','commit','-m',str(self.problem_number)]

        proc = subprocess.Popen(command, cwd=cwd, stdout=self.pipe, stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'
    
    def push(self):
        cwd = self.repo_name
        command = ['git','push','-u','origin','master']

        proc = subprocess.Popen(command, cwd=cwd, stdout=self.pipe, stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'
    
    def remote(self):
        cwd = self.repo_name
        url = repo_url % (self.user_id, self.repo_name) + '.git'
        command = ['git','remote','add','origin',url]

        proc = subprocess.Popen(command, cwd=cwd,stdout=self.pipe,stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'

    def init(self):
        cwd = self.repo_name
        command = ['git','init']

        proc = subprocess.Popen(command, cwd=cwd,stdout=self.pipe,stderr=self.pipe)
        stdout, stderr = proc.communicate()

        if not stdout is None:
            print(stdout.decode())
        if not stderr is None:
            print(stderr.decode())
        if proc.returncode != 0:
            return True, str(proc.returncode)
        
        return False, 'done'

    def save_file(self):
        path2 = '%s/%s' % (self.repo_name, self.boj.file_info['dir'])
        path = path2 + '/%s' % self.file_name
        if not os.path.isdir(path2):
            os.makedirs(path2)

        with open(path, 'w') as f:
            f.write(self.boj.submit_code)
    
    def run(self):
        self.load_user_data()
        self.pull()
        self.set_mkdir()

        print(self.repo_name)

        if not os.path.isdir(self.repo_name):
            error, result = self.clone()
            if error:
                return True, result
            print(result)
            error, result = self.init()
            if error:
                return True, result
            print(result)
        
        self.save_file()

        error, result = self.add()

        if error:
            print("Error add")
            return True, result
        
        error, result = self.commit()

        if error:
            print("Error commit")
            return True, result

        error, result = self.push()

        if error:
            print("Error push")
            return True, result
        
        return False, 'done'

