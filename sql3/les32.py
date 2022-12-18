import sqlite3

db = sqlite3.connect("database2.db")
c = db.cursor()
tab1 = """
CREATE TABLE IF NOT EXISTS konf(
    title text,
    full_text text,
    views integer,
    avtor text
);
"""
c.execute(tab1)
#
# into1 = "INSERT INTO konf VALUES('Facebook is cool','why not', 60,'Modest');"
#
# c.execute(into1)

# # print(c.fetchmany(2))
# # print(c.fetchone()[0])
#
# vib2 = "SELECT rowid, views FROM konf;"
# c.execute(vib2)
# print(c.fetchall())
#
# vib3 = "SELECT * FROM konf WHERE views > 60;"
# c.execute(vib3)
# print(c.fetchall())
vib1 = "SELECT * FROM konf;"
c.execute(vib1)
print(c.fetchall())

del1 = "DELETE FROM konf WHERE rowid > 1;"
c.execute(del1)

# upd1 = """UPDATE konf SET views = '80' WHERE views = '100';"""
# c.execute(upd1)

vib1 = "SELECT * FROM konf;"
c.execute(vib1)
print(c.fetchall())

db.commit()
c.close()
db.close()
