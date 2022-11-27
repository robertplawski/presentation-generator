from typing import Optional, List
from pathlib import Path
import typer

from pypresentation import core, __app_name__, __version__

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.command()
def generate(topics: List[str], path: Path = typer.Option("./data/output.pptx","--output","-o"),author: str = typer.Option("Author","--author","-a"),title: str = typer.Option("Title", "--title", "-t"),lang: str = typer.Option("pl","--language","-l"),max_letters_per_page:int = typer.Option(500, "--max_letters","-m"), split_on:str = typer.Option("\n", "--split_on","-s")):
    generator = core.Generator(topics=topics, lang=lang, path=path, author=author, title=title, max_letters_per_page=max_letters_per_page, split_on=split_on)
    raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show application's version and exit",
        callback=_version_callback,
        is_eager=True
    )
) -> None:
    return
