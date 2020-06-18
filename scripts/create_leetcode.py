
#!/usr/bin/env python3
# -*- coding:utf-8 -*-
####################################
#author        terry.li
#date          18/06/2020
#version       1.0.0
#description   Create the post              
####################################

import sys
import argparse

def cmdline_args():
        # Make parser object
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    
    parser.add_argument('-t', '--type', dest='type', 
        choices=['contest', 'liner', 'nonliner', 'dp' ,'other'], 
        type=str, 
        required=True,
        help='the types of leetcode [contest, liner, nonliner, dp, other]')
    parser.add_argument('-n', '--name', required=True, dest='name', type=str, help='file name')
    parser.add_argument('--title', dest='title',required=False, default="", type=str, help='leetcode title')
    parser.add_argument('-i', '--id', dest='id',required=False, default="", type=str, help='id')
    parser.add_argument('-l', '--level', dest='level',required=False, 
        default="", 
        type=str,
        choices=['h', 'm', 'e'],  
        help='level')

    return(parser.parse_args())


if __name__ == '__main__':

    try:
        args = cmdline_args()
        if args.type == 'contest':
            path = 'contest'
        elif args.type == 'liner':
            path = 'liner-data-structure'
        elif args.type == 'nonliner':
            path = 'nonliner-data-structure'
        elif args.type == 'dp':
            path = 'dp'
        else:
            path = 'other'

        level = ''
        if args.level == 'e':
            level = 'Easy'
        elif args.level == 'm':
            level = 'Medium'
        elif args.level == 'h':
            level = 'Hard'

        filename = args.name + '.md'
        f = open('./_leetcode-' + path + '/' + filename, 'a' ,encoding='utf_8')
        f.write(f"""---
layout: default
title: {args.title}
---

## [{args.id}\. {args.title}](https://leetcode-cn.com/problems/{args.name}/)

> {level}

#### 思路

#### 代码""")
        f.close()
        print("create file success!!!")
        print("-----------")
        print(f"|{args.id}|[{args.title}](https://leetcode-cn.com/problems/{args.name}/)|{level}||[查看](./{path}/{args.name})|")
        print("-----------")

    except Exception as e:
        print(e)

    print()