// @ts-check
import { defineConfig } from 'astro/config';

// O domínio definitivo é o da UFABC. Até a FBC liberar o apontamento de DNS,
// o site roda numa URL provisória do Cloudflare Pages — trocar aqui na virada.
export default defineConfig({
  site: 'https://labobserva.pesquisa.ufabc.edu.br',
  output: 'static',
  build: {
    // URLs sem barra final: /relatorios, não /relatorios/
    format: 'file',
  },
});
