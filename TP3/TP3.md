### 1. TOR (The Onion Router)

#### P1.1

#### 1)

Não, o comando *sudo anonsurf start* apenas gera um ip aleatório o que faz com que não seja possível garantir que estaremos localizados nos EUA.

#### 2) 

Visto que há várias ligações numa conexão TOR, devidos aos vários OR’s, e estas são alteradas ao longo do tempo (de minuto a minuto), o OR3 irá sempre ter um IP novo e uma localização diferente, daí ser impossível garantir que, numa determinada altura, a nossa localização seja nos EUA.

#### P1.2

#### 1)

Clicando no lado esquerdo da barra de URL, verificamos qual é o circuito para esse site:
- This browser
- France
- Germany
- United States
- Relay
- Relay
- Relay
- site final que indicamos

#### 2)

Ao contrário da maioria, ambos os sites fornecidos apresentam-se como serviços anónimos, o que leva o protocolo a criar os 3 "*relay*s" da alínea anterior. 

Ao contrário dos três primeiros, *Onion Routers*, onde o utilizador tem acesso e pode alterar estes, estes três "*relay*s" aparecem assim porque não foram escolhidos pelo utilizador, e correspondem ao circuito TOR que foi estabelecido entre o servidor *web* e o *rendezvous point*, e como tal não possuímos informação sobre os mesmos. 

Assim, o único ponto de comunicação com este serviço é pelo *rendezvous point*, comunicação essa constituída por 6 "saltos", dois circuitos TOR, desde o utilizador até ao *rendezvous point* e do *rendezvous point* ao servidor *web*.