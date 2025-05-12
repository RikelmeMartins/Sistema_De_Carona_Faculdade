import os
passageiros = list()
motoristas = list()
admin = list()
caronas = list()
emergencia = list()
roxo = '\033[95m'
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
    print("=" * 127)

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
        print("=" * 80)

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
                    print("Email invalido!")
                    email = input("Informe um email valido: ")
            
            if (email in passageiros):
                print("\nEmail ja existente no nosso sistema!\n")
                print("Tente novamente com outro email!")
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
                print("Passageiro cadastrado!")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif(op == '2'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de motoristas!\n")          

            nome = input("Informe seu nome: ")
            email = input("Informe um email: ")
            emailValidacao = False
            while not emailValidacao:
                if (email.endswith("@gmail.com")):
                    emailValidacao = True
                else:
                    print("Email invalido!")
                    email = input("Informe um email valido: ")
            
            if (email in motoristas):
                print("\nEmail ja existente no nosso sistema!\n")
                print("Tente novamente com outro email!")
            else:
                senha = input("Informe uma senha: ")
                usuario = {
                    'email': email,
                    'nome': nome,
                    'senha': senha,
                }
                motoristas.append(usuario)
                print("Motorista cadastrado!")
                os.system('cls' if os.name == 'nt' else 'clear')

        elif(op == '3'):
            os.system('cls' if os.name == 'nt' else 'clear')
            print("\nCadastro de motoristas!\n")          

            chave = input("Informe a chave de acesso: ")

            if (chave == chaveAcesso):
                print("Acesso permitido!")

                nome = input("Informe seu nome: ")
                email = input("Informe um email: ")
                emailValidacao = False
                while not emailValidacao:
                    if (email.endswith("@gmail.com")):
                        emailValidacao = True
                    else:
                        print("Email invalido!")
                        email = input("Informe um email valido: ")

                if (email in motoristas):
                    print("\nEmail ja existente no nosso sistema!\n")
                    print("Tente novamente com outro email!")
                else:
                    senha = input("Informe uma senha: ")
                    usuario = {
                        'email': email,
                        'nome': nome,
                        'senha': senha,
                    }
                    admin.append(usuario)
                    print("Admin cadastrado!")    
                    os.system('cls' if os.name == 'nt' else 'clear')
            else:
                print("Acesso negado!")
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
        print("=" * 60)
        print("Faça seu login!\n")
        usuario_encontrado = False
        emailLogin = input("Informe seu email: ")
        for p in passageiros:
            if (emailLogin == p["email"]):
                senhaLogin = input("Informe sua senha: ")
                if (senhaLogin == p["senha"]):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    usuario_encontrado = True
                    print("Login concluido!")
                    print(f"\nBem vindo {p["nome"]} ao partiu!\n")
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
                            print("Lista de caronas disponiveis!\n")
                            print("="*60)
                            for c in caronas:
                                print(f"Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                print("="*60)
                        
                        elif(op == '2'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Origem e destino!\n")

                            origemBusca = input("Informe a origem: ")
                            destinoBusca = input("Informe o destino: ")

                            for c in caronas:
                                if (origemBusca in c["origem"] and destinoBusca in c["destino"]):
                                    print("\nCarona encontrada!\n")
                                    print("=" * 60)
                                    print(f"Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    print("=" * 60)
                                else:
                                    print("\nNenhuma carona encontrada!\n")
                        
                        elif (op == '3'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Reservar vagas!\n")

                            emailBusca = input("Informe o email do motorista: ")
                            dataBusca = input("Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print("=" * 60)
                                    print("\nCarona encontrada!\n")
                                    print(f"Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]}.")
                                    reserva = input("\nDeseja reserva uma vaga (s/n): ").upper()

                                    if (reserva == 'S'):
                                        if (p["saldo"]  < c["valor"]):
                                            print("Saldo insuficiente!")
                                            break
                                        elif(c["vagas"] == 0):
                                            print("Vagas esgotadas!")
                                            break
                                        else:
                                            print("Vaga reservada!")
                                            c["vagas"] -= 1
                                            p["saldo"] -= c["valor"]
                                            c["passageiros"].append(p["nome"])
                                            break
                                    else:
                                        break
                                else:
                                    print("\nCarona não encontrada!\n")
                        
                        elif (op == '4'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Remover reserva!\n")

                            emailBusca = input("Informe o email do motorista: ")
                            dataBusca = input("Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                        print("=" * 60)
                                        print("\nCarona encontrada!\n")
                                        print(f"Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}.")
                                        reserva = input("\nDeseja remover sua vaga (s/n): ").upper()

                                        if (reserva == 'S'):
                                            senha = input("Informe sua senha: ")
                                            if (senha == p["senha"]):
                                                print("Reservada cancelada!")
                                                c["vagas"] += 1
                                                p["saldo"] += c["valor"]
                                                c["passageiros"].remove(p["nome"])
                                            else:
                                                print("Senha invalida!\n")
                                                print("Tente novamente cancelar sua reserva!")
                                        else:
                                            break
                                else:
                                    print("\nCarona não encontrada!\n")

                        elif(op == '5'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Detalhes da carona!\n")
                            
                            emailBusca = input("Informe o email do motorista: ")
                            dataBusca = input("Informe a data da carona: ")

                            for c in caronas:
                                if (emailBusca in c["email"] and dataBusca in c["data"]):
                                    print("=" * 60)
                                    print("\nCarona encontrada!\n")
                                    print(f"Nome do motorista: {c["nome"]},\n"
                                            f"Email do motorista: {c["email"]},\n"
                                            f"Origem: {c["origem"]},\n"
                                            f"Destino: {c["destino"]},\n"
                                            f"Data: {c["data"]},\n"
                                            f"Horario: {c["hora"]},\n"
                                            f"Vagas: {c["vagas"]},\n"
                                            f"Valor por vagas: R${c["valor"]},\n"
                                            f"Passageiros: {c["passageiros"]}")
                                
                                else:
                                    print("Carona não encontrada!")
                        
                        elif (op == '6'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Caronas Cadastradas!\n")
                            print("="*60)
                            for c in caronas:
                                print(f"Nome do motorista: {c["nome"]},\n"
                                        f"Email do motorista: {c["email"]},\n"
                                        f"Origem: {c["origem"]},\n"
                                        f"Destino: {c["destino"]},\n"
                                        f"Data: {c["data"]},\n"
                                        f"Horario: {c["hora"]},\n"
                                        f"Vagas: {c["vagas"]},\n"
                                        f"Valor por vagas: R${c["valor"]},\n"
                                        f"Passageiros: {c["passageiros"]}")
                            print("="*60)

                        elif(op == '7'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Corrida de emergência!\n")

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
                            print("Corrida de emergência concluido. Espero um motorista aceitar!")

                        elif(op == '8'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Depositar dinheiro!\n")

                            valor = float(input("Informe o valor do deposito: "))

                            p["saldo"] += valor
        
                            print("\nDeposito efetuado!")
                            print(f"Seu saldo: R${p["saldo"]}")
                        
                        elif (op == '9'):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("Verificar se o chamado foi atendido!\n")

                            for e in emergencia:
                                if (e["atendido"] == True):
                                    print("Sua corrida foi aceita!")
                                    print(f"Nome do motorista: {e["motorista"]}")
                                else:
                                    print("Aguarde mais um pouco!")

                else:
                    print("Senha ou email invalido!\n")
                    break
        if not usuario_encontrado:
            for m in motoristas:
                if(emailLogin == m["email"]):
                    senhaLogin = input("Informe sua senha: ")
                    if (senhaLogin == m["senha"]):
                        os.system('cls' if os.name == 'nt' else 'clear')
                        print("\nLogin concluido!")
                        print(f"\nBem vindo {m["nome"]} ao partiu!")
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
                                print("Cadastrar uma carona!\n")
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

                                caronas.append(dadosCarona)

                            elif(op == '2'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Remover carona!\n")

                                dataBusca = input("Informe a data da carona: ")
                                indice = -1
                                for ind in range(len(caronas)):
                                        if(dataBusca == caronas[ind]["data"]):
                                            indice = ind
                                        if(indice == -1):
                                            print("Não encontrou o usuário!")
                                        else:
                                            print("Carona encontarda!")
                                            print(f"Nome do motorista: {c["nome"]},\n"
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
                                                senhaValidacao = input("Informe sua senha: ")
                                            if (senhaValidacao == m["senha"]):
                                                print("Carona removida!")
                                                caronas.pop(indice)
                                            else:
                                                print("Senha invalida!")

                            elif (op == '3'):
                                os.system('cls' if os.name == 'nt' else 'clear')
                                print("Corrida de emergencia!\n")

                                for e in emergencia:
                                    print("Corridas de emergencia registradas!\n")

                                    if (e["atendido"] == True):
                                        print("Nenhuma corrida de emergencia pendente!\n")

                                    else:
                                        print(f"Nome: {e["nome"]},\n"
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
                                            print(f"Corrida de emergencia aceita! Contate o usuario: {e["nome"]}, {e["email"]}")

                                        else:
                                            break
                    else:
                        print("Senha ou email invalido!\n")
                        break
        
        if not usuario_encontrado:
            for a in admin:
                if(emailLogin == a["email"]):
                    senhaLogin = input("Informe sua senha: ")
                    if (senhaLogin == a["senha"]):
                        chave = input("Informe a chave de acesso: ")
                        if (chave == chaveAcesso):
                            os.system('cls' if os.name == 'nt' else 'clear')
                            print("\nAesso liberado!")
                            print(f"\nBem vindo {a["nome"]} ao partiu!")
                            while True:
                                op = input("Escolha uma das opções\n\n" \
                                "[1] - Lista de usuarios\n" \
                                "[2] - Remover usuario\n"
                                "[0] - Sair\n\n" \
                                "Opção: ")

                                if (op == '0'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    break

                                elif (op == '1'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Lista de usuarios!\n")
                                    print("=" * 60)
                                    print("Passageiros!")
                                    print("=" * 60)
                                    for usu in passageiros: 
                                        print(f"Nome: {usu["nome"]}")
                                        print(f"Email: {usu["email"]}")    
                                    print("=" * 60)
                                    print("Motoristas!") 
                                    print("=" * 60)
                                    for mot in motoristas: 
                                        print(f"Nome: {mot["nome"]}")
                                        print(f"Email: {mot["email"]}")  

                                elif (op == '2'):
                                    os.system('cls' if os.name == 'nt' else 'clear')
                                    print("Remover um usuario!\n")

                                    emailBusca = input("Digite o email para buscar: ")
                                    indice = -1
                                    for ind in range(len(passageiros)):
                                        if(emailBusca == passageiros[ind]["email"]):
                                            indice = ind
                                        if(indice == -1):
                                            print("Não encontrou o usuário!")
                                        else:
                                            print("Passageiro removido!")
                                            passageiros.pop(indice)

                                    for ind in range(len(motoristas)):
                                        if(emailBusca == motoristas[ind]["email"]):
                                            indice = ind
                                        if(indice == -1):
                                            print("Não encontrou o usuário!")
                                        else:
                                            print("Motorista removido!")
                                            motoristas.pop(indice)
                    else:
                        print("Senha ou email invalido!\n")
                        break