## Regular Expression: re######

#A regular expression in a programming language is a special text string used for describing a search pattern. It is extremely useful for extracting information from text such as code, files, log, spreadsheets or even documents.#

#Regular expressions are used to identify whether a pattern exists in a given sequence of characters (string) or not. They help in manipulating textual data, which is often a pre-requisite for data science projects that involve text mining. You must have come across some application of regular expressions: they are used at the server side to validate the format of email addresses or password during registration, used for parsing text data files to find, replace or delete certain string, etc.

#RE can be used in Natural language processing in supervised learning.

#################################
# Methods:
#findall, search and match
#rx return the match if found else return None.
#rx.match() : returns a match object. But the difference is, it requires the pattern to be present at the beginning of the text itself.

#rx.search():  searches for the pattern in a given text. Not neccesary to be at first but only one occurance will be returend. 

# rx.findall(): which returns the matched portions of the text as a list. All ocurance will be return.

#rx.sub(): substitue one test with another, like find and replace.
# You can control the number of replacements by specifying the count parameter:

# .group() : will conslidate the output in exact string group.


import re
match='ab'
string="""abcdegfgd sadjhjsad asdjhhsdf
dfjhjhdsf
abcdsdg
"""
text1='abc pqr abc abcdef pqrabc'
#re.match('ab',string) # span=(0, 2)
#re.match('ab',string).group() # return first occurance and group the element.
#print(re.match('cd',string)) #None as this match is in between the string. and match function only search the pattern in satrt of string.
#print(re.match('sa',string)) #None as this match is in between the string.
#print(re.search('cd',string)) # span=(2, 4) , search will return the first occurance of the match in the string, same as find.
#print(re.search('sa',string)) # span=(10, 12) , search will return the first occurance of the match in the string, same as find.
print(re.findall('cd',string)) #['cd', 'cd'], will return the list if occurance found , All occurnace. 
print(re.findall('sa',string)) # ['sa', 'sa'],
print(text1)
print(re.sub('abc','xyz', text1)) # will replace all the occurnace of abc with pqr.only on the fly change will happen and not the actual variable will change as string is immutable.
print(re.sub('abc','xyz', text1,2))# will only replace 2 occurnace os abc with xyz
print(x)
print(text1)

# two different syntax for regular expression.
import re  
text = """101 COM    Computers
205 MAT   Mathematics
189 COM   English"""  
regex = re.compile('COM')
regex.findall(text) # syntax 1  
# or
re.findall('COM', text) # syntax 2


#######################
"""BASIC SYNTAX

.             One character except new line
\.            A period. \ escapes a special character.
\d            One digit
\D            One non-digit
\w            One word character including digits
\W            One non-word character
\s            One whitespace
\S            One non-whitespace	
\n            Newline
\t            Tab
\A	          Returns a match if the specified characters are at the beginning of the string	"\AThe"
\B	Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word	r"\Bain"
r"ain\B"	
\b            Word boundary, Returns a match where the specified characters are at the beginning or at the end of a word	r"\bain"
r"ain\b"	
\Z	Returns a match if the specified characters are at the end of the string	"Spain\Z"	


MODIFIERS

$             End of string
^             Start of string
ab|cd         Matches ab or de. Either or. 
[ab-d]	      One character of: a, b, c, d
[^ab-d]	      One character except: a, b, c, d
()            Items within parenthesis are retrieved. Capture and group
(a(bc))       Items within the sub-parenthesis are retrieved

# Example of set []:
[arn]	Returns a match where one of the specified characters (a, r, or n) are present	
[a-n]	Returns a match for any lower case character, alphabetically between a and n	
[^arn]	Returns a match for any character EXCEPT a, r, and n	
[0123]	Returns a match where any of the specified digits (0, 1, 2, or 3) are present	
[0-9]	Returns a match for any digit between 0 and 9	
[0-5][0-9]	Returns a match for any two-digit numbers from 00 till 59	
[a-zA-Z0-9]	Returns a match for any character alphabetically between a and z, lower case OR upper case	and any digit between 0 to 9.
[+]	In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string


REPETITIONS

[ab]{2}       Exactly 2 continuous occurrences of a or b
[ab]{2,5}     2 to 5 continuous occurrences of a or b
[ab]{2,}      2 or more continuous occurrences of a or b
+             Previous charachter, One or more
*             Previous charachter, Zero or more
?             Previous charachter,, 0 or 1
"""

# practice: BASIC SYNTAX
1) .             One character except new line

text = 'Hello World again'
text1="""hello
world
again"""
print(re.findall('.', text))  # .   Any character except for a new line. ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd', ' ', 'a', 'g', 'a', 'i', 'n']
print(re.findall('H..lo', text))  # Hello
print(re.findall('...', text))# ['Hel', 'lo ', 'Wor', 'ld ', 'aga']
#print(re.findall('.', text1))  # .Any character except for a new line. ['h', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', 'a', 'g', 'a', 'i', 'n']  
#print(re.findall('...', text1)) # ['hel', 'wor', 'aga']


text='abc pqr 123 hello wo1rld 345.com $'
text1 ="""Hello
world
                      8     again
"""
#print(re.findall('.',text)) # all charcters (period) in the string except new line, ['a', 'b', 'c', ' ', 'p', 'q', 'r', ' ', '1', '2', '3', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '.', 'c', 'o', 'm']
#print(re.findall('\.',text)) # if need to search for '.' itslef we need to add escape character., ['.']
#print(re.findall('\d',text)) # One digit, ['1', '2', '3', '1', '3', '4', '5']
#print(re.findall('\D',text)) # One Non digit, ['a', 'b', 'c', ' ', 'p', 'q', 'r', ' ', ' ', 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd', ' ', '.', 'c', 'o', 'm']
#print(re.findall('\w',text)) # One word character including digits, ['a', 'b', 'c', 'p', 'q', 'r', '1', '2', '3', 'h', 'e', 'l', 'l', 'o', 'w', 'o', '1', 'r', 'l', 'd', '3', '4', '5', 'c', 'o', 'm']
#print(re.findall('\W',text)) # One non-word character, [' ', ' ', ' ', ' ', ' ', '.', ' ', '$']
#print(re.findall('\s',text)) # One whitespace, [' ', ' ', ' ', ' ', ' '] 
#print(re.findall('\S',text)) # One non-whitespace ['a', 'b', 'c', 'p', 'q', 'r', '1', '2', '3', 'h', 'e', 'l', 'l', 'o', 'w', 'o', '1', 'r', 'l', 'd', '3', '4', '5', '.', 'c', 'o', 'm', '$']
print(re.findall('\b',text1)) # Word boundary []
#Word boundaries \b are commonly used to detect and match the beginning or end of a word. That is, one side is a word character and the other side is whitespace and vice versa.
#For example, the regex \btoy will match the ‘toy’ in ‘toy cat’ and not in ‘tolstoy’. In order to match the ‘toy’ in ‘tolstoy’, you should use toy\b
#Can you come up with a regex that will match only the first ‘toy’ in ‘play toy broke toys’? (hint: \b on both sides)
print(re.findall('\n',text1)) # Newline ['\n', '\n', '\n']
print(re.findall('\t',text1)) # Tab []

2) Practice: MODIFIERS

#escape charatcter and negation (^)
text = 'Helloworld.com'
txt1='Hello world again'
print(re.findall('\.', text))  # matches a period(dot), \works as a escape character.
print(re.findall('[^\.]', text))  # matches anything but a period,^ is used for Not or negation.
print(re.findall('[^o]', text)) # everything except o. ['H', 'e', 'l', 'l', 'w', 'r', 'l', 'd', '.', 'c', 'm']
print(re.findall('[^ ]', text)) # everything except blank space, ['H', 'e', 'l', 'l', 'o', 'w', 'o', 'r', 'l', 'd', '.', 'c', 'o', 'm']

text='abc abc def abc'
text1='pqr abc dpq abc pqr pqpqpq'
#print(re.findall("abc$",text)) # End of string, String ends with abc , output:['abc']
#print(re.findall("abc$",text1)) # []
#print(re.findall("^abc",text))# start of string, string start with abc , output: ['abc']
#print(re.findall("^abc",text1)) # []
#print(re.findall("ab|pq",text1)) # ['pq', 'ab', 'pq', 'ab', 'pq', 'pq', 'pq', 'pq']
#print(re.findall("[ab-d]",text1))  # ['a', 'b', 'c', 'd', 'a', 'b', 'c']
#print(re.findall("[^ab-d]",text1)) # ['p', 'q', 'r', ' ', ' ', 'p', 'q', ' ', ' ', 'p', 'q', 'r', ' ', 'p', 'q', 'p', 'q', 'p', 'q']
print(re.findall("([abq]pq$)",text1)) # match any charcater in a, b or q and ending with pq. ['qpq']
print(re.findall("[abq]pq$",text1)) # This will also work but better to enclose within bracket.


3) Practice: REPETITIONS
text='abc abc def abcaa bb ab bb bbac'
text1='pqr abc dpq abc pqr pqpqpq bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbac'
#print(re.findall("[ab]{2}",text)) # Exactly 2 continuous occurrences of a or b, ['ab', 'ab', 'ab', 'aa', 'bb', 'ab', 'bb', 'bb']
#print(re.findall("[ab]{2,5}",text)) #2 to 5 continuous occurrences of a or b, ['ab', 'ab', 'ab', 'aa', 'bb', 'ab', 'bb', 'bba']
#print(re.findall("[ab]{2,}",text1)) # ['ab', 'ab', 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbba']
#print(re.findall("[ab]{2,5}",text1)) # ['ab', 'ab', 'bbbbb', 'bbbbb', 'bbbbb', 'bbbbb', 'bbbbb', 'bbbbb', 'bbbbb']

1) #* : Previous charachter, Zero or more
#ca*t will match ct (0 a characters), cat (1 a), caaat (3 a characters), and so forth

# a[bcd]*b: This matches the letter 'a', zero or more letters from the class [bcd], and finally ends with a 'b'. Now imagine matching this RE against the string abcbd. 

text= 'cat ct caaaaaaaaaat cat'
re.findall('ca*t',text) # ['cat', 'ct', 'caaaaaaaaaat', 'cat']
text= 'abcbd'
re.findall('a[bcd]*b',text) # ['abcb']  # Greedy search, it could have given ab also as [bcd]* zero occurance is also possible.

2) # +:  which matches one or more times. * matches zero or more times, so whatever’s being repeated may not be present at all, while + requires at least one occurrence. To use a similar example, ca+t will match cat (1 a), caaat (3 a‘s), but won’t match ct.

text= 'cat ct caaaaaaaaaat cat'
re.findall('ca+t',text) # ['cat', 'caaaaaaaaaat', 'cat']
text= 'abcbd'
text1='ab'
#  differenc between + and *
print(re.findall('a[bcd]+b',text)) # ['abcb']
print(re.findall('a[bcd]*b',text1)) # ['ab']
print(re.findall('a[bcd]+b',text1)) # ['']

# write a program to find the string start with a and end with b , in between can conatin any repetation of [a-zA-Z]

text= 'cat ct caaaaaaaaaab catb'
print(re.findall('c[a-zA-Z]*b',text)) # ['caaaaaaaaaab', 'catb']
print(re.findall('c\w*b',text)) # any substring start with c and contains any didgit or character (anynumber of time) and then ends with b. output: ['caaaaaaaaaab', 'catb']

3) # ?: the question mark character, ?, matches either once or zero times; you can think of it as marking something as being optional. For example, home-?brew matches either homebrew or home-brew but not home--brew.

print(re.findall("home-?brew", "homebrew")) #['homebrew']
print(re.findall("home-?brew", "home-brew")) #['home-brew']
print(re.findall("home-?brew", "home--brew")) #[]


#############################################
#Greedy vs non greedy(Lazy) search???????
#Greedy : BY default regex is greedy , it tries to extract as much as possible until it conforms to a pattern even when a smaller part would have been syntactically sufficient.

text = "< body>Regex Greedy Matching Example < /body>"
re.findall('<.*>', text)
output: '< body>Regex Greedy Matching Example < /body>' # Instead of matching till the first occurrence of ‘>’, which would happen at the end of first body tag "< body> and </body>" itself, it extracted the whole string. This is the default greedy or ‘take it all’ behavior of regex

#Lazy matching, on the other hand, ‘takes as little as possible’. This can be effected by adding a `?` at the end of the pattern.
re.findall('<.*?>', text)
output: ['< body>', '< /body>']

# If you want only the first match to be retrieved, use the search method instead.
re.search('<.*?>', text).group()
output: <body>


##### example / Assignment 1
text = """101   COM   Computers
205   MAT   Mathematics
189   ENG    English"""  

# 1. extract all course numbers
re.findall('[0-9]+', text)

# 2. extract all course codes
re.findall('[A-Z]{3}', text)

# 3. extract all course names
re.findall('[A-Za-z]{4,}', text)

# define the course text pattern groups and extract
course_pattern = '([0-9]+)\s*([A-Z]{3})\s*([A-Za-z]{4,})'
re.findall(course_pattern, text)


# Assignment 2:

1) Extract the user id, domain name and suffix from the following email addresses.
"""
emails = """zuck26@facebook.com
page33@google.com
jeff42@amazon.com"""

desired_output = [('zuck26', 'facebook', 'com'),
 ('page33', 'google', 'com'),
 ('jeff42', 'amazon', 'com')]
"""


Sol:
pattern = r'(\w+)@([A-Z0-9]+)\.([A-Z]{2,4})' # we need three group so three () has been used. each () will give each invidual string like user id, domain name and suffix.
re.findall(pattern, emails, flags=re.IGNORECASE)
#>  [('zuck26', 'facebook', 'com'),
#>  ('page33', 'google', 'com'),
#>  ('jeff42', 'amazon', 'com')]  


#Assignemnt 3:

#Extract all the text portions between the tags from the following HTML page: https://raw.githubusercontent.com/selva86/datasets/master/sample.html

import requests
r = requests.get("https://raw.githubusercontent.com/selva86/datasets/master/sample.html")
r.text  # html text is contained here

#desired_output = ['Your Title Here', 'Link Name', 'This is a Header', 'This is a Medium Header', 'This is a new paragraph! ', 'This is a another paragraph!', 'This is a new sentence without a paragraph break, in bold italics.']

re.findall('<.*?>(.*)</.*?>', r.text) 


#Assignemnt 4:

Retrieve all the words starting with ‘b’ or ‘B’ from the following text.
text = """Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better.""" 
import re
re.findall(r'\bB\w+', text, flags=re.IGNORECASE)

# assignments 5:
to verify mobile number
'\d{9,10}'