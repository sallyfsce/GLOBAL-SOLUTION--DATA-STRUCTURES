
#   GS2026.1 - Monitoramento de Missão Espacial
#   Linguagem: Python

# Lista para guardar o histórico de leituras
historico = []


# FUNÇÕES

def inserir_dados():
    print("\n--- INSERIR DADOS ---")

    while True:
        try:
            temperatura = float(input("Temperatura da nave (graus C): "))
            break
        except ValueError:
            print("Valor invalido. Digite um numero.")

    while True:
        try:
            energia = float(input("Nivel de energia (%): "))
            if 0 <= energia <= 100:
                break
            else:
                print("Digite um valor entre 0 e 100.")
        except ValueError:
            print("Valor invalido. Digite um numero.")

    while True:
        try:
            comunicacao = int(input("Comunicacao (1 = ativa / 0 = falha): "))
            if comunicacao in (0, 1):
                break
            else:
                print("Digite apenas 0 ou 1.")
        except ValueError:
            print("Valor invalido. Digite 0 ou 1.")

    leitura = {
        "temperatura": temperatura,
        "energia": energia,
        "comunicacao": comunicacao
    }
    historico.append(leitura)
    print("Dados registrados com sucesso!")


def verificar_condicoes(leitura):
    alertas = []

    if leitura["temperatura"] > 80:
        alertas.append("ALERTA: Superaquecimento detectado!")
    else:
        alertas.append("Temperatura normal.")

    if leitura["energia"] < 20:
        alertas.append("ALERTA: Energia critica - modo de economia ativado!")
    else:
        alertas.append("Energia suficiente.")

    if leitura["comunicacao"] == 0:
        alertas.append("ALERTA: Falha na comunicacao!")
    else:
        alertas.append("Comunicacao ativa.")

    return alertas


def visualizar_status():
    print("\n--- STATUS ATUAL ---")

    if len(historico) == 0:
        print("Nenhum dado cadastrado ainda.")
        return

    ultima = historico[-1]
    print("Temperatura:", ultima["temperatura"], "graus C")
    print("Energia:", ultima["energia"], "%")

    if ultima["comunicacao"] == 1:
        print("Comunicacao: ATIVA")
    else:
        print("Comunicacao: FALHA")


def executar_analise():
    print("\n--- ANALISE AUTOMATICA ---")

    if len(historico) == 0:
        print("Nenhum dado para analisar.")
        return

    ultima = historico[-1]
    alertas = verificar_condicoes(ultima)

    for alerta in alertas:
        print(alerta)

    tem_alerta = False
    for alerta in alertas:
        if "ALERTA" in alerta:
            tem_alerta = True

    if tem_alerta:
        print("\nSTATUS GERAL: MISSAO EM RISCO")
    else:
        print("\nSTATUS GERAL: MISSAO OPERACIONAL")


def exibir_historico():
    print("\n--- HISTORICO DE LEITURAS ---")

    if len(historico) == 0:
        print("Nenhuma leitura registrada.")
        return

    for i in range(len(historico)):
        leitura = historico[i]
        if leitura["comunicacao"] == 1:
            com = "ATIVA"
        else:
            com = "FALHA"

        print("Leitura", i + 1, "- Temp:", leitura["temperatura"],
              "| Energia:", leitura["energia"], "%",
              "| Comunicacao:", com)

    print("Total de leituras:", len(historico))


# MENU PRINCIPAL

def menu():
    print("\n---------------------------")
    print("     MENU PRINCIPAL")
    print("---------------------------")
    print("1 - Inserir dados")
    print("2 - Visualizar status")
    print("3 - Executar analise")
    print("4 - Historico das leituras")
    print("0 - Encerrar sistema")
    print("---------------------------")
    opcao = input("Escolha uma opcao: ")
    return opcao


def main():
    print("---------------------------")
    print("  SISTEMA DE MONITORAMENTO")
    print("      MISSAO ESPACIAL")
    print("---------------------------")

    while True:
        opcao = menu()

        if opcao == "1":
            inserir_dados()
        elif opcao == "2":
            visualizar_status()
        elif opcao == "3":
            executar_analise()
        elif opcao == "4":
            exibir_historico()
        elif opcao == "0":
            print("\nSistema encerrado. Boa missao!")
            break
        else:
            print("Opcao invalida. Tente novamente.")


main()