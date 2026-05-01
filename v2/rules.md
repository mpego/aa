# Game Rules

[Game Setup](#game-setup) | [Turn](#turn) | [Game Objective](#game-objective) | [Production](#production) | [Tiles and Unit movement](#tiles-and-unit-movement) | [Infrastructure](#infrastructure) | [Units](#units) | [IPC Collection](#ipc-collection) | [Combat](#combat) | [Developments](#developments-under-development-) | [Proof of Concepts](#proof-of-concepts) | [Stats](stats.html)

## Game Setup
* Each player choses a starting location at least 10 tiles apart of each other.
* **Army setup**
  Place a main industrial complex in each home tile.

  The initial army of each player is 1 infantry, 1 mechanized infantry, 1 artillery, 1 tank and 50 IPC.
* Chose a player to go first.
  Start the turn as normal.

## Game Objective
**Goal:** Conquer enemies' central base.
* Once a central base is conquered, conquered troops have the following turn to recover it before getting out of the game. At which point the army is considered conquered.
* In a more than two player game, the player that conquers a central base rolls a die:
  * On a 3 or less he preserves the army and infrastructure.
  * On other cases, the troops losing their home base go off the game.
* The army that conquers a central base wins 50 IPC to spend in amry and infrastructure as player best see fit.

## Production
* Each Industrial Complex accounts for up to 20 IPC of production per turn. All IPCs of production from all complexes is summed up to determine the total production of the player for the turn.
* Production of units cannot be split across multiple turns.
  * Land units must be located at a Military Base.
  * Infantry can be located in any tile with units or infrastructure.
  * Planes must be located at an Air Base.
  * Ships must be located at a Sea Base.

## Tiles and Unit movement
* Any given tile can hold up to one complex and up to 10 units.
* Unit being transported are not counted.
* For an island to be usable as land must be the size of at least half of a tile.
* Air units must end its movement in an Air Base, Aircra Carrier or Refueler. If not the unit is destroyed.

## Infrastructure
Infrastructure can be built in any tile with player units or next to a tile with a player complex.
* **Main Industrial Comples:** It is the main base of the player.
  If player has no Refineries it allows to roll 2 dice for IPC collection. On a 2 or less earn 5 IPCs for each die.

  They come with defense against ICBM. Roll three dice, on one 3 or less, the missile is destroyed before attack.
  
  If the missile hits the complex it counts as one hit.
* **Industrial Complex:** It increse production of units.
  These does not come with ICBM defense.
  
  For 50 IPC one of these can be swapped with the Main Industrial Complex.
* **Refinery:** Each refinery has oil production value equal to the value of a roll of 1 die when a truck arrives.
  A Refinery accespts only one transporter at a time.
  
  Can be built on land or sea but there must be 3 tiles separating it from any other infrastructure.
* **Military Base:** Is the starting base for land units.
* **Air Bases:** Can hold a max of 5 planes.
* **Naval Bases:** Can hold a max of 1 ships docked.
* **ICBM Silo:** Can hold 1 ICBM.
* **Roads:** Roads allow units to move an extra half of their movement as long as the unit keeps on the road. Going off the road stops the movement.
* Infrastructure requires 2 hits to be destroyed; one hit disables it.
* Complexes can be attacekd as if they were land units. They always receive one damage if the tile is conquered with a combat.
* Disabled infrastructure cannot produce, fix, lunch or receive units of any kind.
  
  In the case of Air bases, the planes must be sent to other bases in the range of movement of the plane or are considered destroyed.
* Disabled units only can be moved; planes cannot land nor take off from them.
* Repairs of any complex or unit cost half of its construction cost.

## Units
* **Mechanized Infantry and sea transport:** Can transport Oil
* **Aircraft Carrier:** They are not transpornts, they act as sea bases. Can hold up to 3 air units. Requires 2 hits to be destroyed, one hit disables it. Has to dock at a port to be fixed. Repair cost is half the ship costs.
* **Sea or Air Transports:** Can be by sea or air.
  * Can be used to transport up to two land troops.
  * It cannot attack nor defend from an attack.
  * Air transports can land with troops on an Aircraft Carrier, yet troops must be unloaded at an Air base.
  * Sea transport can transport oil from refineries, cannot combine units and oil at the same time. When tranporing oil they count as 2 units, in that case roll 2 dice.
* **AAA:** Have an auto defence system that allows them to perform an defensive attack on passing by planes, ICBM or surface ships at shore on enemy turn.
* **Submarines:** Have an auto defence system that allows them to perform an defensive attack on passing by ships on enemy turn.
* **ICBM:** Can attack any tile (works like strategic bomber attack).
  * On a 5 or less the attack succeeds. On a 5 the impact is in the tile and all surroundings.
  * Accounts for any number of hits required to destroy what is on the tile.
* **Refueler:** Refueling implies restore the full range for the plane to continue its movement.
  * Can refuel any air unit in the same territory. A plane can be refueled only once per turn. The unit can complete its movement at the refueler in which case in cannot defend if attacked and other planes cannot refuel at the refueler.
* Units being transported cannot defend.
* Units transporting oil cannot attack nor defend.
* If a ship is docked it cannot defend if the territory is attacked, and uniits being transported cannot either.

## IPC Collection
IPC is collected every time a truck with oil reaches an Industrial Complex or Main Industrial Complex.
* Oil must be moved from Refineris either be land, sea or combination of both to Industrial Complex or Main Industrial Complex to be converted into production IPCs.
  
  Each transport can carry load from one Refinery at a time. To load or unload oil the movement must end in the corresponding complex.
* Collected IPC accumulate to what player already has, up to a maximum of 50 IPC.

## Combat
Each unit has an attack and defence value depending of the unit type.

Either attack or defence is a hit if the die roll value for the unit is equal or less of the value for the unit type.

As units move, if there are enemy units in the destination tile, combat occurs. A tile can be attacked only once per turn.

Multiple units can attack the same tile in the same turn only if the attackers were declared before the first attack on the tile took place.

Winning player takes control of remaining complexes in the tile.

* **Resolving combat:** Roll one die per unit. Each unit accounts damage according its type.
  * The atack can continue as long as attacking units can damage defending units.
  * If defending units cannot defend against attacking units, the atatack finalizes when the attackers says so, or the die roll makes no damage.
  * The attacker choose what defending unit or complex get the damage. Units can be any unit in the tile.
  * If the tile has constructions, they can also be chosen as a target instead of units.
  * If the tile is conquered, all attacking units remain in the new tile and undestroyed complexes or bases gets one damage.
  * Abandoning an on-going attack does not count as retreat.

## Turn
* Move units
  * Move as many units as wanted. Each unit can move only once.
  * If the tile is occupied by enemy units, combat is declared.
  * Combat enables options for the attacked player:
    * Move units to the attacked tile:
      * Attacked player can move units to each tile under attack.
    * Retreat units from the attacked tile:
      * Units can move as long as they end its movement a friendly tile.
    * Retreat all defending units from the attacked tile:
      * All defending units retreat from the attacked tile to a friendly not attacked tile.
      * In this case the retreat has no cost for defending player.
    * If either of the actions happens on a tile, the attacking player can move more units that have not yet moved, to the tile, or retreat units from it.
    * Units reacting to an attack does not consume movement points for its next turn.
    * Units attacking or defending as a reaction can not be retreated.
    * Player retreating a unit from an attacked tile cannot move more units to it.
    * All movements must comply with maximum unit moving points each time.
    * Players lose 3IPC per each retreated unit.
* Resolve combats
  * Roll dice for attackers and defenders.
  * If no enemy units in tile, player conquers the tile and infrastructure without damaging it.
  * When combat finishes air units must use its remaining movement points to reach an airbase
* Regroup
  * Unit moving points gets reset. Units can regroup as long as their movement ends in a friendly tile
* Buy units or build infrastructure
  * Buy units and infrastructure and place in map

At no point the tile must contains more units of a player exceeding the maximum allowed per tile.

All movements must comply with maximum unit moving points each time.
* Repeat for next player.

## Developments (under development ...)
Every turn a player can spend up to 10 IPC in development.

Only one development can be undergoing at a time.

A completion dice is rolled every turn after spending in development reaches 30 IPC.

A development is complete when the completion dice roll is 5 or 6.

An extra completion dice can be bought with 10 IPC.
* **Land units level up:** Land units can be damaged by other units with same or higher level. Before rolling the completion dice, a level up dice must be roll with a value higher that the current level.
* **Air units level up:** Air units can be damaged by other units with same or higher level. Before rolling the completion dice, a level up dice must be roll with a value higher that the current level.
* **Sea units level up:** Sea units can be damaged by other units with same or higher level. Before rolling the completion dice, a level up dice must be roll with a value higher that the current level.
* **Portable AAA:** AAA can be installed in Battleship and Aircraft Carriers

## Proof of concepts
