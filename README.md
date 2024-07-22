# Calculadora-Python
Calculadora simples usando a biblioteca tkinter.

Resumo do Código: Calculadora com Tkinter
Este projeto consiste em uma aplicação de calculadora simples desenvolvida em Python utilizando a biblioteca Tkinter para a interface gráfica. A calculadora permite realizar operações aritméticas básicas como adição, subtração, multiplicação e divisão.

Descrição do Código
Importações:

from tkinter import *: Importa todos os componentes da biblioteca Tkinter.
from tkinter import ttk: Importa o módulo ttk, que fornece widgets temáticos.
Paleta de Cores:
Defino cinco cores (preto, branco, laranja, cinza e azul) utilizadas na interface.

Configuração da Janela Principal:
Cria a janela principal com título "Calculadora", define seu tamanho e cor de fundo, e restringe o redimensionamento.

Divisão da Tela:
display_tela: Frame que exibe os valores digitados e os resultados.
display_corpo: Frame que contém os botões da calculadora.

Variáveis Globais:
todos_valores: Armazena os valores e operações inseridos.
valor_texto: StringVar que atualiza o display com os valores e resultados.

Funções:
entrada_valores(event): Atualiza a variável todos_valores com o valor do botão pressionado e exibe no display.
limpar_tela(): Limpa o display e reseta a variável todos_valores.
calcular(): Avalia a expressão matemática contida em todos_valores e exibe o resultado. Em caso de erro, exibe "Erro".

Display da Calculadora:
Label que exibe os valores digitados e os resultados, configurado com estilo e alinhamento apropriados.

Configuração dos Botões:
Cria uma lista de botões com seus respectivos textos, comandos, posições na grade (grid) e, quando necessário, a largura (colspan).
Usa um loop para criar e posicionar os botões no frame display_corpo utilizando o método grid.

Loop Principal da Interface Gráfica:
janela.mainloop(): Inicia o loop principal da interface gráfica, mantendo a janela aberta e interativa.

Estrutura do Código
O código está organizado para facilitar a leitura e manutenção, utilizando métodos como grid para disposição dos botões e listas para a configuração dos mesmos, evitando repetição e tornando o código mais conciso e escalável.

Funcionalidades
Operações Básicas: Adição, subtração, multiplicação e divisão.
Tecla de Limpeza: Limpa o display e reseta os valores.
Tratamento de Erros: Exibe uma mensagem de erro em caso de entrada inválida.
Este projeto é ideal para quem está começando com Tkinter e deseja aprender sobre a criação de interfaces gráficas e manipulação de eventos em Python.

