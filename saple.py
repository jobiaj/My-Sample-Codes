import sys
import re
def extract_names(filename):
	k = filename
	w = open(k,'r').read()
	
	year = re.search(r'(<h3 align="center">Popularity in )(\d\d\d\d)',w)
	if year:
		birth_year = year.group(2)
		print birth_year
	fnew = open(("details of the" + birth_year),'w')
	fnew.write("birth year:"+ birth_year+"\n")
	fnew.write("Rank	Male	Female"+"\n")
	rank=re.findall(r'<tr align="right"><td>(\d+)</td><td>(\w*)</td><td>(\w*)</td>',w)
	for i in rank:
		fnew.write(i[0]+"	" + i[1] + "	   " +i[2]+"\n")
	fnew.close()


extract_names('1.html')
	
