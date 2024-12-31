# Scraping Wellhub Franca-SP

Este projeto realiza web scraping no site [Wellhub](https://wellhub.com/pt-br/search/sp/franca/) para listar academias e estúdios fitness localizados em Franca-SP. O script acessa a página inicial, coleta informações básicas, e depois visita as páginas individuais para capturar dados adicionais relevantes.

<picture width="500">
  <img
    src="https://logodownload.org/wp-content/uploads/2024/11/wellhub-logo.png"
    alt="Wellhub Logo"
  />
</picture>


---

## Dependências

O projeto utiliza as seguintes dependências:

- **Python**: 3.13.1
- **Selenium**: ^4.27.1
- **BeautifulSoup4**: ^4.12.3
- **Pandas**: ^2.2.3
- **Psycopg2-binary**: ^2.9.10
- **SQLAlchemy**: ^2.0.36
- **Python-dotenv**: ^1.0.1

**Nota:** O projeto foi desenvolvido utilizando o navegador Chrome na versão **131.0.6778.204** e seu respectivo ChromeDriver. Você pode baixá-los [aqui](https://googlechromelabs.github.io/chrome-for-testing/).

---

## Instalação

### Requisitos

- **Pyenv**: [Instruções de instalação](https://github.com/pyenv/pyenv)
- **Pipx**: [Instruções de instalação](https://github.com/pypa/pipx)

### Passo a passo

1. Clone o repositório:

   ```bash
   mkdir wellhub
   cd wellhub
   git clone https://github.com/GuilhermehVinicius/Scraping_Welhub.git
   ```

2. Crie uma variável de ambiente chamada `DATABASE_URL` com sua string de conexão dentro de um arquivo `.env` dentro do diretório wellhub.

3. Configure o ambiente Python:

   ```bash
   pyenv install 3.13.1
   pyenv local 3.13.1
   pipx install poetry
   poetry shell
   poetry install
   ```

4. Execute o script principal:

   ```bash
   python main.py
   ```

---

## Utilização com Docker

Para rodar o projeto via Docker, siga os passos abaixo:

1. Construa a imagem Docker:

   ```bash
   sudo docker build -t scrapyng_wellhub_franca .
   ```

2. Execute o container:

   ```bash
   sudo docker run -d scrapyng_wellhub_franca
   ```

---

## Autor

Projeto desenvolvido por GuilhermehVinicius.

