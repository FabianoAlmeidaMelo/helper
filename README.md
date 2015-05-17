# Helper

Sistema para gerenciamento de eventos (compromissos, consultas, atendimentos, ...)
que possibilita a interação de vários usuáios com múltiplas agendas, em um mesmo ambiente.

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


Fabiano Almeida / José Thomazini
