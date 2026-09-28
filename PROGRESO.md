# Progreso — Ruta 24 Semanas
Marca con [x] lo completado. Un cuadrito = un logro.

---

## FASE 1 — Python y POO (Semanas 1-8)

### Semana 1: Setup + fundamentos
- [x] VS Code funcionando
- [x] Variables y tipos de datos
- [x] Operadores
- [x] Git instalado y configurado
- [x] Repo en GitHub + primer commit y push
- [ ] input/print: repaso con ejercicios
- [ ] Entorno virtual (venv) + pip
- [ ] 15 ejercicios de lógica pura

### Semana 2: Estructuras de control
- [x] if/elif/else
- [ ] while
- [ ] for
- [ ] break/continue
- [ ] 20 katas de lógica (FizzBuzz, tablas, patrones)

### Semana 3: Estructuras de datos
- [ ] Listas
- [ ] Tuplas y sets
- [ ] Diccionarios
- [ ] Comprensión de listas
- [ ] Práctica: conteo de frecuencias y deduplicación

### Semana 4: Funciones
- [ ] Funciones, parámetros, *args/**kwargs
- [ ] Scope y recursión básica
- [ ] try/except
- [ ] Refactorizar semanas 1-3 en funciones

### Semana 5: POO parte 1
- [ ] Clases, atributos, métodos
- [ ] __init__ y self
- [ ] Encapsulamiento
- [ ] Modelar 3 entidades (CuentaBancaria, Estudiante, Producto)

### Semana 6: POO parte 2
- [ ] Herencia
- [ ] Polimorfismo
- [ ] __str__ y __repr__
- [ ] Composición
- [ ] Extender el modelo de la semana 5

### Semana 7: Archivos y testing
- [ ] Archivos .txt, .csv, .json
- [ ] Módulos y paquetes propios
- [ ] Testing básico (assert/unittest)
- [ ] Programa que lee/procesa/escribe datos

### Semana 8: Proyecto de Fase 1
- [ ] Repaso: 10 ejercicios sin ayuda
- [ ] Clases Cliente y CuentaBancaria con herencia
- [ ] Depósito, retiro, transferencia, historial
- [ ] Persistencia en JSON
- [ ] Manejo de excepciones
- [ ] README.md del proyecto
- [ ] Criterio: no crashea con ninguna entrada inválida

---

## FASE 2 — Redes, Linux/WSL e Internet (Semanas 9-16)

### Semana 9: WSL2 + Linux esencial
- [ ] WSL2 (Ubuntu) instalado
- [ ] Sistema de archivos y permisos (chmod/chown)
- [ ] apt
- [ ] Flujo de trabajo migrado a Linux

### Semana 10: Bash scripting
- [ ] Variables, condicionales, loops
- [ ] Pipes y redirecciones
- [ ] grep/sed/awk básico
- [ ] 10 scripts .sh de automatización
- [ ] (Opcional) OverTheWire Bandit

### Semana 11: TCP/IP y OSI
- [ ] Capas, IP, puertos, MAC, subredes
- [ ] ping, tracert, ipconfig
- [ ] "Ver" la red de mi casa

### Semana 12: DNS
- [ ] Resolución de nombres
- [ ] Registros A, MX, CNAME, TXT
- [ ] dig/nslookup
- [ ] Documentar DNS de 3 dominios (solo lectura pasiva)

### Semana 13: HTTP/HTTPS
- [ ] Métodos, códigos de estado, headers, cookies
- [ ] TLS/SSL (conceptual)
- [ ] curl y Postman/Insomnia con APIs públicas

### Semana 14: APIs REST (cliente)
- [ ] JSON y autenticación básica (API keys, tokens)
- [ ] Cliente en Python que consume una API pública

### Semana 15: Mi propia API
- [ ] Flask/FastAPI instalado
- [ ] 3-4 endpoints (GET/POST)
- [ ] Reutilizar el modelo bancario

### Semana 16: Proyecto de Fase 2
- [ ] API con 4+ endpoints en WSL
- [ ] Accesible desde otro dispositivo en mi red local
- [ ] Script de diagnóstico (ping, DNS, tiempos HTTP) con reporte
- [ ] Todo documentado en GitHub
- [ ] Criterio: explicar sin notas el recorrido de un paquete

---

## FASE 3 — SQL, OWASP y Labs Defensivos (Semanas 17-24)

### Semana 17: SQL fundamentos
- [ ] SELECT, WHERE, JOIN, GROUP BY
- [ ] Diseño de esquemas y normalización básica
- [ ] JSON del banco migrado a SQLite

### Semana 18: PostgreSQL
- [ ] PostgreSQL instalado
- [ ] Conexión desde Python (psycopg2/SQLAlchemy)
- [ ] API reescrita para usar PostgreSQL

### Semana 19: OWASP parte 1 (SQL Injection)
- [ ] SQLi explotada en entorno local controlado
- [ ] Corregida con consultas parametrizadas

### Semana 20: OWASP parte 2
- [ ] Broken Authentication
- [ ] XSS
- [ ] CSRF
- [ ] Labs en DVWA/Juice Shop (local)

### Semana 21: OWASP parte 3
- [ ] Configuraciones inseguras
- [ ] Exposición de datos sensibles
- [ ] Secretos (.env) y hashing con bcrypt
- [ ] Auditar mi API: 3 malas prácticas corregidas

### Semana 22: Scripting de seguridad
- [ ] Escaneo de puertos básico (solo mi red local)
- [ ] Logging y monitoreo simple
- [ ] Script que audita mi propia API

### Semana 23: Hardening
- [ ] Cabeceras de seguridad HTTP
- [ ] Rate limiting simple
- [ ] Validación de inputs
- [ ] Menor privilegio en la BD
- [ ] Evidencia antes/después

### Semana 24: Capstone "SecureBank API"
- [ ] API en PostgreSQL con contraseñas hasheadas
- [ ] Consultas parametrizadas
- [ ] Validación estricta y errores sin fugas de información
- [ ] Script de auditoría propio
- [ ] INFORME.md (1-2 páginas)
- [ ] Criterio: puedo defender cada decisión de diseño y seguridad