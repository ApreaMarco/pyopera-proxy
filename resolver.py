from dns.resolver import Resolver as Res, NoAnswer, NXDOMAIN
from dns.rdatatype import AAAA, A
from dns.exception import Timeout

DOT = '.'


class Resolver:
    def __init__(self, address, timeout):
        self.resolver = Res()
        self.resolver.nameservers = [address]
        self.resolver.timeout = timeout

    def resolve_a(self, domain):
        results = []
        if not domain:
            return results
        if domain[-1] != DOT:
            domain += DOT
        try:
            answers = self.resolver.resolve(domain, A)
            for answer in answers:
                results.append(answer.address)
        except (NoAnswer, NXDOMAIN, Timeout):
            pass
        return results

    def resolve_aaaa(self, domain):
        results = []
        if not domain:
            return results
        if domain[-1] != DOT:
            domain += DOT
        try:
            answers = self.resolver.resolve(domain, AAAA)
            for answer in answers:
                results.append(answer.address)
        except (NoAnswer, NXDOMAIN, Timeout):
            pass
        return results

    def resolve(self, domain):
        results = self.resolve_a(domain)
        if not results:
            results = self.resolve_aaaa(domain)
        return results


# Esempio di utilizzo
resolver = Resolver('8.8.8.8', 5)  # Utilizza il resolver DNS di Google con un timeout di 5 secondi
print(resolver.resolve('example.com'))
