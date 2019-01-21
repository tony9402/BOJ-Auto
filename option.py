import json
import os
import sys

DEFAULT_OPTION_FILE = 'option.json'
ERROR_FORMAT = '\n* ERROR: [%s] [%s]\n'

class Option:

    def __init__(self):
        self.option = ''
        self.source_path = ''

    def get_option(self):
        return self.option

    def set_option(self):
        if not os.path.isfile(DEFAULT_OPTION_FILE):
            print(ERROR_FORMAT % ('set_option', '%s not found' % (DEFAULT_OPTION_FILE)))
            return True
        try:
            self.option = json.loads(open(DEFAULT_OPTION_FILE, 'r').read())
        except json.decoder.JSONDecodeError as e:
            print(ERROR_FORMAT % ('set_option', e))
            return True
        return False

    def Source_path(self):
        if not 'source_path' in self.option:
            return True, ''
        
        return False, self.option["source_path"]
    
    def get_source_path(self):
        if self.source_path == '':
            print(ERROR_FORMAT % ('source_path', 'there is no source_path in %s' % DEFAULT_OPTION_FILE))
            return True, ''
        
        return False, self.source_path
    
    def run(self):
        error = self.set_option()

        if error:
            return True, ''
        
        error, result = self.Source_path()

        self.source_path = result
        return False, result
