@Cadastro
Feature: Cadastrar um usuario
  A fim de realizar um cadastro de usuario
  Como usuario legal do site
  Que o mesmo possa ganhar um resultado benefico que o promova a meta

  Background: Acessar pagina de login
    Given esta na pagina home do site
    When seleciona botao Login
    Then o site redireciona para pagina de login

@PaginaCadastro
  Scenario Outline: Preencher formulario de cadastro
    When seleciona botao "Criar conta"
    When o site redireciona para pagina de cadastro
    When preenche o campo "nome completo" com "<nome_completo>"
    When preenche o campo "cpf" com "<cpf>"
    When preenche o campo "email" com "<email>"
    When preenche o campo "whatsapp" com "<whatsapp>"
    And seleciona botao "PROSSEGUIR"
    When preenche o campo "senha" com "<senha>"
    When preenche o campo "confirmar senha" com "<confirmar_senha>"
    When seleciona "<sexo>" no select "sexo"
    When preenche o campo "data de nascimento" com "<data_nascimento>"
    When preenche o campo "cep" com "<cep>"
    When preenche o campo "numero" com "<numero>"
    When aceita os termos de uso selecionando o botao "checkbox"
    And seleciona botao "CADASTRAR"
    Then o cadastro e realizado com sucesso
    Examples:
      | nome_completo           | cpf         | email                         | whatsapp     | senha    | confirmar_senha | sexo      | data_nascimento | cep      | numero |
      | Carlos Henrique Pereira | 87651132092 | carloshenriquepp22@gmail.com  | 11940028922  | 12062019 | 12062019        | Masculino | 09122001        | 74820010 |  00    |