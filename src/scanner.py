import nmap3
nmap = nmap3.Nmap()
def scan(host):
    return nmap.nmap_os_detection(host)

print(scan(""))


    