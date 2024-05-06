# Filmdatenbank_M122
Herzlich Willkommen zu meinem Modul 122 Projekt.
![image](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/assets/145564904/d2fb3d95-7b32-4fc8-ae56-4c2c092c3eea)

___
# Filmdatenbank Projekt

Dieses Projekt umfasst die Entwicklung einer umfassenden Filmdatenbank von der Einrichtung der PostgreSQL-Datenbank bis hin zur Implementierung einer Webanwendung mit Flask und dynamischen Webtechnologien. Ziel war es, eine benutzerfreundliche Plattform zu schaffen, auf der Benutzer Filme suchen, ansehen und verwalten können.

## Technologien

- **Datenbank**: PostgreSQL
- **Backend**: Python, Flask
- **Frontend**: HTML, CSS, JavaScript
- **Automatisierung**: Cronjob

## Projektübersicht

### 1. Erstellung der Datenbank
Zunächst wurde eine PostgreSQL-Datenbank erstellt, um die Grundlage für die Speicherung und Verwaltung von Filmdaten zu schaffen.

### 2. Datenimport mit Python
Ein Python-Skript wurde entwickelt, um Filmdaten effizient in die Datenbank zu importieren. Dieses Skript berücksichtigt auch die Vermeidung von Duplikaten, um die Datenintegrität zu gewährleisten.

### 3. Implementierung eines Duplikatfilters
Ein spezieller Algorithmus verhindert, dass Duplikate in die Datenbank gelangen. Dies stellt sicher, dass jeder Film nur einmal vorhanden ist.

### 4. Einrichtung von Flask
Die Webanwendung wurde mit Flask eingerichtet, was ein effizientes Routing und eine gute Verwaltung von Benutzeranfragen ermöglicht.

### 5. Gestaltung der Webseite
Die Webseite wurde mit HTML, CSS und JavaScript entworfen. Ein benutzerdefinierter Filter verbessert das Benutzererlebnis, indem er das Durchsuchen der Filmdatenbank nach verschiedenen Kriterien ermöglicht.

### 6. Automatisierung durch Cronjob
Ein Cronjob wurde konfiguriert, um das Python-Skript täglich um 12 Uhr auszuführen. Dies garantiert, dass die Datenbank regelmäßig aktualisiert wird, ohne manuelles Eingreifen.


![image](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/assets/145564904/beb7bd0d-7e70-4153-b457-d7251e2227ad)
___

**Nebenbei habe ich auch noch einen log file und einen config file erstellt.
Und im Code kann man eine mail angeben und den Personen die Tabelle als zip file senden!(Dauert aber sehr lange)**
![image](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/assets/145564904/301013be-ea3b-4a20-8ec2-da4ed4aa1579)
![image](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/assets/145564904/093a21ab-9798-43cb-ba5b-1ccd20672769)


___

# UML 
```

               .--------.
              (   Start   )
               '--------'
                   |
                   v
               .---------------.
              ( Read config.json )
               '---------------'
                   |
                   v
               .------------------.
              ( Initialize Logger )
               '------------------'
                   |
                   v
               .------------------.
              ( Connect to Database )
               '------------------'
                   |
        +----------+----------+
        |  Connection Failed?  |
        +----------+----------+
        |                      |
      Yes                     No
        |                      |
        v                      v
    .----------.          .-----------.
   ( Log Error  )        ( Execute SQL )
    '---------'          '-----------'
                           |
                           v
                      .------------.
                     ( Import Data )
                      '------------'
                           |
                  +--------+--------+
                  |  Import Failed?  |
                  +--------+--------+
                  |                 |
                Yes                No
                  |                 |
                  v                 v
       .-----------------.   .-------------.
      ( Log Import Error ) ( Log Success )
       '-----------------'   '-------------'
                  |                 |
                  v                 v
              .------------.   .-------------.
             ( Error Page  ) ( Set Up Flask  )
              '------------'   '-------------'
                               |
                               v
                          .------------.
                         ( Config Mail )
                          '------------'
                               |
                               v
                         .---------------.
                        ( Flask Routing  )
                         '---------------'
                               |
                               v
                         .-------------.
                        ( Serve Pages  )
                         '-------------'
                               |
                               v
                         .-------------.
                        ( Send Email   )
                         '-------------'
                               |
                               v
                             .-----.
                            (  End  )
                             '-----'

```


___

Vielen Dank für das lesen, und ich hoffe Ihnen gefällt mein kleines Projekt!

![2a848b5ac4b72488fe3bde248d87be08_w200](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/assets/145564904/88e72c6d-d9f0-4fce-8e9c-075731992c0a)

---
[Python Code](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/blob/main/M122/Filmdatenbank/Main.py) <br>
[Html + CSS + Java Script Code](https://github.com/AndrinRueeggNoser/Filmdatenbank_M122/blob/main/M122/Filmdatenbank/templates/index.html)
