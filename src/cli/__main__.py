import typer
from auth_app.db import sqlalchemy
from auth_app.main import create_engine_

from cli import admin

app = typer.Typer(name="cli")

sqlalchemy.engine = create_engine_()

app.add_typer(admin.router, name="admin")

if __name__ == "__main__":
    app()
