# TodoApp
## Teste back-end Biome-hub (Parcialmente Completo)

Implementar uma TODO List utilizando Python, Django e outras bibliotecas/tecnologias que achar necessário.

(X) Possibilidade de criar uma nova conta, realizar login e recuperação de senha;
(X) CRUD de TODO Lists: criar, remover, editar o título;
- CRUD de tarefas: para cada TODO List, possibilidade de criar tarefas, editar, remover, marcar com concluída e adicionar uma deadline;
- Possibilidade de atribuir uma tarefa para um usuário;
- Relatório diário via e-mail de tarefas concluídas naquele dia e próximas prioridades, baseado no deadline;
- Possibilidade de solicitar um relatório, enviando a data de início e fim, em um endpoint REST com autenticação utilizando token. A resposta do endpoint deve ser imediata, informando se é possível a geração do relatório e, se sim, para qual e-mail será enviado. A geração e envio via e-mail deve acontecer de forma assíncrona (em background);
- Possibilidade de fazer login no usuário `admin@biome-hub.com`, onde seu password será `xxyyzz` onde `xx` será o dobro do dia atual, `yy` será o dobro do mês e `zz` a hora atual (sempre 6 caracteres);

## Must Have (OK)
(X) Python 3.6+;
(X) Django 2.0+;
(X) Git para versionamento do projeto;

## O que será avaliado?
- Arquitetura e modularidade so sistema;
- Conhecimento da linguagem de programação (Python);
- Conhecimento do framework utilizado (Django);
- Uso do Git;

## Bônus
- Utilizar Docker;
(X) Deploy em algum serviço de cloud (https://todoapp-karol.herokuapp.com/);
- O Relatório de tarefas ser em PDF;
