# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 10:20:55 2018

@author: mingyang.wang
"""

import os
import numpy as np

class LoadProcess():
    """加载、处理数据"""
    def load_seq(self, file_path, encoding='utf-8', lang_type='eng'):
        """读取文件，返回切分后的列表"""
        try:
            with open(file_path, encoding=encoding) as f:
                lines = f.readlines()
                if lang_type == 'eng':
                    data = [list(line.strip().lower().split(' ')) for line in lines]
                elif lang_type == 'ch':
                    data = [list(line.strip()) for line in lines]
                else:
                    print('Don’t support this language!')
        except:
            print('Load sequence error!')
        return data, len(lines)
        
    def data_preprocess(self, src_train_path, tgt_train_path):
        src_
        
        
file_path = 'E:\\data\\translate\\transformer_1107\\1108.txt'
data1 = LoadProcess()
print(data1.load_seq(file_path, encoding='gbk', lang_type='ch'))