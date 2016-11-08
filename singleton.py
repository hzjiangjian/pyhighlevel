# -*- coding: utf-8 -*-

'''
method 1
'''
class SingletonBase(object):
	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			cls._instance = super(SingletonBase, cls).__new__(cls, *args, **kw)

		return cls._instance


'''
method 2
'''
class SingletonBase2(object):
	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_state'):
			cls._state = {}

		ins = super(SingletonBase2, cls).__new__(cls, *args, **kw)
		ins.__dict__ = cls._state

		return ins


'''
method3
'''
def SingletonDecorator(cls, *args, **kw):
	instance = {}

	def singleton():
		if cls not in instance:
			instance[cls] = cls(*args, **kw)

		return instance[cls]

	return singleton


'''
method4
'''
class SingletonMetaClass(type):
	def __init__(cls, name, bases, dic):  
		super(SingletonMetaClass, cls).__init__(name, bases, dic)

		cls._instance = None  

	def __call__(cls, *args, **kw):  
		if cls._instance is None:  
			cls._instance = super(SingletonMetaClass, cls).__call__(*args, **kw)  

		return cls._instance  















