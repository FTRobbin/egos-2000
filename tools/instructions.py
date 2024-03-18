import re
import os

# see Table 20.2: RISC-V pseudoinstructions.
alias = {'beqz': 'beq', 'bgez' : 'bge', 'bgtz' : 'blt', 'blez' : 'bge',
        'bltz' : 'blt', 'bnez' : 'bne', 'j' : 'jal', 'jr' : 'jalr',
        'mv' : 'addi', 'neg' : 'sub', 'nop' : 'addi', 'not' : 'xori',
        'ret' : 'auipc', 'seqz' : 'sltiu', 'snez' : 'sltu', 'li' : 'lui',
        'csrr' : 'csrrs', 'csrw' : 'csrrw', 'csrs' : 'csrrs', 'csrc' : 'csrrc',
        'zext.b' : 'andi'}

files = os.listdir("build/debug")

instructions = set()
for file in files:
    print("processing {}".format(file))
    f = open("build/debug/{}".format(file), "r")
    for line in f:
        l = re.split('\t|\n', line)
        if len(l) > 2 and len(l[2]) > 0 and len(l[0]) == 9:
            inst = l[2]
            if inst in alias:
                instructions.add(alias[inst])
            else:
                instructions.add(inst)
    f.close()

print("\033[1;32m[INFO] In total, there are {} instructions.\033[0m".format(len(instructions)))
print(sorted(list(instructions)))

exist = {"lui", "auipc", "jal", "jalr", "beq", "bne", "blt", "bge", "bltu", "bgeu", "lb", "lh", "lw", "lbu", "lhu", "sb", "sh", "sw", "addi", "slti", "sltiu", "xori", "ori", "andi", "slli", "srli", "srai", "add", "sub", "sll", "slt", "sltu", "xor", "srl", "sra", "or", "and", "wfi", "ecall", "ebrack", "mret", "csrrw", "csrrs", "csrrc", "fen"}

print("\033[1;32m[INFO] There exist {} instructions.\033[0m".format(len(exist)))
print(sorted(list(exist)))

rest = instructions - exist
print("\033[1;32m[INFO] There are {} more instructions to be implemented.\033[0m".format(len(rest)))
print(sorted(list(rest)))
