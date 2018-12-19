# Fundamentos de Redes

**3º Grado en Ingeniería Informática - Universidad de Granada - Curso 2018-2019**

> **Advertencia:** estos apuntes se encuentran en desarrollo, y son para uso personal. Si quieres contribuir o crees que he cometido errores, siéntete libre de hacer una *pull request*.

Este documento recoge apuntes de la asignatura **Fundamentos de Redes**, basados en el material docente ofrecido por el *departamento de Teoría de la Señal, Telemática y Comunicaciones* de la Universidad de Granada.

---

## Índice

<!--ts-->
   * [Fundamentos de Redes](#fundamentos-de-redes)
      * [Índice](#índice)
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



---

## Referencias
[^1]: [Modelo OSI - Wikipedia](https://es.wikipedia.org/wiki/Modelo_OSI)
[^2]: [International Organization for Standardization - Wikipedia](https://es.wikipedia.org/wiki/Organizaci%C3%B3n_Internacional_de_Normalizaci%C3%B3n)
[^3]: [Protocolo TCP - Wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_control_de_transmisi%C3%B3n)
[^4]: [Internet Protocol - Wikipedia](https://es.wikipedia.org/wiki/Protocolo_de_internet)
[^5]: [Peering - Wikipedia](http://en.wikipedia.org/wiki/Peering)
[^6]: [Tier 1 Networks - Wikipedia](https://en.wikipedia.org/wiki/Tier_1_network)
[^7]: [Internet Exchange Point - Wikipedia](https://en.wikipedia.org/wiki/Internet_exchange_point)