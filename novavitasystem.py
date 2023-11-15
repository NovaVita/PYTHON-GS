from datetime import datetime
import time
import json
import os

CADASTRO_JSON = 'cadastro.json'
DASHBOARD_JSON = 'dashboard.json'
DUVIDAS_JSON = 'duvidas.json'

lista = []
lista_cadastro = []
dicionario = {}

def formatar_data_hora(recv_time):
    # Converte o formato de tempo do JSON para o formato desejado
    data_hora = datetime.strptime(recv_time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return data_hora.strftime("%d/%m/%Y, %H:%M:%S")

def menu_NovaVita1():
        print('----------------------------------------------')
        print('                  \033[34mNovaVita\033[m                ')
        print('----------------------------------------------\n')
        print('1 - Cadastro no site da NovaVita')
        print('2 - Login no site da NovaVita')
        print('3 - Deletar cadastro')
        print('4 - Encerrar o programa\n')
        print('----------------------------------------------\n')
        try:
            escolha_menu1 = int(input("Escolha uma dessas duas opções: "))
            if escolha_menu1 >= 1 and escolha_menu1 <= 4:
                return escolha_menu1
            else:
                raise ValueError
        except ValueError:
            print("\n\033[31mDigite um número inteiro entre 1 e 4!\033[m\n")   
    
def validar_email(email):
    if "@" in email and "." in email:
        return True
    else:
        return False

# Função para validar a senha
def validar_senha(senha):
    if len(senha) >= 8:
        return True
    else:
        return False

def menu_NovaVita2():
    while True:
        try:
            with open(CADASTRO_JSON, 'r', encoding='utf-8') as arquivo:
                dados_cliente = json.load(arquivo)
            print('----------------------------------------------')
            print('                  \033[34mNovaVita\033[m                ')
            print('----------------------------------------------\n')
            for dic in dados_cliente:
                    if dic['e-mail'] == email:
                        print(f'\033[33mSeja bem vindo(a) {dic["nome"]}!\033[m\n')
            print('1 - Ver a última atualização do Soul')
            print('2 - Ver monitoramento')
            print('3 - Suporte especializado - dúvidas e perguntas')
            print('4 - Mostrar todas as operações realizadas')
            print('5 - Log-out\n')
            print('----------------------------------------------\n')

            escolha_menu2 = input("Escolha uma dessas duas opções: ")
        
            match int(escolha_menu2):
                case 1: 
                    print("\n\033[34múltima atualização dos componentes eletrônicos da Soul:\033[m") 
                    print("                    --                      ") 
                    print("Placa DOIT ESP32 (Bluetooth e Wifi)")
                    print("Sensor de oxigenação do sangue")
                    print("Sensor de glucose do sangue")
                    print("Sensor de monitoramento de frequência cardíaca e pressão arterial por infravermelho")
                    print("Sensor de Temperatura da pele (DeRoyal)")
                    print("                    --                      \n")
                    lista.append('Ver a última atualização dos componentes eletrônicos da Soul')
                case 2:
                    print('----------------------------------------------')
                    print('                  \033[34mNovaVita\033[m                ')
                    print('----------------------------------------------\n')
                    print("Escolha o sensor que deseja visualizar:")
                    print()
                    print("1 - Temperatura corporal")
                    print("2 - Oxigenação do sangue")
                    print("3 - Glucose no sangue")
                    print("4 - Frequencia cardíaca")
                    print("5 - Pressão arterial")
                    print()
                    try:
                        escolha_sensor = int(input("Escolha o sensor (1-5): "))
                        quantidade_leituras = int(input("Digite a quantidade de leituras desejada (max: 50): "))
                    except ValueError:
                        print()
                        print("\033[31mOpção inválida. Por favor, insira um número válido.\033[m")
                        print()
                        continue
                    
                    if escolha_sensor < 1 or escolha_sensor > 5:
                        print()
                        print("\033[31mSensor inválido. Por favor, escolha uma opção de sensor válida.\033[m")
                        print()
                        continue
                    
                    if quantidade_leituras > 50:
                        print()
                        print("\033[31mA quantidade de leituras não pode ser maior que 50.\033[m")
                        print()
                        continue
                    
                    with open(DASHBOARD_JSON, 'r', encoding='utf-8') as arquivo:
                        dados = json.load(arquivo)
                        
                        for sensor_data in dados:
                            sensor_name = sensor_data['name']
                            sensor_values = sensor_data['values']
                            
                            if escolha_sensor == 1 and sensor_name != 'temperature':
                                continue
                            elif escolha_sensor == 2 and sensor_name != 'oxigenacao':
                                continue
                            elif escolha_sensor == 3 and sensor_name != 'glucose':
                                continue
                            elif escolha_sensor == 4 and sensor_name != 'frequencia':
                                continue
                            elif escolha_sensor == 5 and sensor_name != 'pressao':
                                continue

                            sensor_nome_dash = sensor_name
                            unidade_sensor = ""
                            
                            if sensor_name == 'temperature':
                                sensor_nome_dash = "Temperatura Corporal"
                                unidade_sensor = "°C"
                            elif sensor_name == 'oxigenacao':
                                sensor_nome_dash = "Oxigenação Sanguinea"
                                unidade_sensor = "%"
                            elif sensor_name == 'glucose':
                                sensor_nome_dash = "Glucose no sangue"
                                unidade_sensor = "mg/dL"
                            elif sensor_name == 'frequencia':
                                sensor_nome_dash = "Frequencia Cardíaca"
                                unidade_sensor = "bpm"
                            elif sensor_name == 'pressao':
                                sensor_nome_dash = "Pressão Arterial"
                                unidade_sensor = "mmHg"

                            print()
                            print(f"\033[34mÚltimas {quantidade_leituras} leituras de {sensor_nome_dash}:\033[m")
                            print()
                            
                            for value in sensor_values[-quantidade_leituras:]:
                                valores = value['attrValue']
                                data_hora = value['recvTime']
                                data_hora_formatados = datetime.strptime(data_hora, "%Y-%m-%dT%H:%M:%S.%fZ").strftime("%d/%m/%Y, %H:%M:%S")
                                print(f"{valores} {unidade_sensor} - {data_hora_formatados}")
                                print()
                        lista.append('Ver monitoramento')
                case 3:
                    if os.path.exists(DUVIDAS_JSON):
                        with open(DUVIDAS_JSON, 'r', encoding='utf-8') as arquivoduvidas:
                            duvidas_existente = json.load(arquivoduvidas)
                    else:
                        duvidas_existente = []
                    for i in range(5):
                        i = "."
                        print(i)
                    num = None
                    while num is None:
                        try:
                            num = int(input("Digite a quantidade de dúvidas (0 para sair): "))
                            if num == 0:
                                print('\nAgradecemos pela colaboração.\n')
                                lista.append("Suporte especializado - Não teve nenhuma dúvida")
                                break
                            elif num < 1:
                                print("\n\033[31mPor favor, insira um número positivo.\033[m")
                                num = None
                            else:
                                contador = 0
                                while contador < num:
                                    duvida = input(f"Escreva sua {contador + 1}ª dúvida ao lado: ")
                                    print()
                                    print(f"{duvida}\n")
                                    contador += 1
                                    duivida_input = {f'Duvida {contador}': duvida}

                                    duvidas_existente.append(duivida_input)
                                    with open(DUVIDAS_JSON, 'w', encoding='utf-8') as arquivoduvidas:
                                        json.dump(duvidas_existente, arquivoduvidas, indent=4, ensure_ascii=False)
                                
                                print("\nAgradecemos pelas dúvidas. Elas serão analisadas e retornadas em breve no seu e-mail...\n")
                                lista.append("Suporte especializado - Teve dúvida")
                        except ValueError:
                            print("Digite um número inteiro válido.")
                        print()
                case 4:
                    try:
                        print()
                        resposta = input("Deseja ver o resumo de operações realizadas do menu? (sim/não): ").lower()
                        print()
                        if resposta.isdigit():
                            raise ValueError
                        elif resposta == "não" or resposta == "n" or resposta == "nao":
                            print("Obrigado por utilizar o programa!")   
                        elif resposta == "sim" or resposta == "s":
                            print("Resumo das operações realizadas:")
                            print()
                            for n in lista:
                                print(f"\033[34m{n}\033[m")
                            lista.append("Mostrar todas as operações realizadas")
                        print()
                        
                        resposta2 = input("Deseja continuar? (sim/não): ").lower()
                        print() 
                        if resposta2.isdigit():
                            raise ValueError
                        elif resposta2 == "não" or resposta2 == "n" or resposta2 == "nao":
                            print(f'\033[33mObrigado pela compreensão! Te esperamos em breve novamente!\033[m\n')
                            for dic in dados_cliente:
                                if dic['e-mail'] == email:
                                    print(f'\033[33mObrigado por usar nossos serviços {dic["nome"]}!\033[m\n')
                            return True
                    except ValueError:
                        print('\033[31mDigite apenas sim ou não!\033[m\n')  
                case 5:
                    for dic in dados_cliente:
                        if dic['e-mail'] == email:
                            print(f'\n\033[33mObrigado por usar nossos serviços {dic["nome"]}!\033[m\n')
                    return True
                case _:
                    print("\n\033[31mError!! Número inválido!\033[m \n")
        except ValueError:
            print("\n\033[31mDigite um número inteiro!\033[m\n")                

while True:
    escolha_menu1 = menu_NovaVita1() 
    try:
        # Verifica o tamanho do arquivo
        tamanho_arquivo = os.path.getsize('cadastro.json')

        if tamanho_arquivo > 0:
            with open(CADASTRO_JSON, 'r', encoding='utf-8') as arquivo:
                lista_cadastro = json.load(arquivo)
            with open(CADASTRO_JSON, 'r', encoding='utf-8') as arquivo:
                lista_cadastro_existentes = json.load(arquivo)
        else:
            # O arquivo está vazio, inicializa a lista como vazia
            lista_cadastro = []
            lista_cadastro_existentes = []
    except FileNotFoundError:
        # O arquivo não foi encontrado
        lista_cadastro = []
        lista_cadastro_existentes = []
    except json.JSONDecodeError:
        # O arquivo existe, mas não pode ser decodificado como JSON
        print("\n\033[31mErro ao ler o arquivo JSON. O arquivo pode estar corrompido.\033[m")
        lista_cadastro = []
        lista_cadastro_existentes = []

    if escolha_menu1 == 1:
        current_time = datetime.now()
        print(f"\nHora atual: {current_time.strftime('%H:%M:%S')}")
        time.sleep(1)

        while True:
            nome = input('\nDigite o seu nome: ')
            email = input('Informe seu e-mail: ')
            senha = input('Digite sua senha (8 caracteres): ')

            email_valido = validar_email(email)
            senha_valida = validar_senha(senha)

            # if email_valido and senha_valida:
            #     break
            # else:
            if not email_valido and not senha_valida:
                print("\n\033[31mEmail e senha inválidos! Tente novamente!\033[m")
            elif not email_valido:
                print("\n\033[31mEmail inválido! Certifique-se de usar um formato de email válido.\033[m")
            elif not senha_valida:
                print("\n\033[31mSenha inválida! A senha deve ter pelo menos 8 caracteres.\033[m")
            else:
                email_existente = False
                for cadastro_existente in lista_cadastro:
                    if cadastro_existente['e-mail'] == email:
                        email_existente = True

                if email_existente == True:
                    print("\n\033[31mEste email já está cadastrado! Tente com um email diferente.\033[m\n")
                else:
                    cadastro = {'nome': nome, 'e-mail': email, 'senha': senha}
                    lista_cadastro.append(cadastro)
                    print('\n\033[32mCadastro realizado com sucesso!\033[m\n')
                    lista.append("Cadastro no site do NovaVita")
                try:
                    with open(CADASTRO_JSON, 'w', encoding='utf-8') as arquivo:
                        json.dump(lista_cadastro, arquivo, indent=4, ensure_ascii=False)
                    break
                except IOError:
                    print("\n\033[31mErro ao salvar o cadastro. Por favor, tente novamente.\033[m")

    elif escolha_menu1 == 2:
        current_time = datetime.now()
        print(f"\nHora atual: {current_time.strftime('%H:%M:%S')}\n")
        time.sleep(1)

        if os.path.exists(CADASTRO_JSON) and lista_cadastro: 
            email = input('Informe seu e-mail: ')
            senha = input('Digite sua senha(8 caracteres): ')
            
            email_valido = validar_email(email)
            senha_valida = validar_senha(senha)

            if email_valido and senha_valida:
                for cadastro_existente in lista_cadastro:
                    if cadastro_existente['e-mail'] == email and cadastro_existente['senha'] == senha:
                        print("." * 5)
                        print("Sincronizando com a sua conta...")
                        print("." * 5)
                        print("\n\033[32mSeja bem-vindo ao NovaVita!\033[m\n")
                        lista.append('Login no site da NovaVita')
                        retorno = menu_NovaVita2()
                        if retorno == True:
                            break
                else:
                    print("\n\033[31mOs dados não corresponderam com o do cadastro feito!\033[m\n")
            else:
                print("\n\033[31mE-mail ou senha inválidos! Tente novamente!\033[m\n")
        else:
            print('\033[31mNão existe nenhum cadastro no banco de dados!\033[m\n')
    elif escolha_menu1 == 3:
        if os.path.exists(CADASTRO_JSON) and lista_cadastro_existentes:
            teste = True
            while teste:
                email = input('Informe seu e-mail: ')
                senha = input('Digite sua senha: ')

                email_valido = validar_email(email)
                senha_valida = validar_senha(senha)
                encontrado = False

                if email_valido and senha_valida:
                    for cadastro_existente in lista_cadastro_existentes:
                        if cadastro_existente['e-mail'] == email and cadastro_existente['senha'] == senha:
                            lista_cadastro_existentes.remove(cadastro_existente)
                            lista.append('Deletar cadastro')
                            try:
                                with open(CADASTRO_JSON, 'w', encoding='utf-8') as arquivo:
                                    json.dump(lista_cadastro_existentes, arquivo, indent=4, ensure_ascii=False)
                                print('\n\033[32mCadastro deletado realizado com sucesso!\033[m\n')
                                teste = False
                                encontrado = True
                                break
                            except IOError:
                                print("\n\033[31mErro ao salvar a lista de cadastros. Por favor, tente novamente.\033[m")
                                print()
                    if not encontrado:
                        print("\n\033[31mE-mail e/ou senha inválidos! Tente novamente!\033[m\n")
                else:
                    print("\n\033[31mE-mail e/ou senha em formato invalidos! Tente novamente!\033[m\n")
        else:
            print('\n\033[31mNão existe nenhum cadastro no banco de dados!\033[m\n')

    elif escolha_menu1 == 4:
        break
    
