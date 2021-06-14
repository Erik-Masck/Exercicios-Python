from numeros import eh_primo
from numeros import lista_primos
from numeros import conta_primos
from numeros import eh_armstrong
from numeros import eh_quase_armstrong
from numeros import lista_armstrong
from numeros import eh_perfeito
from numeros import lista_perfeitos

#Os comentários abaixo representam os resultados esperados pelos testes!

teste_primos = [2, 5, 24, 19, 9, 30, 41]
#true, true, false, true, false, false, true
teste_lista_primos = 29
#[2, 3, 5, 7, 11, 13, 17, 19, 23]
teste_conta_primos = [97, 11, 8, 15, 11, 53, 11]
#{11:3 53:1 97:1}
teste_armstrong = [2, 10, 153, 15, 370, 4, 72]
#true, false, true, false, true, true, false
teste_quase_armstrong = [4, 35, 75]
#false, true, true
teste_lista_armstrong = 370
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 153]
teste_perfeito = [4, 25, 28, 72, 496, 6]
#false, false, true, false, true, true
teste_lista_perfeitos = 496
#[6,28]

def eh_primo(n):
    mtp=0
    if n>=2:
        for c_nt in range(2,n):
            if (n % c_nt == 0):
                mtp += 1
        if(mtp==0):
            return True
        else:
            return False
    else:
        return False
print("Teste eh_primo")
for x in teste_primos:
    print(eh_primo(x), end=" ")
print("")
print("")

def lista_primos(n):
    ln = [x for x in range(n)]
    l1 = list()
    l_dl = [x for x in ln if x != 0]
    for nmr in ln:
        tot_d = 0
        for dv in l_dl:
            if nmr % dv == 0:
                tot_d += 1
            elif nmr < dv:
                break
        if tot_d == 2:
            l1.append(nmr)
    return l1
teste_lista_primos = 29
# retorno [2, 3, 5, 7, 11, 13, 17, 19, 23]
print("Teste lista_primos")
print(lista_primos(teste_lista_primos))
print("")

def conta_primos(s):
    dc = dict()
    for aux in sorted(vlr):
        if eh_primo(aux):
            if aux in dc:
                dc[aux] += 1
            else:
                dc[aux] = 1
    return dc
print("Teste conta_primos")
print(conta_primos(teste_conta_primos))
print("")

def eh_armstrong(n):
    ordn = len(str(n))
    i = 0
    aux = n
    while aux > 0:
        digit = aux % 10
        i += digit ** ordn
        aux //= 10
    if (n == i):
        return True
    else:
        return False
print("Teste eh_armstrong")
for x in teste_armstrong:
    print(eh_armstrong(x), end=" ")
print("")
print("")

def eh_quase_armstrong(n):
    ordn = len(str(n))
    i = 0
    xuxa = n
    while xuxa > 0:
        digit = xuxa % 10
        i += digit ** ordn
        xuxa //= 10
    if (n == i-1)or(n==i+1)and(n>=0):
        return True
    else:
        return False
print("Teste eh_quase_armstrong")
for x in teste_quase_armstrong:
    print(eh_quase_armstrong(x), end=" ")
print("")
print("")

def lista_armstrong(n):
    l_1=list()
    soma=0
    for val in range(1,n-1):
        if(eh_armstrong(val)):
            l_1.append(val)
        elif(eh_armstrong==False):
            break
    return l_1
print("Teste lista_armstrong")
print(lista_armstrong(teste_lista_armstrong))
print("")

def eh_perfeito(n):
    totovs = 0
    for dv in range(1,n):
        if n % dv == 0:
            totovs += dv
    if n == totovs:
        return True
    else:
        return False
print("Teste eh_perfeito")
for x in teste_perfeito:
    print(eh_perfeito(x), end=" ")
print("")
print("")

def lista_perfeitos(n):
    l_1=list()
    soma=0
    for val in range(1,n-1):
        if(lista_perfeitos(val)):
            l_1.append(val)
        elif(lista_perfeitos==False):
            break
    return l_1
print("Teste lista_perfeitos")
print(lista_perfeitos(teste_lista_perfeitos))

