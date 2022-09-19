import sqlite3
con = sqlite3.connect("feedr.db")
cur = con.cursor()

with open('gilda_cves.txt') as f:
    for line in f:
        cveQuery = line.replace('\n', '')
        cve = line.replace('\n', '').replace('%', '').replace('_', '-')

        print(cve)

        queryTemplate = """
                        select title, url
                        FROM export WHERE
                        text like '<REPLACEME>'
                        group by title
                        order by lastmodified ASC
                        """
        queryTemplate = queryTemplate.replace('<REPLACEME>', cveQuery)
        res = cur.execute(queryTemplate)
        rows = res.fetchall()
        with open('autogen/' + cve + '.md', 'a') as mdOut:
            mdOut.write('# ' + cve)
            mdOut.write('\n')
            for row in rows:
                mdOut.write('* ' + row[0] + '\n')
                mdOut.write('* * ' + row[1] + '\n')

cur.close()