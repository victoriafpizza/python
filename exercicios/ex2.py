# Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categoria de 
# acordo com as seguintes condições:

# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.

print("por favor insira sua idade")
idade = int(input())

if idade > 0 and idade < 12:
    print("voce é criança")
elif idade >= 13 and idade <= 18:
    print("voce é adolescente")
else: 
    print("voce é adulto")

