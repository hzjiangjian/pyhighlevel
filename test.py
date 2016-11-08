# -*- coding: utf-8 -*-

import singleton


class A(object):
	a = 0
	pass


class A1(singleton.SingletonBase):
	pass



class A2(singleton.SingletonBase2):
	a = 0
	pass
	

@singleton.SingletonDecorator
class A3(object):
	pass
	


class A4(singleton.SingletonBase):
	__metaclass__ = singleton.SingletonMetaClass

	pass


if '__main__' == __name__:
	a01 = A()
	a02 = A()
	print a01 == a02

	a01.a = 1
	print a02.a

	a11 = A1()
	a12 = A1()
	print a11 == a12

	a21 = A2()
	a22 = A2()
	print a21 == a22
	a21.a = 1
	print a22.a

	a31 = A3()
	a32 = A3()
	print a31 == a32

	a41 = A4()
	a42 = A4()
	print a41 == a42
	