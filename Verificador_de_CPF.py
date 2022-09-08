#Programa Verificador de CPF
print('Olá caro(a) usuário(a)! Este é um programa verificador de cpf!\n')
print('Temos duas formas de funcionamento:\n')
print('Pressione 1 -> Inserir o valor inteiro do cpf e retornamos se é válido ou não;\n')
print('Pressione 2 -> Inserir os nove(9) primeiros números e retornamos o código de verificação(os dois últimos dígitos do respectivo CPF.\n')
escolha = int(input('Digite aqui a funcionalidade desejada!: '))

def remove_pontos_tracos(cpf):
    cpf = cpf.replace('-','').replace('.','')
    return cpf

#Tratamento de Informação

while (escolha != 1 and escolha != 2):
    aviso   = print('Você não inseriu valores inteiros entre 1 e 2,pr favor digite novamente o seu objetivo.\n')
    escolha = int(input('Digite aqui a funcionalidade desejada!: '))
    if (escolha == 1 or escolha == 2):
        print('\n')
        break

#Opcional 1: Verificação do CPF

if(escolha ==1):
    cpf, c1,c2 =input('insira o cpf que deseja ser consultado.\n'), 10, 11
    cpf= remove_pontos_tracos(cpf)

    matriz=[int(valor) for valor in cpf] #list comprehension: loop que cria uma lista 

    soma, Resposta,Tamanho = 0,0, len(cpf)
    for j in range(len(cpf)-2):
        Resposta += (Tamanho-1) * int(cpf[j])
        Tamanho = Tamanho-1
    #print('\n')
    #print('Somatório 1: ',Resposta)

    resp = Resposta *10
    resto_1= resp % 11
    if resto_1 == 10:
        resto_1=0
        dig_1=resto
    else:
        dig_1= resp % 11
    #print('O primeiro Dígito Verificador é: ', dig_1)

    Tamanho_2, Resposta_2= len(cpf), 0

    #print('Resposta_2: ',Resposta_2)
    for m in range(len(cpf)-1):
        Resposta_2 += (Tamanho_2) * int(cpf[m])
        Tamanho_2 -=1
        #print('cpf[',m,']: ', cpf[m])
        #print('Tamanho_2: ',Tamanho_2)
        #print('\n')
    #print('Somatório 2: ',Resposta_2)

        
    resp_2= Resposta_2 *10

    dig_2= resp_2 % 11
    #print('O segundo dígito verificador: ',dig_2)

    cpf_str=[]
    cpf_str= str(cpf)
    d1=str(dig_1)
    d2=str(dig_2)
    soma_d1_d2=d1+d2

    if (cpf_str[9:11] == soma_d1_d2):
        print('O cpf digitado --->',cpf,' é válido!')
    else:
        print('Infelizmente o cpf digitado --->',cpf,' é inválido!')
#Opcaional 2
else:
    
    cpf_2= input('Por favor, digite os nove(9) primeiros números e retornamremos o código de verificação!:')
    cpf_2= remove_pontos_tracos(cpf_2)

    matriz_2=[int(valor_2) for valor_2 in cpf_2] #list comprehension: loop que cria uma lista

    
    Resultado, comprimento = 0, len(cpf_2)
    for s in range(len(cpf_2)):
        Resultado += (comprimento+1) * int(cpf_2[s])
        comprimento -= 1
    #print('\n')
    #print('Somatório 1: ',Resultado)

    result = Resultado *10
    r1= result % 11
    if r1 == 10:
        r1=0
        dig_ver_1=r1
    else:
        dig_ver_1= r1
    #print('O primeiro Dígito Verificador é: ', dig_ver_1)

    Resultado_2= 0  
    cpf_str1=str(cpf_2)
    str_d1=str(dig_ver_1)
    cpf_str1 += str_d1
    print(cpf_str1)

    matriz_2=[int(valor_2) for valor_2 in cpf_str1] #list comprehension: loop que cria uma lista
    comprimento_2= len(cpf_str1)
    for t in range(len(cpf_str1)):
        Resultado_2 += (comprimento_2+1) * int(cpf_str1[t])
        comprimento_2 -= 1
        #print('cpf[',m,']: ', cpf[m])
        #print('Tamanho_2: ',Tamanho_2)
        #print('\n')
    #print('Somatório 2: ',Resultado_2)

        
    result_2= Resultado_2 *10
    dig_ver_2= result_2 %11
    #print('O segundo dígito verificador: ',dig_ver_2)

    cpf_str2= cpf_str1
    digito1=str(dig_ver_1)
    digito2=str(dig_ver_2)
    soma_digito_1_digito2= digito1 + digito2
    soma_cpf= cpf_str2 + digito2

    print('O seu código verificador do cpf: ',cpf_2,' é: ',soma_digito_1_digito2)
    print('\n')
    print('então o seu cpf completo fica: ', soma_cpf[0:3],'.',soma_cpf[3:6],'.',soma_cpf[6:9],'-',soma_cpf[9:11])
















