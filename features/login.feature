@Login
Feature: Login no site
  A fim de realizar login no site
  Como usuario legal
  Que o mesmo possa ganhar um resultado benefico que o promova a meta

  Background: Acessar pagina de login
    Given esta na pagina home do site
    When seleciona botao Login
    Then o site redireciona para pagina de login


  Scenario Outline: Preencher dados do login
    When preenche o campo "Email" com "<email>"
    When preenche o campo "Senha" com "<senha>"
    And seleciona o botao "ENTRAR"
    Then o site redireciona para o dashboard
    Examples:
      | email                            | senha         |
      | carloshenriquepp22@gmail.com     |    12062019   |

