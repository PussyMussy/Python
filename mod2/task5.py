dns = input()
dns_strlen = len(dns)
domains = []
domainTemp = ''

for char in enumerate(dns):
    if char[1] != '.':
        domainTemp += char[1]
        if char[0] != dns_strlen - 1:
            continue
    domains.insert(0, domainTemp)
    domainTemp = ''

for domain in domains:
    print(domain)