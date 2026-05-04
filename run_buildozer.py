#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import os

# 添加用户 site-packages 路径
sys.path.insert(0, '/Users/beibeiqi/Library/Python/3.9/lib/python/site-packages')

# 设置环境变量
os.environ['PYTHONPATH'] = '/Users/beibeiqi/Library/Python/3.9/lib/python/site-packages'

# 导入并运行 buildozer
from buildozer.scripts.client import main
if __name__ == '__main__':
    sys.argv = ['buildozer', '-v', 'android', 'debug']
    main()
