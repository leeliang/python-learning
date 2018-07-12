#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
	print("move({0},{1},{2},{3})".format(n,a,b,c))
	if n == 1:
		print("从 {0} 移动到 {1}".format(a,c))
	else:
		move(n-1, a, c, b) # 借助 c 将 
		move(1, a, b, c)
		move(n-1, b, a, c)

if __name__ == '__main__':
	move(3, 'A', 'B', 'C')