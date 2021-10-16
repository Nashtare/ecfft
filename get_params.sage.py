

# This file was *autogenerated* from the file get_params.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_64 = Integer(64); _sage_const_1 = Integer(1); _sage_const_4 = Integer(4); _sage_const_0x30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd47 = Integer(0x30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd47); _sage_const_5612291247948481584627780310922020304781354847659642188369727566000581075360 = Integer(5612291247948481584627780310922020304781354847659642188369727566000581075360); _sage_const_0 = Integer(0)
def to_limbs(x):
    mask = _sage_const_2 **_sage_const_64  - _sage_const_1 
    return [(x>>(_sage_const_64 *i)) & mask for i in range(_sage_const_4 )]

p = _sage_const_0x30644e72e131a029b85045b68181585d97816a916871ca8d3c208c16d87cfd47 
F = GF(p)
a,b = _sage_const_1  ,_sage_const_5612291247948481584627780310922020304781354847659642188369727566000581075360 
E = EllipticCurve(F, [a,b])
n = E.order().p_primary_part(_sage_const_2 )
log_n = n.log(_sage_const_2 )

g = E.gens()[_sage_const_0 ]
G = (g.order()//n) * g
assert G.order() == n

R = E.random_element()
H = [R + i*G for i in range(_sage_const_2 **log_n)]
L = [h.xy()[_sage_const_0 ] for h in H]
S = [L[i] for i in range(_sage_const_0 , n, _sage_const_2 )]
S_prime = [L[i] for i in range(_sage_const_1 , n, _sage_const_2 )]

s = "\n".join([str(l) for x in L for l in to_limbs(int(x))])
open('yo', 'w').write(s)

def isogenies(log_n, S, S_prime, E):
    isos = []
    for i in range(log_n, _sage_const_0 , -_sage_const_1 ):
        n = _sage_const_1  << i
        nn = n // _sage_const_2 

        for iso in E.isogenies_prime_degree(_sage_const_2 ):
            psi = iso.x_rational_map()
            if len(set([psi(x) for x in S]))==nn:
                break
        isos.append(psi)
        S = [psi(x) for x in S[:nn]]
        S_prime = [psi(x) for x in S_prime[:nn]]
        E = iso.codomain()

    return isos

isos = isogenies(log_n-_sage_const_1 , S, S_prime, E)
print(len(isos))
s = "\n".join([str(l) for psi in isos for coeff in list(psi.numerator())+list(psi.denominator()) for l in to_limbs(int(coeff))])
open('ya', 'w').write(s)



