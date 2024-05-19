Il file utils.go contiene una serie di funzioni di utilità che supportano la gestione delle connessioni di rete, l'autenticazione di base, la gestione delle intestazioni HTTP e le operazioni asincrone con goroutine e canali. Di seguito è riportata una panoramica delle funzioni chiave:

Autenticazione di base (Basic Auth):

basic_auth_header(login, password string) string: Genera un'intestazione HTTP per l'autenticazione di base a partire da un login e una password.
Proxying delle connessioni di rete:

proxy(ctx context.Context, left, right net.Conn): Gestisce il proxying bidirezionale tra due connessioni di rete utilizzando goroutine e un gruppo di sincronizzazione (sync.WaitGroup).
proxyh2(ctx context.Context, leftreader io.ReadCloser, leftwriter io.Writer, right net.Conn): Simile a proxy, ma per la gestione delle connessioni HTTP/2.
Gestione delle intestazioni HTTP:

copyHeader(dst, src http.Header): Copia le intestazioni HTTP da una sorgente a una destinazione.
delHopHeaders(header http.Header): Rimuove le intestazioni HTTP hop-by-hop, che non dovrebbero essere inoltrate a un backend.
Hijacking e flushing delle connessioni HTTP:

hijack(hijackable interface{}) (net.Conn, *bufio.ReadWriter, error): Esegue il hijacking di una connessione HTTP per ottenere l'accesso diretto alla connessione di rete sottostante.
flush(flusher interface{}) bool: Esegue il flush di un flusher HTTP, se supportato.
Copiatura dei corpi delle richieste/risposte HTTP:

copyBody(wr io.Writer, body io.Reader): Copia i dati da un lettore (io.Reader) a uno scrittore (io.Writer) utilizzando un buffer di dimensione fissa.
Operazioni temporizzate:

AfterWallClock(d time.Duration) <-chan time.Time: Restituisce un canale che riceve un valore dopo una durata specificata, tenendo conto della precisione del tempo di parete (wall clock).
runTicker(ctx context.Context, interval, retryInterval time.Duration, cb func(context.Context) error): Esegue una funzione di callback (cb) a intervalli regolari, con la possibilità di un intervallo di retry in caso di errore.
