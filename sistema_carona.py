import os
passageiros = list()
motoristas = list()
admin = list()
caronas = list()
emergencia = list()
roxo = '\033[95m'
verde = '\033[92m'
vermelho = '\033[91m'
azul = '\033[94m'
chaveAcesso = '23052005'
while True:
    bemvindo = f"""{roxo}
 ____  ______ __  __    __      _______ _   _ _____   ____               ____      _____        _____ _______ _____ _    _ _ 
|  _ \|  ____|  \/  |   \ \    / /_   _| \ | |  __ \ / __ \        /\   / __ \    |  __ \ /\   |  __ \__   __|_   _| |  | | |
| |_) | |__  | \  / |    \ \  / /  | | |  \| | |  | | |  | |      /  \ | |  | |   | |__) /  \  | |__) | | |    | | | |  | | |
|  _ <|  __| | |\/| |     \ \/ /   | | | . ` | |  | | |  | |     / /\ \| |  | |   |  ___/ /\ \ |  _  /  | |    | | | |  | | |
| |_) | |____| |  | |      \  /   _| |_| |\  | |__| | |__| |    / ____ \ |__| |   | |  / ____ \| | \ \  | |   _| |_| |__| |_|
|____/|______|_|  |_|       \/   |_____|_| \_|_____/ \____/    /_/    \_\____/    |_| /_/    \_\_|  \_\ |_|  |_____|\____/(_)                                                                                                                                                                                                                  
    """
    bemvindoCenter = bemvindo.center(60, " ")
    print(f"{roxo}=" * 127)
    print(bemvindoCenter)
    print(f"{roxo}=" * 127)

    opcao = input("\nEscolha uma das opções\n\n"
                    "[1] - Cadastro\n"
                    "[2] - Login\n" 
                    "[0] - Logout\n\n" 
                    "Opção: ")
    
    if (opcao == '0'):
        print("Saindo...")
        break

    elif(opcao == '1'):
        os.system('cls' if os.name == 'nt' else 'clear')
        bemvindo = f"""{roxo}
   _____          _           _             
  / ____|        | |         | |            
 | |     __ _  __| | __ _ ___| |_ _ __ ___  
 | |    / _` |/ _` |/ _` / __| __| '__/ _ \ 
 | |___| (_| | (_| | (_| \__ \ |_| | | (_) |
  \_____\__,_|\__,_|\__,_|___/\__|_|  \___/                                                                                                                                                                                                               
    """
        bemvindoCenter = bemvindo.center(80)
        print(f"{roxo}=" * 80)
        print(bemvindoCenter)
        print(f"{roxo}=" * 80)

        op = input("Escolha uma das opções\n\n" \
                    "[1] - Passageiro\n" \
                    "[2] - Motorista\n"
                    "[3] - Admin\n" \
                    "[0] - Sair\n\n" \
                    "Opção: ")   

        if (opcao == '0'):  
            print("\nSaindo...")
            os.system('cls' if os.name == 'nt' else 'clear')     
            break
        
        elif (op == '1'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de passageiros!\n")

            nome = input("Informe seu nome: ")
            email = input("Informe um email: ")
            emailValidacao = False
            while not emailValidacao:
                if (email.endswith("@gmail.com")):
                    emailValidacao = True
                else:
                    print(f"{vermelho}Email invalido!")
                    email = input(f"{roxo}Informe um email valido: ")
            
            if (email in passageiros):
                print(f"{vermelho}Email ja existente no nosso sistema!\n")
                print(f"{vermelho}Tente novamente com outro email!")
            else:
                senha = input("Informe uma senha: ")
                usuario = {
                    'email': email,
                    'nome': nome,
                    'senha': senha,
                    'vagasOcupada': 0,
                    'saldo': 0
                }
                passageiros.append(usuario)
                print(f"{verde}Passageiro cadastrado!")
                input(f"{roxo}Aperte enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif(op == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de motoristas!\n")          

            nome = input(f"{roxo}Informe seu nome: ")
            email = input(f"{roxo}Informe um email: ")
            emailValidacao = False
            while not emailValidacao:
                if (email.endswith("@gmail.com")):
                    emailValidacao = True
                else:
                    print(f"{vermelho}Email invalido!")
                    email = input(f"{roxo}Informe um email valido: ")
            
            if (email in motoristas):
                print(f"{vermelho}Email ja existente no nosso sistema!\n")
                print(f"{vermelho}Tente novamente com outro email!")
            else:
                senha = input("Informe uma senha: ")
                usuario = {
                    'email': email,
                    'nome': nome,
                    'senha': senha,
                }
                motoristas.append(usuario)
                print(f"{verde}Motorista cadastrado!")
                input(f"{roxo}Aperte enter para continuar...")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif(op == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"{roxo}\nCadastro de motoristas!\n")          

            chave = input(f"{roxo}Informe a chave de acesso: ")

            if (chave == chaveAcesso):
                print(f"{roxo}Acesso permitido!")

                nome = input(f"{roxo}Informe seu nome: ")
                email = input(f"{roxo}Informe um email: ")
                emailValidacao = False
                while not emailValidacao:
                    if (email.endswith("@gmail.com")):
                        emailValidacao = True
                    else:
                        print(f"{vermelho}Email invalido!")
                        email = input(f"{roxo}Informe um email valido: ")

                if (email in motoristas):
                    print(f"{vermelho}\nEmail ja existente no nosso sistema!\n")
                    print(f"{vermelho}Tente novamente com outro email!")
                else:
                    senha = input(f"{roxo}Informe uma senha: ")
                    usuario = {
                        'email': email,
                        'nome': nome,
                        'senha': senha,
                    }
                    admin.append(usuario)
                    print(f"{verde}Admin cadastrado!")   
                    input(f"{roxo}Aperte enter para continuar...") 
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print(f"{vermelho}Acesso negado!")
                input(f"{roxo}Aperte enter para continuar...") 
                os.system('cls' if os.name == 'nt' else 'clear')
                break
            
        
    elif(opcao == '2'):
        os.system('cls' if os.name == 'nt' else 'clear')
        bemvindo = f"""{roxo}
  _      ____   _____ _____ _   _ 
 | |    / __ \ / ____|_   _| \ | |
 | |   | |  | | |  __  | | |  \| |
 | |   | |  | | | |_ | | | | . ` |
 | |___| |__| | |__| |_| |_| |\  |
 |______\____/ \_____|_____|_| \_|                                                                                                                                                                                                                                       
    """
        bemvindoCenter = bemvindo.center(60, " ")
        print(f"{roxo}=" * 60)
        print(bemvindoCenter)
        print(f"{roxo}=" * 60)
        print(f"{roxo}Faça seu login!\n")
        usuario_encontrado = False
        emailLogin = input(f"{roxo}Informe seu email: ")
        for p in passageiros:
            if (emailLogin == p["email"]):
                senhaLogin = input(f"{roxo}Informe sua senha: ")
                if (senhaLogin == p["senha"]):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    usuario_encontrado = True
                    print(f"{verde}Login concluido!")
                    print(f"{roxo}\nBem vindo {p["nome"]} ao partiu!\n")
                    while True:
                        op = input(f"{roxo}\nEscolha uma das opções\n\n"
                                    "[1] Lista de caronas disponiveis\n"
                                    "[2] Origem e destino\n"
                                    "[3] Reserva vaga\n"
                                    "[4] Cancelar reserva\n"
                                    "[5] Detalhes de carona\n"
                                    "[6] Caronas cadastradas\n"
                                    "[7] SOS\n"
                                    "[8] Depositar dinheiro\n"
                                    "[9] Verificar SOS\n"
                                    "[0] Logout\n\n" 
                                    "Opção: ")
                        
                        if (op == '0'):
                            break

                        elif(op == '1'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Lista de caronas disponiveis!\n")
                            print(f"{roxo}="*60)
                            for c in caronas:
                                print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                print(f"{roxo}="*60)
                            
                            input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif(op == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Origem e destino!\n")

                            origemBusca = input(f"{roxo}Informe a origem: ")
                            destinoBusca = input(f"{roxo}Informe o destino: ")

                            for c in caronas:
                                if (origemBusca in c["origem"] and destinoBusca in c["destino"]):
                                    print(f"{roxo}\nCarona encontrada!\n")
                                    print(f"{roxo}=" * 60)
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    print(f"{roxo}=" * 60)

                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}\nNenhuma carona encontrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif (op == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Reservar vagas!\n")

                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print(f"{roxo}=" * 60)
                                    print(f"{roxo}\nCarona encontrada!\n")
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    reserva = input(f"{roxo}\nDeseja reserva uma vaga (s/n): ").upper()

                                    if (reserva == 'S'):
                                        if (p["saldo"]  < c["valor"]):
                                            print(f"{vermelho}Saldo insuficiente!")
                                            break
                                        elif(c["vagas"] == 0):
                                            print(f"{vermelho}Vagas esgotadas!")
                                            break
                                        else:
                                            print(f"{verde}Vaga reservada!")
                                            c["vagas"] -= 1
                                            p["saldo"] -= c["valor"]
                                            c["passageiros"].append(p["nome"])
                                            input(f"{roxo}Aperte enter para continuar...") 
                                            break
                                    else:
                                        break
                                else:
                                    print(f"{vermelho}\nCarona não encontrada!\n")
                                    input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif (op == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Remover reserva!\n")

                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                        print(f"{roxo}=" * 60)
                                        print(f"{verde}\nCarona encontrada!\n")
                                        print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}.")
                                        reserva = input(f"{roxo}\nDeseja remover sua vaga (s/n): ").upper()

                                        if (reserva == 'S'):
                                            senha = input(f"{roxo}Informe sua senha: ")
                                            if (senha == p["senha"]):
                                                print(f"{verde}Reservada cancelada!")
                                                c["vagas"] += 1
                                                p["saldo"] += c["valor"]
                                                c["passageiros"].remove(p["nome"])
                                                input(f"{roxo}Aperte enter para continuar...") 
                                            else:
                                                print(f"{vermelho}Senha invalida!\n")
                                                print(f"{vermelho}Tente novamente cancelar sua reserva!")
                                                input(f"{roxo}Aperte enter para continuar...") 
                                        else:
                                            break
                                else:
                                    print(f"{vermelho}\nCarona não encontrada!\n")

                        elif(op == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Detalhes da carona!\n")
                            
                            emailBusca = input(f"{roxo}Informe o email do motorista: ")
                            dataBusca = input(f"{roxo}Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print(f"{roxo}=" * 60)
                                    print(f"{verde}\nCarona encontrada!\n")
                                    print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}")
                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}Carona não encontrada!")
                                    input(f"{roxo}Aperte enter para continuar...") 
                        
                        elif (op == '6'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Caronas Cadastradas!\n")
                            print(f"{roxo}="*60)
                            for c in caronas:
                                print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]},\n"
                                        f"Passageiros: {c["passageiros"]}")
                                print(f"{roxo}="*60)

                            input(f"{roxo}Aperte enter para continuar...") 

                        elif(op == '7'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Corrida de emergência!\n")

                            origem = input("Informe a origem: ")
                            destino = input("Informe o destino: ")
                            data = input("Informe a data (dia/mes/ano): ")
                            hora = input("Informe o horario aproximado (hora:minutos): ")
                            motivo = input("Informe o motivo: ")

                            dadosEmergencia = {
                                'nome': p["nome"],
                                'email': p["email"],
                                'origem': origem,
                                'destino': destino,
                                'data': data,
                                'hora': hora,
                                'motivo': motivo,
                                'motorista': '',
                                'atendido': False
                            }

                            emergencia.append(dadosEmergencia)
                            print(f"{verde}Corrida de emergência concluido. Espero um motorista aceitar!")
                            input(f"{roxo}Aperte enter para continuar...") 

                        elif(op == '8'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Depositar dinheiro!\n")

                            valor = float(input("Informe o valor do deposito: "))

                            p["saldo"] += valor
        
                            print(f"{verde}\nDeposito efetuado!")
                            print(f"{roxo}Seu saldo: R${p["saldo"]}")
                            input(f"{roxo}Aperte enter para continuar...") 

                        elif (op == '9'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{roxo}Verificar se o chamado foi atendido!\n")

                            for e in emergencia:
                                if (e["atendido"] == True):
                                    print(f"{verde}Sua corrida foi aceita!")
                                    print(f"{roxo}Nome do motorista: {e["motorista"]}")
                                    input(f"{roxo}Aperte enter para continuar...") 
                                else:
                                    print(f"{vermelho}Aguarde mais um pouco!")
                                    input(f"{roxo}Aperte enter para continuar...") 

                else:
                    print(f"{vermelho}Senha ou email invalido!\n")
                    input(f"{roxo}Aperte enter para continuar...") 
                    break
        if not usuario_encontrado:
            for m in motoristas:
                if(emailLogin == m["email"]):
                    senhaLogin = input(f"{roxo}Informe sua senha: ")
                    if (senhaLogin == m["senha"]):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print(f"{verde}\nLogin concluido!")
                        print(f"{roxo}\nBem vindo {m["nome"]} ao partiu!")
                        while True:
                            op = input(f"{roxo}\nEscolha uma das opções\n\n"
                                        "[1] Cadastro de carona\n"
                                        "[2] Remover carona\n"
                                        "[3] SOS\n"
                                        "[0] Logout\n\n" 
                                        "Opção: ")

                            if (op == '0'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                break

                            elif(op == '1'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Cadastrar uma carona!\n")
                                origem = input("Informe a origem: ")
                                destino = input("Informe o destino: ")
                                data = input("Informe a data (dia/mes/ano): ")
                                hora = input("Informe o horario (hora:minutos): ")
                                vagas = int(input("Informe a quantidade de vagas: "))
                                valor = float(input("Informe o valor por vaga: "))

                                dadosCarona = {
                                    'email': m["email"],
                                    'nome': m["nome"],
                                    'origem': origem,
                                    'destino': destino,
                                    'data': data,
                                    'hora': hora,
                                    'vagas': vagas,
                                    'valor': valor,
                                    'passageiros': []
                                }

                                print(f"{verde}Carona cadastrada!")
                                caronas.append(dadosCarona)
                                input(f"{roxo}Aperte enter para continuar...") 

                            elif(op == '2'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Remover carona!\n")

                                dataBusca = input("Informe a data da carona: ")
                                indice = -1
                                for ind in range(len(caronas)):
                                        if(dataBusca == caronas[ind]["data"]):
                                            indice = ind
                                        if(indice == -1):
                                            print(f"{vermelho}Não encontrou o usuário!")
                                        else:
                                            print(f"{verde}Carona encontarda!")
                                            print(f"{roxo}Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}")

                                            remover = input("Deseja remover essa carona do sistema (s/n)? ").upper()
                                            if (remover == 'S'):
                                                senhaValidacao = input(f"{roxo}Informe sua senha: ")
                                            if (senhaValidacao == m["senha"]):
                                                print(f"{verde}Carona removida!")
                                                caronas.pop(indice)
                                                input(f"{roxo}Aperte enter para continuar...") 
                                            else:
                                                print(f"{vermelho}Senha invalida!")
                                                input(f"{roxo}Aperte enter para continuar...") 

                            elif (op == '3'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print(f"{roxo}Corrida de emergencia!\n")

                                for e in emergencia:
                                    print(f"{roxo}Corridas de emergencia registradas!\n")

                                    if (e["atendido"] == True):
                                        print(f"{verde}Nenhuma corrida de emergencia pendente!\n")

                                    else:
                                        print(f"{roxo}Nome: {e["nome"]},\n"
                                                f"Email: {e["email"]},\n"
                                                f"Origem: {e["origem"]},\n"
                                                f"Destino: {e["destino"]},\n"
                                                f"Data: {e["data"]},\n"
                                                f"Horario: {e["hora"]},\n"
                                                f"Motivo: {e["motivo"]},\n"
                                                f"Atendida: {e["atendido"]},\n"
                                                f"Motorista: {e["motorista"]}")

                                        aceitar = input("Deseija aceitar esse corrida de emergencia (s/n)? ").upper()

                                        if (aceitar == 'S'):
                                            e["atendido"] = True
                                            e["motorista"] = m["nome"]
                                            print(f"{verde}Corrida de emergencia aceita! Contate o usuario: {e["nome"]}, {e["email"]}")
                                            input(f"{roxo}Aperte enter para continuar...") 

                                        else:
                                            break
                    else:
                        print(f"{vermelho}Senha ou email invalido!\n")
                        break
        
        if not usuario_encontrado:
            for a in admin:
                if(emailLogin == a["email"]):
                    senhaLogin = input(f"{roxo}Informe sua senha: ")
                    if (senhaLogin == a["senha"]):
                        chave = input(f"{roxo}Informe a chave de acesso: ")
                        if (chave == chaveAcesso):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print(f"{verde}\nAesso liberado!")
                            print(f"{roxo}\nBem vindo {a["nome"]} ao partiu!")
                            while True:
                                op = input(f"{roxo}Escolha uma das opções\n\n" \
                                "[1] - Lista de usuarios\n" \
                                "[2] - Remover usuario\n"
                                "[0] - Sair\n\n" \
                                "Opção: ")

                                if (op == '0'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                elif (op == '1'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"{roxo}Lista de usuarios!\n")
                                    print(f"{roxo}=" * 60)
                                    print(f"{azul}Passageiros!\n")
                                    for usu in passageiros: 
                                        print(f"{azul}Nome: {usu["nome"]}")
                                        print(f"{azul}Email: {usu["email"]}")    
                                    print(f"{roxo}=" * 60)
                                    print(f"{azul}Motoristas!\n") 
                                    for mot in motoristas: 
                                        print(f"{azul}Nome: {mot["nome"]}")
                                        print(f"{azul}Email: {mot["email"]}")  
                                    
                                    input(f"{roxo}Aperte enter para continuar...") 

                                elif (op == '2'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print(f"{roxo}Remover um usuario!\n")

                                    emailBusca = input(f"{roxo}Digite o email para buscar: ")
                                    indice = -1
                                    for ind in range(len(passageiros)):
                                        if(emailBusca == passageiros[ind]["email"]):
                                            indice = ind
                                        if(indice == -1):
                                            print(f"{vermelho}Não encontrou o usuário!")
                                            input(f"{roxo}Aperte enter para continuar...") 
                                        else:
                                            print(f"{verde}Passageiro removido!")
                                            passageiros.pop(indice)
                                            input(f"{roxo}Aperte enter para continuar...") 

                                    for ind in range(len(motoristas)):
                                        if(emailBusca == motoristas[ind]["email"]):
                                            indice = ind
                                        if(indice == -1):
                                            print(f"{vermelho}Não encontrou o usuário!")
                                            input(f"{roxo}Aperte enter para continuar...") 
                                        else:
                                            print(f"{verde}Motorista removido!")
                                            motoristas.pop(indice)
                                            input(f"{roxo}Aperte enter para continuar...") 
                    else:
                        print(f"{vermelho}Senha ou email invalido!\n")
                        break