# TVMV Default Service Template

```bash
$ git clone https://github.com/tvmidtvest/tvmv-default-service-template.git
$ mv tvmv-default-service-template [your-service-name]
$ cd [your-service-name]
$ rm -rf .git
$ python -m venv .venv
$ source .venv/bin/activate
$ pip install -r requirements.txt
$ cp EXAMPLE.env .env
$ code .
```

- Skriv din kode i `main.py`
- Split op i flere filer, hvis det bliver for uoverskueligt eller det virker logisk at dele det op i flere filer. Brug `import` i main-filen.
- Læg alle dine filer i `app`-mappen

## Logning

```python
import config

# Altid det samme uanset fil: __name__ sørger for at filens navn kommer med i loggen.
logger = config.get_logger(__name__)

# Bruges sådan:
logger.error('ERROR')

# eller sådan, hvis du vil have noget output med:
logger.error(f'ERROR: {e}')
```

I `.env`-filen kan du sætte logningsniveau og om der skal logges til konsollen. Som default står niveau til `INFO` og log til konsollen er `true`.
