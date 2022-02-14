# -*- coding: utf-8 -*-
#

import postgresql

def go():
#    db = postgresql.open('pq://postgres:postgres@localhost:5432/testik')
    db = postgresql.open('pq://invenio:invenio@localhost:5432/invenio')
#    db.execute("DROP TABLE t1")
    db.execute("CREATE TABLE t1 (id integer PRIMARY KEY, txt varchar(255))")
    db.execute("INSERT INTO t1 VALUES (1, 'abc')")
    db.execute("INSERT INTO t1 VALUES (2, 'def')")
    q = db.prepare("SELECT * FROM t1")
    print("", q())
    print("OK")
