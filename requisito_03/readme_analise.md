Análise dos valores obtidos para as redes usadas


Após a obtenção dos gráficos das redes para analisar a proximidade dos nós e arestas com base nas diferentes interpretações dos códigos,
para o código ainda foi feito também a obtenção de valores como a quantidade de nós e arestas, coeficiente da assortatividade, a quantidade de componentes conectados, o tamanho do componente gigante (GCC) e a média da coeficiência de clustering. Com eles, foi gerado uma tabela para comparar os dados.  

A **_assortatividade_** se caracteriza como a conexão de uma entidade com outra semelhante (comum principalmente em sites
e apps de redes sociais), quanto mais próximo de 1 (ou menos negativo), mais assortativa a rede será. Na teoria, quanto maior o grau dos nós, mais assortativo o gráfico será. A **_coeficiência de clustering_** trata da ligação de uma entidade com a rede, se o seu valor for 0, então existe uma entidade ligada a ela, mas os nós não se conectam entre si. Caso seja 1, ambos estão ligados entre si. Pode ainda ser
igual a 1/3, no qual a entidade e os nós estão parcialmente ligados entre si. Uma rede ainda pode ter vários **_componentes conectados_**, porém isso não implica necessariamente numa união, mas sim que pode haver vários grupos distintos. Se um grafo não chega a todos os elementos, ele é fracamente conectado, se os elementos se conectam (independente de direção), ele é fortemente conectado. O **_tamanho do componente gigante (GCC)_** trata pegar os diferentes grupos da rede e uni-los.


Partindo para a análise das redes, a quantidade de componentes conectados obtido foi igual a 1, isso significa que existe somente um único grupo de dentre os exemplos de nós obtidos. Para o Facebook, isso pode ser atribuído a alguma afinidade ou tema que pode unir um usuário a outros. Para o Deezer, a aplicação também se baseia nas amizades em comum, enquanto que para o GitHub está associado ao fato de que diferentes usuários que possuem pelo menos 10 repositórios tenham algo em comum, muito provavelmente da aplicação de um deles de diferentes formas. A rede da Wikipedia trata de uma eleição, como nesse cenário aumenta-se as dispersões e opiniões sobre administração, a consequência é que mais de uma GCC se forme. A rede de uma estrada como o da California também naturalmente terá um alto número de GCC's, pois além do estado como um todo ser considerado, dificilmente teríamos muitos pontos em comum (podemos ter um ou dois caminhos que levam a uma mesma localidade, mas não são todos os caminhos possíveis levam a uma única localidade).


Analisando a coeficiência de clustering, todos os valores obtidos foram mais próximos de 0 que de 1, exceto o do Facebook. O que pode ser concluído é que há uma conexão muito forte entre os usuários e a consequência é que ele é o mais assortativo das redes e o mais próximo de um comportamento de homofilia também em comparação aos demais.  




