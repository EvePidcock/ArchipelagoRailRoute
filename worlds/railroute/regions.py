from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Entrance, Region

if TYPE_CHECKING:
    from .world import RailRouteWorld

# A region is a container for locations ("checks"), which connects to other regions via "Entrance" objects.
# Many games will model their Regions after physical in-game places, but you can also have more abstract regions.
# For a location to be in logic, its containing region must be reachable.
# The Entrances connecting regions can have rules - more on that in rules.py.
# This makes regions especially useful for traversal logic ("Can the player reach this part of the map?")

# Every location must be inside a region, and you must have at least one region.
# This is why we create regions first, and then later we create the locations (in locations.py).


def create_and_connect_regions(world: RailRouteWorld) -> None:
    create_all_regions(world)
    connect_regions(world)


def create_all_regions(world: RailRouteWorld) -> None:
    # Creating a region is as simple as calling the constructor of the Region class.
    menu = Region("Menu", world.player, world.multiworld)
    system_upgrades_green_tier_1 = Region("Tier 1 System Upgrades (Green)", world.player, world.multiworld)
    system_upgrades_green_tier_2 = Region("Tier 2 System Upgrades (Green)", world.player, world.multiworld)
    system_upgrades_green_tier_3 = Region("Tier 3 System Upgrades (Green)", world.player, world.multiworld)


    # Let's put all these regions in a list.
    regions = [menu, system_upgrades_green_tier_1, system_upgrades_green_tier_2, system_upgrades_green_tier_3]

    # Some regions may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    if world.options.red_trains:
        system_upgrades_red_tier_1 = Region("Tier 1 System Upgrades (Red)", world.player, world.multiworld)
        system_upgrades_red_tier_2 = Region("Tier 2 System Upgrades (Red)", world.player, world.multiworld)
        system_upgrades_red_tier_3 = Region("Tier 3 System Upgrades (Red)", world.player, world.multiworld)
        regions.append(system_upgrades_red_tier_1)
        regions.append(system_upgrades_red_tier_2)
        regions.append(system_upgrades_red_tier_3)

    # We now need to add these regions to multiworld.regions so that AP knows about their existence.
    world.multiworld.regions += regions


def connect_regions(world: RailRouteWorld) -> None:
    # We have regions now, but still need to connect them to each other.
    # But wait, we no longer have access to the region variables we created in create_all_regions()!
    # Luckily, once you've submitted your regions to multiworld.regions,
    # you can get them at any time using world.get_region(...).
    menu = world.get_region("Menu")
    system_upgrades_green_tier_1 = world.get_region("Tier 1 System Upgrades (Green)")
    system_upgrades_green_tier_2 = world.get_region("Tier 2 System Upgrades (Green)")
    system_upgrades_green_tier_3 = world.get_region("Tier 3 System Upgrades (Green)")

    # An even easier way is to use the region.connect helper.
    menu.connect(system_upgrades_green_tier_1, "Menu to Green Tier 1")
    system_upgrades_green_tier_1.connect(system_upgrades_green_tier_2, "Green Tier 1 to 2")
    system_upgrades_green_tier_2.connect(system_upgrades_green_tier_3, "Green Tier 2 to 3")

    # Some Entrances may only exist if the player enables certain options.
    # In our case, the Hammer locks the top middle chest in its own room if the hammer option is enabled.
    # In this case, we previously created an extra "Top Middle Room" region that we now need to connect to Overworld.
    if world.options.red_trains:
        system_upgrades_red_tier_1 = world.get_region("Tier 1 System Upgrades (Red)")
        system_upgrades_red_tier_2 = world.get_region("Tier 2 System Upgrades (Red)")
        system_upgrades_red_tier_3 = world.get_region("Tier 3 System Upgrades (Red)")

        menu.connect(system_upgrades_red_tier_1, "Menu to Red Tier 1")
        system_upgrades_red_tier_1.connect(system_upgrades_red_tier_2, "Red Tier 1 to 2")
        system_upgrades_red_tier_2.connect(system_upgrades_red_tier_3, "Red Tier 2 to 3")
