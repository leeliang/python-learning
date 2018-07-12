# 备忘录
***
## 1 函数的参数
```python
def person(name, age=10, *args, **kw, *, city, job):
    pass
```
分别为必选参数、默认参数、可变参数、关键字参数和命名关键字参数。
*  可变参数：参数个数可变，仅需传入参数值；
*  关键字参数：传入参数名和值；
*  命名关键字参数：传入指定的参数名和值。



