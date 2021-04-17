t = []
r = []
soma_t = 0.0
soma_r = 0.0

print("==============TITULARES================")
for i in range(1,6):
    print("Informe o salário do ",i,"º Jogador:")
    val = round(float(input()),2)
    t.append(val)
print("==============RESERVAS=================")
for i in range(1,6):
    print("Informe o salário do ",i,"º Jogador:")
    val = round(float(input()),2)
    r.append(val)
int(input())
for salario in t:
    soma_t += round(salario,2)

for salario in r:
    soma_r += round(salario,2) 

g = t+r
soma_g = round((soma_t + soma_r),2)
media_t = round(soma_t/len(t),2)
media_r = round(soma_r/len(r),2)
media_g = round(soma_g/len(g),2)
t.sort()
menor_t = t[0]
t.sort(reverse=True)
maior_t = t[0]
r.sort()
menor_r = r[0]
r.sort(reverse=True)
maior_r = r[0]
g.sort()
menor_g = g[0]
g.sort(reverse=True)
maior_g = g[0]
print()
print("==============RESULTADO================")
print("Titulares:")
print(t)
print("Soma (R$):",soma_t)
print("Média (R$):",media_t)
print("Menor (R$):",menor_t)
print("Maior (R$):",maior_t)
print()
print("Reservas:")
print(r)
print("Soma (R$):",soma_r)
print("Média (R$):",media_r)
print("Menor (R$):",menor_r)
print("Maior (R$):",maior_r)
print()
print("Geral:")
print(g)
print("Soma (R$):",soma_g)
print("Média (R$):",media_g)
print("Menor (R$):",menor_g)
print("Maior (R$):",maior_g)
print()