#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else:
    	return trim(s[:-1])

if __name__ == '__main__':   
	if trim('hello  ') != 'hello':
		print('测试失败!')
	elif trim('  hello') != 'hello':
		print('测试失败!')
	elif trim('  hello  ') != 'hello':
		print('测试失败!')
	elif trim('  hello  world  ') != 'hello  world':
		print('测试失败!')
	elif trim('') != '':
		print('测试失败!')
	elif trim('    ') != '':
		print('测试失败!')
	else:
		print('测试成功!')