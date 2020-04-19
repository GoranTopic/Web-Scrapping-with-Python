Web Scrappoing usin Python
====

This are the parctice scrips used to practice web scapping 
---

*bold*
_italics


### REGEX Cheatsheet 

| Character |  Example         | Definition |
|-----------|------------------|-----------|
| *		  	  | a*b*  		  		 | Matches the previous character 0 or more times   |
| +		  	  | a+b+  		  		 | Matches the previous character 1 or more times   |
| [ ] 		  | [a-z] 		  		 | Matches any character from a to z                |
| [\^ ]	    | [a-z]   	  		 | Does *not* matches any character from a to z     | 
| ()        | (a*b)* 	     	   | A grouped subexpression, this are executed first |
| \|        | (foo|foot)s  	   | _or_ Matches one of the other expression|
| {m,n}     | a{2,3}   	   	   | Matches the preceding character, m to n |
| .   		  | b.d              | Matches any charater 																|
| \^        | \^a              | Indicates an expression at the begining of the sting |
| \\        | \^ \|\\          | An escape charater  |
| $         | [A-Z]*$          | Often at the of the expression it matches the end of the string  |
| ?!        | ^((?![A-Z]).)*$  | Does seomthing?? *expand*          | |
| ?         | (swimming )? pool| makes the previous expression optional |
| ??        | (swimming )? pool| lazy |
| (?=)      | A(?=B)           | _look ahead_  Matches an A followed by a B: AB, ABC,|
| (?!)  	  | A(?!B)           | _look ahead negatice_	find a expression A where B *does not * follows | 
| (?<=)     | (?<=B)A          | _look behind_ Find Expresion A where B preceds it | 
| (?<!)  	  | (?<!B)A          | _look behind negatice_	 find expression A where expression B *does not* precced |
| (?>)  	  | (?>foo|foot)s    | _atomic groups_	 a groupe which trows away altenative patterns if the first alternative does not match | 

 



> 


