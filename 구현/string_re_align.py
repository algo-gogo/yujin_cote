parameter = list(map(str,input()))

parameter.sort()

total = 0

i = 0
while i < len(parameter):
    if( '9' >= parameter[i] >= '0' ):
        total += int(parameter[i])
        del parameter[i]
    else:
        i += 1

print( "".join(parameter)+str(total) )