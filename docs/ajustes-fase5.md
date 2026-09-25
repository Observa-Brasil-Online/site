# Ajustes de design/UX — Fase 5

Transcrição do board (Freeform) do Lucas, tela a tela. `[x]` = confirmado, `[?]` = aguardando
resposta. Implementar tudo de uma vez quando as três telas estiverem fechadas.

## Convenções do board

- **FA (Fonte A)** = tipografia do headline do hero: Archivo 800, tracking −0.02em, entrelinha 0.98.
  Vira a classe utilitária `.type-fa`.
- **"Contraste"** = medir na escala WCAG. Mínimo AA (4,5:1 texto normal, 3:1 texto grande);
  AAA (7:1) para texto sobre navy, trocando azul-céu por creme.
- **Raio de borda** = token global `--radius` em `tokens.css`. Começar em 10px; testar 8px.
- **Barra de medida com setas e "+"** = o componente deve correr a largura toda do frame em que
  está, respeitando as bordas/padding do contêiner.

Medições de referência: azul-céu/navy 5,6:1 (AA) · âmbar-escuro/cinza-névoa **3,4:1 (reprova AA)** ·
creme/navy 11,8:1 · navy/cinza-névoa 8,2:1.

## Home

### Header
- [x] Wordmark "BRASIL ONLINE" maior; "Uma série do OBSERVA" no mesmo tamanho, estilo mono
      mantido; os dois na mesma linha, altura casada com o símbolo (+2px), centralizados verticalmente
- [x] Sublinhado da aba ativa mais grosso (só depois considerar fundo preenchido)

### Hero
- [x] Kicker "OBSERVA · ELEIÇÕES 2026" → creme
- [x] Parágrafo (lede) → creme
- [x] Botões usam `--radius`

### Destaque da semana
- [x] Frase-headline vira link para a página da edição
- [x] Remover ponto final da frase
- [x] Legenda do StatCallout ao lado do número, não embaixo
- [x] Rótulos da ComparisonBar abaixo da barra

### Três camadas
- [x] Eyebrow "COMO FUNCIONA" → navy (corrige 3,4:1)
- [x] Título → "Três camadas de análise", em FA
- [x] Card 02 → "Os números"; card 03 → "As narrativas"; card 01 "Coleta" mantém
      (nota: eram copy verbatim do carrossel publicado — divergência consciente com o Instagram)
- [x] Cards usam `--radius`

### Edições anteriores
- [x] Título em FA
- [x] "Ver todas" → "Ver todos"
- [x] Remover tags de tema dos cards na Home
- [x] Trocar a ordem dos botões "Ver edição" / "Baixar PDF"
- [x] Cards usam `--radius`
- [x] Título "Edição anterior" (singular); a seção mostra **só a edição imediatamente anterior**
      à do hero (1 card, não grade de 3)
- [x] Chamada do card corre a largura toda do card (remover max-width 62ch)
- [x] Tags saem **só da Home** (as outras telas terão tratamento próprio — ideia do Lucas a testar)

### Faixa de plataformas / rodapé
- [x] Remover a faixa "X · Instagram · TikTok — 162 perfis monitorados"
- [x] Rodapé: remover o e-mail; deixar só "© 2026 OBSERVA"

## Quem Somos (parcial — bloco "O Recorte", veio junto com a Home)
- [x] Números maiores
- [x] "2" → "Esquerda e Direita" no estilo dos números; legenda "sempre comparados"
- [x] Legendas ao lado dos números, para os três

## Relatórios

### Hero
- [x] "ACERVO" (kicker) e "2 EDIÇÕES PUBLICADAS" → creme (5,65:1 → 11,76:1)
- [x] h1 "Relatórios" já usa o tratamento FA — nenhuma mudança

### Barra de filtros
- [x] Ícone de drop (▾) nos três gatilhos — glifo/triângulo CSS, sem biblioteca de ícones
- [x] Ordem da barra: `[Semana] [Plataforma] [Temas] · [APLICAR] [LIMPAR]` — filtros primeiro na
      posição atual, Aplicar antes de Limpar
- [x] Âmbar **só no estado ativo** do filtro (preenchimento âmbar + texto grafite = 7,35:1;
      âmbar como texto reprovaria a 2,15:1). Preserva a regra de ≤10% de âmbar e dá função ao acento
- [x] "Aplicar" é o gatilho: marcar caixas não filtra nada; a lista só muda no clique. Botão fica
      apagado quando não há mudança pendente, aceso quando há
- [x] O âmbar do gatilho reflete o estado **aplicado**, não o marcado

### Cards de edição
- [x] Remover prefixo "CONFLITO" das tags → "Político", "Moral"; "Disputas sociais" mantém.
      Renomear no frontmatter das duas edições (o filtro Temas acompanha automaticamente)
- [x] Cabeçalho "Temas" antes do grupo de tags no card — resume o que as tags significam e
      referencia o filtro. Só nesta tela (na Home as tags saem)

### ReportCard (componente compartilhado)
- [x] Aplicar aqui as mesmas mudanças pedidas na Home: trocar ordem "Ver edição"/"Baixar PDF"
      e chamada em largura total
- [x] Única diferença desta tela: o card exibe as tags, precedidas do cabeçalho "Temas"
      (prop de variante)

### FA
- [x] Onde FA foi definido como padrão, aplicar sem precisar de marcação no board; validar com o
      Lucas se surgir inconsistência em mudanças futuras

## Quem Somos (restante)

### Equipe
- [x] Remover o parágrafo de pendência ("Formação, grupo, Lattes e redes sociais ainda não
      constam...") — **depende** de os dados da equipe chegarem antes da publicação; sem eles a
      página vai ao ar com 41 nomes sem explicação
- [x] Cards de pessoa usam o raio global
- [x] Título "41 pesquisadoras e pesquisadores" em FA (padrão, sem marcação no board)

### Contato e rodapé
- [x] Remover a seção "Contato" inteira
- [x] Remover a faixa creme entre os dois blocos navy (some sozinha ao remover o Contato)
- [x] E-mail do rodapé → já coberto pela decisão da Home (opção C: só "© 2026 OBSERVA")
- [x] Canal de contato = **botões de rede social** no rodapé: Instagram, LinkedIn, TikTok, X.
      Único link disponível hoje: `https://www.instagram.com/observa.internet/`
- [x] Manter o respiro de 96px antes do rodapé
- [x] Assinatura do rodapé → **creme** (aplica o critério AAA, 5,65 → 11,76:1). Desvio consciente
      do azul-céu especificado no manual

Medição extra: parágrafo do rodapé (creme a 82% sobre navy) = 8,43:1, AAA — sem problema.

### Equipe — recorte na publicação
- [x] Manter os 41 nomes como placeholder durante o desenvolvimento; **ao publicar**, filtrar a
      grade para mostrar só quem devolveu as informações
- [x] Critério de corte: exibir quem tiver `formacaoAtual` preenchido

### Redes sociais
- [x] **Logos reais** (SVG inline, sem dependência) — desvio consciente da regra do manual, que
      trata das plataformas *monitoradas*, não dos perfis do próprio projeto
- [x] Cabeçalho **"Nos sigam nas redes:"** acima dos botões
- [x] Renderizar **só o que tem link**. Hoje: Instagram
      (`https://www.instagram.com/observa.internet/`). Os demais entram conforme os links chegarem

---

# Experimentos aprovados (entram junto com os 48)

Direção vinda dos prints de referência (Realtime Colors). Aprovados com as contrapropostas.

## E1 — Composição de blocos no espaço vazio do hero
- [x] Grade de blocos chapados no lado direito do hero, **carregando o dado da semana** em vez de
      ser decorativa. Resolve sozinho o teto de ~10% de âmbar: ele aparece na proporção real da
      Direita
- [x] Lê do content collection da **edição mais recente** — se redesenha sozinho a cada edição nova,
      sem trabalho manual
- [x] Fonte de dados em dois níveis, com degradação graciosa:
      **(a)** `dados.interacoesEsquerda/Direita`, que já existe e está preenchido — versão de dois
      blocos, custo zero por semana;
      **(b)** novo campo **opcional** `dados.plataformas` — quando preenchido, ganha três blocos com
      as proporções por plataforma. Ausente, cai em (a) sem quebrar

## E2 — Rodapé em duas colunas
- [x] Coluna 1 institucional: símbolo, assinatura OBSERVA, frase do recorte da amostra
- [x] Coluna 2: navegação + botões de rede (com o cabeçalho "Nos sigam nas redes:")
- [x] Divisor e linha de base com "© 2026 OBSERVA"
- [x] Assinatura OBSERVA permanece obrigatória e em destaque; **sem emoji** (a referência usa, o
      manual proíbe)

## E3 — Composições centralizadas
- [x] Só onde há pouco texto: título "Três camadas de análise" + os três cards, e o bloco "O Recorte"
- [x] Hero e corpo dos relatórios continuam alinhados à esquerda

---

# Backlog — ideias para depois da Fase 5

Não entram agora; registradas para não se perder.

- **Divulgação com o link do `workers.dev` até o domínio da UFABC resolver** (Lucas, 2026-09-10):
  ok divulgar publicamente com `https://site-observa.lucas360oliveira23.workers.dev` desde já —
  quando `labobserva.pesquisa.ufabc.edu.br` for liberado, ele entra como Custom Domain no painel
  Cloudflare e os dois endereços passam a funcionar ao mesmo tempo (nenhum link antigo quebra).
  Pendências a revisitar nessa hora:
  - Considerar redirect do `workers.dev` para o domínio da UFABC, se o Lucas quiser um único
    endereço "oficial" dali pra frente (opcional — os dois podem conviver para sempre).
  - Enquanto isso, existe um descompasso cosmético: `astro.config.mjs` já declara `site` como o
    domínio da UFABC, então OG tags/sitemap apontam pra lá mesmo o site sendo servido no
    `workers.dev` por enquanto. Não quebra nada, só deixa o preview de link em redes sociais
    mostrando a URL "errada" até a virada.
- **Carrossel de edições anteriores na Home** — substituir o card único de "Edição anterior" por um
  carrossel quando houver acervo suficiente (Lucas, 2026-09-10).
  - Quando for mexer nisso, aproveitar para **preencher `dados.publicacoesEsquerda/Direita`
    retroativamente nas edições 02, 03 e 04** (Lucas, 2026-09-14) — o número já existe em cada PDF
    ("X publicações únicas de direita contra Y de esquerda", seção 3.2), só falta extrair. Sem isso,
    o gráfico de produção da seção "destaque" da Home só aparece nas edições 01 e 05 (as únicas com
    o campo preenchido hoje); com todo o acervo preenchido, o carrossel pode mostrar esse dado de
    forma consistente edição a edição.
- **Ajustes de layout na versão mobile** (Lucas, 2026-09-25) — alguns layouts precisam de revisão
  no celular; Lucas vai detalhar quais telas/seções quando for tratar o item.
- **Tratamento próprio das tags de tema** nas telas de Relatórios e Relatório-detalhe — ideia do
  Lucas, a testar quando esses boards forem analisados.
- **Estado ativo do menu com fundo preenchido** — só se o sublinhado mais grosso não bastar.
- **Painel de dados da semana no site** (fase 2 do projeto) — o schema `dados` já grava os números.
- **CMS visual sobre o Git** para a equipe publicar edições sem tocar em código.
- **Links de LinkedIn, TikTok e X** do projeto — pegar com a equipe e adicionar ao rodapé. Cada um
  é uma linha em `config.ts` (Lucas, 2026-09-10). Nota: a ata de 18/08 decidiu **não** priorizar
  TikTok, então talvez nem existam todos.
- **Preencher `dados.plataformas`** nas edições — campo opcional; quando preenchido, a composição
  do hero ganha três blocos com as proporções reais por plataforma (números da Tabela 1 do PDF).
