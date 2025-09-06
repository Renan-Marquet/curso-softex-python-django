logs=[('192.168.1.1','2023-01-01'),('10.0.0.2','2023-01-02'),('192.168.1.1','2023-01-03')]
ips_nos_dois=set()
ips=set()
ips_unicos=set()
for ip,dia in logs:
    for ip2,dia2 in logs:
        if ip==ip2:
             ips.add(ip2)
             if ip==ip2 and dia2!=dia:
                ips_nos_dois.add(ip2)
ips_unicos=ips.difference(ips_nos_dois)
print(ips_unicos)


