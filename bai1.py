def longestRepeat(s):
   a="qwertyuiopasdfghjklzxcvbnm"
   b=a.upper()
   d=""
   e=""
   for i in s:
        if( ((i in a) or (i in b)) and (s.count(i)>1) ):
            d=d+i
   if(len(d)>0):
        return d
   else:
        return e
c="abcdefaa"
longestRepeat(c)
    