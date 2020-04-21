Web Scrappoing usin Python
====

This are the parctice scrips used to practice web scapping 
---

*bold*
_italics_


### REGEX Cheatsheet


| Character |  Example         | Definition |
|-----------|------------------|-----------|
| *		  	  | a*b*  		  		 | Matches the previous character 0 or more times   |
| +		  	  | a+b+  		  		 | Matches the previous character 1 or more times   |
| [ ] 		  | [a-z] 		  		 | Matches any character from a to z                |
| [\^ ]	    | [a-z]   	  		 | Does *not* matches any character from a to z     |
| ()        | (a*b)* 	     	   | A grouped subexpression, this are executed first |
| <code>&#124;</code>| <code> (foo&#124;foot)s </code>    | _or_ Matches one of the other expression|
| {m,n}     | a{2,3}   	   	   | Matches the preceding character, m to n |
| .   		  | b.d            | Matches any charater |
| \^        | \^a              | Indicates an expression at the begining of the sting |
| \\        | \^               | An escape charater  |
| $         | [A-Z]*$          | Often at the of the expression it matches the end of the string  |
| ?!        | ^((?![A-Z]).)*$  | _Does not contain_  seomthing?? *expand*           |
| ?         | (swimming )? pool| makes the previous expression optional |
| ??        | (swimming )? pool| lazy |
| (?=)      | A(?=B)           | _look ahead_  Matches an A followed by a B: AB, ABC,|
| (?!)      | A(?!B)         | _look ahead negatice_	find a expression A where B *does not * follows |
| (?<=)     | (?<=B)A          | _look behind_ Find Expresion A where B preceds it |
| (?<!)     | (?<!B)A          | _look behind negatice_	 find expression A where expression B *does not* precced |
| (?>)      | <code>(?>foo&#124;foot)s </code>  | _atomic groups_	 a groupe which trows away altenative patterns if the first alternative does not match |

 
###BeautifulSoup4

It is a Python libraby used for scrapping websites

It probably might have to be installed. I used  `pip-3.6 install beautifulsoup4`

The beautifulSoup librabry creates a data structure out of the html document, enabiling the user to maniputale HTML tags a data objs. This is very useful if one is looking traverse links.

One can create a beautifulSoup object by passing the the html document and a parser.

> soup = BaautifulSoup(html_doc, 'html\_parser')

one can see the html page with:
> print(soup.prettify())









