#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 14, 2014

@author: anroco

How working operators + and * with string in python?

Como funciona el operador + y * con los string en python?
'''

#create a str
s = 'hello'
print (s)

#The * operator allow repeat the str
print(s * 5)

#create two str
s1 = 'hello '
s2 = 'world'

#The + operator allow create a str joining two or more strigs
s = s1 + s2
print(s)

#create a string combining operators
s = 'by' + 'e' * 6 + '!'
print(s)
