#!/usr/bin/env python3

'''
test terminal true color support
best results should be achieved under konsole
with font size=6 and scale=4 (local var here)
with font 8 and scale 5 is also ok.
'''

def gen_clr_seq(clr_lst):
    ''' gen all possible color seq '''
    if len(clr_lst) == 0:
        return ['']

    rest_clr_lst = gen_clr_seq(clr_lst[1:])

    tmp_set = set()
    for item in rest_clr_lst:
        for ndx in range(len(item) + 1):
            tmp_lst = list(item)
            tmp_lst.insert(ndx, clr_lst[0])
            tmp_set.add(''.join(tmp_lst))
    return sorted(tmp_set)

def gen_clr_code_step_lst(scale):
    ''' helper func to gen list of color code steps '''
    step = 2**scale
    tmp_lst = list(range(-1, 256, step))
    tmp_lst[0] = 0
    return tmp_lst

def gen_clr_codes_lst(clr_nmbr, scale):
    ''' gen color codes list '''
    if clr_nmbr <= 1:
        return [[clr_code] for clr_code in gen_clr_code_step_lst(scale)]
    else:
        rest_clr_code_lst = gen_clr_codes_lst(clr_nmbr - 1, scale)

    tmp_lst = []
    for clr_code in gen_clr_code_step_lst(scale):
        for item in rest_clr_code_lst:
            tmp_lst.append([clr_code] + item)
    return tmp_lst

def prnt_clr_tbls():
    ''' print color tables '''
    clr_seq_lst = gen_clr_seq(['r', 'g', 'b'])
    clr_codes = gen_clr_codes_lst(clr_nmbr=3, scale=5)

    # terminal color related vars
    clr_str_hdr = '\x1b[48;2;'  # 48 is bg, 38 is symbol color
    clr_str_ftr = '\x1b[0m'     # reset color
    text = ' '

    for clr_seq in clr_seq_lst:
        print(clr_seq)
        for clr_code in clr_codes:
            red = clr_seq.index('r')
            green = clr_seq.index('g')
            blue = clr_seq.index('b')
            clr_str = clr_str_hdr + \
                      str(clr_code[red]) + ';' + \
                      str(clr_code[green]) + ';' + \
                      str(clr_code[blue]) + 'm' + \
                      text + \
                      clr_str_ftr
            print(clr_str, end='')
            if clr_code[1] == clr_code[2] == 255:
                print()
        print()

if __name__ == '__main__':
    prnt_clr_tbls()
