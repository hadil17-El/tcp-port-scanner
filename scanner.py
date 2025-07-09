# Importa il modulo socket, che serve per creare connessioni di rete (TCP/UDP).
import socket
#Chiede all'utente l'indirizzo IP o hostname (es. 127.0.0.1, google.com, ecc.)
target= input("Inserisci l'IP o l'host da scansionare: ")
# È una lista di porte TCP da scansionare:21:FTP,22:SSH,80:HTTP,443:HTTPS,445:SMB,8080:HTTP alternativo
porte = [21,22,23,25,53,80,110,139,443,445,8080]
#Stampa un messaggio che dice dove si sta facendo la scansione.
print(f"\nScansione in corso su {target}...\n")
#Cicla ogni numero di porta nella lista porte.
for porta in porte:
    #🔌 Crea un nuovo socket TCP (IPv4).
    #AF_INET: tipo di indirizzo IPv4
    #SOCK_STREAM: tipo di socket TCP (stream)
    #socket.socket(...):È una funzione della libreria socket di Python.
    #Serve a creare un oggetto socket, cioè una connessione di rete.
    # AF_INET:Indica il tipo di indirizzo IP che vuoi usare.
    #AF_INET = IPv4 (es. 192.168.1.1)
    #Se volessi IPv6, useresti AF_INET6
    # 💡 Significa: "Voglio usare indirizzi IPv4"
    #🔹 SOCK_STREAM:Indica che vuoi usare il protocollo TCP (stream).
    #TCP è affidabile, con controllo di errore, usato per HTTP, HTTPS, SSH, ecc.
#Se volessi usare UDP (meno sicuro, ma più veloce), useresti SOCK_DGRAM
#💡 Significa: "Voglio una connessione TCP, non UDP"

    s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
    #Imposta un timeout di 1 secondo per evitare che il programma si blocchi se una porta non risponde.
    s.settimeout(1)
#Prova a connettersi alla porta indicata sul target:
    #connect_ex() restituisce:
        #0 → connessione riuscita (porta aperta)
        #altro valore → porta chiusa o filtrata
    result = s.connect_ex((target, porta))
    if result == 0:
        print(f"Porta {porta} aperta ✅")
    else:
        print(f"Porta {porta} chuisa ❌")
# Chiude il socket per quella porta, libera le risorse.
    s.close()


#🧠 Risultato finale:
#Ricevi un output tipo questo:
#python-repl
#Scansione in corso su 127.0.0.1...
#Porta 21 chiusa ❌
#Porta 22 aperta ✅
#Porta 80 chiusa ❌
#Porta 443 aperta ✅