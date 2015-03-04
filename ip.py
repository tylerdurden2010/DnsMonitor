import dns.resolver


def FileOpen():
    filehandle2 = open('result.txt','r')
    summary = filehandle2.readline()
    while(summary):
        search_result = []
        result_ip = []
        summary =  summary.strip('\n')
        domain =  summary.split(' ')[0]
        try:
            ipaddress = dns.resolver.query(domain,rdtype='A')
            for i in ipaddress:
                search_result.append(str(i))
        except:
            print domain,"No anwser error"

        deep = len(search_result)
        
        search_result.sort()
        if deep and summary > 1:
            for i in range(deep):
                try:
                    summary = summary.strip('\n')
                    ip = summary.split(' ')[1]
                    result_ip.append(ip)
                    result_ip.sort()
                    summary = filehandle2.readline()
                except IndexError:
                    continue
            if(search_result == result_ip):
                print domain,'OK'
            else:
                print domain,search_result,result_ip
        else:
            result_ip.append(summary.split(' ')[1] )
            if( search_result == result_ip and search_result):
                print domain,'OK'
            else:
                print 'not ok',domain,search_result
            summary = filehandle2.readline()

if __name__ == '__main__':
    FileOpen()

