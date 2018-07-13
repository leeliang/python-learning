#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def triangles():
	a = [1]
	while True:
		yield a
		a = [1] + [ a[i]+a[i+1] for i in range(len(a)-1) ] + [1]

if __name__ == '__main__':   
	f = triangles()
	for i in range(4):
		print(next(f))