Il file upstream.go contiene la definizione e l'implementazione di un dialer proxy in Go, progettato per gestire le connessioni a server proxy upstream. Questo dialer supporta sia connessioni HTTP che HTTPS, con opzioni per l'autenticazione e la verifica personalizzata dei certificati. Di seguito è riportata una panoramica delle componenti principali del file:

Costanti:

Definisce costanti per il metodo HTTP CONNECT, intestazioni Host e Authorization, e un certificato di collegamento mancante.
Variabili globali:

UpstreamBlockedError: un errore che indica che la connessione è stata bloccata dal proxy upstream.
missingLinkDER e missingLink: certificato utilizzato per la verifica dei certificati intermedi mancanti.
Interfacce Dialer:

Dialer e ContextDialer: interfacce per la gestione delle connessioni di rete, con e senza contesto.
Struttura ProxyDialer:

Struttura che contiene i dettagli del proxy, inclusi indirizzo, nome del server TLS, autenticazione, dialer successivo, workaround intermedi e pool di certificati CA.
Funzioni per la creazione e gestione del ProxyDialer:

NewProxyDialer: crea un nuovo ProxyDialer.
ProxyDialerFromURL: crea un ProxyDialer da un URL.
DialContext: gestisce la connessione al proxy upstream, incluso l'invio della richiesta CONNECT e la gestione della risposta.
Dial: connessione senza contesto.
readResponse: legge la risposta HTTP dal proxy.
