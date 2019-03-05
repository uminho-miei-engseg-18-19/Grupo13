
#### P1.1: TOR

#### 1)

Não, o comando “sudo anonsurf start” apenas gera um ip aleatorio o que faz com que não seja possivel garantir que estaremos localizado nos EUA.

#### 2) 

Visto que há varias ligações numa conexão TOR, devidos aos varios OR’s, e estão são alteradas ao longo do tempo (de minuto a minuto), logo o OR3 irá sempre ter um IP novo e uma localização diferente, daí ser impossível garantir que, numa determinada altura, a nossa localização seja nos EUA.

#### P1.2:

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

Ao contrario da maioria, ambos os sites fornecidos apresentam-se como serviços anonimos, o que leva o protocolo a criar os 3 "*relay*s" extras que vimos anteriormente. Ao contrario dos três primeiros *Onion Routers* onde o utilizador tem acesso e pode alterar estes, estes três "*relay*s" aparecem assim porque, correspondem ao circuito TOR que foi estabelecido entre o servidor *web* e o *rendezvous point* . Assim, o unico ponto de comunicação com este serviço é pelo *rendezvous point*.