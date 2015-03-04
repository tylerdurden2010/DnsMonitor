import dns.resolver
import sys


def FileOpen(filename):
    
    filehandle = open(filename,'r')
    filehandle2 = open('domainip.txt','w')
    domain = filehandle.readline()
    while(domain):
        search_result = []
        domain =  domain.strip('\n')
        try:
            ipaddress = dns.resolver.query(domain,rdtype='A')
        except:
            None
        for i in ipaddress:
            search_result = domain + ' ' + str(i) + '\n'
            filehandle2.write(search_result)
        domain = filehandle.readline()
        


if __name__ == '__main__':
    Filename = sys.argv[1]
    FileOpen(Filename)

