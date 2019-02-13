### 1. Números aleatórios/pseudoaleatórios
#### P1.1

    head -c 32 /dev/random | openssl enc -base64
    head -c 64 /dev/random | openssl enc -base64 
    head -c 1024 /dev/random | openssl enc -base64
    head -c 1024 /dev/urandom | openssl enc -base64

Tando o /dev/random como o /dev/urandom são geradores de números aleatórios baseados na entropia gerada pelo sistema.
O /dev/random fica à espera que seja gerada entropia suficiente para gerar o output pretendido, e bloqueia até essa entropia necessária ser atingida, e como tal quanto maior o tamanho, mais tempo demora a dar um output.
Por outro lado o /dev/urandom, caso não tenha a entropia necessária para gerar o output, utiliza a pool existente e faz uso do CSPNRG para gerar o resto.

#### P1.2

O tempo necessário para gerar um número aleatório através do /dev/random diminui consideravelmente, sendo agora imediato após a instalação do haveged.
Isto deve-se ao facto do algoritmo antes utilizado apenas considerar a entropia gerada por eventos externos, que se encontram no intervalo de 10-100 bits por segundo, o que limita a geração de números de tamanho considerável. 
Assim sendo, o algoritmo HAVEGE permite ultrapassar estas limitações, fazendo uso dos mecanismos de hardware existentes para obter entropia, como cache, contador de ciclos de relógio do processador e outros, mantendo na mesma um nível de imprevisibilidade e segurança altos, pois é praticamente impossível monitorizar os mesmos.

  
#### P1.3
1. Analisando o código do generateSecret-app.py, constatámos que a geração do segredo aleatório provém do método generateSecret() que se encontra definido em shamirsecret.py.
Ao analisarmos o método generateSecret() a geração do segredo aleatório é feito em dois passos:
 - primeiro gera uma sequência aleatória do tamanho do segredo:

		s = utils.generateRandomData(secretLength - l)
    
	no qual o generateRandomData() faz uso do urandom() para gerar uma 													string aleatória
 - depois percorre a string resultado, *s*, e selecciona apenas letras e dígitos para o segredo:



	    for c in s:
                if (c in (string.ascii_letters + string.digits) and l < secretLength): # printable character
                    l += 1
                    secret += c
                    
	Assim sendo o processo vai se repetir até o segredo ter o tamanho desejado e apenas contém letras e dígitos.

2. Poderiamos utilizar diretamente o resultado do método generateRandomData(), ao invés de eliminar do mesmo tudo o que não fosse letras e dígitos, e assim o output não seria limitado.

#### P2.1
A.
gerar mykey.pem

openssl genrsa -aes128 -out mykey.pem 1024

gerar mykey.crt

openssl req -key mykey.pem -new -x509 -days 365 -out mykey.crt

criar segredos partilhados
python createSharedSecret-app.py 8 5 1 mykey.pem
guardar cada componente que seria distribuido para cada utilizador

B.
recoverSecretFromComponents-app.py
	indicamos quantos componentes queremos introduzir, mas sempre maior ou igual que o quorum e menor ou igual que o número total de shares, para recuperar o segredo;
recoverSecretFromAllComponents-app.py
	são necessários todos os componentes para recuperar o segredo

o Allcomponents deverá ser utilizado quando ...


