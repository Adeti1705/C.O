#reg values
# sourcery skip: remove-duplicate-dict-key


f = open("lapt.txt","r")
lines = f.readlines()
f.close()
print(lines)
reg_values = {
    'zero':'0000000000000000000000000000000', 'ra':'0000000000000000000000000000000', 'sp':'0000000000000000000000000000000',
    'gp':'0000000000000000000000000000000', 'tp':'0000000000000000000000000000000', 't0':'0000000000000000000000000000000',
    't1':'0000000000000000000000000000000', 't2':'0000000000000000000000000000000', 's0':'0000000000000000000000000000000',
    's1':'0000000000000000000000000000000', 'a0':'0000000000000000000000000000000', 'a1':'0000000000000000000000000000000',
    'a2':'0000000000000000000000000000000', 'a3':'0000000000000000000000000000000', 'a4':'0000000000000000000000000000000',
    'a5':'0000000000000000000000000000000', 'a6':'0000000000000000000000000000000', 'a7':'0000000000000000000000000000000',
    's2':'0000000000000000000000000000000', 's3':'0000000000000000000000000000000', 's4':'0000000000000000000000000000000',
    's5':'0000000000000000000000000000000', 's6':'0000000000000000000000000000000', 's7':'0000000000000000000000000000000',
    's8':'0000000000000000000000000000000', 's9':'0000000000000000000000000000000', 's10':'0000000000000000000000000000000',
    's11':'0000000000000000000000000000000', 't3':'0000000000000000000000000000000', 't4':'0000000000000000000000000000000',
    't5':'0000000000000000000000000000000', 't6':'0000000000000000000000000000000'
}

#memory allocation of registers
memory = {
    '0x00010000': '0000000000000000000000000000000', '0x00010004': '0000000000000000000000000000000',
    '0x00010008': '0000000000000000000000000000000', '0x0001000c': '0000000000000000000000000000000', 
    '0x00010010': '0000000000000000000000000000000', '0x00010014': '0000000000000000000000000000000',
    '0x00010018': '0000000000000000000000000000000', '0x0001001c': '0000000000000000000000000000000',
    '0x00010020': '0000000000000000000000000000000', '0x00010024': '0000000000000000000000000000000',
    '0x00010028': '0000000000000000000000000000000', '0x0001002c': '0000000000000000000000000000000',
    '0x00010030': '0000000000000000000000000000000', '0x00010034': '0000000000000000000000000000000',
    '0x00010038': '0000000000000000000000000000000', '0x0001003c': '0000000000000000000000000000000',
    '0x00010040': '0000000000000000000000000000000', '0x00010044': '0000000000000000000000000000000',
    '0x00010048': '0000000000000000000000000000000', '0x0001004c': '0000000000000000000000000000000',
    '0x00010050': '0000000000000000000000000000000', '0x00010054': '0000000000000000000000000000000',
    '0x00010058': '0000000000000000000000000000000', '0x0001005c': '0000000000000000000000000000000',
    '0x00010060': '0000000000000000000000000000000', '0x00010064': '0000000000000000000000000000000',
    '0x00010068': '0000000000000000000000000000000', '0x0001006c': '0000000000000000000000000000000',
    '0x00010070': '0000000000000000000000000000000', '0x00010074': '0000000000000000000000000000000',
    '0x00010078': '0000000000000000000000000000000', '0x0001007c': '0000000000000000000000000000000'
}

#dictionary for storing reg values
dict_registers = {
    '00000': '0000000000000000000000000000000',
    '00001': '0000000000000000000000000000000',
    '00010': '0000000000000000000000000000000',
    '00011': '0000000000000000000000000000000',
    '00100': '0000000000000000000000000000000',
    '00101': '0000000000000000000000000000000',
    '00110': '0000000000000000000000000000000',
    '00111': '0000000000000000000000000000000',
    '01000': '0000000000000000000000000000000',
    '01001': '0000000000000000000000000000000',
    '01010': '0000000000000000000000000000000',
    '01011': '0000000000000000000000000000000',
    '01100': '0000000000000000000000000000000',
    '01101': '0000000000000000000000000000000',
    '01110': '0000000000000000000000000000000',
    '01111': '0000000000000000000000000000000',
    '10000': '0000000000000000000000000000000',
    '10001': '0000000000000000000000000000000',
    '10010': '0000000000000000000000000000000',
    '10011': '0000000000000000000000000000000',
    '10100': '0000000000000000000000000000000',
    '10101': '0000000000000000000000000000000',
    '10110': '0000000000000000000000000000000',
    '10111': '0000000000000000000000000000000',
    '11000': '0000000000000000000000000000000',
    '11001': '0000000000000000000000000000000',
    '11010': '0000000000000000000000000000000',
    '11011': '0000000000000000000000000000000',
    '11100': '0000000000000000000000000000000',
    '11101': '0000000000000000000000000000000',
    '11110': '0000000000000000000000000000000',
    '11111': '0000000000000000000000000000000'
}

B_opcode = '1100011'
J_opcode = '1101111'
R_opcode = '0110011'
S_opcode = '0100011'
U_opcode = {'0110111':'lui', '0010111':'auipc'}
I_opcode = {'0000011':'lw', '0010011':'addi', '0010011':'sltiu', '1100111':'jalr'}
   # sourcery skip: simplify-numeric-comparison

# r type funcs

# binary to decimal and vice versa conversion
def decimal_to_binary(n):
    if n < 0:
        n = (1<<32) + n
    format_string = '{:0>' + str(32) + '}'
    return format_string.format(bin(n)[2:])

def binary_to_decimal(binary_string):
    if binary_string[0] == '1':
        return -1 * (int(''.join('1' if b == '0' else '0' for b in binary_string), 2) + 1)
    else:
        return int(binary_string, 2)

def binary_addition(a, b):  
    max_len = 32
    a = a.zfill(max_len)
    b = b.zfill(max_len)
    result = ''
    carry = 0

    # Traverse both strings from right to left
    for i in range(max_len-1, -1, -1):
        temp = carry
        temp += 1 if a[i] == '1' else 0
        temp += 1 if b[i] == '1' else 0
        result = ('1' if temp % 2 == 1 else '0') + result
        carry = 0 if temp < 2 else 1       

    if carry != 0: 
        result = f'1{result}'

    return result.zfill(max_len)
def binary_subtraction(a, b):
    # Convert b to its 2's complement form
    b = ''.join('1' if bit == '0' else '0' for bit in b)
    b = binary_addition(b, '1')

    # Perform binary addition
    result = binary_addition(a, b)

    # Ignore overflow
    result = result[-32:]

    return result

def R_type(ins):  # sourcery skip: for-index-underscore, low-code-quality, use-fstring-for-concatenation
    if ins[25:32]=="0100000":
        if ins[15:20]=='00000':
            dict_registers[ins[7:12]]=binary_subtraction('0', dict_registers[ins[20:25]])
            return
        dict_registers[ins[7:12]]=binary_subtraction(dict_registers[ins[15:20]], dict_registers[ins[20:25]])
        return
    elif ins[12:15]=="000":
        dict_registers[ins[7:12]]=binary_addition(dict_registers[ins[15:20]], dict_registers[ins[20:25]])
        return
    elif ins[12:15]=="001":
        x=binary_to_decimal('0'+dict_registers[20:25][-5::1])
        dict_registers[ins[7:12]]=dict_registers[ins[15:20]][x:]+dict_registers[ins[15:20]][:x]
        return
    elif ins[12:15]=="010":
        if binary_to_decimal(dict_registers[ins[15:20]]) < binary_to_decimal(dict_registers[ins[20:25]]):
            dict_registers[ins[7:12]]=decimal_to_binary(1)
            return
    elif ins[12:15]=="011":
        if abs(binary_to_decimal(dict_registers[ins[15:20]])) < abs(binary_to_decimal(dict_registers[ins[20:25]])):
            dict_registers[ins[7:12]]=decimal_to_binary(1)
            return
    elif ins[12:15]=="100":
        a=dict_registers[ins[15:20]]
        b=dict_registers[ins[20:25]]
        x=''.join('0' if a[i]==b[i] else '1' for i in range(32))
        dict_registers[ins[7:12]]=x
        return
    elif ins[12:15]=="101":
        pass
        #right shift will solve later
    elif ins[12:15]=="110":
        dict_registers[ins[7:12]]=('0' if dict_registers[ins[15:20]][i]==dict_registers[ins[20:25]][i]=="0" else '1' for i in range(32))
    elif ins[12:15]=="111":
        dict_registers[ins[7:12]]=('1' if dict_registers[ins[15:20]][i]==dict_registers[ins[20:25]][i]=='1' else '0' for i in range(32))
        return

#i type
def I_type(ins):
    if ins[7:12]=='000':
        dict_registers[20:25]=binary_addition(ins[20:32], dict_registers[15:20])

def auipc(instruction_bin, pc):
    instruction = binary_to_decimal(instruction_bin[31:11:-1])
    new_pc=pc+int(instruction)
    return new_pc
def lui(instruction_bin):
    instruction = binary_to_decimal(instruction_bin[31:11:-1])
    return instruction
def U_type(ins,pc):
    a=0
    for i in dict_registers.keys():
        if ins[11:6:-1]==i:
            a=i;
            break
        if ins[6:-1:-1]=="0010111":
            dict_registers[a]=auipc(ins, pc)
        elif ins[6:-1:-1]=="0110111":
            dict_registers[a]=lui(ins)
def jal(instruction_bin, pc):
    imm = binary_to_decimal(instruction_bin[20])*2**20+binary_to_decimal(instruction_bin[1:11])*2**10+binary_to_decimal(instruction_bin[11])*2**11+binary_to_decimal(instruction_bin[12:20])
    if instruction_bin[20]=='1':
        imm-=2**21
    target_address=pc+imm
    new_pc=pc+4
    return new_pc, target_address
def B_type(last_line,PC):
    if last_line[-7:]=="1100011":
        func3=last_line[-15:-12]
        imm =last_line[-12:-7]+last_line[-30:-24]+last_line[-25]+last_line[-1]
        print("imm",imm)
        imm1=imm+"0"
        rs1_0 = last_line[-20 :-15]
        rs2_0 = last_line[-25 :-20]


        for i in register:
            if rs1_0 == register[i]:
                temp2=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp2:
                        rs1=format(reg_value, '032b')

        for i in register:
            if rs2_0 == register[i]:
                temp3=i
                for reg_name, reg_value in reg_val.items():
                    if reg_name==temp3:
                        rs2=format(reg_value, '032b')
                        
        if func3=="000": #beq
            print("hello ridhi")
            temp= PC
            print(PC, 'PC')
            if bin_to_int(rs1)==bin_to_int(rs2):
                PC = bin_to_int(PC) + bin_to_int(imm1)
                print ("imm 1 : ",imm1)
                PC= int_to_bin(PC)
                print("pc is  : ",PC)
            t=' '.join('0b'+format(value,'032b') for value in reg_val.values())
            # print(t)
            # values_list = list(reg_val.values()) 
            # print(values_list)
            outfile.write(('0b'+PC))
            outfile.write(" ")
            outfile.write(t)
            outfile.write('\n')
            return PC
start_index=0
line = 0
while(line < len(lines)):
    # print("inside for")
    l=line*4
    l = format(l,'032b')
    # k=k+1ṇ
    # print('loop', k)
    # print(line,l)
    if lines[line][-8:].strip() == "0110011":
        R_type(lines[line].strip(),l)
    elif lines[line][-8:].strip() == "1100111":
        l=(lines[line].strip(), l)
        line = R_type(line + int(l)//4)-1
        print(line , "L")
        print(l, 'a')
    # elif lines[line][-8:].strip() in ["0000011", "0010011"]:
    #     I_type(lines[line].strip(),l)
    # elif lines[line][-8:].strip() == "0100011":
    #     S_type(lines[line].strip(),l) 
    # elif lines[line][-8:].strip() == "1100011":
    #     B_type(lines[line].strip(),l) 
    # elif lines
    line = line+1
# m = '\n'.join('0b{:032}'.format(value) for value in memory.values())
m = '\n'.join('0b'+format(value, '032b') for value in memory.values())
