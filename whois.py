#Install package (run next line (without #) in command line before launch the script)
#pip install python-whois

#Import package
import whois

#Open txt files with domains for reading
DomainList = open('domains.txt', 'r')


# Read domains.txt line by line
for DomainName in DomainList:
    # Print name of domain
    print (DomainName.strip())
    WhoisData = whois.whois(DomainName.strip())
    #Print expiration date of domain
    print (WhoisData.expiration_date)    

#Close domains.txt file
DomainList.close()
