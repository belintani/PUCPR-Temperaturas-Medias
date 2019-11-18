import biblioteca as b


def main():

    arquivoDestinoParaEscrita = './out/output.txt'
    arquivoOrigemDados = './data/'

    debug = True

    if debug:
        regiao = 1 #Curitiba
        tituloRegiao = ''
        tipo = 2 #Mensal
        ano = 2018
        meses = [1, 12]
        tituloPeriodo = ''
        opcaoHorario = 1
        horarioFixo = 12
        meioDeResposta = 3
        desejoGrafico = 's'
        opcaoGrafico = 2
    else:
        regiao = 0
        tituloRegiao = ''
        tipo = 0
        ano = 0
        meses = [0, 0]
        tituloPeriodo = ''
        opcaoHorario = 0
        horarioFixo = -1
        meioDeResposta = 0
        desejoGrafico = ''
        opcaoGrafico = 0


    ## 1. Inicialmente, o usuário deverá escolher a região para que a pesquisa seja realizada.
    while regiao < 1 or regiao > 3: ## enquanto regiao não é valida
        regiao = b.LeRegiao()

    if 1 == regiao:
        arquivoOrigemDados = arquivoOrigemDados + "Curitiba.csv"
        tituloRegiao = "Curitiba"
    elif 2 == regiao:
        arquivoOrigemDados = arquivoOrigemDados + "Londrina.csv"
        tituloRegiao = "Londrina"
    elif 3 == regiao:
        arquivoOrigemDados = arquivoOrigemDados + "Paranagua.csv"
        tituloRegiao = "Paranagua"

    try:
        registros = b.LeArquivo(arquivoOrigemDados)
    except: ## pode ser que dê um erro na hora de ler o arquivo, nesse caso, o programa é encerrado
        print('Não foi possível ler o arquivo com as temperaturas. Por favor, verifique se o arquivo está na pasta de origem do projeto')
        return


    while tipo < 1 or tipo > 2:  ## enquanto regiao não é valida
        tipo = b.LeTipoPeriodoDatas()


    ## 2. Após a região ter sido escolhida, o programa deverá pedir um período de datas para o usuário

    while ano < 2018 or ano > 2019: ## enquanto o ano não é válido
        ano = b.LeAno()

    if 1 == tipo:
        meses = [1, 12]

    elif 2 == tipo:
        while meses[0] < 1 or meses[1] > 12 or meses[0] > meses[1]: ## enquanto os meses não são válidos
            meses = b.LeMeses()

    tituloPeriodo = b.converterPeriodoEmTexto(meses, ano)

    ## 3. Dentro do período de datas escolhido pelo usuário e devidamente validado pelo programa, deverá ser questionado ao usuário se ele deseja que seja considerado
    while opcaoHorario < 1 or opcaoHorario > 2:  ## enquanto opcao de horário não é valida
        opcaoHorario = b.LeOpcaoHorarios()


    registrosfiltrados = []
    ## 4. Conforme escolhas do usuário até essa etapa, agora deverão ser abertas as seguintes opções de Consulta:
    if 1 == opcaoHorario:

        while horarioFixo != 0 and horarioFixo != 12 and horarioFixo != 18:
            horarioFixo = b.LeHorarioFixo()

        registrosfiltrados = b.filtraRegistros(registros, ano, meses, horario=horarioFixo)

    elif 2 == opcaoHorario:
        registrosfiltrados = b.filtraRegistros(registros, ano, meses)

    tempMedia = b.TempMedia(registrosfiltrados)
    tempMinima = b.TempMinima(registrosfiltrados)
    tempMaxima = b.TempMaxima(registrosfiltrados)

    ##5. Após a escolha da Consulta será solicitado o meio de obtenção da resposta
    while meioDeResposta < 1 or meioDeResposta > 3:
        meioDeResposta = b.LeMeioDeResposta()

    if 1 == meioDeResposta:
        b.ImprimeResultadoTela(tempMinima, tempMedia, tempMaxima)

    elif 2 == meioDeResposta:
        b.GravaResultadoArquivo(arquivoDestinoParaEscrita, tempMinima, tempMedia, tempMaxima)

    elif 3 == meioDeResposta:

        while 's' != desejoGrafico and 'n' != desejoGrafico:
            desejoGrafico = b.LeDesejoGrafico()

        b.GravaResultadoArquivo(arquivoDestinoParaEscrita, tempMinima, tempMedia, tempMaxima)

        if 's' == desejoGrafico:
            while opcaoGrafico < 1 or opcaoGrafico > 2:
                opcaoGrafico = b.LeEscolhaGrafico()

            if 1 == opcaoGrafico:
                b.GraficoBarra(tempMinima, tempMedia, tempMaxima, horarioFixo, tituloRegiao, tituloPeriodo)
            elif 2 == opcaoGrafico:
                registrosTempMediaPorDia = b.TempMediaPorDia(registrosfiltrados)
                b.GraficoLinhaHorario(registrosTempMediaPorDia, horarioFixo, tituloRegiao, tituloPeriodo)

        elif 'n' == desejoGrafico:
            b.ImprimeResultadoTela(tempMinima, tempMedia, tempMaxima)

main()
print("Fim")
