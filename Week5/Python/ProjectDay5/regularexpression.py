import re

text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
Ha HaHa
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
coreyms.com

cat
mat
bat
rat

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov


321-555-4321
123.555.1234
123*555*1234
800-555-1234
900-555-1234
Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''

#patterns = re.compile(r'abc') #absolute text "abc"
#patterns = re.compile(r'.') #all characters except line break
#patterns = re.compile(r'\.') #only full stops ".", relevant for these special characters . ^ $ * + ? { } [ ] \ | ( )
#patterns = re.compile(r'coreyms\.com') #for urls, since . is there, \ needed
#patterns = re.compile(r'\d') #all digits
#patterns = re.compile(r'\w') #all alpha numeric characters (big +small)+ _
#patterns = re.compile(r'\W') #Capitals are negates of small, so W is not(w)
#patterns = re.compile(r'\bHa') #\b is for word boundary(spaces, newline,etc), here we are finding characters after word boundary
#patterns = re.compile(r'\BHa') #finding characters which do not have word boundaries before it
#patterns = re.compile(r'^abc') #^ is for start a string, here we start with \n, hence result = NULL
# patterns = re.compile(r'T$') #is for end of string
#patterns = re.compile(r'\d\d\d') #3 digits in a row
# patterns = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d') #321-555*4321, 800-55512,321d555 4321
#patterns = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d') #[-.]-> - OR . ->800.555-1234
#patterns = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d') #number starting from 800/900 800-555-1234, 900-555-1234
#patterns = re.compile(r'[1-5]') #digits between 1 to 5
#patterns = re.compile(r'[a-z]') #characters between a to z
#patterns = re.compile(r'[a-zA-Z]') # a to z and A to Z
#patterns = re.compile(r'[a-zA-Z0-9]') #a to z and A to Z and 0 to 9
#patterns = re.compile(r'[^a-zA-Z]') #^will negate in [], this expr means, characters outside a-Z
#patterns = re.compile(r'[^b]at') #->cat, mat, rat but not "bat"
#patterns = re.compile(r'\d{3}.\d{3}.\d{4}') #check below Qantifiers ->\d\d\d.\d\d\d.\d\d\d\d
#patterns = re.compile(r'Mr\.') #find all "Mr."
#patterns = re.compile(r'Mr\.?') #?-> optional (0 or 1) so Mr and Mr. gets identified
#patterns = re.compile(r'Mr\.?\s[a-zA-Z]*') #Mr.(opt)(space)(characters-multiple)  Mr. Schafe, Mr Smith
#patterns = re.compile(r'Mr\.?\s[A-Z]\w*') #instead of a-z, defyning it via word characters
#patterns = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*') #group characters (r|s)-> r or s ->Mrs. Robinson,cMr. Schafer,Ms Davis,Mr Smith
#patterns = re.compile(r'(Mr|Ms|Mrs)\.?\s[A-Z]\w*') #same as above, but readable, w is for word
# patterns = re.compile(r'[a-zA-z]+@[a-zA-z]+\.com') #CoreyMSchafer@gmail.com
# patterns = re.compile(r'[a-zA-z0-9-.]+@[a-zA-z-]+\.(com|edu|net)') #all emails present in file
#patterns = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+') #standard email regex from online
#patterns = re.compile(r'https?://(www\.)?\w+\.\w+') #all urls
#patterns = re.compile(r'abc') #
#patterns = re.compile(r'abc') #

# matches = patterns.finditer(text_to_search)
# for match in matches:
#     print(match)


#Group Section starts
url="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""
patterns = re.compile(r'https?://(www\.)?(\w+)(\.\w+)') #url divided into 3 sectioins, and we can print them individually
matches = patterns.finditer(text_to_search)
for match in matches:
    print(match.group(3))
sub_url=patterns.sub(r'\2\3',url)   #substitutes group2 and group 3, and prints that -? google.com, youtube.com
print(sub_url)
#Group section ends

#findall method -> finds and prints resutls
#match method->it returns first match or None

#
# .       - Any Character Except New Line
# \d      - Digit (0-9)
# \D      - Not a Digit (0-9)
# \w      - Word Character (a-z, A-Z, 0-9, _)
# \W      - Not a Word Character
# \s      - Whitespace (space, tab, newline)
# \S      - Not Whitespace (space, tab, newline)
#
# \b      - Word Boundary
# \B      - Not a Word Boundary
# ^       - Beginning of a String
# $       - End of a String
#
# []      - Matches Characters in brackets
# [^ ]    - Matches Characters NOT in brackets
# |       - Either Or
# ( )     - Group
#
# Quantifiers:
# *       - 0 or More
# +       - 1 or More
# ?       - 0 or One
# {3}     - Exact Number
# {3,4}   - Range of Numbers (Minimum, Maximum)
#
#
# #### Sample Regexs for email ####
#
# [a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+
