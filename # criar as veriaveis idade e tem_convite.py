# criar as veriaveis idade e tem_convite

idade = float(input("digite a idade"))

tem_convite = True #booleano

if idade>= 18:
    if tem_convite:
        print("pode entar na festa")
    else :
        print("prcisa de um convite para entar na festa")
else :   print("nao pode entar . E menor de idade")
 