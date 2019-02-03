# Fundamentos de Redes

**3º Grado en Ingeniería Informática - Universidad de Granada - Curso 2018-2019**

> **Advertencia:** estos apuntes se encuentran en desarrollo, y son para uso personal. Si quieres contribuir o crees que he cometido errores, siéntete libre de hacer una *pull request*.

Este documento recoge apuntes de la asignatura **Fundamentos de Redes**, basados en el material docente ofrecido por el *departamento de Teoría de la Señal, Telemática y Comunicaciones* de la Universidad de Granada, y en los apuntes recogidos por [Marta Gómez y Braulio Vargas](https://github.com/mgmacias95/Apuntes/blob/master/FR/apuntesfr.tex).

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

Un **Sistema de comunicación** es una infraestructura que permite el intercambio de información. Podemos expresarlo como un conjunto de elementos: 

- **Emisor:** origen de la información.
- **Destino:** destinatario de la información transmitida.
- **Transmisor:** intermediario entre el canal y el emisor, encargado de adaptar la señal transmitida a las características del medio de transimisión.
- **Receptor:** intermediario entre el canal y el receptor, encargado de adaptar las características de la señal a las del destino.


![conceptos basicos](https://i.imgur.com/NGO3Alr.png)


La **información** es un conjunto de datos con significado.

Una **red de dispositivos** es un caso particular de sistema de comunicación, y dispone de sistemas finales (terminales) *autónomos* que facilita el intercambio *eficaz* y *transparente* de información.

#### 1.2. Características de las redes

- **Interconexión:** la existencia de canales de transmisión permite la comunicación entre los equipos de la red.
- **Autonomía:** los equipos son independientes en cuanto a funcionamiento.
- **Intercambio de información.**

El objetivo principal de las redes es el de **compartir recursos**. Sin embargo, hay más razones por las que resultan de gran utilidad:

- **Escalabilidad:** una red es mucho más fácil de escalar que un computador tradicional, ya que si necesitamos ampliar recursos, en la red bastaría con añadir equipos, sin necesidad de sustituir componentes.
- **Fiabilidad:** al disponer de varios equipos conectados, puede haber *duplicidad* de recursos, por lo que es menos probable que se pierdan.
- **Ahorro de costes:** los equipos de una red son más fáciles de mantener que un supercomputador; por tanto, saldrá más barato.

#### 1.3. Clasificación de redes

Las redes se clasifican en base a dos principales criterios:

**Por escala: **
- *Local* Area Network (LAN)
- *Medium* Area Network (MAN)
- *Wide* Area Network (WAN)

**Por tecnología de transmisión o uso del canal de comunicación**
- **Difusión:** las transmisiones se realizan desde un único medio, compartido por todos los equipos.
- **Punto a punto:** existen enlaces entre dos equipos en los que ambos actúan de emisor y receptor, dependiendo de la transmisión. Cuando el número de enlaces es igual al de parejas posibles de equipos, se llama *topología*, pero no es usual debido a su alto coste.

![tecnologia transmision](https://i.imgur.com/kbpwu0w.png)

Las redes LAN utilizan tecnología de difusión, mientras que las WAN usan la comunicación punto a punto.

#### 1.4. Estructura y elementos de una red

Podemos definir los siguientes elementos en una red:

**Hosts:** sistemas finales (terminales) autónomos.

**Subred:** infraestructura para el transporte de información, compuesta por:
- **Líneas de transmisión**.
- **Nodos o elementos de conmutación:** dispositivos que transportan datos desde un origen a un destino. Ejemplos:
  - Routers
  - Switches
  - Estaciones base
  - Etc.

	![Nodos](https://i.imgur.com/a2QUSPS.png)

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

Veremos a continuación diferentes soluciones a estos problemas.

#### 2.2. Conceptos y principios de diseño

El diseño de una red se plantea por **capas**. Cada capa se encarga de una función, obteniendo así un sistema modular, mucho más flexible. Una vez disponemos de un conjunto de capas, cada una con su funcionalidad, ya tenemos un **modelo de referencia**.

Existen dos tipos de modelos de red:

- ***De facto*:** se adoptan sin haber seguido un proceso de estandarización.
- ***De jure*:** han sido desarrollados por organismos de estandarización reconocidos.

Los modelos más conocidos son **OSI** y **TCP/IP**.

![OSI TCP](https://i.imgur.com/TKxmJHy.png)

**Modelo OSI**
El modelo OSI (*Open System Interconnection*) es un modelo de referencia para los protocolos de red creado por la ISO en 1980

El modelo define las siguientes **capas** (de arriba a abajo):
- **Aplicación:** servicios finales que se ofrecen al usuario (correo electrónico, Discord, etc).
- **Presentación:** en esta capa se resuelven problemas sobre la representación de datos que provienen de la capa superior (codificación, por ejemplo).
- **Sesión:** esta capa se encarga de gestionar el turno de palabra entre los hosts participantes.
- **Transporte:** controla la transmisión de datos entre los hosts, y se asegura de que se realiza correctamente.
- **Red:** tiene tres funciones principales:
  - *Encaminamiento*: establecimiento de la ruta a seguir desde un host a otro.
  - *Control de congestión*: evita la saturación de la subred como consecuencia de un tráfico elevado.
  - *Interconexión de redes*: posibilita la transmisión de datos entre hosts situados en diferentes redes.
- **Enlace:** en esta capa, los bits de datos se agrupan en bloques llamados "tramas". Realiza las siguientews funciones:
  - *Delimitación de tramas*: permite conocer el inicio y fin de un bloque de datos y sincronizar al emisor y al receptor.
  - *Control de errores*: comprueba que la información recibida corresponde con la enviada.
  - *Control de flujo*: evita que el emisor sature el *buffer* de recepción del destino debido a una velocidad diferente entre las dos partes.
- **Física:** en ella se llevan a cabo funciones relacionadas con la transmisión de datos desde el punto de vista de la gestión de características eléctricas, mecánicas y funcionales para una adecuada transferencia sobre el canal. Sería la tarjeta de red.

El modelo OSI tiene capas con muy poco contenido. Por eso es normal ver un numero menor de capas en otros modelos, ya que varias funciones se asocian a la misma capa. En **TCP/IP** se distinguen las siguientes capas:

- **Aplicación:** se definen en esta capa servicios como *telnet* (acceso remoto), *ftp* (transmisión de archivos), *http* (web), etc.
- **Transporte:** control de flujo, de errores, de congestión y de conexión (extremo a extremo).
- **Red:** encaminamiento.

TCP/IP es el modelo que se utiliza en internet, y es una red software, ya que se puede implementar sobre cualquier tecnología de red. Es un ejemplo de modelo *de facto*, y el más extendido en la actualidad.
La red subyacente no se tiene en consideración en TCP/IP, ya que al ser un modelo software, no especifica las características de la misma, pudiendo variar en cada ordenador.

### 3. Terminología y servicios

#### 3.1. Modelo OSI: comunicación real frente a comunicación virtual

![OSI capas](https://i.imgur.com/iE6Ki8u.png)

Dadas dos capas adyacentes, la capa inferior se denomina **proveedora de servicios**, y la inferior, **usuaria de servicios**, ya que la capa inferior ofrece una serie de servicios transparentes a la superior.

Los elementos software o hardware de una capa se conocen como **entidades de nivel N**. Las entidades de nivel N en el emisor y en el receptor se conocen como **entidades pares**, ya que se conectan dos a dos.

Existen dos tipos de comunicación entre emisor y receptor:
- **Comunicación real (vertical):** es el flujo que sigue la información entre el emisor y el receptor, en sentido descendente (aplicación a física) en el emisor y ascendente (física a aplicación) en el receptor.
- **Comunicación virtual (horizontal):** comunicación entre entidades pares. En la transmisión de un mensaje se necesita la colaboración de las entidades pares emisora y recepotora. Para ello, en cada capa (salvo en la física) se añade una cabecera para ayudar a comunicar las partes involucradas.

Un **protocolo** es el conjunto de reglas y convenciones que se tienn que aplicar en una comunicación entre dos entidades. A las capas y protocolos asociados se les denomina **arquitectura de red**. En este sentido, OSI no es una arquitectura, ya que no define protocolos, mientras que TCP/IP sí, ya que en cada capa se conocen los protocolos que se tienen que tener en cuenta. La especificación en capas de una arquitectura de red se denomina **pila de protocolos**.

La comunicación vertical se realiza mediante la **interfaz**, concretamente con los **puntos de acceso (*Service Access Points, SAP*)**. Dentro de la información que se transmite se distinguen la **unidad de datos de servicio (*Data Service Unit, SDU*)**, que son los datos que se quieren enviar (provienen de la capa superior), y la **unidad de datos de protocolo (*Protocol Data Unit, PDU*)**, que es la cabecera añadida para llevar a cabo las operaciones con entidades paritarias.


#### 3.2. Retardo

El **retardo** es el tiempo que tarda la información en llegar desde el host origen al destino.

![Retardo](https://i.imgur.com/w48FNJX.png)

Deben distinguirse dos tiempos:
- **Tiempo de transmisión:** cuánto se tarda en transmitir todos los bits a la red.


![img](http://www.sciweavers.org/tex2img.php?eq=T_%7Bt%7D%20%3D%20%5Cfrac%7BTam%20%28B%29%7D%7BV_%7Bt%7D%20%28bps%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)

- **Tiempo de propagación:** cuánto tarda la información en llegar al destino.


![img2](http://www.sciweavers.org/tex2img.php?eq=T_%7Bt%7D%20%3D%20%5Cfrac%7BDistancia%20%28m%29%7D%7BV_%7Bpropagacion%7D%20%28m%2Fs%29%7D&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0)


#### 3.3. Servicios

Los diferentes servicios que se pueden ofrecer son los siguientes:

- **Orientado a Conexión:** se establece una conexión como paso previo a la transmisión de datos entre el emisor y el receptor. Se realiza enviando un paquete de un tamaño por parte del emisor que el receptor debe devolver. Una vez devuelto, comienza el envío del resto de paquetes. Este tipo de servicios se utilizan cuando necesitamos que no haya pérdidas de información.
- **No Orientado a Conexión:** no requiere de una conexión como el anterior, y el envío se realiza con una gran rapidez, aunue existan pérdidas en la transmisión. Un ejemplo de estos servicios es la reproducción de contenido multimedia online, en el que no importa si perdemos un frame o dos, pero necesitamos que lleguen constantemente para que la reproducción sea fluida.
- **Confirmado (fiable):** el host emisor tiene constancia de que el receptor tiene el paquete.
- **No confirmado (no fiable):** el host emisor no tiene forma de saber si el receptor tiene el paquete.



### 4. Internet: arquitectura y direccionamiento

#### 4.1. Arquitectura 

Se establece una **topología jerárquica** entre diferentes tipos de redes:
- **Intranets (*Ethernet*) del usuario:** zona pública + zona privada. Son las redes locales de usuario, en las que se incluyen direcciones privadas para la subred local y direcciones públicas para acceder a la red.
- **Redes de acceso:** diferentes métodos de acceso, como el ADSL o la fibra óptica, pertenecientes al ISP (*Internet Service Provider*).
- **Redes troncales:** son diferentes redes de grandes operadores de telecomunicaciones. Un ejemplo sería la *red Iris*, que conecta la comunidad investigadora y las universidades españolas. Hay varios tipos según su tamaño: *Tier-1*, *Tier-2* y *Tier-3*.
- **Internet Exchange Points (IXP):** también conocidos como **puntos neutros**, son aquellos en los que las redes ISP se encuentran para intercambiar tráfico.

#### 4.2. Direccionamiento

Cuando queremos, por ejemplo, acceder a una página web, se genera un paquete de datos con la información necesaria para que las distintas capas por las que va a pasar sepan qué hacer con él, y lo transmitan entre los diferentes nodos por los que debe pasar hasta llegar a su destino. Una vez llegue, se nos devolverá la información que hemos pedido.

Para conseguir que el paquete llegue a su destino necesitamos **direccionarlo**.
El direccionamiento necesitamos los siguientes elementos:

- **Nombre de dominio:** El nombre de dominio se especifica en la capa de aplicación, ya que es la que interactúa con el usuario. La capa se encarga de traducirlo a una dirección IP. Ej: https://github.com/patchispatch
- **Dirección IP:** necesaria para identificar los host, se enuentra en la capa de red. Existen dos tipos:
  - *Públicas:* direccionan a un único dispositivo y se paga (o se alquila) por ella. Son unívocas en todo Internet.
  - *Privadas:* son direcciones que se pueden repetir en el mundo, pero no dentro de una red privada, ya que identifican a los diferentes dispositivos de la misma. Sin ellas, habríamos agotado el número de IPs disponibles en el mundo hace años.
- **Puertos:** sieven para establecer diferentes conexiones y responder peticiones de otros dispositivos. Se localizan en la capa de transporte.



---

## Tema 2: servicios y protocolos de aplicación en Internet

### 1. Introducción a las aplicaciones de red

#### 1.1. Arquitectura Cliente/Servidor

Un  **servidor** es una aplicación que permite el acceso remoto a recursos software o hardware en un host. Estará en escucha hasta recibir alguna solicitud por parte de un **cliente**.

Las características del cliente y el servidor son diferentes:

**Servidor**
- Siempre en funcionamiento.
- IP permanente y pública.
- Pueden estar agrupados en *granjas*.

**Clientes**
- Funcionan de forma intermitente.
- Pueden tener IP dinámica y privada.
- Se comunican con el servidor.
- No se comunican entre sí.

Son los clientes los que inician la conexión, y por lo general no se comunican entre sí.

El proceso envía y recibe mensajes desde su **socket**.
Para poder recibir mensajes, un proceso debe estar identificado por su IP y su puerto.

#### 1.2. La interfaz socket

Un **socket** es un descriptor de transmisión entre aplicaciones. Cuenta con una especie de API que los procesos utilizan para acceder a los servicios de transporte de forma segura. Cuando se quiere realizar una comunicación, se le asigna un **puerto**.

En definitiva, un socket es un proceso o thread que existe en el cliente y el servidor, que se utiliza para que ambos escriban y lean la información, que será transmitida por las capas de red. Es un puntero a una estructura.

![socket](https://i.imgur.com/qvMMbjZ.png)

#### 1.3. Protocolos de aplicación

¿Qué define un protocolo?
- **El tipo de servicio**
  - Orientado a conexión o no.
  - Realimentado o no.
- **El tipo de mensaje**
- **La sintaxis**
  Definición y estructura de campos en el mensaje.
- **La semántica**
  Significado de los campos.
- **Las reglas**
  Envío y respuesta de mensajes por parte de los procesos.

Existen varios tipos de protocolos:
- **Protocolos de dominio público:** están definidos en los [RFCs](https://www.wikiwand.com/en/Request_for_Comments), y buscan ser estandarizados. Ejemplos: HTTP, FTP.
- **Protocolos propietarios:** son creados por un organismo privado, y buscan ser lo más opacos posible, para que nadie sepa cómo funcionan.

También hay varias clasificaciones de protocolos, aunque menos importantes:
- **Protocolos in-band *versus* out-of-band:** los protocolos *in-band* envían en el mismo mensaje tanto la información como los datos de control, mientras que en *out-of-band* se utilizan diferentes canales para cada cosa.
- **Protocolos stateless *versus* state-full:** los protocolos *stateless* no guardan información de los clientes en el servidor, mientras que los *state-full* sí. HTTP por ejemplo es stateless, ya que no guarda nuestros datos. Sin embargo, utiliza **cookies**, ficheros almacenados localmente en el cliente. 
- **Protocolos persistentes *versus* no persistentes:** los protocolos *persistentes* se mantienen conectados, mientras que los *no persistentes* crean una conexión para cada envío de información.

La tendencia es **definir los protocolos de forma flexible**, utilizando una cabecera fija y una serie de trozos (*chunks*), algunos obligatorios y otros opcionales.

Los trozos pueden incluir una cabecera específica más una serie de datos como parámetros. Para los parámetros se usa el formato TLV (*Type-Length-Value*).

![TLV](https://i.imgur.com/l1l7IRh.png)


#### 1.4. Características

**Pérdida de datos**
Algunas aplicaciones soportan mejor la pérdida de datos que otras. En audio, por ejemplo, es tolerable; otros servicios como *telnet* o *ssh* requieren fiabilidad en la transmisión.

**Requisitos temporales**
Algunas apps requieren retardo acotado (bajo *delay*) para ser efectivas, como pueden ser las de telefonía o juegos.

**Rendimiento (*throughput*)**
Algunas apps necesitan enviar datos a una determinada tasa de transmisión. Por ejemplo, al ver una película por streaming necesitamos que cada cierto tiempo nos lleguen frames, o se parará. 

**Seguridad**
Encriptación, autenticado, etc.

A continuación se muestran ejemplos de aplicaciones de red, y la importancia que le dan a las anteriores características:

| **Aplicación**            | **Pérdida de datos** | **Rendimiento**            | **Sensible al tiempo** |
|---------------------------|----------------------|----------------------------|------------------------|
| Transferencia de archivos | no hay pérdida       | elástico                   | no                     |
| E-mail                    | no hay pérdida       | elástico                   | no                     |
| Documentos web            | no hay pérdida       | elástico                   | no                     |
| Multimedia en tiempo real | se puede perder algo | audio: 5kpbs video: 10kbps | sí                     |
| Audio o vídeo almacenado  | se puede perder algo | audio: 5kpbs video: 10kbps | sí                     |
| Videojuegos online        | se puede perder algo | unos cuantos kbps          | sí                     |
| Mensajería instantánea    | no hay pérdida       | elástica                   | depende                |


En la mensajería instantánea es preferible que el mensaje tarde algo más en llegar a que existan pérdidas, de ahí el *depende* en la tabla.

#### 1.5. Protocolos

Los protocolos están estructurados de la siguiente forma:



![Protocolos](https://i.imgur.com/75FvHlr.png)



Nos vamos a centrar en **TCP** y **UDP**.

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

	deiit.ugr.es

En este ejemplo, *.es* es el dominio de nivel 1 o superior, que engloba al subdominio *ugr*. Este, a su vez, engloba a *deiit*.

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

El dominio raíz "." está gestionado por la [ICANN](http://www.icann.org), que suele delegar en centros regionales. En España, este centro es [Red.es](https://red.es/redes/).

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

El contenido de las páginas se direcciona mediante una **URL** (*Uniform Resource Locator*), que indica el protocolo (*http* o *https* normalmente), el servidor (o el dominio) y el puerto (si es necesario), de la siguiente forma:

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

En el **correo electrónico** intervienen cuatro componentes principales:

- **Cliente de correo (*user agent*)** y **servidor de correo(*mail server*):** son los agentes de la conversación (remitente y destinatario) y los servidores, respectivamente. Por cada origen y cada destino, hay un cliente y un servidor.
- **Simple Mail Transfer Protocol (SMTP):** es el protocolo utilizado para el correo electrónico, aunque no el único implicado en el proceso. 
- **Protocolos de descarga:** sirven para descargar el correo recibido. Algunos de ellos son **POP3**, **IMAP** y **HTTP**.

#### 4.1. SMTP (RFC 2821)

![SMTP](https://i.imgur.com/tywMwh8.png)


En la imagen podemos ver los pasos necesarios para el envío y recepción de un correo electrónico. Si pensamos bien, el modelo cliente-servidor no nos sirve para esto, ya que no es necesario que el destinatario del correo esté conectado para poder enviarlo. Necesitamos disponer de una especie de intermediario que recoja el correo por él, al que pueda pedírselo cuando sí esté en línea. 

Los pasos para el envío de un correo electrónico, algo más explicados que en la imagen, son los siguientes:

1. El usuario origen compone el correo dirigido al usuario destino, utilizando su *agente de usuario*.
2. Cada usuario tiene asociado un servidor de correo, válido tanto para enviar como para recibir. El usuario origen envía mediante SMTP o HTTP el mensaje a su servidor de correo, que dispone de dos colas: la **cola de salida**, a la que llegan los correos que han sido enviados, y la **cola de entrada**, en la que cada usuario del servidor tiene un espacio reservado en el que se reciben sus correos. 
3. Periodicamente, el servidor libera todos los correos de la cola de salida, estableciendo una **conexión TCP** con los servidores destino y enviándolos a través de la misma. Se establece una comunicación servidor-servidor.
4. El servidor del usuario destino ubica los mensajes dirigidos a él en su *mailbox* o espacio reservado.
5. El usuario, a través de su agente de usuario, descarga los correos utilizando **POP3**, **IMAP** o **HTTP**.

La comunicación entre los agentes es cliente-servidor, pero no siempre en el mismo sentido. El envío de correos entre servidores siempre se realiza utilizando SMTP, pero cuando un usuario descarga el correo, lo hace con el protocolo de descarga de su elección.

##### 4.1.1. Características de SMTP

SMTP se implementa en dos programas:

- **Cliente SMTP:** el servidor actúa como cliente cuando recibe un correo y tiene que reenviarlo a otro servidor. Para ello, activa un puerto dinámico que se conecta con el puerto 25 del destino, y envía el correo a través de esa conexión.
- **Servidor SMTP:** cuando enviamos un correo, el servidor escucha peticiones en el pueto 25.

Se utiliza el protocolo de transporte **TCP**, ya que no queremos perder información, y no necesitamos un envío instantáneo.

Las fases de SMTP, sin contar con las de conexión y desconexión de TCP, son tres:

- Conexión o *handshaking*.
- Transferencia de mensajes.
- Cierre.

La interacción entre cliente y servidor SMTP es interactiva, y se realiza mediante comandos-respuesta, de forma muy parecida a *telnet*. Cuando realizamos acciones desde nuestro cliente de correo (Thunderbird, Mailspring, web), están enviando comandos al servidor web.

Los mensajes deben estar codificados en ASCII de 7 bits, lo cual limita mucho la capacidad de enviar multimedia. Para sortear este problema se añadieron las **extensiones MIME**, para añadir otro tipo de codificación, sobre todo para archivos adjuntos.

#### 4.2. Protocolos de acceso al correo

El protocolo **POP3**, al igual que SMTP, tiene tres fases:

- **Fase de conexión:** se realiza una autenticación mediante usuario y contraseña.
- **Fase de transacción:** se listan los correos, asociándolos a un índice para operar con ellos (leer, eliminar, etc.). En POP3, tras leer un correo se elimina inmediatamente, ya que no está preparado para guardar correos a largo plazo.
- **Fase de actualización:** tras cerrar la conexión, se eliminan los correos que se le han indicado al servidor.

**IMAP** tiene ventajas frente a POP3:

- Es ***state-full***: permite organizar los correos en el servidor, y almacenarlos a largo plazo.
- Permite descargar partes de los mensajes.
- Se puede acceder desde varios clientes.

Y por último, **webmail** dispone de todas las ventajas de HTTP:

- **Organización total en el servidor:** el agente de correo está integrado en el servidor web.
- **Seguridad:** se utiliza HTTPS, y los emails se envían encriptados.

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
