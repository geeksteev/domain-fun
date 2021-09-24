import os
import re

def getDomainTrustOutput():
    with open("/home/steev/project/domain_trusts.txt","r") as domain_trusts:
        f = domain_trusts.readlines()
        return f


def buildDomainList(data):
    domain_regex = "(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]"
    domain_list = []
    for line in data:
        domain_list.append(re.findall(domain_regex, line))

    return domain_list


def printDomainList(list):
    for item in list:
        print(item)


if __name__ == "__main__":

    printDomainList(buildDomainList(getDomainTrustOutput()))
