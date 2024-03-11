#same for all
def convert_binary(n): 
    x= bin(abs(n)).replace("0b", "")
    if len(x)+1>32:
        return "error"
    if n>=0:
        return ('0'*(32-len(x))+x)
    l=len(x)+1
    final=bin(2**l+n).replace('0b',"")

    return (final[0]*(32-len(final))+final)

registers_encodings = {
    'zero': '00000', 'ra': '00001', 'sp': '00010', 'gp': '00011', 'tp': '00100',
    't0': '00101', 't1': '00110', 't2': '00111', 's0': '01000', 's1': '01001',
    'a0': '01010', 'a1': '01011', 'a2': '01100', 'a3': '01101', 'a4': '01110',
    'a5': '01111', 'a6': '10000', 'a7': '10001', 's2': '10010', 's3': '10011',
    's4': '10100', 's5': '10101', 's6': '10110', 's7': '10111', 's8': '11000',
    's9': '11001', 's10': '11010', 's11': '11011', 't3': '11100', 't4': '11101',
    't5': '11110', 't6': '11111'
}

#R type
r_type = {
    'add': '000', 'sub': '000', 'sll': '001', 'slt': '010',
    'sltu':'011', 'xor': '100','srl':'101',
    'or': '110', 'and': '111'}

def r_encoding(line,ins):
    if ins=='sub':
        funct7='0100000'
    else:
        funct7='0000000'
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
    for i in reg[:0:-1]:
        s+=registers_encodings[i]
    return funct7+s+r_type[ins]+registers_encodings[reg[0]]+"0110011"
#I type
i_type = {'addi': '000','sltiu': '011', 'lw': '010', 'jalr': '000'}
def i_encoding(line,ins):
    if ins=='lw':
        opcode='0000011'
    elif ins == 'jalr':
        opcode='1100111'
    else:
        opcode== '0010011'

    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    k=convert_binary(int(reg[-1]))
    reg=reg[0:-1]
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
        else:
            s+=registers_encodings[i]
    return k[20::]+s[5:]+i_type[ins]+s[:5]+opcode
#B type
b_type = {'beq': '000','bne': '001','blt': '100','bge':'101'}
def b_encoding(line,ins):
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    k=convert_binary(int(reg[-1]))
    k=k[-1::-1]
    reg=reg[0:-1]
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
        else:
            s+=registers_encodings[i]
        return k[12]+k[10:5:-1]+s+b_type[ins]+k[4:1:-1]+k[11]+"1100011"
#U type
u_type={"lui":"0110111","auipc":"0010111"}
def u_encoding(line,op):
    reg=(line[line.index(" ")+1::]).split(',')
    s=''
    k=convert_binary(int(reg[-1]))
    k=k[-1::-1]
    reg=reg[0:-1]
    for i in reg:
        if i not in registers_encodings.keys():
            return 'error'
        else:
            s+=registers_encodings[i]
        return k[31:12:-1]+s+u_type[op]
# J type
def j_encoding(line):
    reg=(line[line.index(" ")+1::]).split(',')
    if reg[0] in registers_encodings.keys():
        x=convert_binary(int(reg[1]))[::-1]
        return x[20]+x[10:0:-1]+x[11]+x[19:11:-1]+registers_encodings[reg[0]]+'1101111'



fobj=open("name.txt")
output=open("Output.txt",'w')
data=fobj.readlines()
for line in data:
    if line!=" ":
        ins=''
        for ch in line:
            if not ch.isspace():
                ins+=ch
            else:
                break
        if ins in r_type.keys():
            print(r_encoding(line,ins))
        elif ins in i_type.keys():
            print(i_encoding(line,ins))
        elif ins in b_type.keys():
            print(b_encoding(line,ins))
        elif ins in u_type.keys():
            print(u_encoding(line,ins))
        elif ins=='jal':
            print(j_encoding(line))
        elif ins in s_type.keys():
            print(s_encoding(line,ins))
        else: 
            print('error')


#1111111111111111000011101111    
# 110000000000