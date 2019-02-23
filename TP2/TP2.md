
#### P2.1 i)Anexe os resultados do _SSL Server test_ à sua resposta
Como pedido, escolhemos três sites de empresas cotadas no ***NASDAQ***, empresas essas:
- [Microsoft Corporation](www.microsoft.com)
	- [SSL](https://www.ssllabs.com/ssltest/analyze.html?d=www.microsoft.com&latest)
	- [HTML](./SSL-Results/Microsoft.html)
- [Apple Inc.](www.apple.com)
	- [SSL](https://www.ssllabs.com/ssltest/analyze.html?d=www.apple.com&latest)
	- [HTML](./SSL-Results/Apple.html)
- [Facebook](https://www.facebook.com)
	- [SSL](https://www.ssllabs.com/ssltest/analyze.html?d=www.facebook.com)
	- [PDF](./SSL-Results/Facebook.html)

Em primeiro lugar é importante de notar que ambas as três empresas apresentam mais que um server capaz de transmitir o site à altura dos testes feitos, apresentando todos a mesma classificação. Como tal, avaliaremos apenas um dos servidores de cada empresa.
Como podemos ver, o site da *[Microsoft](microsoft.com)*
![Microsoft.com Scan Summary](./SSL-Results/Microsoft.png) e da *[Apple](apple.com)*![Apple.com Scan Summary](./SSL-Results/Microsoft.png) apresentam, respetivamente, A+ e A na classificação dada pelo *SSL*.

Já o site do *[Facebook](facebook.com)* apresenta uma classificação de B:
![Facebook.com Scan Summary](./SSL-Results/Facebook.png)

#### P2.1 ii) Analise o resultado do _SSL Server test_ relativo ao site escolhido com pior rating. Que comentários pode fazer sobre a sua segurança. Porquê?
Como vimos, o pior valor atribuido foi ao site da rede social. Não só o site aceita cifras [RC4](https://blog.qualys.com/ssllabs/2013/03/19/rc4-in-tls-is-broken-now-what?_ga=2.16122420.326019711.1550941154-115483375.1550941154), mesmo que seja só com protocolos antigos, como vemos na imagem anterior, como também, numa exploração mais aprofundada da analise feita pelo *SSL*, vemos que o site aceita diversas *Cipher Suites* nao recomendadas no TLS 1.2, de entre elas três inseguras e sete muito fracas.
![Facebook Cipher Suites](./SSL-Results/Facebook_Cipher_Suites.png)
Comparando o tamanho das chaves aqui apresentadas e a lista do NIST, vemos que muitas destas chaves deveriam apresentar um tamanho bastante superior para assegurar melhor a sua segurança, bem como deixar de suportar as três cifras inseguras.

Mesmo com as notas positivas apresentadas no [resumo inicial](./SSL-Results/Facebook.png),como o suporte a TLS 1.3, *[Static Public Key Pinning](https://scholarworks.iu.edu/dspace/bitstream/handle/2022/21039/PKI-ASAF-design-docs.pdf?sequence=4)* e *[HTTP Strict Transport Security](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security)* (HSTS) com longa duração, estas medidas baixam a avaliação para B.

#### P2.1 iii) É natural que tenha reparado na seguinte informação: "_OpenSSL Padding Oracle vuln. (CVE-2016-2107)_" na secção de detalhe do protocolo. O que significa, para efeitos práticos?


