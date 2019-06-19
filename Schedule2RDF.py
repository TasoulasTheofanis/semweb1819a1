import csv

with open('Schedule.csv', 'r', newline='') as ifp, open('Schedule2.csv', 'w', newline='')as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    header = next(reader)

    for i, row in enumerate(reader, start=1):

        for col, value in zip(header, row):
            if col == 'Ώρα':
                time = value.split('-')
                writer.writerow([i, 'Ώρα Έναρξης', time[0]])
                writer.writerow([i, 'Ώρα Τέλους', time[1]])
            else:
                writer.writerow([i, col, value])

with open('Schedule2.csv',  'r', newline='') as ifp, open('Schedule3.csv', 'w', newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)

    for s, p, o in reader:
        s2, o2 = 'b:' + s, o
        if p in ['Μάθημα','Διδάσκων','Αίθουσα']:
            o2 = 'u:' + o
        else:
            o2 = 'l:' + o
        writer.writerow([s2, p, o2])

with open('Schedule3.csv',  'r', newline='') as ifp, open('Schedule_uri.csv', 'w', newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)

    for row in reader:
        s = row[0]
        p = "http://host/sw/p15taso/myvocab#" + row[1]
        o = row[2]
        if o.startswith('u:'):
            o = 'http://host/sw/p15taso/resource/'
            for i in row[2][2:]:
                if i == " ":
                    o += "%20"
                else:
                    o += i
        writer.writerow([s, p, o])

with open('Schedule_uri.csv',  'r', newline='') as ifp, open('rdf_data.nt', 'w') as ofp:
    reader = csv.reader(ifp)

    for s, p, o in reader:
        s2 = f'_:b{s[2:]}'
        p2 = f'<{p}>'
        if o[:2] == 'l:':
            o2 = o[2:]
            if 'Ώρα' in p:
                o2 += ':00'
            o2 = f'"{o2}"'
        else:
            o2 = f'<{o}>'

        ofp.write(' '.join([s2, p2, o2]) + ' .\n')