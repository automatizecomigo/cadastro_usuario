Feature: Acessar a pagina Goden Movie Studio e realizar busca de filmes

   @Buscar_filmes
  Scenario: Realizar a busca de filmes
    Given que estou na página Goden Movie Studio
    When Busco por filmes
    Then valido se a busca foi realizada com sucesso