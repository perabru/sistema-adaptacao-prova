# Escola Máximu's — Sistema Final Firebase Responsivo

Versão final com Firebase Authentication, Firebase Realtime Database, cadastro manual de alunos, cadastro manual de professores e importação por planilha.

## Como abrir

1. Extraia o ZIP.
2. Clique duas vezes em `abrir-sistema-windows.bat`.
3. Acesse:
   - Coordenação: `http://localhost:5500/admin.html`
   - Professor: `http://localhost:5500/index.html`

Não abra o HTML por duplo clique. Use sempre o servidor local.

## Configuração obrigatória no Firebase

1. Ative **Authentication > Sign-in method > E-mail/Senha**.
2. Crie ou use um **Realtime Database**.
3. Publique o conteúdo de `firebase-rules.json` nas regras do Realtime Database.
4. Mantenha os arquivos `admin.html`, `index.html`, `app.js` e `styles.css` na mesma pasta.

## O que esta versão faz

### Coordenação

- Login pelo Firebase Authentication.
- Primeiro cadastro da coordenação pela tela inicial.
- Cadastro manual de aluno novo.
- Cadastro manual de professor novo.
- Importação de alunos via planilha `.xlsx`, `.xls` ou `.csv`.
- Importação de professores via planilha `.xlsx`, `.xls` ou `.csv`.
- Edição e exclusão de alunos.
- Exclusão de professores cadastrados no banco.
- Associação de professores às turmas importadas ou digitadas manualmente.
- Visualização das colunas lidas da planilha.
- Backup JSON.
- Dados sincronizados em tempo real pelo Firebase Realtime Database.

### Professor

- Login pelo Firebase Authentication.
- Visualização somente das turmas vinculadas pela coordenação.
- Seleção de turma e aluno.
- Complemento pedagógico por aluno salvo em tempo real.
- Geração automática de prova ou atividade.
- PDF individual do aluno.
- PDFs da turma inteira.
- QR Code pedagógico.
- Lista clara das adaptações aplicadas no PDF e na tela.

## Cadastro manual de aluno

A coordenação pode cadastrar aluno manualmente informando:

- nome;
- turma;
- número;
- diagnóstico/laudo/necessidade;
- tipo de documento/adaptação;
- adaptações necessárias;
- orientações pedagógicas.

Esse cadastro aparece automaticamente para o professor vinculado à mesma turma.

## Cadastro manual de professor

A coordenação pode cadastrar professor manualmente informando:

- nome;
- e-mail;
- senha;
- confirmação de senha;
- turmas marcadas na lista;
- turmas extras digitadas manualmente.

O professor é criado no Firebase Authentication e recebe um perfil no Realtime Database.

## Importação por planilha

### Alunos

A importação percorre todas as abas da planilha, tenta encontrar o cabeçalho automaticamente e preserva todas as colunas. O sistema identifica campos como:

- nome do aluno;
- turma/série;
- número;
- diagnóstico/laudo;
- adaptação;
- tipo de prova;
- orientações.

### Professores

A planilha de professores pode conter:

- nome;
- email/e-mail;
- senha;
- turmas.

Para várias turmas, separe por vírgula, ponto e vírgula ou barra vertical.

## Adaptações automáticas aplicadas

O sistema detecta informações do laudo, adaptação, tipo de prova, orientação da coordenação e complemento do professor. Com base nisso, aplica:

- fonte ampliada;
- espaçamento ampliado;
- linguagem simplificada;
- comandos em blocos;
- dica pedagógica;
- espaço maior para resposta;
- prova completamente adaptada quando indicado;
- letra maiúscula quando indicado;
- múltipla escolha quando indicado;
- redução de carga cognitiva;
- apoio para TDAH;
- apoio para TEA;
- apoio para DI;
- apoio para Dislexia;
- apoio para DPAC;
- orientação de tempo/apoio ampliado.

## Responsividade

A interface foi ajustada para:

- celular;
- tablet;
- notebook;
- desktop;
- telas pequenas com rolagem segura;
- tabelas com rolagem horizontal;
- formulários em uma coluna no celular;
- menu lateral transformado em navegação horizontal em telas menores;
- botões grandes para toque;
- prévia de PDF com rolagem segura.

## Arquivos principais

- `admin.html`: área da coordenação.
- `index.html`: área do professor.
- `app.js`: lógica Firebase, importação, cadastro manual e geração de provas.
- `styles.css`: visual responsivo.
- `firebase-rules.json`: regras do Realtime Database.
- `servidor-local.py`: servidor local.
- `abrir-sistema-windows.bat`: atalho para abrir no Windows.


## Atualizações desta versão

- Logo oficial da escola aplicado na prova/PDF.
- Adaptações pedagógicas não aparecem no corpo do PDF; elas ficam registradas dentro do QR Code da assinatura digital.
- Ações de cadastro e geração agora têm animações de carregamento.
- Textos das ações ficaram mais limpos, sem exibir o nome da tecnologia no uso diário.
- Responsividade refinada para celular, tablet e desktop.

## IA local para gerar questões pelo conteúdo ministrado

Esta versão adiciona um campo chamado **Conteúdo ministrado para a IA gerar questões** na área do professor.

Como usar:

1. Selecione turma e aluno.
2. Preencha disciplina, tema, quantidade, dificuldade e formato.
3. Cole no campo de conteúdo ministrado o texto da aula, resumo, tópicos, apostila ou conteúdo trabalhado.
4. Clique em **Gerar questões com IA**.
5. O sistema analisa palavras-chave, frases principais e área do conhecimento para montar questões relacionadas ao conteúdo.
6. O professor pode revisar e editar tudo no editor estilo Word antes de gerar a prévia ou PDF.

Observação: a IA desta versão é local, roda dentro do navegador e não envia o conteúdo para serviços externos. Ela usa análise de texto, extração de conceitos e modelos pedagógicos para criar questões automaticamente.


## Atualização: menu dropdown e IA com formatação pronta

Esta versão adiciona:

- Menu rápido em dropdown na área da coordenação.
- Menu rápido em dropdown na área do professor.
- A IA passa a gerar a atividade já formatada em blocos bonitos, no mesmo padrão visual da prévia.
- O conteúdo gerado pela IA já aparece organizado no editor estilo Word.
- A prévia e o PDF preservam a formatação da atividade gerada.




## Atualização: IA local melhorada no app.js

Esta versão remove a IA generativa externa e volta para uma IA local em JavaScript, funcionando diretamente no `app.js`, sem chave de API e sem depender de internet.

Melhorias adicionadas:

- análise de conteúdo ministrado diretamente no navegador;
- extração de palavras-chave e conceitos principais;
- identificação de frases relevantes;
- identificação de definições do tipo “é”, “são”, “representa”, “significa”;
- extração de exemplos e números/frações;
- classificação automática da área do conhecimento;
- geração melhorada para Português, crase, frações, tecnologia, ciências e humanas;
- respeito ao formato escolhido: misto, múltipla escolha ou discursiva;
- adaptação ao perfil do aluno;
- geração já formatada em cards bonitos no editor;
- prévia e PDF continuam preservando a formatação.


## Atualização: app.js parrudo para conteúdos do Ensino Médio

Esta versão melhora fortemente a IA local dentro do `app.js`, sem depender de APIs externas.

A IA local agora foi preparada para conteúdos do Ensino Médio, incluindo:

- Matemática: frações, porcentagem, funções, equações, geometria, trigonometria, estatística e probabilidade.
- Língua Portuguesa: crase, interpretação textual, gramática e leitura.
- Redação: tese, argumentos, repertório, conclusão e proposta de intervenção.
- Literatura: escolas literárias, contexto histórico, linguagem e características de obras.
- Inglês: leitura, vocabulário e gramática básica.
- Física: cinemática, dinâmica, energia, eletricidade, ondas e óptica.
- Química: atomística, ligações químicas, estequiometria, soluções, pH, orgânica, termoquímica e equilíbrio químico.
- Biologia: célula, genética, ecologia, evolução e fisiologia.
- História: Brasil Colônia, revoluções, guerras, democracia, cidadania e processos históricos.
- Geografia: clima, cartografia, urbanização, globalização e meio ambiente.
- Filosofia: ética, conhecimento e filosofia política.
- Sociologia: cultura, desigualdade e trabalho.
- Artes, Educação Física e Tecnologia.

Melhorias técnicas:

- classificador de disciplina e área;
- detector de tópicos do Ensino Médio;
- extração de frases relevantes;
- extração de definições;
- extração de exemplos;
- extração de datas, números, porcentagens, frações e fórmulas;
- plano de avaliação por dificuldade;
- variação entre identificar, compreender, aplicar, relacionar, analisar, comparar, avaliar, resolver e sintetizar;
- respeito ao formato escolhido: misto, múltipla escolha ou discursiva;
- geração com linguagem escolar e adaptada;
- formatação automática no modelo bonito da prévia.


## Atualização: colagem simples, PDF com quebra melhorada e hamburger em todas as telas

Esta versão adiciona:

- placeholder grande no campo de conteúdo, com exemplos prontos de como colar tópicos;
- botões de modelos rápidos para preencher o conteúdo automaticamente:
  - modelo simples;
  - frações;
  - crase;
  - física/cinemática;
- leitura melhorada de tópicos colados em lista com hífen, bolinha ou numeração;
- IA local ainda mais preparada para entender estrutura do tipo Tema, Tópicos, Exemplos, Fórmulas e Objetivo;
- correção da quebra de página do PDF, evitando cortar questões, cards, assinaturas e blocos importantes no meio da página;
- menu hamburger em todas as telas principais, com menu lateral em gaveta também no desktop.


## Atualização: QR Code em JSON + IA local mais forte + inserção mais simples

Esta versão garante que o QR Code da prova/atividade retorne um JSON válido ao ser lido.

O JSON contém:

- sistema;
- tipo de mensagem;
- código do documento;
- dados do documento;
- dados do aluno;
- mensagem de conferência;
- lista `adaptacoes_feitas`;
- dados pedagógicos;
- assinatura de validação.

Também foram melhoradas:

- a forma de inserir conteúdo, com painel de 3 passos;
- modelos rápidos adicionais: redação, química, biologia e história;
- botão “Organizar conteúdo colado”;
- botão “Limpar conteúdo”;
- análise de conteúdos estruturados com Tema, Tópicos, Exemplos, Fórmulas, Dados importantes e Objetivos;
- leitura de objetivos/habilidades;
- geração de questões usando fórmulas, datas e objetivos quando aparecem no conteúdo;
- uso de tópicos manuais mesmo quando o sistema não reconhece um tema específico.


## Atualização: correção de layout

Esta versão corrige o layout da área do professor e da coordenação:

- sidebar agora funciona corretamente como gaveta;
- hamburger permanece disponível;
- menu fica fechado por padrão para não apertar o conteúdo;
- cards e painéis ficaram mais largos;
- editor e toolbar ficaram melhor distribuídos;
- campos e selects agora não estouram com nomes maiores;
- grade principal vira uma coluna em telas menores;
- padding e espaçamento foram ajustados para desktop, tablet e celular.


## Atualização: layout final para GitHub Pages

Esta versão remove o menu dropdown e mantém apenas o menu hamburger com navegação lateral.

Correções:

- menu dropdown removido da área do professor e da coordenação;
- hamburger não aparece mais nas telas de login;
- correção do conflito entre `.app` e `.hidden`;
- menu lateral fica fechado por padrão;
- layout pronto para GitHub Pages;
- arquivo `.nojekyll` adicionado para publicação estática;
- espaçamentos e responsividade ajustados para desktop, tablet e celular.
