import whois
import time

def is_domain_available(domain):
    try:
        w = whois.whois(domain)
        if w.status == None:
            return True
        else:
            return False
    except:
        return False

with open("list.txt") as f:
    domains = f.read().splitlines()

for domain in domains:
    time.sleep(0.5)
    if is_domain_available(domain):
        print(f"{domain} is available for purchase.")
    # else:
    #     print(f"{domain} is not available for purchase.")