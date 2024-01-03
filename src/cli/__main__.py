import typer

from auth_app.db import sqlalchemy
from auth_app.main import create_engine_
from cli import admin

from . import auth, user_rep

app = typer.Typer(name="cli")

sqlalchemy.engine = create_engine_()

app.add_typer(auth.router, name="auth")
app.add_typer(user_rep.router, name="user_rep")
app.add_typer(admin.router, name="admin")

if __name__ == "__main__":
    app()
