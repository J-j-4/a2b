import sys
import string
import struct
import os
import shutil
import time

'''
python3 ascii file convert to binary file
'''
dict = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'a':10,'b':11,'c':12,'d':13,'e':14,'f':15,'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}
    
def write_binary(number,fp):
    parsedata_id = struct.pack("B",number)
    fp.write(parsedata_id)
    fp.flush()

def write_ibyte(ih,il,fp):
    num = 16*ih+il
    write_binary(num,fw)

def write_sbyte(sh,sl,fp):
    a0 = dict[sh]
    a1 = dict[sl]
    num = 16*a0+a1
    write_binary(num,fp)

def atobin(src,dir):
    fr = open(src,'r+')
    fw = open(dir,'wb')

    size = os.path.getsize(src)
    print ('total src size:%d' % size)
    curpos = fr.tell()

    lastpro=0
    while (curpos<size):
        pro = (curpos*100/size)
        if(pro-lastpro>=1):
            print ('progress:%%%d' % (pro))
            lastpro=pro
        str = fr.read(2)
        if(len(str)<2):
            break
        
        if((str[0] in dict) and (str[1] in dict)):
            write_sbyte(str[0],str[1],fw)
            curpos =  fr.tell()
        elif (str[0] in dict):
            snext=str[1]
            while((snext in dict)==False and curpos<size):
                snext = fr.read(1)
                curpos =  fr.tell()
            write_sbyte(str[0],snext,fw)
            
            
        elif (str[1] in dict):
            snext='l'
            while((snext in dict)==False and curpos<size):
                snext = fr.read(1)
                curpos =  fr.tell()

            write_sbyte(str[1],snext,fw)
    
        else:
            pass

    fr.close()
    fw.close()
    

if __name__ == '__main__':
    src="asc_src.tim"
    dir="binary_dir.dat"
    '''
    localtime = time.strftime("cpy %Y-%m-%d %H-%M-%S", time.localtime())
    toname = ('%s %s' % (localtime,dir))
    shutil.copy(dir,  toname)
    os.remove(dir)
    '''

    atobin(src,dir)

    print ('compelete!')
