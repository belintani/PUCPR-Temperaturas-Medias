import pandas as pd
import matplotlib.pyplot as plt


def TempMinima(registrosFiltrados):
    minima = -9999
    for r in registrosFiltrados:
        if -9999 == minima or minima > r['Temperatura']:
            minima = r['Temperatura']

    if minima == -9999:
        minima = 0

    return minima


def TempMediaPorDia(registrosFiltrados):

    ultimaChave = ''
    count = 0
    regs = []

    for r in registrosFiltrados:
        key = str(r['Ano']) + str(r['Mes']) + str(r['Dia'])

        if key != ultimaChave:

            if '' != ultimaChave:
                regs.append(ultimoRegistro)

            ultimaChave = key
            count = 1
            ultimoRegistro = r

        else:
            temp = ultimoRegistro["Temperatura"] * count
            count = count + 1
            ultimoRegistro["Temperatura"] = (temp + r["Temperatura"]) / count

    return regs


def TempMedia(registrosFiltrados):
    soma = 0
    conta = 0

    for r in registrosFiltrados:
        soma = soma + r['Temperatura']
        conta = conta + 1

    if conta == 0:
        return soma

    return soma / conta  # calculo de média


def TempMaxima(registrosFiltrados):
    maxima = 9999
    for r in registrosFiltrados:
        if 9999 == maxima or maxima < r['Temperatura']:
            maxima = r['Temperatura']

    if maxima == 9999:
        maxima = 0

    return maxima


def traduzirMes(mes):
    if 1 == mes:
        return "Jan"
    if 2 == mes:
        return "Fev"
    if 3 == mes:
        return "Mar"
    if 4 == mes:
        return "Abr"
    if 5 == mes:
        return "Mai"
    if 6 == mes:
        return "Jun"
    if 7 == mes:
        return "Jul"
    if 8 == mes:
        return "Ago"
    if 9 == mes:
        return "Set"
    if 10 == mes:
        return "Out"
    if 11 == mes:
        return "Nov"
    if 12 == mes:
        return "Dez"


def converterPeriodoEmTexto(meses, ano):
    if meses[0] == meses[1]:
        return traduzirMes(meses[0]) + " de " + str(ano)
    else:
        return traduzirMes(meses[0]) + " até " + traduzirMes(meses[1]) + " de " + str(ano)


def filtraRegistros(registros, ano, meses, **kwargs):
    registrosFiltrados = []

    for r in registros:
        if ano == r['Ano'] and (
                meses == [0, 0] or (meses[0] <= r['Mes'] <= meses[1])):  # está no ano e no mes que eu quero?
            if kwargs.get('horario') == None or kwargs.get('horario') == r['Hora']:  # está na hroa que eu quero
                registrosFiltrados.append(r)

    return registrosFiltrados


##### FUNCOES PARA MANIPULAR O ARQUIVO #####
def LeArquivo(caminho):
    # lê o arquivo (com dados separados pelo ';') no caminho especificado
    dadosCSV = pd.read_csv(caminho, sep=';')

    # lista de todos os registros em forma de estrutura
    registros = []
    conta = 0
    for data in dadosCSV['Data']:
        obj = {
            "Ano": int(data[6:]),
            "Mes": int(data[3:5]),
            "Dia": int(data[0:2]),
            "Hora": dadosCSV["Hora"][conta],
            "Temperatura": dadosCSV["Temperatura"][conta]
        }
        registros.append(obj)
        conta = conta + 1

    return registros


def GravaResultadoArquivo(caminho, min, med, max):
    # cria ou abre o arquivo para escrita
    arq = open(caminho, 'w')

    # escreve os resultados no arquivo
    arq.write('*********************** RESULTADO *************************\r\n')
    arq.write('A temperatura MÍNIMA     vale:' + str(round(min, 2)) + 'ºC \r\n')
    arq.write('A MÉDIA das temperaturas vale:' + str(round(med, 2)) + 'ºC \r\n')
    arq.write('A temperatura MÁXIMA     vale:' + str(round(max, 2)) + 'ºC \r\n')
    arq.write('***********************************************************')

    # fecha o arquivo
    arq.close()


##### FUNCOES PARA ESCRITA DE MENSAGENS #####
def ImprimeResultadoTela(min, med, max):
    print('*********************** RESULTADO *************************')
    print('A temperatura MÍNIMA     vale:', round(min, 2), 'ºC')
    print('A MÉDIA das temperaturas vale:', round(med, 2), 'ºC')
    print('A temperatura MÁXIMA     vale:', round(max, 2), 'ºC')
    print('***********************************************************')


def limpa_tela():
    print('\n' * 50)  # simula um "limpa tela"


def LeRegiao():
    limpa_tela()
    print("** Escolha qual a região para que a pesquisa seja realizada **")
    print("* (1) Curitiba                                               *")
    print("* (2) Londrina                                               *")
    print("* (3) Paranaguá                                              *")
    print('**************************************************************')
    return int(input())


def LeTipoPeriodoDatas():
    limpa_tela()
    print("** Qual o tipo de período de datas  **")
    print("* (1) Anual                          *")
    print("* (2) Mensal                         *")
    print('**************************************')
    return int(input())


def LeAno():
    limpa_tela()
    print("***************** Informe o ano (4 dígitos)  *****************")
    return int(input())


def LeMeses():
    limpa_tela()
    print("******* Informe o mês inicial (2 dígitos)  *******")
    inicial = int(input())
    print("*** Informe o mês final do mês ano (2 dígitos) ***")
    final = int(input())
    return [inicial, final]


def LeOpcaoHorarios():
    limpa_tela()
    print("*************** Especifique um horário a ser considerado ***************")
    print("* (1) um horário específico da leitura, podendo ser às 0h – 12h – 18h  *")
    print("* (2) todos os horários de leitura deverão ser considerados            *")
    print('************************************************************************')
    return int(input())


def LeHorarioFixo():
    limpa_tela()
    print("************** Suas opções são 0 – 12 – 18 **************")
    return int(input())


def LeOpcaoConsulta():
    limpa_tela()
    print("(1) Temperaturas mínimas, médias e máximas do período através das médias das temperaturas diárias")
    print("(2) Temperaturas mínimas, médias e máximas do período através de um horário específico de leitura diária")
    return int(input())


def LeMeioDeResposta():
    limpa_tela()
    print("***** Qual o meio de obtenção da resposta? *****")
    print("* (1) Na tela                                  *")
    print("* (2) Gravada em arquivo texto                 *")
    print("* (3) Na tela e gravada em arquivo texto       *")
    print('************************************************')
    return int(input())


def LeDesejoGrafico():
    limpa_tela()
    print("*** Deseja que a apresentação dos resultados seja feita via Gráfico ? ***")
    print("* ( s ) para sim                                                        *")
    print("* ( n ) para não                                                        *")
    print('*************************************************************************')
    return input()


def LeEscolhaGrafico():
    limpa_tela()
    print("******************* Qual gráfico deve ser impresso ?  *******************")
    print("* (1) Temperaturas minima, média e máxima → gráfico de barras)          *")
    print("* (2) Acompanhamento diário → gráfico em linhas                         *")
    print('*************************************************************************')
    return int(input())


### FUNCOES GRAFICO
# Gráfico de linha os resultados de temperaturas mínimas, médias e máximas do período através das médias das temperaturas diárias.
def GraficoLinhaHorario(registrosFiltrados, horarioFixo, tituloRegiao, tituloPeriodo):
    data = []
    temp = []
    i = 0

    for r in registrosFiltrados:
        data.append(i)
        i = i + 1
        temp.append(r['Temperatura'])

    plt.plot(data, temp, lw=3)

    plt.xlabel(tituloPeriodo, fontsize='x-large')
    plt.ylabel("Temperatura ° C", fontsize='x-large')

    if -1 == horarioFixo:
        plt.title('Temperatura média dos dias em ' + tituloRegiao)
    else:
        plt.title('Temperatura média de ' + tituloRegiao + ' baseado nos registros das ' + str(horarioFixo) + " horas")

    plt.show()
    return


# Gráfico de barra os resultados de temperaturas mínimas, médias e máximas do período através de um horário específico de leitura diária.
def GraficoBarra(min, med, max, horarioFixo, tituloRegiao, tituloPeriodo):
    objects = ('Mínimo', 'Medio', 'Máximo')

    performance = [min, med, max]

    plt.bar(objects, performance, align='center', alpha=0.5)
    plt.xticks(objects, objects)

    plt.xlabel(tituloPeriodo, fontsize='x-large')
    plt.ylabel('Temperatura ° C', fontsize='x-large')

    if -1 == horarioFixo:
        plt.title('Temperaturas médias consolidadas em ' + tituloRegiao)
    else:
        plt.title('Temperaturas médias consolidadas de ' + tituloRegiao + ' baseado nos registros das ' + str(horarioFixo) + " horas")

    plt.show()
    return
