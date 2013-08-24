# -*- coding: UTF-8 -*-
import datetime

CURRENT_VERSION = 1

class UpdateDB:
    def __init__(self, db):
        self.db = db
        self.version = self.get_version()
        self.update_db()

    def get_version(self):
        try:
            result = self.db.query("select version from dbversion")
        except:
            return 0

        return result[0]["version"]

    def update_version(self, newVersion):
        oldVersion = newVersion - 1

        self.db.update('dbversion',
                version=newVersion,
                updated=datetime.datetime.now(),
                where='version = %s' % oldVersion
            )

        self.version = newVersion

    def update_db(self):
        while self.version < CURRENT_VERSION:
            if self.version < 1:
                self.db.query(
                    """
                    create table dbversion (
                        version int not null default 0,
                        updated datetime not null
                    );
                    """
                    )
                self.db.insert('dbversion', version=0, updated=datetime.datetime.now())

                self.db.query(
                    """
                    create table galleries (
                        name varchar(255) not null,
                        num_collections int not null default 0,
                        num_images int not null default 0,
                        cover_thumb varchar(1024) not null,
                        last_update datetime
                    );
                    """
                )
                self.update_version(1)
