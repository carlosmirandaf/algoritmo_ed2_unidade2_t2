# Análise dos gráficos das redes

 Para este trabalho, foram utilizadas cinco redes para mostrar o funcionamento de conceitos sobre assortatividade, small worlds e homofilia. Das cinco, quatro dessas redes envolvem redes sociais (considerando aqui o GitHub e Wikipedia como duas delas) e uma rede é sobre a estrada do estado da California, nos EUA. Adiante, em cada exemplo de rede dentro das descrições de aplicações, como consta o site da SNAP, foi observado um comportamento similar em quatro dessas redes, exceto o do exemplo da estrada.

 
  A rede do Facebook trata de uma combinação de egonets de usuários (i.e., foi focado em um nó específico e nele todos os nós que estão 
conectados a ele, podendo ter ou não laços em comum). Essa combinação se dá por gostos em comum ou não que estão anonimizados. Pelo gráfico gerado, foi observado uma considerável proximidade de valores entre o grau do nó e do grau médio de vizinho, o que pode ser observado é que como gostos similares por diferentes temas (política, por exemplo) são compartilhados de um usuário para vários dentro do ciclo de amizade, isso se reflete na proximidade de nós e arestas conforme observado no Scatter Plot. O comportamento observado é característico da homofilia.


  A rede do Deezer se refere às redes de amizade de usuários da Romênia, com nós representando os usuários e as arestas representando as
amizades em comum. Mesmo com uma quantidade de nós e arestas maior que o do Facebook, menos elementos foram observados no gráfico, muito
disso pode ter ocorrido pelo gráfico se basear em um único país, enquanto que o Facebook possivelmente considera diferentes lugares e países, além de que o Deezer, em essência, é uma plataforma de streaming para ouvir músicas, as relações em comum não é um elemento obrigatório ou prioritário, já que o usuário pode seguir um artista com conta e o mesmo não tem a obrigação de seguir um usuário de volta, p. ex.


  A próxima rede analisada foi a do Github, que pega a relação de desenvolvedores com pelo menos 10 repositórios (os nós) e os seguidores
mútuos entre eles (as arestas). Como os nós representam os repositórios, a maior parte é concentrada na parte um pouco maior que 0 e como
há proximidades entre eles, pode-se observar que há homofilia de forma similar ao do Facebook, já que um repositório pode ter sido reaproveitado para outros tipos de código de diferentes usuários.


  A rede da Wikipedia trata do voto público para administração do site. Os nós são os usuários e as arestas são os votos, porém mesclados
os votos dos usuários com os administradores. Como se trata de uma "eleição", observa-se que o voto em um candidato em comum cria uma rede de proximidades, porém como pode haver vários candidatos, o que temos é um gráfico mais disperso.


  Por fim, temos a rede de estradas da Calfornia, com nós sendo interseções e endpoints e arestas sendo as estradas que se conectam a elas. Ao contrário dos exs. anteriores, aqui foi observado uma dispersão bem maior porque o gráfico trata de espaço e como a rede em questão trata de um estado como um todo e não um fragmento, menos elementos comumente irão aparecer. Caso pegássemos uma cidade ou uma rua, o que possivelmente veríamos eram mais estradas conectadas a essas interseções (diferentes estradas e ruas poderiam levar a um mesmo ponto, p. ex.).
