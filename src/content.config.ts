import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

/**
 * Uma edição = um arquivo Markdown aqui + um PDF em public/relatorios/.
 * O corpo do Markdown é a apresentação (2–3 parágrafos, voz descritiva,
 * amostra nomeada, números ancorados — ver README).
 *
 * `dados` fica preenchido desde a v1 mesmo sem ser exibido no site ainda,
 * para a fase 2 (gráficos no site) não exigir reabrir o acervo inteiro.
 * Só entra o que o relatório afirma como agregado — nada é calculado ou
 * estimado aqui.
 */
const relatorios = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/relatorios' }),
  schema: () =>
    z.object({
      edicao: z.number().int().positive(),
      periodoInicio: z.coerce.date(),
      periodoFim: z.coerce.date(),
      dataPublicacao: z.coerce.date(),
      titulo: z.string(),
      /** Uma frase para o card da lista e para a meta description */
      chamada: z.string(),
      plataformas: z.array(z.enum(['X (Twitter)', 'Instagram', 'TikTok'])),
      temas: z.array(z.string()),
      perfisMonitorados: z.number().int().positive(),
      dados: z
        .object({
          publicacoesEsquerda: z.number().min(0).max(100).optional(),
          publicacoesDireita: z.number().min(0).max(100).optional(),
          interacoesEsquerda: z.number().min(0).max(100).optional(),
          interacoesDireita: z.number().min(0).max(100).optional(),
        })
        .optional(),
      /** Caminho em public/, ex.: /relatorios/edicao-01.pdf */
      pdf: z.string(),
      /**
       * true quando o corpo (apresentação) foi redigido por IA a partir do
       * resumo executivo do PDF, em vez de escrito por alguém da equipe.
       * Quando true, a tela de Relatório-detalhe é obrigada a exibir a nota
       * de rodapé de divulgação — ver RelatorioDetalhe (fase 4). Cada edição
       * some esse campo (ou vira false) assim que alguém da equipe assinar
       * o texto de fato.
       */
      apresentacaoGeradaPorIA: z.boolean().optional(),
    }),
});

/**
 * Uma pessoa = um arquivo Markdown. Só `nome` é obrigatório — a ficha técnica
 * do relatório não traz formação, Lattes nem rede social de ninguém; esses
 * campos ficam undefined até a equipe de divulgação levantar a informação.
 */
const integrantes = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content/integrantes' }),
  schema: () =>
    z.object({
      nome: z.string(),
      formacaoAtual: z.string().optional(),
      grupo: z.string().optional(),
      lattes: z.string().url().optional(),
      redeSocial: z.string().url().optional(),
      /** Ordem de exibição dentro do grupo — menor primeiro. Sem valor, entra por ordem alfabética do nome. */
      ordem: z.number().optional(),
    }),
});

export const collections = { relatorios, integrantes };
