/**
 * Constantes do projeto.
 * O recorte metodológico (amostra) fica aqui porque precisa aparecer, com o
 * mesmo número, em toda página que exibe dado — é regra editorial da série.
 */

export const SITE = {
  name: 'Brasil Online',
  endorsement: 'Uma série do OBSERVA',
  institution: 'OBSERVA — Observatório de Conflitos na Internet',
  university: 'UFABC',
  description:
    'Relatório semanal sobre a polarização do debate político nas redes sociais durante as Eleições Presidenciais de 2026, produzido pelo OBSERVA — Observatório de Conflitos na Internet (UFABC).',
  contact: 'claudio.penteado@ufabc.edu.br',
  locale: 'pt-BR',
} as const;

/** Recorte da série — mencionar sempre que houver número na tela. */
export const AMOSTRA = {
  perfis: 162,
  plataformas: ['X', 'Instagram', 'TikTok'] as const,
  campos: ['Esquerda', 'Direita'] as const,
} as const;

export const NAV = [
  { label: 'Início', href: '/' },
  { label: 'Relatórios', href: '/relatorios' },
  { label: 'Quem somos', href: '/quem-somos' },
] as const;

/**
 * Perfis do projeto. Só entra no rodapé o que tem `url` — botão que não leva
 * a lugar nenhum é pior que botão ausente. Para publicar uma rede nova, basta
 * preencher a url aqui.
 */
export const REDES = [
  { rede: 'instagram', label: 'Instagram', url: 'https://www.instagram.com/observa.internet/' },
  { rede: 'linkedin', label: 'LinkedIn', url: '' },
  { rede: 'tiktok', label: 'TikTok', url: '' },
  { rede: 'x', label: 'X', url: '' },
] as const;
