# Contextualização de texto por linha

No momento, os textos analisados estão em main. Tem três exemplos, na linha <code>textoAnalisado = ...</code> é possivel escolher qual vai ser usado.

## Modo de uso

### Inicie um ambiente virtual
    python3 -m venv local-env

### Ative o ambiente
UNIX:

    source local-env/bin/activate

Windows:

    local-env\Scripts\activate
    
### Instale pacotes necessarios

    pip install -r requirements.txt


### Indique a API-Key
Crie uma API-Key em https://aistudio.google.com/app/apikey se você ainda não tiver uma. Crie um arquivo .env na pasta do projeto e inclua nele:
    
    GOOGLE_API_KEY=alguma-chave

### Inicie o script

    python3 src/main.py