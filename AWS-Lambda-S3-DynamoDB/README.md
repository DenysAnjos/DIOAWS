# AWS Lambda + S3 + DynamoDB com LocalStack

Este projeto teve como objetivo praticar tarefas automatizadas utilizando AWS Lambda, Amazon S3 e Amazon DynamoDB em um ambiente local com LocalStack.

A ideia foi simular um fluxo onde um arquivo JSON é enviado para um bucket S3, processado por uma função Lambda e registrado em uma tabela DynamoDB.

## Metas
* Aplicar conceitos aprendidos no curso
* Criar recursos AWS em ambiente local usando LocalStack
* Criar um bucket S3 para receber arquivos
* Criar uma tabela DynamoDB para armazenar os dados processados
* Criar uma função Lambda para processar um arquivo JSON
* Simular um evento do S3 para executar a Lambda
* Documentar o processo realizado no GitHub

## Recursos utilizados
* LocalStack
* AWS CLI
* Amazon S3
* AWS Lambda
* Amazon DynamoDB
* PowerShell
* Visual Studio Code
* GitHub

## Processo realizado
1. Criação da estrutura do projeto no VS Code
2. Inicialização do LocalStack
3. Configuração da AWS CLI com credenciais fictícias
4. Criação do bucket S3 `notas-fiscais-upload`
5. Criação da tabela DynamoDB `NotasFiscais`
6. Criação da função Lambda `ProcessarNotasFiscais`
7. Criação do arquivo `notas_fiscais.json`
8. Upload do arquivo JSON para o bucket S3
9. Invocação da Lambda com um payload simulando evento do S3
10. Processamento dos registros pela função Lambda
11. Gravação dos dados processados na tabela DynamoDB
12. Validação dos registros criados no DynamoDB

## Insights adquiridos
* Entendi como utilizar o LocalStack para simular serviços AWS localmente
* Aprendi a criar recursos AWS locais usando AWS CLI
* Entendi melhor como S3, Lambda e DynamoDB podem trabalhar juntos
* Aprendi como uma função Lambda pode processar dados a partir de um evento
* Percebi que arquivos JSON com encoding incorreto podem gerar erro no processamento
* Aprendi a validar cada etapa separadamente antes de continuar o fluxo
* O uso do LocalStack ajuda a testar serviços AWS sem gerar custos na conta real
