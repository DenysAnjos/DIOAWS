Este projeto teve como objetivo criar minha primeira stack utilizando a AWS CloudFormation, aplicando conceitos de Infrastructure as Code(IaC) para provisionar recursos de forma automatizada.

O que é uma stack?
Uma Stack é um conjunto de recursos AWS criados e gerenciados como uma única unidade.
Em vez de criar manualmente, como por exemplo:
- 1 instância EC2
- 1 Security Group
- 1 bucket S3
- 1 banco RDS
- Regras de rede
- Permissões IAM

Você descreve tudo em um arquivo (YAML/JSON) e o CloudFormation cria tudo isso automaticamente

## Metas
- Aplicar conceitos aprendidos no curso
- Criar uma Stack do zero
- Documentar o processo realizado
- Publicar a implementação no GitHub

## Recursos utilizados:
- AWS CloudFormation
- Amazon S3(bucket)
- Visual Studio Code
- GitHub

## Processo realizado
1. Criação do template YAML no VS Code
2. Upload do template para o AWS CloudFormation
3. Criação da Stack
4. Verificação do bucket S3 criado
5. Exclusão da Stack e remoção do Bucket

## Insights adquiridos
- Entendi como uma Stack funciona na prática
- Aprendi como a criar e gerenciar uma Stack usando YAML
- Aprendi que o CloudFormation pode automatizar tarefas que normalmente seriam feitas manualmente
- Aprendi que excluir uma Stack também remove os recursos associados
- Percebi como Infrastructure as Code facilita muito a produtividade