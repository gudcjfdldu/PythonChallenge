#!/usr/bin/python

hint_string = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc
dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle.
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."""

clear = ''.join(map(lambda x: chr((ord(x)-ord('a')+2)%26+ord('a'))
    if 'a'<=x<='z' else x,hint_string))

print clear
