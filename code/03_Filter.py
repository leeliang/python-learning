#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return True

if __name__ == '__main__':
	print(list(filter(is_palindrome, range(1, 200))))