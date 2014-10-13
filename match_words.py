def match_ends(words):
        count = 0
        for i in words:
                if (len(i)>=2):
			s = list(i)
			if(s[0]==s[-1]):
	                        count =  count +1
        return count

print match_ends(['qwq','qwq','wew','eew','iuy','uyu','ueb'])
