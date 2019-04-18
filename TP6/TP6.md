
### 1. RGPD (Regulamento Geral de Proteção de Dados)

#### P1.1
Nós decidimos escolher a pergunta que estuda o RGPD, pois achamos que um conhecimento aprofundado deste regulamento será bastante benéfico, visto que, por enquanto, temos pouco conhecimento sobre o mesmo.

Como somos o grupo 13, calhou-nos falar sobre o artigo 5º. Este artigo fala sobre os "princípios relativos ao tratamento de dados pessoais".

Os dados pessoais são objetos que devem ter um tratamento lícito, leal e transparente em relação ao titular dos dados, ou seja, estes dados podem ser tratados desde que cumpram as leis que estão impostas a estes e desde que todo o seu tratamento seja do conhecimento do titular dos dados.

Os dados só podem ser guardados para fins determinados, explícitos ou legítimos, não podendo ser tratados posteriormente. Isto pode acontecer apenas para fins de arquivo de interesse público, para fins de investigação científica ou histórica, ou para fins estatísticos. Logo, deve ser pensado, de antemão, qual a finalidade que estes dados vão servir, pois não devem ser armazenados mais dados do que aqueles necessários para o cumprimento da sua finalidade. Isto também implica que os dados sejam versáteis, ou seja, que haja uma atualização, retificação ou remoção dos dados caso necessário, ou caso seja pedido pelo titular dos dados.

Os dados guardados não podem ser sempre associados ao titular, ou seja, apenas durante o tempo que estes são usados para um determinado fim, estes podem e devem estar associados a uma certa entidade, mas mal esse fim seja atingido, a entidade em questão não puderá mais ser associada a estes dados. Quando isto acontece, os dados podem ser eliminados ou guardados caso sejam usados, futuramente, para fins de investigação científica, para fins históricos ou para fins estatísticos.

Por fim, as entidades responsáveis por armazenar estes dados devem ter alguns cuidados a tomar neste processo. Pois, é necessário proteção para que estes não sejam tratados para fins não autorizados e para que estes não se percam. Com isto é necessário adotar estratégias que asseguram a integridade e confidencialidade dos dados em questão.

#### P1.2

O documento *Privacy and Data Protection by Design – from policy to engineering* secção 3.2, apresenta 8 estratégias de privacy design, sendo que estas podem ser divididas em duas secções: estratégias orientadas aos dados e estratégias orientados aos processos.

**Estratégias orientadas aos dados**

1. MINIMISE

Esta estratégia tem por base apenas processar a menor quantidade de informação possível, de modo a limitar o impacto do sistema em relação aos dados privados, e assim garantir que dados desnecessários não são coletados.
Para tal devemos seguir a prática de escolher antes de coletar, isto é, escolher os dados a processar e só depois coletar.

2. HIDE

Nesta estratégia devemos esconder os dados pessoais e relações dos mesmos, apesar de a estratégia não especificar de quem devemos esconder, pois depende do contexto nos quais os dados se encontram.
Um exemplo de aplicação desta estratégia está presente na cifragem de dados.

3. SEPARATE

Esta estratégia indica que os dados devem ser processados ou armazenados de forma distribuída, em diferentes compartimentos.
Isto permite que os dados relativos a um utilizador estejam espalhados, o que em caso de perda de alguns, não permitirá revelar a informação total sobre o mesmo.

4. AGGREGATE

Finalmente a última estratégia orientada aos dados define que os dados pessoais devem ser tratados no maior nível de agregação possível, isto é, com o menor detalhe sobre cada indivíduo, como por exemplo juntar a informação sobre um atributo dos vários indivíduos, o que permite não revelar a conexão entre os mesmos.

**Estratégias orientadas aos processos**

5. INFORM

Esta estratégia indica que os utilizadores que forneceram a informação pessoal devem ser informados sempre que esta for processada. Que informação é processada, para que propósito, e como é obtida, são algumas das questões aos quais o utilizador deve ter resposta.
Esta estratégia é aplicada, por exemplo, nas secções de preferência da privacidade dos sistemas, que permitem ao utilizador saber a resposta às questões referidas.

6. CONTROL

Esta estratégia estabelece que um sujeito deve ser capaz de controlar a informação que é processada.
Isto verifica-se nas capacidades do sujeito poder ver, atualizar e apagar a informação pessoal recolhida sobre si.

7. ENFORCE

Esta estratégia indica que uma política de privacidade deve estar em funcionamento, sendo que esta deve ser compatível com os requerimentos legais.
Isto implica que devem existir mecanismos de prevenção de violação dessa mesma política de privacidade em vigor.

8. DEMONSTRATE

Finalmente a última estratégia, requer que um controlador de dados consiga demonstrar que o sistema está de acordo com a política de privacidade e com os requerimentos legais.
Isto pode ser implementado utilizando logging e auditing.


#### P1.3

#### 1. 

Segundo o [Guidelines on Data Protection Impact Assessment (DPIA) and determining whether processing is “likely to result in a high risk” for the purposes of Regulation 2016/679](https://github.com/uminho-miei-engseg-18-19/engseg/blob/master/TPraticas/Aula7/EU.20171013_wp248_rev01_enpdf.pdf) do _ARTICLE 29 DATA PROTECTION WORKING PARTY_, existem nove critérios que devem ser considerados para avaliar se o processamento de dados pessoais irá resultar num risco elevado, devendo ser efetuado um DPIA(_Data Protection Impact Assessment_) sempre que o processamento satisfizer dois desses critérios, critérios esses:

 1. Avaliação ou Pontuação, que inclui _profiling_ e previsões;
 2. Decisões automáticas com um efeito legal ou semelhante;
 3. Monitorização automatica;
 4. Informação sensivel ou de natureza pessoal;
 5. Processamento de informação em grande escala. Para saber se é de grande escala, a **WP29** apresenta certos fatores para ajudar: 
	- o numero de afetados deve ser ou um numero ou uma percentagem da população relevante;
	- o volume e/ou alcance da informação a ser processada;
	- a duração, ou permanencia, do ato de processamento da informação;
	- a extensão geografica da atividade.
 6. Combinação de _datasets_;
 7. A informação refere-se a informação de sujeitos vulneráveis;
 8. Uso inovador ou aplicação de novas tecnologias ou soluções organizacionais;
 9.  Quando o processo previne os sujeitos da informação de usufruir de um direito, serviço ou contracto.

#### 2.

Imaginemos que o projeto tem como objetivo uma aplicação identica ao _MB Way_, onde os clientes são capazes de consultar o saldo, fazer transferências e pagamentos bancérios ou pagar contas em estabelecimentos físicos através da aplicação mobile. Assim, a projeto fica com os dados bancários dos seus clientes, bem como uma lista de transações por eles efetuadas.
Dos critérios apresentados anteriormente, este projeto apresenta a necessidade da realização de um DPIA por encaixar nos critérios:

 - 3. Monitorização automatica;
 - 4. Informação sensivel ou de natureza pessoal;
 - Possivel 5. Processamento de informação em grande escala.

#### 3.

Como vimos, este projeto requer a criação de um DPIA, este que completamos e apresentamos como [DPIA](DPIAMBWay.pdf), que preenchemos imaginando como seria uma possível implementação de algo semelhante.

#### P1.4

O PIA está preencido e com o nome [PIA.pdf](PIA.pdf)