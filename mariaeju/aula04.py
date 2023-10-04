salario = float(input("Informe o salário: ")) #Float usado para números decimais

if salario<= 3000:
    print("Programador junior")
#elif em outras linguagens é o else, porém no Phyton usamos elif combinado com and.(elif= então)
elif salario> 3000 and salario<= 6000:
    print("Programador pleno")
elif salario > 6000 and salario <= 15000:
    print("Programador Senior")
else:
    print("Gerente de projetos")