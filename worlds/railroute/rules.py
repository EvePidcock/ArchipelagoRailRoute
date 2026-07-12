from __future__ import annotations
from rule_builder.rules import Has, True_

from typing import TYPE_CHECKING

from BaseClasses import CollectionState
from worlds.generic.Rules import add_rule, set_rule

if TYPE_CHECKING:
    from .world import RailRouteWorld


def set_all_rules(world: RailRouteWorld) -> None:
    # In order for AP to generate an item layout that is actually possible for the player to complete,
    # we need to define rules for our Entrances and Locations.
    # Note: Regions do not have rules, the Entrances connecting them do!
    # We'll do entrances first, then locations, and then finally we set our victory condition.

    set_all_entrance_rules(world)
    set_all_location_rules(world)
    set_completion_condition(world)


def set_all_entrance_rules(world: RailRouteWorld) -> None:
    # First, we need to actually grab our entrances. Luckily, there is a helper method for this.

    menu_to_green_1 = world.get_entrance("Menu to Green Tier 1")
    green_1_to_2 = world.get_entrance("Green Tier 1 to 2")
    green_2_to_3 = world.get_entrance("Green Tier 2 to 3")

    if world.options.system_upgrade_locked_behind_keys:
        world.set_rule(menu_to_green_1, Has("Progressive System Upgrade Tier Unlock (Green)", 1))
        world.set_rule(green_1_to_2, Has("Progressive System Upgrade Tier Unlock (Green)", 2))
        world.set_rule(green_2_to_3, Has("Progressive System Upgrade Tier Unlock (Green)", 3))


    if world.options.red_trains:
        menu_to_red_1 = world.get_entrance("Menu to Red Tier 1")
        red_1_to_2 = world.get_entrance("Red Tier 1 to 2")
        red_2_to_3 = world.get_entrance("Red Tier 2 to 3")

        if world.options.system_upgrade_locked_behind_keys:
            world.set_rule(menu_to_red_1, Has("Progressive System Upgrade Tier Unlock (Red)", 1))
            world.set_rule(red_1_to_2, Has("Progressive System Upgrade Tier Unlock (Red)", 2))
            world.set_rule(red_2_to_3, Has("Progressive System Upgrade Tier Unlock (Red)", 3))


def set_all_location_rules(world: RailRouteWorld) -> None:
    # Location rules work no differently from Entrance rules.
    # Most of our locations are chests that can simply be opened by walking up to them.
    # Thus, their logical requirements are covered by the Entrance rules of the Entrances that were required to
    # reach the region that the chest sits in.
    # However, our two enemies work differently.
    # Entering the room with the enemy is not enough, you also need to have enough combat items to be able to defeat it.
    # So, we need to set requirements on the Locations themselves.
    # Since combat is a bit more complicated, we'll use this chance to cover some advanced access rule concepts.


    eight_green_xp_loc = world.get_location("Earn 8 Green XP")
    eight_green_xp_rule = Has("") | True_

    world.set_rule(eight_green_xp_loc, eight_green_xp_rule)



def set_completion_condition(world: RailRouteWorld) -> None:
    # Finally, we need to set a completion condition for our world, defining what the player needs to win the game.
    # You can just set a completion condition directly like any other condition, referencing items the player receives:
    world.multiworld.completion_condition[world.player] = lambda state: state.has_all(("Sword", "Shield"), world.player)

    # In our case, we went for the Victory event design pattern (see create_events() in locations.py).
    # So lets undo what we just did, and instead set the completion condition to:
    world.multiworld.completion_condition[world.player] = lambda state: state.has("Victory", world.player)
