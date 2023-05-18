from icmplib import multiping


ips=[]

with open('ips.txt', 'r') as f: 
    for line in f:
        ips.append(line.strip())

hosts = multiping(ips)

for host in hosts:
    if host.is_alive:
    # See the Host class for details
    
        with open('Result_ips.txt',"a") as f:
            f.write(f'{host.address},up'+"\n")
        print(f'{host.address},up',end="\n")
    else:
        with open('Result_ips.txt',"a") as f:
            f.write(f'{host.address},down'+"\n")
        print(f'{host.address},down',end="\n")

