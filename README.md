# TVMV Python Service Boilerplate

Standardudgangspunkt for Python-projekter i TV MIDTVEST-regi.

Intern note: Navngiv gerne med 'tvmv-' foran navnet på din service. Det er mere overskueligt i produktionsmiljøet.

```bash
git clone https://github.com/tvmidtvest/tvmv-default-service-template.git [tvmv-your-service-name]
```

```bash
cd [tvmv-your-service-name]
```

```bash
rm -rf .git
```

```bash
python -m venv .venv
```

```bash
source .venv/bin/activate
```

```bash
pip install -r requirements.txt
```

```bash
cp EXAMPLE.env .env
```

```bash
code .
```

- Skriv din kode i `main.py` og eksekver med `python app/main.py` fra kommandolinjen.
- Split op i flere filer, hvis det bliver for uoverskueligt eller det virker logisk at dele det op i flere filer. Brug `import` i main-filen.
- Læg alle dine python-filer i `app`-mappen
- Læg miljøvariabler som adgangskoder, api-nøgler etc i `.env`-filen.
- Fjern teksten i denne README og beskriv din service: Hvad gør den? Hvad er der af afhængigheder?

## Github

Inden du lægger det på Github eller når du har pip-installeret nye moduler, husk da at lave en `pip freeze > requirements.txt` så de moduler servicen har brug for kommer med i requirements.txt.

Det er god stil at synkronisere med Github mindst én gang pr. dag, hvor du arbejder på koden. Ved du, at flere arbejder på samme kode, så husk at lave en `git pull` af og til, så du har den seneste version af koden.

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

Husk i øvrigt også lige at tjekke denne en gang i mellem: https://github.com/tvmidtvest/tvmv-docs/blob/main/best-practices.md 😉
