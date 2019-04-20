import re
examples = {}

# read examples from input file
with open('input_part_1.txt') as inp:
    key = 0
    example = {}

    for line in inp:
        if line == "\n":
            continue
        else:
            nums = list(map(int, re.findall('\d+', line.strip())))

            if line.startswith("Before:"):
                example['before'] = nums

            elif line.startswith("After:"):
                example['after'] = nums
                examples[key] = dict(example)
                key += 1

            else:
                example['op'] = nums


def addr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        reg[out] = reg[in1] + reg[in2] 
        return reg


def addi(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = reg[in1] + in2
        return reg


def mulr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        reg[out] = reg[in1] * reg[in2] 
        return reg


def muli(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = reg[in1] + in2
        return reg


def banr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        reg[out] = reg[in1] & reg[in2] 
        return reg


def bani(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = reg[in1] & in2
        return reg


def borr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        reg[out] = reg[in1] | reg[in2] 
        return reg


def bori(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = reg[in1] | in2
        return reg


def setr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = reg[in1]
        return reg


def seti(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        reg[out] = in1
        return reg


def gtir(in1, in2, out, reg):
    reg = reg[::]
    if in2 < len(reg):
        if in1 > reg[in2]:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


def gtri(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        if reg[in1] > in2:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


def gtrr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        if reg[in1] > reg[in2]:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


def eqir(in1, in2, out, reg):
    reg = reg[::]
    if in2 < len(reg):
        if in1 == reg[in2]:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


def eqri(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg):
        if reg[in1] == in2:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


def eqrr(in1, in2, out, reg):
    reg = reg[::]
    if in1 < len(reg) and in2 < len(reg):
        if reg[in1] == reg[in2]:
            reg[out] = 1
        else:
            reg[out] = 0

        return reg


ops = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr
}

three_or_more = 0

for key in examples:
    valid = 0
    valid_ops = list()
    example = examples[key]
    reg = example['before']
    for op in ops:
        ret = ops[op](*example['op'][1:], reg)
        if ret and ret == example['after']:
            valid += 1
            valid_ops.append(op)

    if valid >= 3:
        three_or_more += 1
        print([key, valid, sorted(valid_ops)])

print(three_or_more)
