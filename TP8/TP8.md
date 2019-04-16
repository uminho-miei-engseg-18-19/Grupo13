
### 1. Vulnerabilidade de codificação

#### P1.1

#### 1.

Tendo por base a métrica que indica que por cada 1000 linhas de código temos entre 5 a 50 bugs, obtemos então:

|  							| Linhas de código 	|	Número de bugs(estimativa)	|
|:-------:|:-----:|:-----:|
|Facebook       			|  62 milhões   	|	310.000 a 3.100.000			|
|*software* de automóveis     |	100 milhoes    	|	500.000 a 5.000.000			|
|Linux 3.1         			|  15 milhoes   	|	75.000 a 750.000			|
|serviços Internet da Google|	2 mil milhoes  	|	10.000.000 a 100.000.000	|

#### 2.

Não é possível estimar o número de vulnerabilidades a partir do número de bugs, pois não sabemos quantos destes são vulnerabilidades.

#### P1.2
A **Segurança de *software*** diz respeito a três tipos de vulnerabilidades.
Vamos começar por explicar o que são estas vulnerabilidades, seguindo depois com os exemplos:

- Vulnerabilidade de Projeto
	- 
	- É uma vulnerabilidade introduzida durante a fase de projeto do *software* (obtenção de requisitos e desenho do *software*)
	
	- Alguns exemplos claros disto seriam: possível [injeção de argumentos](https://cwe.mitre.org/data/definitions/20.html), quando o *software* não delimita corretamente o que pode receber como argumentos, ou um simples [privilégio que esteja a ser adicionado (ou a faltar)](https://cwe.mitre.org/data/definitions/250.html) a um utilizador. Ambos estes exemplos são de simples resolução e devem ser bem declarados e tratados na formulação dos requisitos do sistema.

- Vulnerabilidade de Codifição
	- 
	- Já só aparece durante a programação do *software* ( que pode ser tratado como um bug com implicações de segurança)
	
	- Como exemplo temos o [acesso a variáveis privadas por um método publico](https://cwe.mitre.org/data/definitions/767.html), que acontece quando o modelo apresenta um método público capaz de alterar variáveis privadas, que se pode evitar com o uso e implementação correta do métodos que acedem e modificam estas variáveis; ou um Buffer Overflow, quer numa [Stack](https://cwe.mitre.org/data/definitions/121.html), [Heap](https://cwe.mitre.org/data/definitions/122.html) ou mesmo num [Integer](https://cwe.mitre.org/data/definitions/680.html). Tratar estas vulnerabilidades já requerem um conhecimento do acesso que o código tem e o que pode mudar se certos limites não forem estabelecidos, mostrando-se mais difícil de corrigir que os anteriores.

- Vulnerabilidade Operacional
	-
	- Causada pelo ambiente no qual o *software* é executado ou pela sua configuração
	
	-  Aqui temos a [limitação imprópria do PathName](https://cwe.mitre.org/data/definitions/22.html) onde o *software* usa entrada externa para construir um nome de caminho destinado a identificar um arquivo ou diretoria localizada sob uma diretoria pai restrita, mas o *software* não neutraliza adequadamente elementos especiais dentro do nome do caminho, que podem fazer com que o nome do caminho seja resolvido para um local está fora da diretoria restrita; ou o [Download de código sem testar a sua integridade](https://cwe.mitre.org/data/definitions/494.html), que acontece quando o produto baixa o código-fonte ou um executável de um local remoto e executa o código sem verificar totalmente a origem e a integridade desse código. Para evitar ambos estes problemas podemos recorrer a firewalls, mas dificulta bastante se não soubermos o sistema ounde o *software* vai correr.

#### P1.3

Uma vulnerabilidade dia-zero é uma vulnerabilidade que apenas é conhecida num meio restrito e, como tal, não foi feito um patch para impedir que essa vulnerabilidade possa ser explorada. Uma vulnerabilidade de codificação que não seja de dia-zero, é uma vulnerabilidade conhecida ,ou seja, é do conhecimento dos desenvolvedores e podem, como tal, prevenir que seja explorada.