#import module
import re

# # finding phone number in string
# sr='My phone number is 080-4132-7147'
# # d means digits and {3} means number of digits
# # is_phone_number= re.compile(r'\d\d\d-\d\d\d\d-\d\d\d\d')
# is_phone_number= re.compile(r'\d{3}-\d{4}-\d{4}')
# #search-> to search the pattern in string
# mobile=is_phone_number.search(sr)
# # grouping ->to call the match object
# mobile=mobile.group()
# print("My phone number is :",mobile)

# Matching Multiple Groups with the Pipe

# returns first matched string

# ame= "surya and yondhen"
# n="yondhen and surya"
# name1=re.compile(r'surya|yondhen')
# name1=name1.search(n)
# name1=name1.group()
# print('My name is :',name1)
# n

# Optional Matching with the Question Mark
""""
Sometimes there is a pattern that you want to match only optionally. That is, the
regex should find a match whether or not that bit of text is there. The ? character flags the group
that precedes it as an optional part of the pattern
"""
# batRegex=re.compile(r'Bat(wo)?man')
# mo1=batRegex.search('The Adventures of Batman')
# bat=mo1.group()
# print(bat)

# phone=re.compile(r'(\d{3}-)?\d{3}-\d{3}')
# ph=phone.search('My phone number is 454-454')
# ph=ph.group()
# print(ph)

# Matching Zero or More with the Star
"""
The * (called the star or asterisk) means 
“match zero or more”—the group that precedes 
the star can occur any number of times in the 
text. It can be completely absent or repeated 
over and over again
If you need to match an actual star character, 
prefix the star in the regular expression with a 
backslash, \*.
"""
# batregex=re.compile(r'Bat(wo)*man')
# mo1=batregex.search('The Adventures of Batwowowowoman')
# print(mo1)
# if mo1!=None:
#     mo1=mo1.group()
#     print(mo1)
# else:
#     print('The match could not found!')

# Matching One or More with the Plus
""""
While * means “match zero or more,” the + (or plus) 
means “match one or more.” Unlike the star, which 
does not require its group to appear in the matched 
string, the group preceding a plus must appear at least
once. It is not optional.
"""

# batRegex=re.compile(r'Bat(wo)+man')
# mo1=batRegex.search('The Adventures of Batwowoman')
# mo1=mo1.group()
# print(mo1)

# Matching Specific Repetitions with Curly Brackets
"""
If you have a group that you want to repeat a specific number of times, follow the group in your regex with a number in curly brackets. For example, the regex
(Ha){3} will match the string 'HaHaHa', but it will not match 'HaHa', since the latter has only two repeats of the (Ha) group.
Instead of one number, you can specify a range by writing a minimum, a comma, and a maximum in between the curly brackets. For example, the regex
(Ha){3,5} will match 'HaHaHa', 'HaHaHaHa', and 'HaHaHaHaHa'.
"""

# haRegex=re.compile(r'(Ha){3}')
# mo1=haRegex.search('HaHaHa')
# mo1=mo1.group()
# print(mo1)

# note: 
# Here, (Ha){3} matches 'HaHaHa' but not 'Ha'. Since it doesn’t match 'Ha', search() returns None.

#Greedy and Nongreedy Matching

"""
Since (Ha){3,5} can match three, four, or five instances of Ha in the string 'HaHaHaHaHa', you may wonder why the Match object’s call to group() in the previous curly bracket example returns 'HaHaHaHaHa' instead of the shorter possibilities. After all, 'HaHaHa' and 'HaHaHaHa' are also valid matches of the regular expression (Ha){3,5}.
Python’s regular expressions are greedy by default, which means that in ambiguous situations they will match the longest string possible. The nongreedy version of the curly brackets, which matches the shortest string possible, has the closing curly bracket followed by a question mark.
"""
# greedyHaRegex=re.compile(r'(Ha){3,5}')
# mo1=greedyHaRegex.search('HaHaHaHaHaHaHa')
# mo1=mo1.group()
# print(mo1)#HaHaHaHaHa
# print("*******"*5)
# greedyHaRegex=re.compile(r'(Ha){3,5}?')
# mo1=greedyHaRegex.search('HaHaHaHaHaHaHa')
# mo1=mo1.group()
# print(mo1) #HaHaHa

# The findall() Method
"""
In addition to the search() method, Regex objects also have a findall()
method. While search() will return a Match object of the first matched text in
the searched string, the findall() method will return the strings of every match
in the searched string. To see how search() returns a Match object only on the first instance of matching text.

tuples. Each tuple represents a found match, and its items are the matched strings
for each group in the regex. 
"""

# phoneNumberRegex=re.compile(r'\d{3}-\d{4}-\d{4}')
# mo1=phoneNumberRegex.findall('Cell:455-5641-4551 work:465-2133-4521')
# print()

# Character Classes
# \d Any numeric digit from 0 to 9.
# Shorthand character class
# Represents
# \D->Any character that is not a numeric digit from 0 to 9.
# \w-># Any letter, numeric digit, or the underscore character. (Think of this as matching “word” characters.)
# \W-> Any character that is not a letter, numeric digit, or the underscore character.
# \s-># Any space, tab, or newline character. (Think of this as matching “space” characters.)
#^->By placing a caret character (^) just after the character class’s opening bracket, you can make a negative character class. A negative character class will match all the characters that are not in the character class.
#^->You can also use the caret symbol (^) at the start of a regex to indicate that a match must occur at the beginning of the searched text. 
#$->you can put adollar sign ($) at the end of the regex to indicate the string must end with this
# regex pattern. And you can use the ^ and $ together to indicate that the entire string must match the regex—that is, it’s not enough for a match to be made on some subset of the string.

# alphaRegex=re.compile(r'[aeio0-9]')
# alphaRegex1=re.compile(r'[^aeio0-9]')
# alphaRegex2=re.compile(r'^surya$',re.IGNORECASE)
# mo=alphaRegex.findall('lamasurya1 yondhen1321@_')
# mo1=alphaRegex1.findall('lamasurya1 yondhen1321@_')
# mo2=alphaRegex2.findall('Surya')
# print(mo)
# print(mo1)
# print(mo2)

# The Wildcard Character
"""
The . (or dot) character in a regular expression is called a wildcard and will match any character except for a newline.
"""
# atRegex=re.compile(r'.at')
# mo=atRegex.findall('The cat in the hat sat on the flat mat.')
# print(mo)

# Matching Newlines with the Dot Character

#(.*)-> will match everything except new line
# if you want to include . also then you can use re.DOTALL

noNewLineRegex=re.compile(r'.*')
newLineRegex=re.compile(r'.*',re.DOTALL)
mo=noNewLineRegex.search('Serve the public trust.\nProtect the innocent.')
mo1=newLineRegex.search('Serve the public trust.\nProtect the innocent.')
mo=mo.group()
mo1=mo1.group()
print(mo)
print(mo1)