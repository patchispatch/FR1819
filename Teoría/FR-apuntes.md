# Fundamentos de Redes

**3º Grado en Ingeniería Informática - Universidad de Granada - Curso 2018-2019**

> **Advertencia:** estos apuntes se encuentran en desarrollo, y son para uso personal. Si quieres contribuir o crees que he cometido errores, siéntete libre de hacer una *pull request*.

Este documento recoge apuntes de la asignatura **Fundamentos de Redes**, basados en el material docente ofrecido por el *departamento de Teoría de la Señal, Telemática y Comunicaciones* de la Universidad de Granada.

---

## Índice

<!--ts-->

* [Tema 1: Introducción a los Fundamentos de Redes](#tema-1-introducción-a-los-fundamentos-de-redes)
   * [1. Sistemas de comunicación y redes](#1-sistemas-de-comunicación-y-redes)
      * [1.1. Conceptos básicos](#11-conceptos-básicos)
      * [1.2. Razones para usar redes](#12-razones-para-usar-redes)
      * [1.3. Clasificación de redes](#13-clasificación-de-redes)
      * [1.4. Estructura y elementos de una red](#14-estructura-y-elementos-de-una-red)
   * [2. Diseño y estandarización de redes](#2-diseño-y-estandarización-de-redes)
      * [2.1. Problemas a resolver](#21-problemas-a-resolver)
      * [2.2. Conceptos y principios de diseño](#22-conceptos-y-principios-de-diseño)
   * [3. Terminología y servicios](#3-terminología-y-servicios)
      * [3.1. Modelo OSI: comunicación real frente a comunicación virtual](#31-modelo-osi-comunicación-real-frente-a-comunicación-virtual)
      * [3.2. Servicios](#32-servicios)
   * [4. Internet: arquitectura y direccionamiento](#4-internet-arquitectura-y-direccionamiento)
      * [4.1. Arquitectura](#41-arquitectura)
      * [4.2. Direccionamiento](#42-direccionamiento)
* [Tema 2: servicios y protocolos de aplicación en Internet](#tema-2-servicios-y-protocolos-de-aplicación-en-internet)
* [Referencias](#referencias)

<!-- Added by: patchispatch, at: 2018-12-01T22:03+01:00 -->

<!--te-->

---

## Tema 1: Introducción a los Fundamentos de Redes

### 1. Sistemas de comunicación y redes

#### 1.1. Conceptos básicos

Un **Sistema de comunicación** es una infraestructura que permite el intercambio de información.

	Insertar imagen p4

La **información** es un conjunto de datos con significado.

Una **red de dispositivos** es un sistema de comunicación con sistemas finales (terminales) *autónomos* que facilita el intercambio *eficaz* y *transparente* de información.

#### 1.2. Razones para usar redes

- Compartir recursos
- Escalabilidad
- Fiabilidad, robustez -> Duplicidad (redundancia)
- Ahorro de costes (computación distribuida)

#### 1.3. Clasificación de redes

**Por escala**
- *Local* Area Network (LAN)
- *Medium* Area Network (MAN)
- *Wide* Area Network (WAN)

**Por tecnología de transmisión o uso del canal de comunicación**
- Difusión
- Punto a punto

	Insertar imagen p5

#### 1.4. Estructura y elementos de una red

**Hosts:** sistemas finales (terminales) autónomos.

**Subred:** infraestructura para el transporte de información, compuesta por:
- Líneas de transmisión.
- Nodos o elementos de conmutación. Ejemplos:
  - Routers
  - Switches
  - Estaciones base
  - Etc.

	Insertar imagen p6

### 2. Diseño y estandarización de redes

#### 2.1. Problemas a resolver

Existen una serie de **problemas** que la red debe resolver, para garantizar *transparencia* y *eficacia*:
- ¿Cómo enviar físicamente la información?
- Compartición del medio y segmentación de la información.
- Control de flujo y de errores.
- Control de encaminamiento (*routing*) de los mensajes.
- Control de congestión.
- Entrega ordenada de los mensajes.
- Gestión del diálogo o turno de palabra.
- Representación de los datos (sintaxis).
- Significado de los datos (semántica).

#### 2.2. Conceptos y principios de diseño

**Conceptos de diseño**
- Funcionalidad en capas.
- Definición de *modelo de referencia* -> capas + funcionalidades.

**Principios de diseño pafra el modelo**
- Funcionalidades distintas en distintas capas
- Minimización del flujo de información entre capas.

**Modelo OSI**
El modelo OSI[^1] (*Open System Interconnection*) es un modelo de referencia para los protocolos de red creado por la ISO[^2] en 1980

El modelo define las siguientes **capas** (en orden):
- Aplicación
- Presentación
- Sesión
- Transporte
- Red
- Enlace
- Física

**Modelo TCP/IP**
El modelo de referencia TCP/IP se basa en el protocolo TCP[^3] sobre la red de transmisión IP[^4], y describe las siguientes **capas**:
- Aplicación
- Transporte
- Red
- Red subyacente

### 3. Terminología y servicios

#### 3.1. Modelo OSI: comunicación real frente a comunicación virtual

	 Insertar imagen p16

**Terminología**
- Comunicación real (vertical).
- Comunicación virtual (horizontal).
- Entidad del nivel N (1 = físico ... 7 = aplicación).
- Entidades pares.
- Protocolo.
- Interfaz.
- Servicio.
- Capa proveedora/usuario del servicio.
- Pila de protocolos
- Arquitectura de red
- SAP (*Service Access Point*).
- SDU (*Service Data Unit*).
- PDU (*Protocol Data Unit*).

	 Insertar imagen p18
	 Insertar imagen p19

#### 3.2. Servicios

**Tipos**
- Orientado a Conexión (OC).
- No Orientado a Conexión (NOC).
- Confirmado (fiable).
- No confirmado (no fiable).

### 4. Internet: arquitectura y direccionamiento

#### 4.1. Arquitectura 

**Topología jerárquica**
- Intranets (*Ethernet*) del usuario: zona pública + zona privada.
- Redes de acceso.
- Redes troncales de grandes operadores de telecomunicaciones.
- Acuerdos de Peering[^5] y tránsito.
- Tier1[^6], Tier2 y Tier3
- Internet Exchange Points (IXP)[^7]

#### 4.2. Direccionamiento

Para realizar el direccionamiento, necesitamos lo siguiente:
- Nombre de dominio. Ej: https://github.com/patchispatch
- Dirección IP, necesaria para identificar los hosts (capa de red):
  - Fuente.
  - Destino.
- Puertos, para diferentes conexiones (capa de transporte).

---

## Tema 2: servicios y protocolos de aplicación en Internet

### 1. Introducción a las aplicaciones de red

#### 1.1. Arquitectura Cliente/Servidor

**Servidor**
- Siempre en funcionamiento.
- IP permanente y pública.
- Pueden estar agrupados en *granjas*.

**Clientes**
- Funcionan de forma intermitente.
- Pueden tener IP dinámica y privada.
- Se comunican con el servidor.
- No se comunican entre sí.

**Proceso cliente:** proceso que inicia la comunicación.
**Proceso servidor:** proceso que espera a ser contactado (IP permanente y pública).

El proceso envía y recibe mensajes desde su **socket**.
Para poder recibir mensajes, un proceso debe estar identificado por su IP y su puerto.

#### 1.2. La interfaz socket

Un **socket** es un descriptor de transmisión entre aplicaciones. Permite el acceso entre la aplicación y los servicios de transporte.

En la práctica, un socket es un puntero a una estructura de datos relativos a la comunicación.

	Insertar imagen p7

#### 1.3. Protocolos de aplicación

¿Qué define un protocolo?
- **El tipo de servicio**
  - Orientado a conexión o no
  - Realimentado o no
- **El tipo de mensaje**
- **La sintaxis**
  Definición y estructura de campos en el mensaje
- **La semántica**
  Significado de los campos
- **Las reglas**
  Envío y respuesta de mensajes por parte de los procesos

Tipos de protocolos
- Protocolos de dominio público *versus* propietarios.
- Protocolos in-band *versus* out-of-band.
- Protocolos stateless *versus* state-full.
- Protocolos persistentes *versus* no persistentes.

La tendencia es definir los protocolos de forma flexible, utilizando una cabecera fija y una serie de trozos (*chunks*), algunos obligatorios y otros opcionales.

Los trozos pueden incluir una cabecera específica más una serie de datos como parámetros. Para los parámetros se usa el formato TLV (*Type-Length-Value*).

#### 1.4. Características

**Pérdida de datos**
Algunas aplicaciones soportan mejor la pérdida de datos que otras. En audio, por ejemplo, es tolerable; otros servicios como telnet o ssh requieren fiabilidad en la transmisión.

**Requisitos temporales**
Algunas apps requieren retardo acotado (delay) para ser efectivas, como pueden ser las de telefonía o juegos.

**Ancho de banda**
Algunas apps necesitan enviar datos a una determinada tasa de transmisión.

**Seguridad**
Encriptación, autenticado, etc.

#### 1.5. Protocolos

| **Protocolo TCP**     | **Protocolo UDP**         |
|-----------------------|---------------------------|
| Orientado a conexión  | No orientado a conexión   |
| Transporte fiable     | Transporte no fiable      |
| Control de flujo      | Sin control de flujo      |
| Control de congestión | Sin control de congestión |

Al ser usuarios del protocolo IP, ni TCP ni UDP garantizan
- Retardo acotado
- Fluctuaciones acotadas
- Mínimo *throughput*
- Seguridad

### 2. Domain Name Service (DNS)

Para comunicarse en Internet, necesitamos direcciones IP, que identifican a cada máquina involucrada en la comunicación y se utilizan para direccionarlas. Sin embargo, es más cómodo utilizar los llamados **nombres de dominio**, más legibles y fáciles de recordar, para acceder a las diferentes direcciones. 

Para ello, se usa el **Servicio de Nombre de Dominio (DNS)**, que traduce nombres a direcciones IP (servicio de resolución de nombres). 

Sus características principales son:

- Suele ser el paso previo al resto de aplicaciones TCP/IP, ya que las conexiones suelen realizarse mediante un nombre de dominio. Sin embargo, si la conexión se realiza directamente utilizando una IP, el servicio DNS no llega a ejecutarse.
- Es transparente al usuario, es decir, no tiene por qué darse cuenta de que se está ejecutando, pues se realiza de forma automática.

El nombre de dominio, al igual que la dirección IP, debe ser único y universal. Para asegurar esto, los dominios se estructuran de forma jerárquica de la siguiente forma:

	goliat.ugr.es

En este ejemplo, *.es* es el dominio de nivel 1 o superior, que engloba al subdominio *ugr*. Este, a su vez, engloba a *goliat*.

El dominio de nivel 1 se denomina **dominio genérico**. Originalmente se crearon nueve dominios genéricos, aunque ahora existen muchos más:

| **.com**  | organizaciones comerciales                                                       |
|-----------|----------------------------------------------------------------------------------|
| **.edu**  | instituciones educativas                                                         |
| **.gov**  | instituciones gubernamentales de EEUU                                            |
| **.mil**  | grupos militares de EEUU                                                         |
| **.net**  | proveedores de red                                                               |
| **.org**  | organizaciones diferentes a las anteriores                                       |
| **.arpa** | propósitos de infraestructura de Internet (*Address and Routing Parameter Area*) |
| **.int**  | organizaciones estableidas por tratados internacionales                          |
| **.xy**   |  indicativos de zona geográfica (*.es, .uk, .jp, etc*)                           |

El dominio raíz "." está gestionado por la [ICANN](http://www.icann.org), que suele delegar en centros regionales. En España, este centro es Red.es.

#### 2.1. Servidores DNS

Para que DNS pueda funcionar, debe existir una base de datos que contenga todos los dominios existentes y su respectiva traducción a IP, para poder traducir los valores. 
Si esta base de datos estuviese centralizada, prácticamente *todo* el tráfico de internet pasaría por un mismo lugar, ralentizando mucho el servicio, por no hablar de lo complejísimo que sería mantener un servidor de tales magnitudes. 

Es por ello que esta base de datos se halla distribuida en una gran cantidad de servidores a lo largo del mundo, y son de diferentes tipos:

- **Servidores raíz ".":** este tipo de servidores se encargan de resolver una petición para un nombre. Devuelven los dominios **TLD** capaces de resolver la petición. Existen trece servidores "." primarios en el mundo, aunque cada uno realmente es una red de servidores, haiendo realmente unos 250 servidores *root*.
- **Servidores de dominio (TLD, *Top-Level Domain*)**: estos servidores se encargan de los dominios de más alto nivel, como los *genéricos*. Se encargan de resolver la petición DNS, y si no son capaces de hacerlo, darán la dirección del **servidor autorizado** que pueda resolverla.
- **Servidores autorizados:** es un servidor que contiene una base de datos con todas las direcciones IP asociadas a él. Es el más actualizado, y el que resolverá las peticiones DNS en caso de que el servidor local o el TLD no sean capaces de hacerlo. Responderá al **servidor local** con la IP.
- **Servidor local:** un servidor local es aquel que posee cada proveedor de Internet (ISP). Resolverá todas las peticiones DNS que correspondan a su dominio (ej: ```deiit.ugr.es``` es resuelto por el servidor local de la red de la UGR). Suele estar cerca del host al que pertenece.

#### 2.2. Resolución de DNS

La resolución puede realizarse de dos formas distintas, según cómo se recorren los diferentes servidores:

- **Resolución recursiva:** el host que realiza la consulta se la manda a un servidor. Si este no puede resolverla, se la envía a otro, y este a otro distinto, hasta que uno pueda hacerlo. Una vez resuelta la consulta por el servidor *n*, devolverá la IP al servidor *n - 1*, y la irán pasando hacia atrás hasta que llegue al host.
*Problema:* hasta que no se resuelva la petición, el servidor tiene que almacenar la información.
- **Resolución iterativa:** cuando se realiza una consulta DNS y el servidor no la puede responder, se la devuelve al host, que la envía a otro. Si este tampoco puede, la devuelve de nuevo al host, que lo intenta con otro. Esto ofrece una solución al problema de la resolución recursiva. 

#### 2.3. Gestión de la base de datos DNS

La base de datos DNS es distribuida, como hemos comentado anteriormente. Esto presenta ventajas en términos de congestión, pero a la hora de actualizar registros puede volverse un problema: pueden existir varias copias de una traducción en distintos servidores, ya que utilizan memorias caché para aligerar traducciones. A la hora de actualizar una entrada, ¿cómo nos aseguramos de que lo hacemos correctamente? Pues se hace actualizando la tradución en el **servidor autorizado** en el que se aloja.

Las traducciones actualizadas se hallan en servidores primarios, que mantienen la coherencia de la base de datos. No obstante, existen servidores secundarios con copias de serguridad, en caso de necesitarse debido a fallos.

#### 2.4. Respuestas del servidor

¿Qué tipo de respuesta podemos esperar tras realizar una petición DNS?

- **Respuesta con autoridad:** el servidor tiene autoridad sobre la zona en la que se encuentra el nombre solicitado y devuelve la IP.
- **Respuesta sin autoridad:** el servidor no tiene autoridad sobre la zona en la que se encuentra el nombre solicitado, pero tiene la traducción almacenada en caché.
- **No conoce la respuesta:** el servidor enviará la consulta a otros servidores de forma recursiva o iterativa. Se suele elevar la petición a uno de los servidores *root*.

### 3. La navegación web

Cuando navegamos por Internet, no hacemos más que realizar peticiones a un servidor, y este nos responde con algo que nuestro navegador puede interpretar. Este *algo* no es más que un fichero HTML, que contiene el esqueleto de la página, *hiperenlaces* a otras páginas que albergan contenido, imágenes, audio, etc.

El contenido de las páginas se direcciona mediante una **URL** (*Uniform Resource Locator*), que indica el protocolo (http o https normalmente), el servidor (o el dominio) y el puerto (si es necesario), de la siguiente forma:

	https://dominio[:puerto]/path/al/recurso

#### 3.1. El protocolo HTTP

El protocolo HTTP utiliza el modelo *cliente-servidor*:

- **Cliente:** navegador web, que realiza peticiones de objetos, los recibe y los muestra
- **Servidor:** atiende a las peticiones que le llegan, enviando los objetos solicitados.

HTTP utiliza el puerto 80 para realizar las conexiones. El cliente inicia la conexión TCP para solicitar datos, recibiéndola el servidor en el socket correspondiente. El servidor envía por ese socket la información solicitada, y cierra la conexión. El cliente puede estar en uno de estos tres rangos de puertos:

- **Superusuarios:** desde el 0 hasta el 1023.
- **Puertos reservados:** desde el 1024 al 49151. Los utilizan aplicaciones que no requieren permisos de administrador, y son puertos que no están asignados a otro servicio, como por ejemplo el 80 (http).
- **Puertos dinámicos, privados o efímeros:** desde el 49152 al 65535. El sistema operativo los da y libera a los clientes. Una vez un puerto se asigna a un cliente ya no puede ser asignado a otro.

HTTP es un protocolo *stateless*, es decir, no mantiene información sobre las peticiones de los clientes. Para ello utiliza *cookies*, que almacenan la información en el propio cliente.

Existen dos tipos de conexiones HTTP:

- **No persistentes:** se envía un objeto en cada conexión TCP, cerrándose esta cuando se ha terminado el envío.
- **Persistentes:** se pueden enviar varios objetos sobre una única conexión TCP entre el cliente y el servidor.

Podría parecer que la conexión persistente es la más idónea, ya que no hay que abrir y cerrar conexiones por cada elemento que queramos solicitar. Sin embargo, el navegador lanza conexiones no persistentes de forma *pseudo-paralela*, estando bastante optimizados en este aspecto.


##### 3.1.1. Mensajes HTTP

En una conexión HTTP se dan los siguientes pasos:

1. El cliente inicia la conexión y accede al servidor de una determinada dirección web, normalmente en el puerto 80.
2. El servidor acepta (o no) la conexión y envía una confirmación al cliente.
3. Si el servidor ha aceptado, el cliente envía el primer paquete o *request message*
4. El servidor responde con la información solicitada. Si la conexión es persistente, se realizan los pasos 3 y 4 varias veces. Si no, se cierra la conexión.


#### 3.2. Web cache

La caché sirve para ahorrar ancho de banda al resolver una petición que se ha realizado recientemente, o lo que es lo mismo, satisfacer el requisito del cliente sin involucrar al servidor destino.

La caché se basa en disponer de un servidor proxy. Un proxy HTTP es un intermediario por el que pasan todas las conexiones HTTP de la red, y es la única forma de comprobar si una petición se encuentra almacenada o no en caché.

Si un cliente realiza una petición, esta pasará por el proxy, que la guardará en caché. Si otro cliente la realiza tiempo después, será el propio proxy quien responda, ya que la tiene almacenada, respondiendo mucho más rápido.

Las respuestas en caché caducan, o pueden no estar actualizadas. Cuando otro cliente realiza la petición y esta se encuentra en la caché, el proxy envía una petición al servidor para comprobar que su copia está actualizada. Si lo está, envía la respuesta al cliente; si no, actualiza la caché y envía la respuesta al cliente.


### 4. El correo electrónico

	De momento no hay nada, ya lo completaré.


### 5. Protocolos seguros

#### 5.1. Primitivas de seguridad

Las primitivas de seguridad se clasifican en:

- **Confidencialidad:** sólo podrá acceder a la información quien deba hacerlo.
- **Responsabilidad:** es una primitiva muy amplia. Incluye:
  - Autenticación: los agentes de la comunicación deben estar identificados.
  - No repudio: no se puede negar la autoría de una determinada acción en la red.
  - Control de accesos: se debe comprobar quién se ha conectado, desde qué dispositivo, etc.
- **Integridad:** detección de alteraciones de la información, ya sean intencionadas o no. Nadie debería poder modificar la comunicación entre dos agentes, ni la información transmitida.
- **Disponibilidad:** los servicios deberían mantenerse de forma independiente al grueso de la demanda.

#### 5.2. Mecanismos de seguridad

**Cifrado**
Cifrar un mensaje consiste en alterarlo de forma que pueda ser recuperado, utilizando algún tipo de mecanismo. Normalmente suele utilizarse una clave para realizarlo, así como para deshacerlo (estas claves no tienen por qué coincidir). Hay varios tipos:

- **Cifrado simétrico:** la clave de cifrado es la misma que la de descifrado, y debe ser conocida únicamente por el remitente y el destinatario. Algunos de los algoritmos más utilizados para este cifrado son 3DES y AES.
*Problema:* si ambos agentes de la comunicación necesitan conocer la clave, esta debe ser enviada, de una forma u otra. Si es capturada junto con el mensaje, de nada sirve el cifrado.
- **Cifrado asimétrico:** surge para solucionar el problema de la clave única. Este cifrado utiliza dos claves, una para cifrar y otra para descifrar, y este par de claves se generan a partir de un algoritmo, de forma que no se puede calcular una a partir de otra. Estas dos claves funconan de la siguiente forma:
  - *Clave pública:* como su nombre indica, es pública, visible para todo el mundo.
  - *Clave privada:* solo la conoce el propio usuario, y no se envía nunca.

  El cifrado se realiza con la clave pública del destinatario, ya que   únicamente él, con su clave privada, podrá descifrar el mensaje. De esta forma evitamos enviar claves, y la pública no tiene ningún valor por sí misma. Los algoritmos son suficientemente complejos como para evitar que se pueda calcular una clave a partir de la otra, así que podemos respirar tranquilos.

**Funciones hash**
Las funciones hash son aquellas que, recibiendo un input, generan un identificador unívoco, minimizando colisiones. Como mecanismos de seguridad, se utilizan para asegurar que los mensajes no han sido modificados.

- **Message Authentication Code (MAC):** no se debe confundir con la dirección MAC de una tarjeta de red. Se trata de un hash que nos permite saber si un mensaje ha sido modificado o no. Suele combinarse con el cifrado, ya que si el hash está encriptado es imposible modificarlo. Ejemplos de algoritmos son MD5 y SHA-1.
- **Firma digital:** se utiliza para autenticar la autoría de un documento. El procedimiento consiste en hacer un hash del documento utilizando la clave privada, ya que es algo que únicamente posee el autor del documento. Utilizando la clave pública se podría comprobar quién ha firmado el documento. Esto funcionaría idealmente, pero no podemos garantizar que una persona es quien dice ser, así que suele entrar en la comunicación un tercer agente, la *entidad certificadora*.
- **Certificado:** las autoridades certificadoras permiten la creación de certificados, que son la asociación entre una identidad y una clave pública. En HTTPS, se comprueban los certificados de las páginas para evitar ataques de *phishing*.


#### 5.3. Seguridad perimetral

Hemos visto mecanismos para garantizar conexiones seguras, pero nos queda por ver la **seguridad perimetral**. Mientras que la seguridad perimetral física podría ser una valla, cámaras de seguridad o un foso lleno de cocodrilos, en nuestro ámbito nos referimos a los firewalls, sistemas de detección de intrusiones, etc. que nos permiten reaccionar ante determinados ataques.

**Firewalls**
Los firewalls a los que estamos acostumbrados son de sistemas finales. Sin embargo, aquí hablamos de los de redes, que se basan en una serie de reglas definidas par bloquear aquello que no tiene por qué pasar por la red.

**Sistemas de detección de intrusiones**
No bloquean el tráfico como los firewalls, sino que lo analizan en busca de anomalías según reglas definidas. El mas famoso es *Snort*, y es open source.


#### 5.4. Protocolos seguros

En las distintas capas de TCP/IP se definen una serie de **protocolos seguros**. Dependiendo de la capa en la que se encuentren, encontramos algunos.

**Capa de aplicación**
- **Secure Shell (SSH):** es el protocolo más usado en la capa de aplicación, ya que nos permite conectarnos remotamente al shell de un servidor, y está bastante estandarizado.
- **Pretty Good Privacy (PGP):** esquema general de seguridad. Originalmente se diseñó para correo electrónico, pero es prácticamente genérico. Utiliza cifrado asimétrico, simétrico, firma electrónica y certificado, y es fácil de implementar.

**Capa de sesión (entre aplicación y transporte)**
- **Secure Socket Layer (SSL) y Transport Secure Layer (TLS):** estos protocolos se encuentran realmente en la capa de aplicación, pero son necesarios para algunos protocolos. Por ejemplo, HTTPS está basado en aplicar SSL o TLS.

**Capa de red:** debajo se encuentra *IPSec*, que se utiliza para conexiones VPN. Encripta toda la comunicación en la capa de red.

### 6. Aplicaciones multimedia

	Ya lo completaré algún día

### 7. Aplicaciones para interconectividad de redes locales

	Lo mismo


## Tema 3: Capa de transporte en Internet




---

## Referencias
[^1]: [Modelo OSI - Wikipedia](https://es.wikipedia.org/wiki/Modelo_OSI)
[^2]: [International Organization for Standardization - Wikipedia](https://es.wikipedia.org/wiki/Organizaci%C3%B3n_Internacional_de_Normalizaci%C3%B3n)
[^3]: [Protocolo TCP - Wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_control_de_transmisi%C3%B3n)
[^4]: [Internet Protocol - Wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_internet)
[^5]: [Peering - Wikipedia](http://en.wikipedia.org/wiki/Peering)
[^6]: [Tier 1 Networks - Wikipedia](https://en.wikipedia.org/wiki/Tier_1_network)
[^7]: [Internet Exchange Point - Wikipedia](https://en.wikipedia.org/wiki/Internet_exchange_point)