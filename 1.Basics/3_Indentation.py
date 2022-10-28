# A block is a combination of all these statements. Block can be regarded as the grouping 
# of statements for a specific purpose. Most of the programming languages like C, C++, and 
# Java use braces { } to define a block of code. 

# One of the distinctive features of Python is 
# its use of indentation to highlight the blocks of code. Whitespace 
# is used for indentation in Python. All statements with the same distance
# to the right belong to the same block of code. If a block has to be more deeply nested, 
# it is simply indented further to the right. 

# Python program showing
# indentation

site = 'nitt.edu'

if site == 'nitt.edu':
	print('Logging on to nitt.edu ...')
else:
	print('retype the URL.')
print('All set !')

# The lines print(‘Logging on to nitt.edu ...) and print(‘retype the URL.’) 
# are two separate code blocks. The two blocks of code in our example if-statement are both indented four spaces. 
# The final print(‘All set!’) is not indented, and so it does not belong to the else-block. 
