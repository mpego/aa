# Reglas del Juego

## Objetivo del Juego

**Meta:** Conquistar la base central de los enemigos.

* Una vez conquistada una base central, las tropas conquistadas tienen el siguiente turno para recuperarse.
* Si después de este turno la base permanece bajo el control del jugador que la conquistó, entonces, en un juego de más de 2 jugadores:
  * Con un resultado de 3 o menos en la tirada del dado, conservan su ejército e infraestructura.
  * En otros casos, las tropas que pierden su base de origen se eliminan del tablero.
  * Los IPC del jugador perdedor pasan al conquistador hasta su límite máximo posible de IPC.
* En un juego de dos jugadores, el juego termina.

## Configuración

Mapa:
* Se recomienda jugar en una cuadrícula hexagonal de 20 hexágonos de alto y 40 hexágonos de ancho.
* El tamaño del mapa debe ser de al menos 5 por 5 hojas A4 en modo horizontal (landscape).
* Generación de mapas con la [herramienta de código abierto de Azgaar](https://azgaar.github.io/Fantasy-Map-Generator) (simplemente increíble).

Cada jugador elige una ubicación de inicio a al menos 15 casillas (tiles) de distancia entre sí.

**Configuración del ejército:**
* Coloca un Complejo de Base (Base Complex) en cada casilla de origen.
* El ejército inicial de cada jugador es de 4 infanterías y 50 IPC.
* Comienza el turno normalmente.

## Casillas y Movimiento de Unidades

* Cualquier casilla dada puede albergar hasta un máximo de 10 activos (incluyendo infraestructura y unidades) por jugador.
  * Cada base cuenta como 3 unidades de espacio.
  * Las unidades en almacenamiento, acopladas (docked) o estacionadas cuentan para el límite de unidades por complejo y casilla.
  * Las unidades o equipo que están siendo transportados no se cuentan.
* Para que una isla sea utilizable como territorio, debe tener al menos la mitad del tamaño de una casilla.
* Las unidades aéreas deben terminar su movimiento en una Base Aérea, Portaaviones o Reabastecedor. De lo contrario, la unidad es destruida (excepto los reabastecedores).
* El movimiento de las unidades no se puede dividir.
  * *Ej.,* un transporte con movimiento 4 no puede moverse 2 casillas, esperar a que se carguen las unidades y luego moverse de nuevo.
* A excepción del ICBM, cualquier unidad que pase por una casilla en disputa (contested) termina su movimiento.
* Una unidad puede pasar por una casilla ocupada por unidades enemigas solo si dichas unidades no pueden atacar a ninguna de las unidades que se están moviendo y la casilla no está en disputa.
* Algunas unidades necesitan más de un impacto (hit) para ser destruidas.
  * El primer impacto las inhabilita; el segundo las destruye.
  * Si están inhabilitadas, las unidades solo pueden moverse; los aviones no pueden despegar de ellas.
  * Deben ir a la base correspondiente para ser reparadas.
  * El costo de reparación es la mitad del costo de la unidad.

## Infraestructura

La infraestructura solo puede ser construida por unidades de infantería del jugador. Cada unidad puede construir una infraestructura por turno y solo en el lugar donde se encuentra. La construcción no agota el movimiento de la unidad.

### Instalaciones (Facilities)

* **Complejo de Base (Base Complex):**
  * Es el Complejo de Base del jugador.
  * Viene con 2 AAA integrados.
  * Si un misil impacta en el complejo, cuenta como un impacto.
  * Puede producir IPC a partir de petróleo.
* **Complejo de Producción (Production Complex):**
  * Recibe recursos de las refinerías para producir IPC.
* **Complejo Financiero (Financial Complex):**
  * Incrementa la producción de unidades.
  * No necesita estar conectado al complejo principal.
* **Refinería (Refinery):**
  * Cada refinería tiene un valor de producción de petróleo igual al resultado de la tirada de un dado cuando se construye en tierra, y dos dados cuando se construye en el agua (como si fuesen dos refinerías). Cada turno, se tiran los dados correspondientes.
  * Si la producción en una refinería no se recolectó en el turno anterior, cambia al valor más alto.
  * Coloca marcadores de valor en cada refinería para indicar la producción del turno.
  * Se puede construir en tierra o mar, pero debe haber una separación de al menos 3 casillas con respecto a cualquier otra Refinería.
  * Si se construye en una casilla con agua y tierra, siempre se construye en la parte terrestre.
* **Complejo Industrial (Industrial Complex):**
  * Estos sirven para la producción de unidades y equipo.
  * Todas las unidades se producen aquí y se transportan automáticamente por carretera a la base de destino.
  * Si no se pueden mover, el complejo puede albergar hasta tres unidades; estas unidades no pueden moverse, atacar ni defender.
* **Base Militar (Military Base):** Es la base de inicio para unidades terrestres.
* **Base Aérea (Air Base):** Es la base de inicio para unidades aéreas.
* **Base Naval (Naval Base):** Es la base de inicio para unidades navales.
  * Las unidades acopladas cuentan para los límites de nuevas unidades.
  * Se requiere acoplamiento para reparar barcos.
* **Silo de ICBM (ICBM Silo):** Es el lugar desde donde se lanzan los ICBM.

### Reglas de la Infraestructura

* Los complejos pueden ser atacados como si fuesen unidades terrestres.
* Los complejos requieren 2 impactos para ser destruidos; un impacto los inhabilita y el siguiente impacto (si no se repara) los destruye.
  * Si hay unidades en el complejo cuando este es destruido, también son destruidas.
* La infraestructura inhabilitada no puede producir, reparar ni lanzar unidades de ningún tipo, pero sí puede recibir unidades o equipo.
* Las reparaciones de cualquier complejo o unidad cuestan la mitad de su costo de construcción.
* Los complejos se pueden reparar en casillas en disputa, pero no se pueden construir nuevos a menos que la casilla sea amigable.
* Las refinerías en casillas en disputa siguen produciendo mientras no estén inhabilitadas.

### Conectividad y Estructuras

* **Carreteras (Roads):** Las carreteras permiten que la producción llegue a la base de destino.
  * Las carreteras no se conquistan; o bien se destruyen o permanecen utilizables.
* **Tuberías (Pipes):** Las tuberías se utilizan para transportar petróleo para ser procesado.
  * Cuando se construye una línea de tuberías desde una Refinería hasta un complejo de producción, la Refinería se considera conectada y su producción está disponible para el jugador en cada turno.
  * Una tubería en una casilla cuenta como una unidad, por lo que puede ser atacada y destruida.
  * Las tuberías no se conquistan; o bien se destruyen o siguen transportando petróleo.
  * Las tuberías se pueden construir en casillas con unidades amigables.
  * Cada refinería debe tener su propia línea de tuberías.
* **Puentes (Bridges):**
  * No se puede construir un puente en casillas con unidades enemigas.
  * La longitud máxima de un puente es de tres secciones de carretera.
  * Cada sección de puente cuenta como una casilla en lo que respecta al movimiento (igual que la tierra).
  * Las unidades sobre un puente no pueden defender.
  * Los puentes pueden ser atacados como cualquier otra infraestructura (not las secciones individuales del puente).
  * Destruir un puente destruye las unidades que se encuentren sobre él.
  * Solo los submarinos y transportes pueden pasar por agua debajo de los puentes.

*Nota: Los elementos de infraestructura como carreteras, tuberías y puentes se destruyen con un solo impacto.*

## Unidades

* **Infantería (Infantry):** La infantería no se produce; se compra directamente y se puede colocar en cualquier casilla con unidades amigables o complejos en casillas no disputadas.
* **Infantería Mecanizada (Mechanized infantry):** Puede actuar como transporte para la Infantería.
  * Al transportar infantería, la infantería mecanizada no puede atacar ni defender.
  * Descargar la Infantería cuenta como un movimiento; esto libera a la infantería mecanizada para atacar o defender.
* **Transportes (Transports):** Pueden cargar unidades o equipo.
  * La infantería mecanizada puede transportar equipo.
  * El transporte marítimo puede transportar unidades terrestres y equipo.
  * El transporte aéreo puede transportar unidades terrestres y equipo.
  * Los transportes aéreos pueden estacionarse en un Portaaviones, pero las tropas transportadas deben descargarse en una Base Aérea.
* **Acorazado (Battleship):** Requiere 2 impactos para ser destruido.
* **Portaaviones (Aircraft Carrier):** Son transportes y actúan como bases aéreas en el mar. Requiere 2 impactos para ser destruido.
* **AAA:** Tienen un sistema de defensa automática que les permite realizar un ataque preventivo (preemptive engage) sobre aviones que pasen, ICBM o barcos de superficie en la costa en el turno enemigo, una vez por turno. Utiliza estadísticas de ataque.
* **Submarinos (Submarines):** Tienen un sistema de defensa automática que les permite realizar un ataque preventivo sobre barcos que pasen en el turno enemigo, una vez por turno. Utiliza estadísticas de ataque.
* **Reabastecedor (Refueler):** Reabastecer implica restaurar el rango completo del avión.
  * Puede reabastecer a una unidad aérea en el mismo territorio por turno.
  * Los reabastecedores se pueden usar como bases aéreas en el aire o para extender el rango de movimiento de un avión.
* Si un barco está acoplado, no puede defender si el territorio es atacado.
  * Si la casilla es conquistada, el barco acoplado es capturado.
* Las unidades que son transportadas (carried) y pueden actuar de forma independiente pueden atacar y defender.
* Las unidades que están siendo transportadas (transported) no pueden atacar ni defender.
* Las unidades que actúan como transportes (carriers or transports) no pueden atacar ni defender.
* Las unidades tienen una clase que se utiliza para determinar sus capacidades e interacciones con otras unidades.

## Equipo

El equipo mejora a otra unidad o se coloca en una casilla. Solo se puede usar desde la unidad equipada o la casilla donde está equipado.

**Misiles de Largo Alcance (Long Range Missiles)**
* Se pueden equipar en Bombarderos Tácticos (Tactical Bombers).
* Un Misil de Largo Alcance se consume después de su uso.
* Se ve afectado por ataques preventivos.
* Puede sobrevolar territorio con unidades enemigas.

**Torpedos (Torpedo)**
* Se pueden equipar en submarinos o destructores.
* Un torpedo se consume después de su uso.
* Puede sobrepasar territorio con unidades de barcos enemigos.
* Se ve afectado por ataques preventivos.

* Un paquete de equipo cuenta como una unidad para almacenamiento y transporte.
* Una unidad solo se puede equipar en la base correspondiente de dicha unidad.

## Arsenal

El arsenal son como unidades que deben ser transportadas a la base correspondiente para ser utilizadas, o a la casilla para ser desplegadas.

* **ICBM:**
  * Puede atacar cualquier casilla (funciona como un ataque de bombardero estratégico).
  * Solo se puede disparar desde un Silo de ICBM.
  * Al moverse, solo puede tener un cambio de dirección.
  * Con un resultado de 5 o menos, el ataque tiene éxito. Con un 1, el impacto es en la casilla y en todas las casillas adyacentes.
  * Cuenta para cualquier cantidad de impactos necesarios para destruir lo que haya en las casillas.
* **Mina Terrestre (Landmine):**
  * Se puede colocar en una casilla.
  * Ataca a las unidades que pasan por la casilla.
  * Las minas terrestres se consumen si el ataque de la mina tiene éxito.
* **Mina Marina (Seamine):**
  * Se puede colocar en una casilla.
  * Ataca a las unidades que pasan por la casilla.
  * Las minas marinas se consumen si el ataque de la mina tiene éxito.
* **Dron Táctico (Tactical Drone):**
  * Se puede colocar en una casilla.
  * Ataca a las unidades dentro del alcance del dron.
  * El dron se consume después de su uso.

## Recolección de IPC

* Los jugadores pueden elegir tirar dados para la recolección de IPC por cada refinería o tirar un dado por el Complejo de Base.
  * Si se tira por el Complejo de Base, un resultado de 2 o menos otorga 5 IPC.
* El petróleo debe trasladarse desde las refinerías mediante tuberías de petróleo a un Complejo de Producción para convertirse en IPC de producción.
* El valor de conversión es de 1 a 1: el valor del dado de la refinería a IPC.
* El IPC recolectado se acumula a lo que el jugador ya tiene, hasta un máximo de 50 IPC.

## Producción

* El Complejo de Base permite 20 IPC de producción.
* Cada Complejo Financiero aporta 20 IPC de producción adicional por turno. Todos los IPC de producción de todos los complejos se suman para determinar la producción total del jugador para el turno.
* La producción de unidades no se puede dividir en varios turnos.
* La producción de la refinería no se agota.

Las unidades y el equipo se producen en Complejos Industriales:
* Al producirse, se transportan automáticamente por carreteras conectadas a la base de destino.
* Si no hay carreteras, la unidad se almacena temporalmente en el Complejo Industrial.
* Hasta tres unidades pueden esperar en el Complejo Industrial para ser transportadas.
* Si se producen más unidades, las unidades deben ser transportadas o descartadas.
  * Las unidades terrestres deben ser transportadas a una Base Militar.
  * Los aviones deben ser transportadas a una Base Aérea.
  * Los barcos deben ser transportados a una Base Naval.
  * Los ICBM deben ser transportados a un Silo de ICBM.

* Todo está en juego a partir de la siguiente fase de movimiento del turno en el que se compra o produce.

## Combate

El combate se resuelve después de que todos los jugadores se han movido, por lo que el orden de las casillas en disputa no es importante.
El combate se resuelve tirando un dado D6 por cada unidad atacante y defensora.
Cada unidad tiene un valor de ataque y defensa según el tipo de unidad.
Tanto el ataque como la defensa se consideran un impacto si el valor de la tirada del dado para la unidad es igual o menor al valor para su tipo de unidad.

A medida que las unidades se mueven, si hay unidades enemigas en la casilla de destino, ocurre un combate.
Cada casilla puede ser atacada solo una vez por turno.

### Resolución del Combate

* De las unidades atacantes, elige hasta 5 unidades para realizar el ataque.
* De las unidades defensoras, elige hasta 5 unidades para realizar la defensa.
* Estas son las únicas unidades que participarán en el combate este turno.
* Todas las demás unidades permanecen en la casilla como unidades de respaldo (backup).
* Tira un dado por cada unidad atacante y defensora elegida. Cada unidad registra daño según su tipo.
* Tanto el daño atacante como el defensor se contabilizan simultáneamente.
* Al final del ataque, no hay unidades de primera línea o de respaldo; todas las unidades quedan en el mismo grupo.
* El jugador que causa el daño elige qué unidad o complejo recibe el daño.
  * Si el daño supera a las unidades de primera línea, el daño puede ir a las unidades de respaldo en la casilla según las reglas de las unidades atacantes (la regla *efectivo contra* en la página de estadísticas se aplica a toda asignación de daño).
* Si la casilla tiene construcciones, estas también pueden elegirse como objetivo en lugar de las unidades.

Después del ataque, las unidades restantes se quedan en la casilla (excepto los aviones, que deben regresar a una base aérea o reabastecedor), y la casilla permanece en disputa.
* El control de las casillas en disputa no cambia hasta que solo un jugador tenga unidades en la casilla, momento en el cual se adueña de ella.
* La infraestructura es completamente operativa (incluyendo tuberías, carreteras y puentes) en las casillas en disputa a menos que reciba daño.
* Cuando una unidad está equipada, el rango de movimiento del equipo es el rango de ataque de dicho equipo.
* La infantería comprada no se puede colocar en casillas en disputa.

El ataque del equipo se resuelve al final de la fase de movimiento del jugador que se está moviendo.
Cuando el objetivo atacado es una base con unidades, si pueden, dichas unidades abandonan la base y pueden moverse en su turno.

Los ataques preventivos (preemptive attacks) no esperan a la fase de combate:
* Pueden ocurrir tantas veces como se cumplan las condiciones durante la misma fase de movimiento, incluso para la misma unidad.
* La única restricción es que cada unidad con ataque preventivo solo se puede usar una vez por ocurrencia.
* Un ataque preventivo se neutraliza si el ejército atacante también tiene al menos una unidad con ataque preventivo. En este caso, el ataque preventivo no ocurre.

## Turno

### Todos los Jugadores

1. **Actualizar la producción de petróleo en las Refinerías:**
   * Cada jugador tira un dado por refinería y asigna la producción a elección del jugador.
   * Los marcadores de producción se pueden colocar boca arriba o boca abajo.
2. **Decidir el orden de juego para mover unidades:**
   * Cada jugador tira un dado; el resultado más bajo va primero.
3. **Comprar unidades y construir/reubicar infraestructura:**
   * Compra unidades hasta el límite máximo de IPC de producción. Todas las unidades deben colocarse en el complejo correspondiente.
   * La infantería se puede colocar en cualquier casilla con unidades amigables o complejos.
   * Compra infraestructura y colócala en el mapa (las casillas deben tener unidades amigables).
   * Reubica infraestructura pagando el costo de reubicación.

### Cada Jugador en Orden

1. **Mover unidades:**
   * Mueve tantas unidades como desees. Cada unidad solo puede moverse una vez por turno.
   * En caso de retirarse de una casilla en disputa, el destino debe ser amigable y no disputado. Las unidades en retirada no pueden moverse a través del borde por el que vinieron los enemigos.
   * Unidades pueden moverse a casillas en disputa.
   * Si la casilla de destino está ocupada por unidades enemigas, se declara combate.
   * En ningún momento una casilla puede contener unidades de un jugador que excedan el máximo permitido por casilla.
   * Para llevar el control de los atacantes en las casillas en disputa, coloca un marcador para el jugador atacante en la casilla.
2. **Resolver combates:**
   * Tira dados para atacantes y defensores.
   * Si no hay unidades enemigas en la casilla, el jugador conquista la casilla y su infraestructura restante.
   * Cuando termina el combate, las unidades aéreas deben usar sus puntos de movimiento restantes para llegar a una base aérea.

### Todos los Jugadores

* Cada jugador recolecta la producción de las Refinerías que estén completamente conectadas.

## Prueba de conceptos

## Desarrollos (bajo desarrollo ...)

Cada turno, un jugador puede gastar hasta 10 IPC en desarrollo. Solo puede haber un desarrollo en curso a la vez.

Se tira un dado de finalización cada turno después de que el gasto en desarrollo alcance los 30 IPC. Un desarrollo se completa cuando el resultado del dado de finalización es 2 o menos.

Se puede comprar un dado de finalización extra por 10 IPC.

* **Radar:** Los radares funcionan en conjunto con las AAA. Los radares pueden detectar unidades aéreas que pasan por casillas adyacentes y extienden el ataque preventivo de las AAA a sus casillas circundantes.
* **Tecnología de Sigilo (Stealth technology):** Una vez desarrollada, el radar no puede detectar unidades aéreas.
* **AAA Portátil:** Las AAA se pueden instalar en Acorazados y Portaaviones.
* **Drones:** Funcionan como ICBM de corto alcance.
* **Paracaidistas:** La infantería se puede lanzar en cualquier casilla que no esté bajo combate.
* **Subida de nivel de unidades terrestres (Land units level up):** Las unidades terrestres pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
* **Subida de nivel de unidades aéreas (Air units level up):** Las unidades aéreas pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
* **Subida de nivel de unidades marítimas (Sea units level up):** Las unidades marítimas pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
