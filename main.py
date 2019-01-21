import sys
import os
import getpass
import requests
import json
import time
from boj import Boj
from option import Option
from git import Git

sess = requests.Session()

if __name__ == "__main__":
    #python main.py 1000.cpp 1000 | python main.py filename problem_number
    if len(sys.argv) != 3:
        print("\nError Input")
        print("ex) python main.py (filename) (problem number)\n")
        exit(1)

    option = Option()
    error, result = Option().run()
    if error:
        exit(1)

    boj = Boj(sess, result, sys.argv)
    result = boj.run()
    
    if result:
        print("Wrong Answer")
        exit(2)
    
    git = Git(boj)
    error, result = git.run()
    if error:
        print(result)
        exit(1)
    
    print("finished")
