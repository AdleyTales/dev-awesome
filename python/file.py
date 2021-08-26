
ips = open('ip.txt')

ip_list = []

for ip in ips:
  ip_list.append(ip.strip())

print(ip_list)

ips.close()
