# produção

www.ctrlh.online ou www.controlh.online

# .env
ex:

```
SECRET_KEY==sua_chave_secreta_aqui
#Local
DEBUG=True

ALLOWED_HOSTS=127.0.0.1, .localhost, .

DATABASE_NAME=helper
DATABASE_USER=fabiano
DATABASE_PASS=fabiano
DATABASE_HOST=localhost
DATABASE_PORT=5432
DATABASE_ENGINE=django.db.backends.postgresql_psycopg2

EMAIL_BACKEND=django.core.mail.backends.console.EmailBackend
EMAIL_HOST=localhost
EMAIL_PORT=25
EMAIL_USE_TLS=False
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
```


# Helper

Sistema para gerenciamento de eventos (compromissos, consultas, atendimentos, ...) que possibilita a interação de vários usuáios com múltiplas agendas, em um mesmo ambiente.

### Clientes e Usuários

* Clinica Média: médicos, secretárias e pacientes.
* Clinica Veterinária: veterinários, secretárias e pacientes.
* Cabelereiro: cabelereiros, manicures, pedicures, secretárias e clientes.
* Advocacia: advogados, secretárias, n clientes.

### Perfis

* profissional core (médico, veterinário, advogado)

* profissional auxiliar (secretária)

* clientes

### Features

* agendar

* calcular data de vencimento de cartão;

    - fracionar um pagamento com cartão em parcelas, dentro das datas corretas das faturas

    - programar envio de email com alerta sobre a fatura (ex: fatura do cartão xxx atingiu $$$,00) 

    - programar alerta: "se a conta entrar no nvermelho" em um período x, ex: daqui 30 dias, ou daqui 3 meses, sistema envia um email de alerta (somente para contas pagas, free não)

    - Listar tarefas, a partir da data.today(), + aquelas que tenham VALOR E não estejam marcadas como PAGO.

* atender

* efetuar transações financeiras

* no cadastro da conta, o dono da conta deve preencher um campo que ajude a identificar o tipo de profissional core da sua conta, e oferecer certa "perssonalização" nos forms

* poder logar com contas: gmail, facebook, linkedin, ...

* cadastro de eventos para profissional Core pelo próprio ou por um profissional auxiliar

* eventos podem ser recorrentes: todo mês, na mesma data, ex:
    - pagamento (-) ou recebimento (+) de cartão de crédito
    - recebimento de salário (todo 5 dia útil)
    - recebimento de aluguel, todo dia x;

* se o profissional core desejar, o cliente poderá cadastrar o evento se a agenda (horários não comprometidos) for pública. Nesse caso, depois um profissional confirmar o agendamento e o valor se houver.

* envio de email confirmando o evento

* envio de email, alertando o compromisso (tipo agenda do gmail, min, h, dia antes)

* possibilidade de agendar ou não mais de um evento para o mesmo horário do mesmo profissional core
    - o default deve ser Não;
    - isso é só uma hipótese, devemos pensar melhor se é útil e gera valor

### Potenciais fontes de remuneração do sistema:

* tipo bitbucket, só que o bitbuquet cobra US$ / mês, ex:
    - até 5 usuários free
    - até 10 usuários U$ 10
    - até 25 usuários U$ 25
    - até 50 usuários U$ 50
    - até 100 usuários U$ 100
    - então, a definir, prioridade é fazer um piloto.

* pagamentos de eventos (consulta, aluguel, ....) via sistema (%) cartão de crédito;

* contas free tem propagandas (); contas pagas podem optar em não ver as propagandas

#Concorrência:

- http://www.infomoney.com.br/conteudo-patrocinado/noticia/4554710/startup-ajuda-empreendedor-gerir-empresa-forma-eficiente

- Conta Azul

```
Ao comprar algo, você registra a compra no sistema e automaticamente ele atualiza o estoque,
atualiza o contas a pagar e por consequência o fluxo de caixa.
Quando você vende é a mesma coisa, o sistema emite a nota fiscal, baixa o estoque,
alimenta o contas a receber e o fluxo de caixa, automaticamente.
O fluxo para prestação de serviços também é muito bem atendido pelo 

O sistema chama atenção pela excelente relação custo-benefício:
a assinatura começa por R$ 29. Além disso, 
utiliza o mesmo sistema de segurança que os bancos,
garantindo o tráfego e armazenamento seguro de todos dados.
Constantes atualizações são feitas para que o sistema esteja sempre
atendendo bem tanto aos requisitos de mercado quanto a aspectos legais e tributários.


```


Fabiano Almeida / José Thomazini
