import click
from flask.cli import FlaskGroup
from app import create_app


def __init_db():
    from app.help.init_db import InitDB
    return InitDB()


def __add_super_admin(init_db):
    print("正在添加超级管理员！")
    init_db.add_administrator()
    print("添加超级管理员已完成！")


@click.group(cls=FlaskGroup, create_app=create_app)
def cli():
    pass


@cli.command()
@click.option("--super_admin/--no_super_admin", default=False)
def db_init(super_admin):
    print("正在初始化数据库！")
    init_db = __init_db()
    init_db.create_db()
    print("数据库初始化已完成！")
    if super_admin:
        __add_super_admin(init_db)


@cli.command()
def db_drop():
    print("正在删除数据库！")
    init_db = __init_db()
    init_db.drop_db()
    print("数据库删除已完成！")


@cli.command()
def add_super_admin():
    init_db = __init_db()
    __add_super_admin(init_db)


if __name__ == '__main__':
    cli()
