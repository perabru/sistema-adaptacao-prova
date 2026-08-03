# Como publicar no GitHub Pages

## 1. Configurar o Firebase

1. Ative **Authentication > E-mail/Senha**.
2. Em **Authentication > Settings > Authorized domains**, adicione `SEU-USUARIO.github.io`.
3. Crie o Realtime Database.
4. Publique o conteúdo de `firebase-rules.json` nas regras do banco.

### Criar a primeira coordenação com segurança

1. Em **Authentication > Users**, crie o usuário da coordenação.
2. Copie o UID gerado.
3. No Realtime Database, crie o caminho `usuarios/UID_COPIADO` com:

```json
{
  "role": "coordenacao",
  "nome": "Coordenação Escola Máximu's",
  "email": "coordenacao@escola.com",
  "turmas": [],
  "ativo": true
}
```

Depois disso, a própria coordenação poderá cadastrar professores pelo sistema.

## 2. Criar o repositório

1. Crie um repositório no GitHub.
2. Envie os arquivos da pasta para a raiz do repositório.
3. Não envie planilhas, backups, laudos ou documentos com dados de alunos.

## 3. Ativar o GitHub Pages

1. Abra **Settings > Pages** no repositório.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Selecione a branch `main` e a pasta `/ (root)`.
4. Clique em **Save**.

O endereço normalmente será:

```text
https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/
```

Área do professor:

```text
https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/index.html
```

Área da coordenação:

```text
https://SEU-USUARIO.github.io/NOME-DO-REPOSITORIO/admin.html
```

## 4. Conferência antes de usar

- login da coordenação;
- importação manual da planilha;
- cadastro de um professor de teste;
- vínculo de turma;
- geração mista e discursiva;
- geração por quantidade mais alunos especiais;
- uso do banco de questões pela IA local;
- PDF individual;
- ZIP da turma;
- abertura pelo celular.
