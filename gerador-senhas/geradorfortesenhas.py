import random

def mudarposicao(string):
    listaTemporaria = list(string)
    random.shuffle(listaTemporaria)
    return ''.join(listaTemporaria)

tipoCaractere1 = chr(random.randint(30,90))
tipoCaractere2 = chr(random.randint(30,90))
tipoCaractere3 = chr(random.randint(45,90))
tipoCaractere4 = chr(random.randint(45,90))
tipoCaractere5 = chr(random.randint(50,90))
tipoCaractere6 = chr(random.randint(50,90))
tipoCaractere7 = chr(random.randint(65,90))
tipoCaractere8 = chr(random.randint(65,90))

senha = tipoCaractere1 + tipoCaractere2 + tipoCaractere3 + tipoCaractere4 + tipoCaractere5 + tipoCaractere6 + tipoCaractere7 + tipoCaractere8
senha = mudarposicao(senha)

print(senha)
    
 