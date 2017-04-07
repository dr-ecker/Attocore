#!/bin/python
import sys

def bits8(val):
    return(str((val/128)%2)+str((val/64)%2)+str((val/32)%2)+str((val/16)%2)+str((val/8)%2)+str((val/4)%2)+str((val/2)%2)+str(val%2))

fp = open(sys.argv[-1])
romout = open("rom.txt","w")

regdict={
        "r0":"0000",
        "ADDR_LSB":"0000",
        "r1":"0001",
        "ADDR_MSB":"0001",
        "r2":"0010",
        "PC_LSB":"0010",
        "r3":"0011",
        "PC_MSB":"0011",
        "r4":"0100",
        "IR":"0100",
        "r5":"0101",
        "ALU_A":"0101",
        "r6":"0110",
        "ALU_B":"0110",
        "r7":"0111",
        "ALU_Y":"0111",
        "r8":"1000",
        "r9":"1001",
        "r10":"1010",
        "r11":"1011",
        "r12":"1100",
        "r13":"1101",
        "r14":"1110",
        "r15":"1110"}

jmpdict={}
pc=0
for line in fp:
    line = line.split(":")
    if len(line)>1:
        jmpdict.update({line[0]:pc})
    line = line[-1]
    cmd = line.split()
    if len(cmd)==0:
        cmd=""
    else:
        cmd=cmd[0]

    if cmd == "NOOP":
        romout.write("00000000\n")

    if cmd == "JUMPCOND":
        target=line.split()[-1]
        if(target in jmpdict):
            romout.write("01100000\n")
            romout.write(bits8(jmpdict[target]%256)+"\n")
            romout.write("01100001\n")
            romout.write(bits8(jmpdict[target]/256)+"\n")
            romout.write("00100001\n")
            pc=pc+4
        else:
            print("Error: Link '" + target + "' not found")


    if cmd == "JUMP":
        target=line.split()[-1]
        if(target in jmpdict):
            romout.write("01100000\n")
            romout.write(bits8(jmpdict[target]%256)+"\n")
            romout.write("01100001\n")
            romout.write(bits8(jmpdict[target]/256)+"\n")
            romout.write("00100000\n")
            pc=pc+4
            print("Jump To: " + str(jmpdict[target]) + " via key " + target)
        else:
            print("Error: Link '" + target + "' not found")

    if cmd == "VALSET":
        data=int(line.split()[-1])
        reg=regdict[line.split()[-2]]
        romout.write("0110"+reg+"\n")
        romout.write(bits8(data)+"\n")
        pc=pc+1

    if cmd == "ADD":
        romout.write("01000000\n")
    if cmd == "SUB":
        romout.write("01000001\n")
    if cmd == "GT":
        romout.write("01000010\n")
    if cmd == "LT":
        romout.write("01000011\n")
    if cmd == "EQ":
        romout.write("01000100\n")
    if cmd == "LSHIFT":
        romout.write("01000101\n")
    if cmd == "RSHIFT":
        romout.write("01000110\n")

    if cmd == "READ":
        target=line.split()[-2]
        address=line.split()[-1]
        romout.write("01100000\n")
        romout.write(bits8(int(address)%256)+"\n")
        romout.write("01100001\n")
        romout.write(bits8(int(address)/256)+"\n")
        romout.write("1000"+regdict[target]+"\n")
        pc=pc+4
    if cmd == "WRITE":
        target=line.split()[-2]
        address=line.split()[-1]
        romout.write("01100000\n")
        romout.write(bits8(int(address)%256)+"\n")
        romout.write("01100001\n")
        romout.write(bits8(int(address)/256)+"\n")
        romout.write("1010"+regdict[target]+"\n")
        pc=pc+4
    if cmd == "COPY":
        src=line.split()[-2]
        dest=line.split()[-1]
        romout.write("11000000\n")
        romout.write(regdict[src]+regdict[dest]+"\n")
        pc=pc+1
    pc=pc+1
    print(line + " at PC: " + str(pc))
