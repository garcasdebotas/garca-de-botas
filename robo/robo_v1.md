# Garça de Botas — Documentação Técnica do Robô V1

**Equipe:** Garça de Botas  
**Categoria:** FIRST LEGO League (FLL)  
**Plataforma:** SPIKE Prime  
**Versão:** 1.0  

---

## Visão Geral

O Robô V1 é a primeira iteração física da equipe Garça de Botas para a temporada atual da FLL. O projeto foi desenvolvido com base em referências de equipes competitivas de alto nível, priorizando estabilidade estrutural, tração e um chassis compacto o suficiente para acomodar o hub centralizado. O design foi influenciado por arquiteturas comuns em equipes como a **LEGO Legends** e equipes sul-americanas de alto desempenho que adotam chassis de perfil baixo com motores de tração duplos centralizados — configuração que oferece simetria mecânica e facilidade de programação de movimentos retos.

---

## Especificações Técnicas

| Parâmetro | Valor |
|---|---|
| Rodas (diâmetro) | 62,4 mm |
| Espessura total estimada | 146,2 mm |
| Motores de tração | 2x Motor Grande SPIKE Prime |
| Motores auxiliares | 2x Motor Médio SPIKE Prime |
| Sensores de cor | 2 unidades |
| Hub | SPIKE Prime Hub (centralizado) |
| Tipo de tração | Diferencial com rodas de grande diâmetro |

---

## Imagens do Projeto CAD

<img width="827" height="574" alt="Captura de tela 2026-05-25 233835" src="https://github.com/user-attachments/assets/4f99b4cf-bdca-4b3f-aa72-1504a1e307cb" />


*Vista lateral: posicionamento dos motores grandes e rodas de tração.*

<img width="1005" height="492" alt="Captura de tela 2026-05-25 233825" src="https://github.com/user-attachments/assets/8aba9879-4e14-4420-946f-80c0f9ab8b5e" />


*Vista frontal: simetria dos dois motores médios e disposição interna.*

<img width="697" height="623" alt="Captura de tela 2026-05-25 233814" src="https://github.com/user-attachments/assets/ea34d708-556d-4a28-9e6c-3c03335d3ed3" />


*Vista inferior: posicionamento dos motores grandes e sensores.*

<img width="953" height="622" alt="Captura de tela 2026-05-25 233803" src="https://github.com/user-attachments/assets/99f915f0-15b8-49a8-a8c5-b94c7c62cb08" />

*Vista traseira: configuração dos motores e suporte à estrutura.*

---

## Estrutura e Chassis

O chassis do V1 foi construído com base em vigas Technic de perfil duplo, formando um quadro rígido que serve de plataforma para o hub SPIKE Prime. O hub está posicionado centralmente na parte superior do robô, fixado sobre uma camada de vigas que distribui o peso de forma relativamente equilibrada entre os dois eixos de tração.

A estrutura base apresenta camadas horizontais bem definidas: a camada inferior concentra os eixos de tração e os motores grandes, enquanto a camada intermediária sustenta os motores médios e os conectores de saída para os anexos. O hub ocupa a camada superior, com acesso facilitado às portas de conexão.

O robô possui dimensões consideráveis para os padrões da FLL, o que é diretamente consequência das escolhas de rodas e da quantidade de motores instalados.

---

## Sistema de Tração

### Rodas

As rodas de 62,4 mm de diâmetro foram selecionadas deliberadamente pela equipe por dois motivos principais:

- **Tração**: o perfil com grip profundo das rodas SPIKE Prime de grande porte proporciona maior aderência à superfície do tapete, reduzindo deslizamento durante acelerações e travagens.
- **Eficiência de percurso**: o diâmetro acima da média significa que, a cada rotação completa do motor, o robô percorre uma distância linear maior em comparação com rodas menores. Isso reduz o número de rotações necessárias para alcançar um ponto distante na arena, contribuindo para maior eficiência energética e menor desgaste nas missões longas.

### Motores

O sistema de tração emprega **dois motores grandes** acoplados diretamente às rodas traseiras principais, responsáveis pela propulsão e pelo controle diferencial de direção. Os **dois motores médios** operam como saídas auxiliares, destinados ao acionamento de mecanismos de anexo.

Essa configuração de 4 motores é adotada por equipes que buscam independência total entre tração e mecanismos, eliminando a necessidade de redistribuir motores de tração para operar anexos.

---

## Sensoriamento

O projeto utiliza **dois sensores de cor**, embora tecnicamente apenas um fosse o mínimo necessário para execução das missões.

A decisão de instalar dois sensores foi estratégica: com dois sensores de cor posicionados simetricamente na parte frontal do robô, a equipe pode implementar a técnica de **alinhamento por linha**. Nessa técnica, o robô não segue a linha continuamente, mas a utiliza como referência pontual — quando ambos os sensores detectam a linha ao mesmo tempo, ou em sequência controlada, o robô corrige seu ângulo e se alinha com precisão antes de executar uma missão.

Isso reduz o efeito cumulativo de pequenos erros de navegação entre missões consecutivas, aumentando a consistência das execuções.

---

## Inspiração em Equipes Competitivas

A arquitetura do V1 apresenta semelhanças visuais e estruturais com abordagens utilizadas por equipes como:

- **Equipes da América do Sul com histórico em torneios regionais** que adotam chassis de duas camadas com hub centralizado e motores de tração laterais simétricos.
- **Equipes que utilizam a configuração "tank drive" pura** — dois motores grandes em drive direto, sem redução por engrenagem — priorizando simplicidade mecânica e previsibilidade na programação.
- A estrutura de vigas duplas horizontais e o posicionamento do hub elevado lembram designs documentados em equipes da Ásia e Europa que competem nas categorias abertas da FLL, onde a eficiência de montagem e desmontagem de anexos é crítica.

---

## Limitações Identificadas

### Tamanho e ocupação de espaço na arena

O maior problema identificado no V1 é o seu **tamanho físico**. O robô ocupa uma área considerável do campo de lançamento e restringe a margem de manobra para posicionamento inicial. Em consequência direta:

- Anexos de maior porte tornam-se inviáveis, pois o robô já ocupa boa parte do espaço disponível.
- O raio de giro é maior, o que pode dificultar missões que exigem curvas apertadas próximas a obstáculos.

### Design de anexos prejudicado pela geometria traseira e lateral

A parte traseira e as laterais do V1 apresentam **geometria irregular**, com motores médios salientes, conectores expostos e vigas em posições assimétricas. Isso dificulta significativamente o desenvolvimento de anexos padronizados, pois não há uma superfície plana ou estrutura de encaixe regular para servir de referência.

Na prática, cada anexo precisou ser desenvolvido de forma específica para aquela posição, aumentando o tempo de design e reduzindo a intercambialidade entre mecanismos.

---

## Pontos Positivos

- Rigidez estrutural razoável para um primeiro projeto.
- Configuração de 4 motores bem segmentada entre tração e mecanismos.
- Escolha de rodas tecnicamente justificada em tração e eficiência.
- Uso estratégico de duplo sensor de cor para alinhamento.
- Hub centralizado facilita o equilíbrio de peso.

---

## Considerações para Próximas Versões

Com base nas limitações identificadas, o V2 deve priorizar:

- Redução do tamanho geral do chassis sem comprometer a rigidez.
- Padronização das interfaces de anexo (superfícies regulares e pontos de encaixe definidos).
- Avaliação do posicionamento dos motores médios para não comprometer a geometria lateral.
- Manutenção ou melhoria do sistema de duplo sensor de cor para alinhamento por linha.

---

*Documentação gerada pela equipe Garça de Botas — temporada FLL atual.*
