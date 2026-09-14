# Game Rules

## Game Objective

**Goal:** Be the global dominator by destroing all enemies Base Complex and troops.

## Setup

Map:
* Recommendation is to play in a hexagonal grid of at least 20 hex height and 40 hex width.
* Map size to be at least 5 by 5 A4 sheets in landscape mode.
* Map generation using the [open-source tool by Azgaar](https://azgaar.github.io/Fantasy-Map-Generator) (simply awesome).

Each player chooses a starting location at least 15 tiles apart from each other.

**Army setup:**
* Place a Base Complex in each home tile.
* The initial army of each player is 4 infantry and 50 IPC.
* Start the turn as normal.

## Turn

### All Players

1. **Update oil production at Refineries:**
   * Each player rolls one die per refinery and allocates production at player choice.
   * Markers of production can be placed face up or down.
2. **Decide playing order for moving units:**
   * Each player rolls a die; the lower roll goes first.
3. **Buy units and build/relocate infrastructure:**
   * Buy units up to the max production IPC. All units must be placed in the corresponding complex.
   * Infantry can be placed in any tile with friendly units or complexes.
   * Buy infrastructure and place it on the map (tiles must have friendly units).
   * Relocate infrastructure paying the relocation cost.

### Each Player in Order

1. **Move units:**
   * Move as many units as wanted. Each unit can move only once per turn.
   * If retreating from a contested tile, the destination must be friendly and non-contested. Retreating units cannot move through the edge enemies came from.
   * Units can move to contested tiles.
   * If the destination tile is occupied by enemy units, combat is declared.
   * At no time may a tile contain units of a player exceeding the maximum allowed per tile.
   * To keep track of attackers at contested tiles, place a counter for the attacking player on the tile.
2. **Resolve combats:**
   * Roll dice for attackers and defenders.
   * If there are no enemy units in the tile, the player conquers the tile and its remaining infrastructure.
   * When combat finishes, air units must use their remaining movement points to reach an airbase.

### All Players

* Each player collects production from fully connected Refineries.

## Tiles and Unit movement

* Any given tile can hold up to 10 assets (including infrastructure and units) per player.
  * Each base accounts for 3 units of space.
  * Units in storage, docked, or parked count towards the limit of units per complex and tile.
  * Units or equipment being transported are not counted.
* For an island to be usable as territory, it must be at least half the size of a tile.
* Air units must end their movement in an Air Base, Aircraft Carrier, or Refueler.
  * If the above is not possible, the unit will be destroyed (except refuelers). In that case it can play a kamiaze attack on the tile it is located against any unit or complex (according to complex rules).
* Movement of units cannot be split.
  * *E.g.,* a transport with movement 4 cannot move 2 tiles, wait for units to be loaded, and then move again.
* Except for ICBM, any unit passing through a contested tile ends its movement.
* A unit can pass by a tile occupied by enemy units only if those units cannot attack any of the units being moved and the tile is not contested.
* Some units need more than one hit to be destroyed.
  * The first hit disables them; the second destroys them.
  * If disabled, units can only be moved; planes cannot take off from them.
  * They need to go to the corresponding base to be repaired.
  * Repair cost is half of the unit's cost.

## Infrastructure

Infrastructure can be built only by player infantry units. Each unit can build one infrastructure per turn and only where it is located. Building does not exhaust unit movement.

### Facilities

* **Base Complex:**
  * It is the Base Complex of the player.
  * Comes with 2 AAA embedded.
  * If a missile hits the complex, it counts as one hit.
  * Can produce IPC from oil.
  * When destoyed units of that player become militia and continues playing. If possible a new base can be built.
* **Production Complex:**
  * Receives resources from refineries to produce IPC.
* **Financial Complex:**
  * Increases production for units.
  * Does not need to be connected to the main complex.
* **Refinery:**
  * Each refinery has an oil production value equal to the roll of one die when built on land, and two dice when built on water (as if it were two refineries). Each turn, roll the corresponding dice.
  * If production in a refinery was not collected in the previous turn, it changes to the higher value.
  * Put value markers on each refinery to track production for the turn.
  * Can be built on land or sea, but there must be at least 3 tiles separating it from any other Refinery.
  * If built on a tile with both water and land, it is always built on land.
* **Industrial Complex:**
  * These are for the production of units and equipment.
  * All units are produced here and are moved automatically by road to the destination base.
  * If they cannot be moved, the complex can hold up to three units; these units cannot move, attack, or defend.
* **Military Base:** Is the starting base for land units.
* **Air Bases:** Is the starting base for air units.
* **Naval Bases:** Is the starting base for naval units.
  * Docked units count toward new unit limits.
  * Docking is required to repair ships.
* **ICBM Silo:** It is from where ICBMs are launched.

### Rules of Infrastructure

* Complexes can be attacked as if they were land units.
* Complexes require 2 hits to be destroyed; one hit disables it, and the next hit (if not repaired) destroys it.
  * If there are units in the complex when it is destroyed, they are also destroyed.
* Disabled infrastructure cannot produce, repair, or launch units of any kind, yet it can receive units or equipment.
* Repairs of any complex or unit cost half of its construction cost.
* Complexes can be repaired in contested tiles, but new ones cannot be built unless the tile is friendly.
* Refineries in contested tiles keep producing as long as they are not disabled.

### Connectivity & Structures

* **Roads:** Roads allow production to reach the destination base.
  * Roads are not conquered; they are either destroyed or remain usable.
* **Pipes:** Pipes are used to flow oil to be processed.
  * When a pipeline is built from a Refinery to a production complex, the Refinery is considered connected and its production is available to the player in every turn.
  * A pipeline in a tile counts as one unit, so it can be attacked and destroyed.
  * Pipelines are not conquered; they are either destroyed or keep passing oil.
  * Pipes can be built in tiles with friendly units.
  * Each refinery must have its own line of pipes.
* **Bridges:**
  * A bridge cannot be built in tiles with enemy units on them.
  * The max length of a bridge is three sections of road.
  * Each bridge section counts as one tile in regards to movement (same as land).
  * Units on a bridge cannot defend.
  * Bridges can be attacked like any other infrastructure (not individual sections of the bridge).
  * Destroying a bridge destroys the units on the bridge.
  * Only submarines and transports can pass by water under bridges.

*Note: Infrastructure elements like roads, pipes, and bridges are destroyed with one hit.*

## Units

* **Infantry:** Infantry is not produced; it is directly bought and can be placed at any tile with friendly units or complexes in non-contested tiles.
* **Mechanized infantry:** Can act as a carrier for Infantry.
  * When carrying infantry, mechanized infantry cannot attack or defend.
  * Unloading Infantry counts as a movement; it frees the mechanized infantry to attack or defend.
* **Transports:** Can load units or equipment.
  * Mechanized infantry can transport equipment.
  * Sea transports can transport land units and equipment.
  * Air transports can transport land units and equipment.
  * Air transports can park on an Aircraft Carrier, yet troops being transported must be unloaded at an Air Base.
* **Battleship:** Requires 2 hits to be destroyed.
* **Aircraft Carrier:** They are carriers and act as air bases at sea. Requires 2 hits to be destroyed.
* **AAA:** Have an auto-defense system that allows them to perform a preemptive engage on passing planes, ICBMs, or surface ships at shore on the enemy's turn, once per turn. Uses attacking stats.
* **Submarines:** Have an auto-defense system that allows them to perform a preemptive engage on passing ships on the enemy's turn, once per turn. Uses attacking stats.
* **Refueler:** Refueling restores the full range of a plane.
  * Can refuel one air unit in the same territory per turn.
  * Refuelers can be used like air bases in the air or to extend the range of movement of a plane.
* If a ship is docked, it cannot defend if the territory is attacked.
  * If the tile is conquered, a docked ship is captured.
* Units being carried can attack and defend.
* Units being transported cannot attack or defend.
* Units acting as carriers or transports cannot attack or defend.
* Units have a class that is used to determine their capabilities and interactions with other units.

## Equipment

Equipment enhances another unit or is placed on a tile. It can be used only from the equipped unit or tile it can equip.

**Long Range Missiles**
* Can be equipped onto Tactical Bombers.
* A Long Range Missile is consumed after use.
* It is affected by preemptive attacks.
* Can overfly territory with enemy units.

**Torpedo**
* Can be equipped onto submarines or destroyers.
* A torpedo is consumed after use.
* Can overpass territory with enemy ship units.
* It is affected by preemptive attacks.

* A pack of equipment counts as one unit for storage and transport.
* A unit can be equipped only at the corresponding base of the unit.

## Arsenal

Arsenal elements are like units that must be transported to the corresponding base to be used, or to a tile to be deployed.

* **ICBM:**
  * Can attack any tile (works like a strategic bomber attack).
  * Can be fired only from an ICBM Silo.
  * When moving, it can have only one change of direction.
  * On a roll of 5 or less, the attack succeeds. On a 1, the impact is in the tile and all adjacent tiles.
  * Accounts for any number of hits required to destroy what is on the tiles.
* **Landmine:**
  * Can be placed on a tile.
  * Attacks units passing by the tile.
  * Landmines are consumed if the mine attack succeeds.
* **Seamine:**
  * Can be placed on a tile.
  * Attacks units passing by the tile.
  * Seamines are consumed if the mine attack succeeds.
* **Tactical Drone:**
  * Can be placed on a tile.
  * Attacks units in range of the drone.
  * The drone is consumed after use.

## IPC Collection

* Players can choose to roll dice for IPC collection for each refinery or roll one die for the Base Complex.
  * If rolling for the Base Complex, a roll of 2 or less earns 5 IPCs.
* Oil must be moved from Refineries by oil pipelines to a Production Complex to be converted into production IPCs.
* Conversion value is 1 to 1: the value of the dice of the Refinery to IPC.
* Collected IPC accumulates to what the player already has, up to a maximum of 50 IPC.

## Production

* Base Complex allows for 20 IPC of production.
* Each Financial Complex accounts for 20 IPC of additional production per turn. All IPCs of production from all complexes are summed up to determine the total production of the player for the turn.
* Production of units cannot be split across multiple turns.
* Refinery production does not exhaust.

Units and equipment are produced in Industrial Complexes:
* When produced, they are automatically transported by roads connected to the destination base.
* If there are no roads, the unit is temporarily stored in the Industrial Complex.
* Up to three units can wait in an Industrial Complex for transport.
* If more units are produced, the units must be transported or discarded.
  * Land units must be transported to a Military Base.
  * Airplanes must be transported to an Air Base.
  * Ships must be transported to a Naval Base.
  * ICBMs must be transported to an ICBM Silo.

* Everything is in play from the next moving phase of the turn in which it is bought or produced.

## Combat

Combat is resolved after all players have moved, so the order of contested tiles is not important.
Combat is resolved by rolling one D6 for each attacking and defending unit.
Each unit has an attack and defense value depending on the unit type.
Either attack or defense is a hit if the die roll value for the unit is equal to or less than the value for the unit type.

As units move, if there are enemy units in the destination tile, combat occurs.
Each tile can be attacked only once per turn.

### Resolving Combat

* From attacking units, choose up to 5 units to run the attack.
* From defending units, choose up to 5 units to run the defense.
* These are the only units that will participate in combat this turn.
* All other units remain in the tile as backup units.
* Roll one die per chosen attacking and defending unit. Each unit accounts for damage according to its type.
* Both attacking and defending damage are accounted for simultaneously.
* At the end of the attack, there are no frontline or backup units; all units are in the same group.
* The player causing damage chooses which unit or complex gets the damage.
  * If damage surpasses frontline units, damage can go to backup units in the tile according to attacking unit rules (*effective against* in the stats page applies to all damage allocation).
* If the tile has constructions, they can also be chosen as a target instead of units.
  * To assign damage to the *Base Complex*, all defending units must been defeated. 

After the attack, remaining units stay in the tile (except for airplanes, which must return to an airbase or refueler), and the tile remains contested.
* Ownership of contested tiles does not change until only one player has units in the tile, at which point they own the tile.
* Infrastructure is fully operative (including pipes, roads, and bridges) in contested tiles unless it receives damage.
    * It must be kept for a full turn before being productive for the new owner.
* When a unit is equipped, the equipment's moving range is the attacking range of such equipment.
* Infantry bought cannot be placed in contested tiles.

Attack of equipment is resolved at the end of the movement phase of the player that is moving.
When the attacked target is a base with units, if able, those units leave the base and can move in their turn if able.

Preemptive attacks do not wait until the combat phase:
* It can happen as many times as the conditions are met during the same movement phase, even for the same unit.
* The only restriction is that each unit with a preemptive attack can only be used once per occurrence.
* A preemptive attack is neutralized if the attacking army also has at least one unit with preemptive attack. In this case, the preemptive attack does not happen.

## Proof of concepts

## Developments (under development ...)

Every turn a player can spend up to 10 IPC in development. Only one development can be undergoing at a time.

A completion dice is rolled every turn after spending in development reaches 30 IPC. A development is complete when the completion dice roll is 2 or less.

An extra completion dice can be bought with 10 IPC.

* **Radar:** Radars work in conjunction with AAA. Radars can detect air units passing by adjacent tiles and extend AAA pre-attack to their surrounding tiles.
* **Stealth technology:** Once developed, radar cannot detect air units.
* **Portable AAA:** AAA can be installed in Battleships and Aircraft Carriers.
* **Drones:** Works like short-range ICBMs.
* **Paratroopers:** Infantry can be dropped in any tile that is not under combat.
* **Land units level up:** Land units can be damaged by units with same or higher level. Before rolling the completion die, a level-up die must be rolled with a value higher than the current level.
* **Air units level up:** Air units can be damaged by units with same or higher level. Before rolling the completion die, a level-up die must be rolled with a value higher than the current level.
* **Sea units level up:** Sea units can be damaged by units with same or higher level. Before rolling the completion die, a level-up die must be rolled with a value higher than the current level.
