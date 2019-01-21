import os
import sys
import getpass
import requests
import re
from bs4 import BeautifulSoup as bs

boj_url = 'https://www.acmicpc.net'

result = {
    '맞았습니다!!',
    '20점','40점','60점','80점','100점',
    '출력 형식이 잘못되었습니다.', '틀렸습니다', '시간 초과',
    '메모리 초과', '출력 초과', '런타임 에러', '컴파일 에러'
}

LANG = {'.c': 0, '.cpp': 88, '.py': 28, '.java': 3, '.txt': 58, '.js': 17, '.php': 7, '.cs': 62,
        '.gs': 79, '.kt': 69, '.swift': 74}

class Boj:

    def __init__(self, sess, path, file):
        self.sess = sess
        self.user_info = {
            'id': '',
            'pw': ''
        }
        self.file_info = {
            'file_name': file[1],
            'problem_number' : file[2],
            'language': '',
            'dir': ''
        }
        self.cookie = ''
        self.option = path
        self.submit_code = ""

    def load_user_data(self):
        with open('./.data/user_boj.dat', 'r') as f:
            data = f.readline().split()
            if len(data) != 2:
                with open('./.data/user_boj.dat', 'w') as f:
                    id_s = input("\nUser ID: ")
                    pw_s = getpass.getpass("User PW: ")
                    f.write(id_s + ' ' + pw_s)
                    self.user_info['id'] = id_s
                    self.user_info['pw'] = pw_s
            else:
                self.user_info['id'] = data[0]
                self.user_info['pw'] = data[1]

    def sign_in(self):
        data = {
            'login_user_id': self.user_info['id'],
            'login_password': self.user_info['pw']
        }
        self.sess.post(boj_url + '/signin', data=data)

        soup = bs(self.sess.get(boj_url).text, 'html.parser')
        if soup.find('a', {'class':'username'}) is None:
            with open('./.data/user_boj.dat', 'w') as f:
                f.write('')
            return True, 'Login failed : Invalid ID or Password'
        
        return False, ''
        
    def submit(self):
        problem_number = self.file_info['problem_number']
        soup = bs(self.sess.get(boj_url + "/submit/" + problem_number).text, 'html.parser')

        try:
            key = soup.find('input', {'name': 'csrf_key'})['value']
        except TypeError:
            print("잘못된 문제 번호입니다.")
            return True
        
        language = self.file_info['language']
        
        if not language in LANG:
            print("지원하지 않는 코드입니다.")
            return True
        language_code = LANG[language]
        
        data = {
            'problem_id': problem_number,
            'source': self.submit_code,
            'language': language_code,
            'code_open': 'onlyaccepted',
            'csrf_key': key
        }
        self.sess.post(boj_url + '/submit/' + problem_number, data=data)
    
    def print_result(self):
        done = False
        problem_number = self.file_info['problem_number']
        while not done:
            url = boj_url + '/status?from_mine=1&problem_id=' + problem_number + '&user_id' + self.user_info['id']
            soup = bs(self.sess.get(url).text, 'html.parser')
            text = soup.find('span', {'class': 'result-text'}).find('span').string.strip()
            print("\r                         ", end='')
            print('\r%s' % text, end='')
            if text in result:
                done = True
        print()
        return text == '맞았습니다!!'
    
    def set_info(self):
        info = self.file_info['problem_number']
        lang = self.file_info['file_name'].split('.')
        self.file_info['language'] = '.' + lang[1]
        num = int(info)
        num = int(num / 100)
        num = int(num * 100)
        self.file_info['dir'] = str(num)

    def load_code(self):
        path = self.option + self.file_info['file_name']
        with open(path, 'r') as f:
            self.submit_code = f.read()

    def run(self):
        self.set_info()
        
        self.load_user_data()
        error, result = self.sign_in()

        if error:
            print(' * ERROR : [%s] [%s]' % ('login', result))
            return True

        self.load_code()
        print("loaded")
        self.submit()
        result = self.print_result()

        if result: #result == '맞았습니다!!'
            return False
        else:
            return True
        
