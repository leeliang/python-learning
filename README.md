# Tabel of Contents

=========
* [1 汉诺塔](#1汉诺塔)
* [2 切片去除字符首位空格](#2切片去除字符首位空格)
* [3 杨辉三角](#3杨辉三角)
* [4 过滤回数](#4过滤回数)

=========

## 1.汉诺塔
递归函数需要考虑的问题有两个：

* `n==1` 时的处理；
* `n` 与 `n-1` 的关系。

考虑 `n==1` 的情况，汉诺塔问题的解决方案为直接移动过去。
``` python
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c)
```

怎么考虑`n` 与 `n-1` 的关系呢，先考虑简单情况 `n==2`。
> move(2, a, b, c) = move(1, a, c, b) + move(1, a, c, c) + move(1, b, a, c)

`n` 变成 `n-1` 的关键在于把最大的盘子移到 C，如果最大的盘子在盘子在 C，这个盘子就可以不用移动了，问题就从 `n` 变成 `n-1`。
> move(n, a, b, c) = move(1, a, b, c) + ?

如果需要最大的盘子能够从 A 移到 C，需要先将 A 上边的 `n-1` 个盘子移到 B。
> move(n, a, b, c) = move(n-1, a, c, b) + move(1, a, b, c) + ?

不需要关心 `move(n-1, a, c, b)` 是怎么操作的，只需要找到 `n` 与 `n-1` 的关系，所有的问题都能够递归为 `n == 1` 的问题，而 `n == 1` 的问题已经给出了解决方案。做完上述两步操作，现在的情况是 A 上没有盘子， B 有 n-1 个盘子，C 有最大的盘子。最终需要将 B 上的盘子移到 C。
> move(n, a, b, c) = move(n-1, a, c, b) + move(1, a, b, c) + move(n-1, b, a, c)

即 `n` 与 `n-1` 的关系为：`n` 的问题可以转换为两个 `n-1` 的问题和 `n==1` 的问题。
``` python
def move(n, a, b, c):
    if n == 1:
        print('move', a, '--->', c) # 一个盘子从 a 到 c
    else:
        move(n-1, a, c, b)   #  先把 a 上面n-1个盘子移到 b
        move(1, a, b, c)   # 把最大的盘子移到 c
        move(n-1, b, a, c) # 把 b 上的 n-1 个盘子移到 c
```

## 2.切片去除字符首位空格
直接判断首尾是否是空格，是空格就利用切片切掉。可以采用循环来处理多个空格的情况。如熟悉递归函数，递归函数处理最简练。

* 如果首尾都不是空格，直接返回字符；
* 如果首不是空格，利用切片去掉首字符重新交给trim处理；
* 如果上述两种都不是，只能是尾部有空格。

``` python
def trim(s):
    if s[:1] != ' ' and s[-1:] != ' ':
        return s
    elif s[:1] == ' ':
        return trim(s[1:])
    else：
        return trim(s[:-1])
```


## 3.杨辉三角
杨辉三角的两边为 1，中间的元素为上一行的相邻元素相加。
```python
def triangles():
	a = [1]
	while True:
		yield a
		a = [1] + [ a[i]+a[i+1] for i in range(len(a)-1) ] + [1]
```


## 4.过滤回数
将数字变为字符，并利用切片反转字符，若相等则为回数。

切片原理： [begin:end:step]，当 step<0 时，表示从右往左切。
```python
def is_palindrome(n):
	if str(n) == str(n)[::-1]:
		return True

if __name__ == '__main__':
	print(list(filter(is_palindrome, range(1, 200))))
```