import { getCollection, type CollectionEntry } from 'astro:content';

export type Relatorio = CollectionEntry<'relatorios'>;

/** Mais recente primeiro. */
export async function getRelatoriosOrdenados(): Promise<Relatorio[]> {
  const todos = await getCollection('relatorios');
  return todos.sort((a, b) => b.data.edicao - a.data.edicao);
}

// As datas do frontmatter são "calendário puro" (ex.: 2026-08-11), sem hora.
// O YAML/Zod as interpreta como meia-noite UTC — formatar em timeZone local
// arrisca exibir o dia anterior (UTC-3 antes das 21h vira o dia de trás).
// Toda formatação de data de conteúdo usa timeZone: 'UTC' por isso.
const TZ_CONTEUDO = 'UTC';

export function formatarPeriodo(inicio: Date, fim: Date): string {
  const opts: Intl.DateTimeFormatOptions = { day: '2-digit', month: 'short', timeZone: TZ_CONTEUDO };
  const i = inicio.toLocaleDateString('pt-BR', opts).replace('.', '');
  const f = fim.toLocaleDateString('pt-BR', { ...opts, year: 'numeric' }).replace('.', '');
  return `${i} a ${f}`;
}

/** Referência acadêmica no formato usado na ficha técnica dos relatórios. */
export function comoCitar(relatorio: Relatorio['data']): string {
  const ano = relatorio.dataPublicacao.getUTCFullYear();
  const num = String(relatorio.edicao).padStart(2, '0');
  return `Penteado et al. Brasil Online: Estudo da polarização nas Eleições Presidenciais 2026. Relatório ${num}. OBSERVA, ${ano}.`;
}
