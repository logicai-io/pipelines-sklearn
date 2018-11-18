from IPython.core.display import HTML

# naive encode a string by a number, simple obfuscator for solutions
def encode(str_, shift):
    return ''.join(map(chr, [(ord(_)+shift) % 256 for _ in str_]))

def decode(str_, shift):
    return ''.join(map(chr, [(ord(_)-shift) % 256 for _ in str_]))

def _get_solution(encrypted_solution):
    number = raw_input('Magic number for solution: ')
    return decode(encrypted_solution, int(number))

solutions = {
    0: '\xcb\x1a06\xe1(05\xe1*5\xe13*()5\xe2\xcb\x15)"5\xe18"4/\xe85\xe1506()\xed\xe1#65\xe145*--\xed\xe1:06\xe1(&5\xe1"\xe14."--\xe113*;&\xed\xe1"\xe11:5)0/\xe1\x06"45&3\xe1&((\xef\xcb\x101&/\xe161\xe11:5)0/\xe1*/\xe15&3.*/"-\xe1"/%\xe15:1&\xe150\xe1(&5\xe1"\xe15*/:\xe146313*;&\xfb\xcb*.1035\xe1"/5*(3"7*5:',
    1: '4\x91\x93\x9eJ\x96\x99\x91JWW\x98\x8b\x97\x8fW\x99\x98\x96\xa3J\xa6J\x91\x9c\x8f\x9aJZZ\x89\x93\x98\x9e\x9c\x994\x91\x93\x9eJ\x96\x99\x91JWW\x98\x8b\x97\x8fW\x9d\x9e\x8b\x9e\x9f\x9dJ\xa6J\x91\x9c\x8f\x9aJZZ\x89\x93\x98\x9e\x9c\x994MJ\x9e\x92\x8fJ\x98\x93\x98\x94\x8bJ\xa1\x8b\xa34\x91\x93\x9eJ\x96\x99\x91JWWJZZ\x89\x93\x98\x9e\x9c\x99X\x93\x9a\xa3\x98\x8c',
    2: ';;h72h6eh;9;5ce4f8532gf54;:6hc6:;f;5d4g:',
    3: '\x19sxuu/<<vx\x83/p>\x81\x84}=\x7f\x88/q>\x81\x84}=\x7f\x88\x19x}st\x87/FDrs?DB==CuutCDA/@??ECC\x19<<</p>\x81\x84}=\x7f\x88\x19:::/q>\x81\x84}=\x7f\x88\x19OO/<@;D/:@;D/OO\x19/stu/|px}78I\x19<////\x81t\x83\x84\x81}/6X\x83/x\x82/p/\x86t{{/z}~\x86}/upr\x83/\x83wp\x83/be]/qtp\x83\x82/vx\x8306\x19:////\x81t\x83\x84\x81}/6X\x83/x\x82/p/\x86t{{/z}~\x86}/upr\x83/\x83wp\x83/vx\x83/qtp\x83\x82/be]06\x19\x19/xu/nn}p|tnn/LL/6nn|px}nn6I\x19/////\x7f\x81x}\x83/|px}78',

}

def get_solution(no):
    print(_get_solution(solutions[no]))

def css_from_file(*filenames):
    css_frame = '<style>%s</style>'
    html = ''
    for filename in filenames:
        with open(filename) as f:
            html += f.read()
    return HTML(css_frame % html)
