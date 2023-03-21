#             .^!)cCCUXzYUYzccXUJJJYr\[i^           I
#           :]/ff/\([+ilII;:;l>~<>i<}xYUn\]"        I
#         ;(vcx{"                    '!{jcYx}"      I
#       '[cQQJzuxnj)<"     .:-)trnur(>'  ^>tx),.    I
#      ;(JqpQ       z].  "tQZJ      Cu}:  'ixY/^    I
#     +YmbdJ /j|_    OQ[.`/qwXtjd     n0wv;  :cmJ-  I
#    ./q*#q\ ~)|-    Qbv`,uOz}?(      YZc!  "jLU/^  I
#    InZppZz        uZQ? ;cwQj        0Zx;   <jux?. I
#    -xzn))z        QQu?. .I(Y       Lu[:    '(uc\^ I
#   ,/rt-  l{fnvccf[!`      :-rvvzXcf],      ')vc|^ I
#   lfj/+`     ...                ..         ')xr<  I
#   .+jvjl         ^I!+{)|/t(_;'21             ;rv/ I
#    '/QU]        ?uJ           ct+"          .{CJ\ I
#     +UUf"      >tj            nzfi         <vQU]  I
#     ^[uXu]`  '}Yz              z/i.     "}uXr_`   I
#      .-XmU)" .{QO              bqc;   "?xYv]"     I
#        :/vji  ^}\|1[]]_+_??+~?/zn?. '+jXX/i       I
#       '!)[;.                   .   !\ct-;.        I
#     .!/cnI                       l/CC\"           I
#   .l1xr|~.                      ^\Xc|,            I
#    `I>,'                         ^:^              I
a=input()
b=input()

def su(e):
    return sum(map(ord,list(e)))

if len(a)==len(b):
    if su(a)==su(b):
        print("2")
    elif a.upper()==b.upper():
        print("3")
    elif su(a.upper())!=su(b.upper()):
        print("4")
elif len(a)!=len(b):
    print("1")
else:
    pass
