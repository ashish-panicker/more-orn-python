"""Pattern matching in python using re module"""
import logging
import re

"""Create a logger for this python module"""
logging.basicConfig(level=logging.DEBUG,
                    format='%(name)s : %(levelname)s : %(message)s')
logger = logging.getLogger(__name__)

"""
Regular exression flags
re.I    Case insensitive
re.X    Multi line
"""

"""match() - Checks if the pattern appears at the begining of string"""
text1 = "Python is amazing language."
text2 = "Programming in Python is amazing."

match = re.match(r'Python', text2)  # r -> raw string
if match:
    logger.info(f"Match found: {match.group()}")
else:
    logger.warning("No match found")


"""search() - checks if the pattern is present anywhere in the string"""
match = re.search(r'Python', text2)  # r -> raw string
if match:
    logger.info(f"Search found: {match.group()}")
else:
    logger.warning("No Search found")


"""finditer() - returns an iterator with match objects"""
text = "She sells sea shells on the sea shore"
pattern = r'sea'
matches = re.finditer(pattern, text)
for match in matches:
    logger.info(f"Match {pattern} found at: {match.start()} - {match.end()}")

"""findall() - returns a list of matching substrings"""
pattern = r'SEA|SHELL'
matches = re.findall(pattern, text, re.I)  # re.I -> case insensitive match
logger.info(f"Finding all matches: {matches}")

"""
more on match object
group()   return matched string
start()   returns start index of the match
end()     returns end index of the match
span()    returns a tuple(start, end) as a range
"""

pattern = r'sea'
match = re.search(pattern, text)
if match:
    logger.info(f"Matched: {match.group()} Start: {match.start()} End: {match.end()} Span: {match.span()}" )