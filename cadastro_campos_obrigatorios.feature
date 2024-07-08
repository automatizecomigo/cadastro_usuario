# Created by rafael.pantoja at 06/07/2024
Feature: Acessar a pagina Goden Movie Studio e realizar o preenchimento de
  campos obrigatórios


  @Cadastro_de_usuario_com_sucesso
  Scenario: Realizar o preenchimento de campos obrigatórios
    Given que estou na página Goden Movie Studio
    When faco o preechimento dos campos obrigatórios
    Then valido se o usuario foi cadastra com sucesso


  @Cadastro_de_usuario_com_nome_invalido
  Scenario: Realizar o preenchimento de campos obrigatórios com credencias invalidas
    Given que estou na página Goden Movie Studio
    When faco o preechimento dos campos obrigatórios com nome invalido
    Then valido que o nome nao e aceito










