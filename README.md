# workshop-aberto-02

[![Arquitetura](arquitetura_workshop.png)](https://link.excalidraw.com/l/8pvW6zbNUnD/5oOZyiYIuS1)

## Processos e Requisitos de Desenvolvimento do ETL

Este projeto de ETL (Extração, Transformação e Carga) envolve os seguintes processos e requisitos:

1º  Baixar arquivos do Google Drive: Os arquivos necessários são baixados do Google Drive para o ambiente local.

2º Listar arquivos no diretório: Os arquivos baixados são listados no diretório para posterior processamento.

3º Checar tipo do arquivo: Os arquivos são verificados quanto ao seu tipo.

- Para arquivos CSV: São lidos como arquivos CSV.
- Para arquivos JSON: São lidos como arquivos JSON.
- Para arquivos Parquet: São lidos como arquivos Parquet.

4º Transformar em DataFrame: Os dados são transformados em DataFrame para facilitar a manipulação.

5º Checar se o arquivo foi processado: Verifica-se se o arquivo já foi processado anteriormente.

- Se sim, o processo é encerrado.
- Se não, o processo continua.
- Salvar no PostgreSQL: Os dados são salvos no PostgreSQL para armazenamento permanente.

5º Registrar arquivo como processado: Após o processamento, o arquivo é registrado como processado para evitar duplicações.

6º Fim do processamento do arquivo: O processo de ETL é concluído.

Este conjunto de processos e requisitos garante uma execução eficiente e eficaz do ETL, permitindo a extração, transformação e carga de dados de forma organizada e controlada.