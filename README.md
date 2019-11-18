
# PUCPR Temperaturas Médias

Nesse projeto, o objetivo final será manipular três arquivos no formato CSV, cada um contendo um grande volume de dados de clima referente às regiões de Curitiba, Paranaguá e Londrina, gerando como resultado algumas estatísticas na forma de texto (na tela ou em arquivo texto), podendo também serem apresentadas as estatísticas mensais na forma de gráficos.

Os três arquivos que servirão como base para esse projeto foram obtidos via site do BDMEP – INMET e contém as temperaturas ambiente (em ºC) obtidas por leitura sensorial em três horários do dia: às 0h, 12h e às 18h entre o período de 01/01 a 31/12 do ano de 2018.

Atentem que os arquivos fornecidos para Paranaguá e Londrina possuem um número de registros bem maior que o arquivo de Curitiba. Esse fato também deverá ser tratado pelo programa desenvolvido nesse projeto.

1. Inicialmente, o usuário deverá escolher a região para que a pesquisa seja realizada. Assim:

		(1) Curitiba
		(2) Londrina
		(3) Paranaguá

2. Após a região ter sido escolhida, o programa deverá pedir um período de datas para o usuário. Esse período poderá referenciar-se:

		• ao ano
		• para esta opção, solicita-se a digitação do ano (4 dígitos)
		• de um mês inicial até um mês final dentro do mesmo ano
		• para esta opção, solicita-se o mês inicial e o mês final (2 dígitos para o mês). 
		
3. Dentro do período de datas escolhido pelo usuário e devidamente validado pelo programa, deverá ser questionado ao usuário se ele deseja que seja considerado:
		
		(1) um horário específico da leitura, podendo ser às 0h – 12h – 18h
		(2) todos os horários de leitura deverão ser considerados (e um valor médio de leitura diária deverá ser considerado)

4. Conforme escolhas do usuário até essa etapa, agora deverão ser abertas as seguintes opções de Consulta:
		
		(1) Temperaturas mínimas, médias e máximas do período através das médias das temperaturas diárias
		(2) Temperaturas mínimas, médias e máximas do período através de um horário específico de leitura diária
			(2.1) para esta opção, solicita-se o horário específico dentre 3 opções (0h, 12h ou 18h)

5. Após a escolha da Consulta será solicitado o meio de obtenção da resposta, que poderá ser:

		(1) Na tela
		(2) Gravada em arquivo texto
		(3) Na tela e gravada em arquivo texto

6. O usuário poderá ainda escolher se deseja ou não que a apresentação dos resultados seja feita via Gráfico. Caso a escolha seja positiva, os seguintes gráficos estarão disponíveis:
		
		(1) Gráfico de linha
			(1.1) somente para consulta de temperaturas mínimas, médias e máximas do período através das médias das temperaturas diárias
		(2) Gráfico de barra
			(2.1) somente para consulta de temperaturas mínimas, médias e máximas do período através de um horário específico de leitura diária
