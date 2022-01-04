import sqlite3

conn = sqlite3.connect('sql1.sqlite')
cur = conn.cursor()

cur.execute('''
DROP TABLE IF EXISTS Counts''')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')
count = 0
fname = input('Enter file name:')
if len(fname) < 1: fname = 'mbox.txt'
fhand = open(fname)
for line in fhand:
    line = line.strip()
    if line.startswith('From:'):
        count = count + 1
        sline = line.split()
        mail = sline[1]
        smail = mail.split('@')
        email = smail[1]
        #print(smail)
        cur.execute('SELECT count FROM Counts WHERE org = ? ', (email,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (email,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (email,))
    conn.commit()

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
