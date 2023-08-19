from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool

from data import config


class Database:

    def __init__(self):
        self.pool: Union[Pool, None] = None

    async def create(self):
        self.pool = await asyncpg.create_pool(
            user=config.DB_USER,
            password=config.DB_PASS,
            host=config.DB_HOST,
            database=config.DB_NAME,
            port=5432   # Shu qo'shilgan qism
        )

    async def execute(self, command, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False
                      ):
        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(command, *args)
                elif fetchval:
                    result = await connection.fetchval(command, *args)
                elif fetchrow:
                    result = await connection.fetchrow(command, *args)
                elif execute:
                    result = await connection.execute(command, *args)
            return result

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id SERIAL PRIMARY KEY,
        full_name VARCHAR(255) NOT NULL,
        username varchar(255) NULL,
        telegram_id BIGINT NOT NULL UNIQUE,
        user_region VARCHAR(15) NULL 
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([
            f"{item} = ${num}" for num, item in enumerate(parameters.keys(),
                                                          start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_user(self, full_name, username, telegram_id):
        sql = "INSERT INTO users (full_name, username, telegram_id) VALUES($1, $2, $3) returning *"
        return await self.execute(sql, full_name, username, telegram_id, fetchrow=True)

    async def select_all_users(self):
        sql = "SELECT * FROM Users"
        return await self.execute(sql, fetch=True)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_arg_s(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_users(self):
        sql = "SELECT COUNT(*) FROM Users"
        return await self.execute(sql, fetchval=True)

    async def update_user_username(self, username, telegram_id):
        sql = "UPDATE Users SET username=$1 WHERE telegram_id=$2"
        return await self.execute(sql, username, telegram_id, execute=True)

    async def update_user_region(self, user_region, telegram_id):
        sql = "UPDATE Users SET user_region=$1 WHERE telegram_id=$2"
        return await self.execute(sql, user_region, telegram_id, execute=True)

    async def delete_user_by_id(self, id):
        return await self.execute("DELETE FROM Users WHERE id = $1", id, execute=True)

    async def drop_users(self):
        await self.execute("DROP TABLE Users", execute=True)

    async def create_table_group(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Group_s (
        id SERIAL PRIMARY KEY,
        group_name VARCHAR(255) NOT NULL,
        group_id BIGINT NOT NULL UNIQUE,
        group_region VARCHAR(15) NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_arg_s(sql, parameters: dict):
        sql += " AND ".join([
            f"{items} = ${nums}" for nums, items in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_group(self, group_name, group_id):
        sql = "INSERT INTO Group_s (group_name, group_id) VALUES($1, $2) returning *"
        return await self.execute(sql, group_name, group_id, fetchrow=True)

    async def select_all_group(self):
        sql = "SELECT * FROM Group_s"
        return await self.execute(sql, fetch=True)

    async def select_group(self, **kwargs):
        sql = "SELECT * FROM Group_s WHERE "
        sql, parameters = self.format_args(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_group(self):
        sql = "SELECT COUNT(*) FROM Group_s"
        return await self.execute(sql, fetchval=True)

    async def update_group_name(self, group_name, group_id):
        sql = "UPDATE Group_s SET group_name=$1 WHERE group_id=$2"
        return await self.execute(sql, group_name, group_id, execute=True)

    async def update_group_region(self, group_region, group_id):
        sql = "UPDATE Group_s SET group_region=$1 WHERE group_id=$2"
        return await self.execute(sql, group_region, group_id, execute=True)

    async def delete_group(self):
        await self.execute("DELETE FROM Group_s WHERE TRUE", execute=True)

    async def drop_group(self):
        await self.execute("DROP TABLE Group_s", execute=True)

    # Hadislar
    async def create_table_hadis(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Hadis (
        id SERIAL PRIMARY KEY,
        hadis_text VARCHAR(9999) NULL
        );
        """
        await self.execute(sql, execute=True)

    @staticmethod
    def format_arg_h(sql, parameters: dict):
        sql += " AND ".join([
            f"{items} = ${nums}" for nums, items in enumerate(parameters.keys(), start=1)
        ])
        return sql, tuple(parameters.values())

    async def add_hadis(self, hadis_text):
        sql = "INSERT INTO Hadis (hadis_text) VALUES($1) returning *"
        return await self.execute(sql, hadis_text, fetchrow=True)

    async def select_all_hadis(self):
        sql = "SELECT * FROM Hadis"
        return await self.execute(sql, fetch=True)

    async def select_hadis(self, **kwargs):
        sql = "SELECT * FROM Hadis"
        sql, parameters = self.format_arg_h(sql, parameters=kwargs)
        return await self.execute(sql, *parameters, fetchrow=True)

    async def count_hadis(self):
        sql = "SELECT COUNT(*) FROM Hadis"
        return await self.execute(sql, fetchval=True)

    async def update_hadis(self, hadis_text):
        sql = "UPDATE Hadis SET id=$1 WHERE hadis_text=$2"
        return await self.execute(sql, id, hadis_text, execute=True)

    async def delete_hadis(self):
        await self.execute("DELETE FROM Hadis WHERE TRUE", execute=True)

    async def drop_hadis(self):
        await self.execute("DROP TABLE Hadis", execute=True)
