# -*- coding:utf-8 -*-

import sys
import os
from os.path import abspath, dirname, join

BASE_DIR = dirname(dirname(abspath(__file__)))
os.chdir(BASE_DIR)
sys.path.insert(0, BASE_DIR)

sys.path.append('..')
