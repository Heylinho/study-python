# Arquivo: exemplo4_for.py
# Dicionário --> chave e valor

aluno = { "nome" : "João" , "idade" : 20 , "cpf" : "123.456.789-10" , "curso" : "Gestão TI" }

for chave, valor in aluno.items() :
    print( f"{chave} --> {valor}" )