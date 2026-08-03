# Escola Máximu's — Sistema de Provas Adaptadas

Aplicação estática preparada para GitHub Pages. A geração pedagógica funciona no navegador, sem chave de API, servidor próprio ou Cloud Functions.

## Recursos

### Coordenação

- login pelo Firebase Authentication;
- cadastro manual e importação de alunos por XLSX, XLS ou CSV;
- cadastro de professores e vínculo com turmas;
- edição, exclusão, pesquisa e backup em JSON;
- sincronização em tempo real pelo Firebase Realtime Database.

### Professor

- turmas vinculadas pela coordenação;
- provas normais e adaptadas por aluno;
- formatos misto, objetivo e discursivo;
- quantidade separada de questões objetivas e discursivas;
- geração local com base no conteúdo ministrado e nos exercícios compatíveis do banco do professor;
- editor visual com imagens, tabelas e textos de apoio;
- importação de PDF, DOCX, TXT e HTML;
- banco particular de questões;
- PDF A4 individual com paginação, rodapé e blocos protegidos contra cortes;
- ZIP da sala completa;
- lote por quantidade: provas normais sem nome + provas nominais dos alunos especiais;
- modo inteligente, duas versões por aluno, somente normal ou somente adaptada.

## Privacidade

Nenhuma planilha de alunos acompanha a versão pública. Importe os dados somente depois de entrar como coordenação. Não envie planilhas, laudos, backups ou documentos internos ao repositório do GitHub.

O cadastro público da primeira coordenação foi removido. O primeiro perfil deve ser criado diretamente no Firebase, conforme `PUBLICAR-NO-GITHUB-PAGES.md`.

## Publicação

Leia `PUBLICAR-NO-GITHUB-PAGES.md`. O projeto deve ser publicado com `index.html`, `admin.html`, `app.js`, `styles.css`, `logo-escola.png`, `firebase-rules.json` e `.nojekyll` na raiz.

## IA local

A IA local utiliza análise de tópicos, palavras-chave, definições, fórmulas, datas, exemplos, modelos pedagógicos por disciplina e exercícios salvos no banco do próprio professor. A seleção do banco prioriza a mesma disciplina e o mesmo tema. Ela não envia o material da aula para serviços externos. Como toda geração automática, o resultado deve ser revisado pelo professor antes da aplicação.

## Gerar uma sala por quantidade

1. Escolha a turma e monte a prova.
2. Marque **Gerar por quantidade + alunos especiais**.
3. Informe quantas provas normais, sem nome, serão impressas.
4. Clique em **Gerar sala completa**.

O ZIP terá as cópias normais numeradas e acrescentará uma versão adaptada nominal para cada aluno da turma cuja ficha indique necessidade de adaptação.
