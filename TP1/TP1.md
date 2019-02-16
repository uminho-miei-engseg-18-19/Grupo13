
### 1. Números aleatórios/pseudoaleatórios
#### P1.1

| Comando | Tempo |
|-------|:-----:|
|head -c 32 /dev/random \| openssl enc -base64|0.006s|
|head -c 64 /dev/random \| openssl enc -base64|0.008s|
|head -c 1024 /dev/random \| openssl enc -base64|15min 34s|
|head -c 1024 /dev/urandom \| openssl enc -base64|0.014s|

Tanto o `/dev/random` como o `/dev/urandom` são geradores de números pseudo-aleatórios baseados na entropia gerada pelo sistema.

O `/dev/random` fica à espera que seja gerada entropia suficiente para gerar o output pretendido, bloqueando até essa entropia necessária ser atingida e, como tal, quanto maior o tamanho do número mais tempo demora a dar um output, mas obtemos uma aleatoriedade de alta qualidade.

Por outro lado, o `/dev/urandom` caso não tenha a entropia necessária para gerar o output, utiliza a pool existente e faz uso do CSPNRG, gerador de número pseudo-aleatório criptograficamente seguro,  para gerar o resto, sendo que será de menor qualidade quando comparado com o anterior.

#### P1.2
| Comando | Tempo |
|:-------:|:-----:|
|head -c 1024 /dev/random \| openssl enc -base64|0.012s|
|head -c 1024 /dev/urandom \| openssl enc -base64|0.014s|

O tempo necessário para gerar um número aleatório através do /dev/random diminui consideravelmente após a instalação do haveged.
Isto deve-se ao facto, do algoritmo antes utilizado apenas considerar a entropia gerada por eventos externos, cujas gerações se encontram no intervalo de 10-100 bits por segundo, o que limita a geração de números de tamanho razoáveis. 

Assim sendo, o algoritmo HAVEGE permite ultrapassar estas limitações de baixa entropia, fazendo uso dos mecanismos de hardware existentes para obter entropia, como cache, contador de ciclos de relógio do processador e outros, mantendo na mesma um nível de imprevisibilidade e segurança altos, pois é praticamente impossível monitorizar os mesmos.
  
#### P1.3

1. Analisando o código do [generateSecret-app.py](https://github.com/uminho-miei-engseg-18-19/engseg/blob/master/TPraticas/Aula2/PseudoAleatorio/generateSecret-app.py), constatámos que a geração do segredo aleatório provém do método *generateSecret()* que se encontra definido em [shamirsecret.py](https://gitlab.com/eVotUM/Cripto-py/blob/master/eVotUM/Cripto/shamirsecret.py).
Ao analisarmos o método *generateSecret()*, a geração do segredo aleatório é feito em dois passos:
 - primeiro gera uma sequência aleatória do tamanho do segredo pedido:

		s = utils.generateRandomData(secretLength - l)
    
	no qual o [generateRandomData()](https://gitlab.com/eVotUM/Cripto-py/blob/master/eVotUM/Cripto/utils.py) faz uso do *urandom* para gerar uma string aleatória;
 - depois percorre a string resultado, *s*, e selecciona apenas letras e dígitos para o segredo:

	    for c in s:
                if (c in (string.ascii_letters + string.digits) and l < secretLength): # printable character
                    l += 1
                    secret += c
                    
	Assim sendo o processo vai se repetir até o segredo ter o tamanho desejado e apenas contém letras e dígitos.

2. Poderiamos utilizar diretamente o resultado do método *generateRandomData()*, ao invés de eliminar do mesmo tudo o que não fosse letras e dígitos, e transformando os bytes retornados em carateres imprimíveis passando-os para base 64. Assim, o output não seria limitado.

#### P2.1

A.
 Começamos por gerar a chave privada, *mykey.pem*, com o comando:

    openssl genrsa -aes128 -out mykey.pem 1024

De seguida gerámos o certificado que servirá para recuperar o segredo, *mykey.crt*, através do comando:

	openssl req -key mykey.pem -new -x509 -days 365 -out mykey.crt

Agora que temos a chave privada, podemos então gerar o segredo que será dividido em 8 partes com quorum de 5, com o comando:

	python createSharedSecret-app.py 8 5 1 mykey.pem

Finalmente, o resultado do comando anterior são as 8 partes do segredo, que seriam distribuídas pelas 8 pessoas.

B.
- recoverSecretFromComponents-app.py

Este programa permite indicar quantos componentes queremos introduzir, mas sendo sempre maior ou igual que o quorum e menor ou igual que o número total de partes, para recuperar o segredo;

- recoverSecretFromAllComponents-app.py

Este programa permite recuperar o segredo apenas se todos os componentes, nos quais o segredo foi dividido, forem introduzidos, neste caso corresponde às 8 partes. 

O recoverSecretFromAllComponents-app.py deverá ser utilizado quando o nível de segurança e acesso é elevado, e queremos garantir a participação e conhecimento de todos os envolvidos na partilha inicial do segredo.

#### P3.1


??? a etiqueta tem de ser cifrada ou é um campo extra??? se for cifrada perde o proposito, pois como ajuda a saber o q esta no segredo se a etiqueta esta cifrada??
?? chave muda todos os dias logo vamos ter um local onde temos armazenadas todas as chaves dos vários dias, e sendo assim a partir da data obtemos a chave para a parte de decifrar???

- Cifrar

Para cifrar são precisos  3 parâmetros:

	segredo_plaintext
	etiqueta
	chave_cifra

Inicialmente ciframos o segredo, garantido assim a confidencialidade do mesmo:

	segredo_cyphertext = cifra(segredo_plaintext)

De seguida, obtemos o *hmac* do resultado anterior, o que permite garantir a integridade e autenticidade, pois este *hmac* só será possível obter com acesso à *chave_cifra* e ao *segredo_plaintext*:

	hmac = hmac(chave_cifra,segredo_cyphertext)

E o resultado final seria:

	segredo_cyphertext + hmac + data + etiqueta

- Decifrar

No processo de decifrar recebemos o resultado de cifrar mais a chave, tendo assim os seguintes parâmetros:

	segredo_cyphertext
	hmac
	data
	etiqueta
	chave_cifra

Para decifrar começamos por obter o *hmac*:

	hmac' = hmac(chave_cifra, segredo_cyphertext)

De seguida comparámos o *hmac* obtido com o fornecido por parâmetro, e caso não sejam iguais, é porque o *segredo_cyphertext* sofreu alterações ou a *chave_cifra* não é a correta, e como tal o processo falharia:

	if(hmac' != hmac)
		return error

Caso os *hmac* sejam iguais, estamos em condições de obter o *segredo_plaintext*:

	segredo_plaintext = decifra (segredo_cyphertext, chave_cifra)

E finalmente podemos retornar o *segredo_plaintext*.

#### P4.1
##### AlfaTrust Certification S.A.
De acordo com o [endereço dado](https://webgate.ec.europa.eu/tl-browser/), encontramos os três seguintes serviços de emissão de certificados no que toca à AlfaTrust Certification S.A. relativa à Roménia:
- AlfaSign Public CA
- AlfaSign Qualified CA
- Alfasign Qualified Root CA
Através da execução do comando dado na nota 2 do enunciado ( `openssl x509 -in cert.crt -text -noout`), conseguimos extrair informação sobre os algoritmos e o tamanho das chaves usadas nos mesmos:

|                Entidade               |    Algoritmo de Assinatura   | Algoritmo de Chave Publica | Tamanho da Chave (bits) | Validade |
|:--------------------------------------|:----------------------------:|:--------------------------:|:-----------------------:|:--------:|
|AlfaSign Public CA| sha1 com RSA | RSA | 2048 | Oct  8 13:57:59 2010 GMT until Oct  7 13:57:59 2015 GMT|
|AlfaSign Qualified CA| sha1 com RSA| RSA | 2048 | Dec  5 18:33:57 2011 GMT until Nov 30 18:33:57 2031 GMT |
|Alfasign Qualified Root CA| sha256 com RSA | RSA | 2048| Aug 11 08:57:10 2017 GMT until Aug 11 09:07:10 2047 GMT|



Relativamente à CENTRUL DE CALCUL SA analisamos o certificado CertDigital Validation Authority G2:

	- Algoritmo de Assinatura:	SHA256 com RSA
	- Algoritmo de Chave Publica: 	RSA
	- Tamanho da chave: 		2048

Ora, segundo a Classificação [ENISA](https://www.enisa.europa.eu/publications/algorithms-key-size-and-parameters-report-2014) de Novembro de 2014, prevê-se que problemas com RSA serão seguros em 10 a 50 anos de vida desde que a chave apresente mais de 3072 bits, o que não se verifica nos certificados analisados. Recomenda também o uso de curvas elípticas de 256 bits quando se trata de primitivas de chaves publicas e preferem o uso de sha512 no que toca a funções de hash, quando comparado ao uso de sha256.