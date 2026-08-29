# Brasil Online — site

Site da série semanal **Brasil Online**, do OBSERVA (Observatório de Conflitos na Internet, UFABC),
que acompanha a polarização do debate político nas redes durante as Eleições Presidenciais de 2026.

Substitui o site em WordPress da FBC. O domínio institucional
`labobserva.pesquisa.ufabc.edu.br` aponta para cá.

## Rodar localmente

```bash
npm install
npm run dev
```

Abre em `http://localhost:4321`.

| Comando | O que faz |
| --- | --- |
| `npm run dev` | Servidor de desenvolvimento com recarga automática |
| `npm run build` | Gera o site estático em `dist/` |
| `npm run preview` | Serve o `dist/` para conferir antes de publicar |

## Estrutura

```
src/
  config.ts            Nome, contato, navegação e o recorte da amostra (162 perfis)
  styles/
    tokens.css         Design system: cores, tipografia, espaçamento, forma
    base.css           Reset, fundações tipográficas, utilitários, acessibilidade
  components/          Primitivos: Symbol, SignatureLockup, Button, Badge, Card,
                       StatCallout, ComparisonBar
  layouts/Base.astro   Casca da página: head, meta, OG, header, footer
  pages/
    index.astro        Home
    kit.astro          Espécime do design system (interno, não indexado)
  content/             Relatórios e integrantes (fase 1)
public/
  fonts/               Archivo e IBM Plex Mono (.woff2, servidos localmente)
  favicon.svg
```

## Regras da marca que são requisito, não estética

Estas vêm do manual de marca e do design system em
`../Marca/Brasil Online Design System/`. Quebrar qualquer uma delas compromete
a reivindicação de imparcialidade do observatório ou a acessibilidade:

- **Assinatura OBSERVA obrigatória em toda página.** A única exceção é o símbolo
  isolado como avatar.
- **Âmbar nunca como texto sobre fundo claro** (2,15:1, reprova na WCAG). Use
  `--amber-dark` (4,92:1, AA). Fill âmbar sobre fundo claro exige contorno navy de 1pt.
- **Nunca o par verde+amarelo** — lê como marcador político de direita desde 2013/2018.
- **Esquerda = Azul OBSERVA, Direita = Âmbar, sempre nessa ordem.** Os dois campos
  recebem o mesmo espaço, o mesmo vocabulário e a mesma qualificação.
- **Toda página que mostra número nomeia a amostra** — período, número de perfis,
  plataformas. A série mede 162 perfis monitorados, não a opinião pública.
- **Voz descritiva, nunca avaliativa.** "A direita concentra 66,3% das interações",
  não "a direita domina as redes". Sem verbos de guerra, sem emoji.
- **Mono em caixa alta e entreletra aberta** para toda data, percentual, nome de
  plataforma e a assinatura. É o que faz o conteúdo ler como relatório de
  observatório em vez de post de rede social.
- **Sem sombra, gradiente, textura, foto ou blur.** Bloco de cor chapado é o
  movimento visual da marca.
- **Nunca girar ou distorcer o símbolo** — girado, deixa de citar a bandeira.

Nenhuma cor, tamanho ou espaçamento deve ser escrito à mão fora de `tokens.css`.

## Publicar

Deploy automático no Cloudflare Pages a cada push. Para publicar uma edição nova,
ver o guia da fase 6 (a escrever).
