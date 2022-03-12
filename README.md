# produção

Era um projeto particlar, para meu próprio controle financeiro e de um Sìtio qu eu gerenciava

Esteve em produção na AWS por alguns anos nos os domínios:

www.ctrlh.online ou www.controlh.online

ssh ubuntu@18.220.11.41


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


