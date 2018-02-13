#Given a URL path for EDGAR 10-K file in.txtformat for a 
#company(CIK) in a year this code will perform word count
import urllib.request as urllib2 #In python 3 urllib2 module has been replaced by urllib.request
import sys
CIK = '1018724'
Year = '2013'
string_match1 = 'edgar/data/1018724/0001193125-13-028520.txt'
url3 = 'https://www.sec.gov/Archives/' + string_match1
#load the page in for the given url in response3
#urllib.request(aka urllib2) is a Python module that can be used for fetching URLs\
response3 = urllib2.urlopen(url3).read()
response4 = response3.decode()
'''sys.stdout = open('test.txt', 'w')
print (response4)'''
#words: list of uncertainty words from Loughran and McDonald (2011)
words=['anticipate','believe','depend','fluctuate','indefinite','likelihood','possible','predict','risk','uncertain']
count = {} # is a dictionary data structure in Python
for elem in words:
    count[elem] = 0
    print (elem)
#The method split() returns a list of all the words in the string
#The split function splits a single string into a string array using #the separator defined.
#If no separator is defined, whitespace is used.
elements = response4.split()
for word in words:
    count[word] = count[word] + elements.count(word)
print (CIK)
print (Year)
print (url3)
print (count)
