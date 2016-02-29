# -*- encoding: utf-8 -*-
# Author: Epix
import os
import pickle
import re
import shutil


def mv(i, o):
    if os.path.isdir(o):
        print(o)
    else:
        shutil.move(i, o)


if __name__ == '__main__':
    rj_re = re.compile(r'RJ\d*')
    db = pickle.load(open('db.pkl', 'rb'))
    input_path = u'.'
    dirs = [f for f in os.listdir(input_path) if os.path.isdir(os.path.join(input_path, f))]
    for d in dirs:
        try:
            match_rj = rj_re.search(d).group()
            output_name = '[%s] %s %s' % (db[match_rj][1], db[match_rj][0], match_rj)
            filtered_output_name = (''.join([i for i in output_name if i not in r"/\\:*?\"<>|"])).strip()
            mv(os.path.join(input_path, d), os.path.join(input_path, filtered_output_name))
        except:
            print(os.path.join(input_path, d))
