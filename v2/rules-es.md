# Reglas del Juego

## Objetivo del Juego

**Meta:** Ser el dominador global destruyendo los Complejos de Base enemigos.

El ganador es el jugador que saque una diferencia de dos puntos de Base con el segundo jugador más cercano.

**Tiempo de juego:** Alrededor de 10 horas para una partida de cuatro jugadores

## Configuración

Mapa:
* Se recomienda jugar en una cuadrícula hexagonal de al menos 20 hexágonos de alto y 40 hexágonos de ancho.
* El tamaño del mapa debe ser de al menos 5 por 5 hojas A4 en modo horizontal (landscape).
* Generación de mapas con la [herramienta de código abierto de Azgaar](https://azgaar.github.io/Fantasy-Map-Generator) (simplemente increíble).


**Configuración del ejército:**
* Los jugadores comienzan con un punto de Base.
* Cada jugador elige una casilla de origen a al menos 15 casillas de distancia entre sí.
* Coloca un Complejo de Base y 4 infanterías en cada casilla de origen.
* Establece 50 IPC como punto de partida.
* Comienza el turno normalmente.

## Turno

### Fase 1: Todos los Jugadores

**Actualizar la producción de petróleo en las Refinerías:**
   * Cada jugador tira un dado por cada refinería que controla y asigna la producción a su elección.
**Decidir el orden de juego para mover unidades:**
   * Cada jugador tira un dado; el resultado más bajo va primero.
**Comprar unidades y construir/reubicar infraestructura:**
   * Compra unidades hasta el límite máximo de IPC de producción. Todas las unidades deben colocarse en el complejo correspondiente.
   * La infantería se puede colocar en cualquier casilla con unidades amigas o complejos.
   * Compra infraestructura y colócala en el mapa (las casillas deben tener unidades amigas).
   * Reubica infraestructura pagando el costo de reubicación.

### Fase 2: Cada Jugador en Orden

**Alianzas**
  * Juega tus alianzas como mejor te parezca.

**Mover unidades:**
   * Mueve tantas unidades como desees. Cada unidad solo puede moverse una vez por turno.
   * Las unidades pueden moverse a casillas en disputa.
   * Si la casilla de destino está ocupada por unidades enemigas, se declara combate.
   * En caso de retirarse de una casilla en disputa, el destino debe ser amigo y no disputado o el Complejo de Base.
    * Las unidades en retirada no pueden moverse a través del borde por el que vinieron los enemigos.
   * Resuelve los ataques preventivos a medida que se cumplan las condiciones.
   * En ningún momento una casilla puede contener unidades de un jugador que excedan el máximo permitido por casilla.
   * Para llevar el control de los atacantes en las casillas en disputa, coloca un marcador para el jugador atacante en la casilla.
**Resolver ataque de equipo**

### Fase 3: Todos los Jugadores

**Resolver combates**
   * Resolver todas las zonas en disputa
   * Resolver el movimiento de unidades que necesitan regresar a una base

**Recolección de IPC**
   * Recolectar IPC de las Refinerías conectadas

## Casillas y Movimiento de Unidades

* Cualquier casilla dada puede albergar hasta un máximo de 10 activos (incluyendo infraestructura y unidades) por jugador.
  * Cada base cuenta como 3 unidades de espacio.
  * Las unidades en almacenamiento, acopladas (docked) o estacionadas cuentan para el límite de unidades por complejo y casilla.
  * Las unidades o equipo que están siendo transportados no se cuentan.
* Para que una isla sea utilizable como territorio, debe tener al menos la mitad del tamaño de una casilla.
* Las unidades aéreas deben terminar su movimiento en una Base Aérea, Portaaviones o Reabastecedor.
* El movimiento de las unidades no se puede dividir.
  * *Ej.,* un transporte con movimiento 4 no puede moverse 2 casillas, esperar a que se carguen las unidades y luego moverse de nuevo.
* Las unidades pueden pasar de largo por casillas con unidades enemigas solo cuando las unidades defensoras no puedan atacar a las unidades que pasan.
* Algunas unidades necesitan más de un impacto para ser destruidas.
  * El primer impacto las inhabilita; el segundo las destruye.
  * Si están inhabilitadas, las unidades solo pueden moverse; los aviones pueden aterrizar pero no despegar de ellas.
  * Deben ir a la base correspondiente para ser reparadas.
  * El costo de reparación es la mitad del costo de la unidad.

## Infraestructura

La infraestructura solo puede ser construida por unidades de infantería del jugador. Cada unidad puede construir una infraestructura por turno donde esté ubicada. 

### Instalaciones

* **Complejo de Base:**
  * Es el Complejo de Base del jugador.
  * Viene con 2 AAA integrados.
  * Si un ICBM impacta en el complejo, cuenta como un impacto.
  * Puede producir IPC a partir de petróleo.
  * Al ser destruido, las unidades de ese jugador se convierten en milicia y continúan jugando. De ser posible, se puede construir una nueva base.
  * **Destruir una Base enemiga te otorga los puntos de Base de ese jugador** más 50 IPC para gastar al final del turno. El IPC no gastado pasa a tu conteo de IPC.
  Coloca un marcador en tu Base de origen con tus puntos actuales.

* **Complejo de Producción:**
  * Recibe recursos de las refinerías para producir IPC.

* **Complejo Financiero:**
  * Incrementa la capacidad permitida de producción por turno.
  * No necesita estar conectado al complejo principal.

* **Refinería:**
  * Cada refinería tiene un valor de producción de petróleo igual a la tirada de un dado cuando se construye en tierra, y dos dados cuando se construye en agua (como si fueran dos refinerías). Cada turno, tira los dados correspondientes.
  * Si la producción en una refinería no se recolectó en el turno anterior, cambia al valor más alto.
  * Coloca marcadores de valor en cada refinería para llevar el control de la producción del turno.
  * Se puede construir en tierra o mar, pero debe haber al menos 3 casillas de separación con cualquier otra Refinería.
  * Si se construye en una casilla con agua y tierra, siempre se construye en tierra.

* **Complejo Industrial:**
  * Son para la producción de unidades y equipo.
  * Todas las unidades se producen aquí y se mueven automáticamente por carretera a la base de destino a menos que la ruta tenga casillas en disputa o con unidades enemigas.
  * Si no se pueden mover, el complejo puede albergar hasta tres unidades; estas unidades no pueden moverse, atacar ni defender.

* **Base Militar:** Es la base de inicio para unidades terrestres.

* **Bases Aéreas:** Es la base de inicio para unidades aéreas.

* **Bases Navales:** Es la base de inicio para unidades navales.
  * Las unidades acopladas cuentan para los límites de nuevas unidades.
  * Se requiere acoplarse para reparar barcos.

* **Silo de ICBM:** Es desde donde se lanzan los ICBM.

### Reglas de la Infraestructura

* Los complejos pueden ser atacados como si fueran unidades terrestres.
* Los complejos requieren 2 impactos para ser destruidos; un impacto los inhabilita y el siguiente impacto (si no se repara) los destruye.
  * Si hay unidades en el complejo (ej.: barcos acoplados en una base naval) cuando es destruido, también son destruidas.
* La infraestructura inhabilitada no puede producir, reparar ni lanzar unidades de ningún tipo, pero sí puede recibir unidades o equipo.
* Los complejos se pueden reparar por un costo.
* Los complejos se pueden reparar en casillas en disputa, pero no se pueden construir nuevos a menos que la casilla sea amiga.
* Las refinerías en casillas en disputa siguen produciendo mientras no estén inhabilitadas.

### Conectividad y Estructuras

* **Carreteras:** Las carreteras permiten que la producción llegue a la base de destino.
  * Las carreteras no se conquistan; o bien se destruyen o permanecen utilizables.
* **Tuberías:** Las tuberías se utilizan para transportar petróleo para ser procesado.
  * Cuando se construye una línea de tuberías desde una Refinería hasta un complejo de producción, la Refinería se considera conectada y su producción está disponible para el jugador en cada turno.
  * Una tubería en una casilla cuenta como una unidad, por lo que puede ser atacada y destruida.
  * Las tuberías no se conquistan; o bien se destruyen o siguen transportando petróleo.
  * Las tuberías se pueden construir en casillas con unidades amigas.
  * Cada refinería debe tener su propia línea de tuberías.
* **Puentes:**
  * No se puede construir un puente en casillas con unidades enemigas.
  * La longitud máxima de un puente es de tres secciones de carretera.
  * Cada sección de puente cuenta como una casilla en lo que respecta al movimiento (igual que la tierra).
  * Las unidades sobre un puente no pueden defender.
  * Los puentes pueden ser atacados como cualquier otra infraestructura (no las secciones individuales del puente).
  * Destruir un puente destruye las unidades sobre el puente.
  * Solo los submarinos y transportes pueden pasar por agua debajo de los puentes.

*Nota: Los elementos de infraestructura como carreteras, tuberías y puentes se destruyen con un solo impacto.*

## Unidades

* **Infantería:** La infantería no se produce; se compra directamente y se puede colocar en cualquier casilla con unidades amigas o complejos en casillas no disputadas (se permite ubicarla en un Complejo de Base en disputa).
* **Infantería mecanizada:** Puede actuar como transporte terrestre.
* **Transportes:** Pueden cargar unidades o equipo.
  * La infantería mecanizada puede transportar infantería, equipo o arsenal.
  * Los transportes marítimos pueden transportar unidades terrestres, equipo o arsenal.
  * Los transportes aéreos pueden transportar unidades terrestres, equipo o arsenal.
  * Los transportes aéreos pueden estacionarse en un Portaaviones, pero las tropas transportadas deben descargarse en una Base Aérea.
* **Acorazado:** Requiere 2 impactos para ser destruido.
* **Portaaviones:** Son transportes y actúan como bases aéreas en el mar. Requiere 2 impactos para ser destruido.
* **AAA:** Tienen un sistema de autodefensa que les permite realizar un ataque preventivo sobre aviones que pasen, ICBMs o barcos de superficie en la costa en el turno enemigo, una vez por turno. Utiliza estadísticas de ataque.
* **Submarinos:** Tienen un sistema de autodefensa que les permite realizar un ataque preventivo sobre barcos que pasen en el turno enemigo, una vez por turno. Utiliza estadísticas de ataque.
* **Reabastecedor:** Reabastecer restaura el alcance total de un avión.
  * Puede reabastecer a una unidad aérea en el mismo territorio por turno.
  * Se puede usar como bases aéreas en el aire para llevar un avión a la vez.


* Si un barco está acoplado, no puede defender si el territorio es atacado.
* Si la casilla es conquistada con barcos acoplados o aviones estacionados, las unidades son capturadas.
* Las unidades transportadas que pueden actuar de forma independiente pueden atacar y defender.
* Las unidades que transportan o que están siendo transportadas no pueden atacar ni defender.
* Las unidades tienen una clase que se utiliza para determinar sus capacidades e interacciones con otras unidades.

## Equipo

El equipo es una unidad que mejora a otra unidad o complejo. Solo se puede usar desde la unidad o complejo equipado.
Debe ser transportado al complejo o base correspondiente para acoplarse a la unidad.

* **Misiles de Largo Alcance**
  * Se pueden equipar en Bombarderos Tácticos.
  * Un Misil de Largo Alcance se consume después de su uso.
  * Se ve afectado por ataques preventivos.
  * Puede sobrevolar territorio con unidades enemigas.

* **Torpedo**
  * Se puede equipar en submarinos o destructores.
  * Un torpedo se consume después de su uso.
  * Puede sobrepasar territorio con unidades de barcos enemigos.
  * Se ve afectado por ataques preventivos.

* **ICBM:**
  * Puede atacar cualquier casilla (funciona como un ataque de bombardero estratégico).
  * Solo se puede disparar desde un Silo de ICBM.
  * Al moverse, solo puede tener un cambio de dirección.
  * Con una tirada de 5 o menos, el ataque tiene éxito. Con un 1, el impacto es en la casilla y en todas las casillas adyacentes.
  * Cuenta para cualquier cantidad de impactos necesarios para destruir lo que haya en las casillas.

* Un paquete de equipo cuenta como una unidad para almacenamiento y transporte.
* Una unidad solo se puede equipar en la base correspondiente de dicha unidad.

## Arsenal

El arsenal son unidades que deben transportarse a una casilla de destino para ser desplegadas.

* **Mina Terrestre:**
  * Se puede colocar en una casilla.
  * Ataca a las unidades que pasan por la casilla.
  * Una vez desplegada no se puede mover.
  * Las minas terrestres se consumen si el ataque de la mina tiene éxito.
* **Mina Marina:**
  * Se puede colocar en una casilla.
  * Ataca a las unidades que pasan por la casilla.
  * Una vez desplegada no se puede mover.
  * Las minas marinas se consumen si el ataque de la mina tiene éxito.
* **Dron Táctico:**
  * Se puede colocar en una casilla.
  * Ataca a las unidades dentro del alcance del dron.
  * El dron se consume después de su uso.

## Recolección de IPC

* Los jugadores siempre producen IPC, ya sea mediante refinerías conectadas si las tienen o a una tasa fija de 2 IPC por turno.
* El petróleo debe trasladarse desde las refinerías mediante tuberías de petróleo a un Complejo de Producción para convertirse en IPC de producción.
* El valor de conversión es de 1 a 1: el valor del dado de la refinería a IPC.
* Se suman todos los IPC de producción de todas las Refinerías para determinar la producción total del jugador para el turno.
* El IPC recolectado se acumula a lo que el jugador ya tiene, hasta un máximo de 50 IPC.

## Producción

* El Complejo de Base permite 20 IPC de producción.
* La producción de unidades no se puede dividir en varios turnos.
* La producción de la refinería no se agota.

Las unidades, el equipo y el arsenal se producen en Complejos Industriales:
* Hasta tres unidades (unidades, equipo o arsenal) pueden almacenarse temporalmente en el Complejo Industrial.
* No se pueden producir más unidades si no se reubican automáticamente.
  * Las unidades terrestres deben reubicarse en una Base Militar.
  * Los aviones deben reubicarse en una Base Aérea.
  * Los barcos deben reubicarse en una Base Naval.

* Todo está en juego desde el momento en que se compra o se produce.

## Combate

* El combate ocurre cuando una unidad invade una casilla ocupada por una unidad enemiga.
* El combate se resuelve en la fase 3 del turno después de que todos los jugadores se hayan movido, por lo que el orden para atender las casillas en disputa no es importante.
* El combate se resuelve tirando un dado D6 por cada unidad atacante y defensora.
* Cada unidad tiene un valor de ataque y defensa según el tipo de unidad.
* Tanto el ataque como la defensa se consideran un impacto si el valor de la tirada del dado para la unidad es igual o menor al valor para su tipo de unidad.
* Cuando el objetivo atacado es una base con unidades, si pueden, dichas unidades abandonan la base y defienden la casilla o se mueven en su turno si pueden.

### Resolución del Combate

* De las unidades atacantes, elige hasta 5 unidades para realizar el ataque (unidades de primera línea).
* De las unidades defensoras, elige hasta 5 unidades para realizar la defensa (unidades de primera línea).
* Estas son las únicas unidades que participarán en el combate este turno.
* Todas las demás unidades permanecen en la casilla como unidades de respaldo.
* Tira un dado por cada unidad atacante y defensora elegida. Cada unidad registra daño según su tipo.
* Tanto el daño atacante como el defensor se contabilizan simultáneamente.
* Al final del ataque, no hay unidades de primera línea o de respaldo; todas las unidades quedan en el mismo grupo.
* El jugador que causa el daño elige qué unidad, complejo o infraestructura recibe el daño (favoreciendo deliberadamente el ataque sobre la defensa).
  * El daño puede ir a unidades de primera línea o de respaldo en la casilla según las reglas de las unidades atacantes (*efectivo contra* en la página de estadísticas se aplica a toda asignación de daño).
  * Para asignar daño al *Complejo de Base*, todas las unidades defensoras deben haber sido derrotadas.

Después del ataque, las unidades restantes se quedan en la casilla (excepto los aviones, que deben regresar a una base aérea o reabastecedor), y la casilla permanece en disputa.
  * Las unidades aéreas deben regresar a una base aérea o reabastecedor. Si eso no es posible, esa unidad puede realizar un ataque kamikaze en la casilla en la que se encuentra contra cualquier unidad o complejo (según las reglas de los complejos).

* La infraestructura no dañada en casillas en disputa es completamente operativa (incluyendo tuberías, carreteras y puentes).
* El control de las casillas en disputa no cambia hasta que solo un jugador tenga unidades en la casilla, momento en el cual se adueña de la casilla y de la infraestructura en ella.
    * La casilla debe mantenerse durante un turno completo antes de que la infraestructura sea productiva para el nuevo dueño.
* La infantería no se puede comprar y colocar en casillas en disputa.

### Resolución de Ataques Preventivos

* Pueden ocurrir tantas veces como se cumplan las condiciones durante la misma fase de movimiento, incluso para la misma unidad.
* La única restricción es que cada unidad con ataque preventivo solo se puede usar una vez por ocurrencia.
* Un ataque preventivo de los atacantes es neutralizado por las unidades defensoras correspondientes con ataque preventivo. En este caso, el ataque preventivo ocurre solo para las unidades excedentes.
* El ataque preventivo se resuelve tan pronto como se cumple la condición.

## Prueba de conceptos

Nada por el momento

## Desarrollos (aún no jugable ...)

Cada turno un jugador puede gastar hasta 10 IPC en desarrollo. Solo puede haber un desarrollo en curso a la vez.

Se tira un dado de finalización cada turno después de que el gasto en desarrollo alcance los 30 IPC. Un desarrollo se completa cuando la tirada del dado de finalización es 2 o menos.

Se puede comprar un dado de finalización extra por 10 IPC.

* **Radar:** Los radares funcionan en conjunto con las AAA. Los radares pueden detectar unidades aéreas que pasan por casillas adyacentes y permiten que las AAA adyacentes a esa casilla realicen un pre-ataque.
* **Tecnología de Sigilo:** Una vez desarrollada, el radar no puede detectar unidades aéreas.
* **AAA Portátil:** Las AAA se pueden usar como equipo.
* **Radar Portátil:** Los radares se pueden usar como equipo.
* **Barcos Mejorados:** Todos los barcos de superficie se pueden equipar con AAA y Radares.
* **Drones:** Extiende el alcance de los Drones en 2 casillas.
* **Mejora de Radar:** Extiende el alcance del Radar en 1 casilla.
* **Paracaidistas:** La infantería se puede lanzar en cualquier casilla que no esté bajo combate.
* **Subida de nivel de unidades terrestres:** Las unidades terrestres pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
* **Subida de nivel de unidades aéreas:** Las unidades aéreas pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
* **Subida de nivel de unidades marítimas:** Las unidades marítimas pueden recibir daño de unidades del mismo nivel o superior. Antes de tirar el dado de finalización, se debe tirar un dado de subida de nivel con un valor superior al nivel actual.
