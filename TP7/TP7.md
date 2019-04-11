
### 1. [Blockchain](main1.1.js)

#### P1.1
No [ficheiro criado](main1.1.js), com base no [tutorial](https://medium.com/@akshaykore/building-a-blockchain-7579c53962dd) dado, o método que cria o Genesis Block é:
	
	createGenesisBlock(){
		return new Block(0, "02/01/2018", "Genesis Block", "0");
	}
De modo a que o timestamp seja a data do dia de hoje e o dado incluído nesse Bloco seja "Bloco inicial da koreCoin", alteramos a função do seguinte modo:

	createGenesisBlock(){
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); 
        //January is 0!
        var yyyy = today.getFullYear();

        today = dd + '/' + mm + '/' + yyyy;

        return new Block(0, today , "Bloco inicial da koreCoin", "0");
    }
#### P1.2
Para criar blocos e simular transações em cada um deles basta acrescentar o código:
	
	koreCoin.addBlock(new Block (1, "01/01/2018", {amount: 20}));
	koreCoin.addBlock(new Block (2, "02/01/2018", {amount: 40}));
	koreCoin.addBlock(new Block (3, "02/01/2018", {amount: 60}));
	koreCoin.addBlock(new Block (4, "01/04/2019", {Bloco1: 
	['transferencia1',40],Bloco2: ['transferencia2',20]}));
	koreCoin.addBlock(new Block (4, "01/04/2019", {Bloco4: 
	['transferencia1',60]}));



### 2. Proof of Work Consensus Model

#### P2.1
O tempo de cada um pode ser visto nos ficheiros na [pasta](Exercicio\ 2\ Docs/)  Exercicio 2 Docs mas, em suma, os resultados que vêmos são, em segundos, para cada dificuldade testada:

 2. 0m0.115s
 3. 0m0.436s
 4. 0m2.143s
 5. 0m27.059s
 6. 6m3.695s
 
Ora, como vemos, cada nível de dificuldade de minerar aumenta o tempo que demora a minerar os blocos.

#### P2.2

#### 1.
    
O algoritmo de proof of work é o seguinte, dado o último proof of work incrementa-se 1, e caso este não seja múltiplo de 9, repete-se o processo até que tal aconteça.
Isto verifica-se no método **proof_of_work**:
    
    def proof_of_work(last_proof):
        
        incrementor = last_proof + 1
        
        while not (incrementor % 9 == 0 and incrementor % last_proof == 0):
            incrementor += 1
        
        return incrementor


#### 2.

Não parece ser o algoritmo mais adequado, pois não existe nenhuma aleatoriedade envolvida, o que permite ao último miner calcular os seguintes valores.

Em termos de complexidade não apresenta uma complexidade elevada, sendo linear, o que também é outra falha deste algoritmo.
