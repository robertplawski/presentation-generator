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
def generate(topics: List[str], path: Path = typer.Option("output.txt","--output","-o"),lang: str = typer.Option("pl","--language","-l")):
    generator = core.Generator(topics=topics, lang=lang, path=path)
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
