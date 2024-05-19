Il file resolver.go contiene una semplice implementazione di un resolver DNS in Go, che utilizza la libreria dnsproxy di AdGuard per effettuare risoluzioni DNS. Questo file definisce una struttura Resolver con metodi per risolvere indirizzi IPv4 (A) e IPv6 (AAAA) per un dato dominio. Di seguito è riportata una panoramica delle componenti principali del file:

Importazioni:

Importa la libreria upstream di AdGuard per la gestione delle risoluzioni DNS.
Importa la libreria dns di Miek Gieben per la manipolazione dei messaggi DNS.
Importa time per gestire i timeout.
Costante DOT:

Definisce una costante DOT utilizzata per verificare se un dominio termina con un punto.
Struttura Resolver:

Contiene un singolo campo upstream di tipo upstream.Upstream.
Funzione NewResolver:

Crea un nuovo Resolver con un indirizzo upstream e un timeout specificati.
Metodi di Resolver:

ResolveA: Risolve record di tipo A (IPv4) per un dominio.
ResolveAAAA: Risolve record di tipo AAAA (IPv6) per un dominio.
Resolve: Risolve prima i record di tipo A e, se non ne trova, prova con i record di tipo AAAA.
