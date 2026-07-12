from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import ItemClassification, Location

from . import items

if TYPE_CHECKING:
    from .world import RailRouteWorld

# Every location must have a unique integer ID associated with it.
# We will have a lookup from location name to ID here that, in world.py, we will import and bind to the world class.
# Even if a location doesn't exist on specific options, it must be present in this lookup.

# ID Format: XXYYZZZ
#
# XX:
#   10 = System Upgrades
#        YY: Tier
#           10 = Green 1, 20 = Green 2, 30 = Green 3, 40 = Red 1, 50 = Red 2, 60 = Red 3
#        ZZZ: id
#
#   11 = Earning Green/Red Trains
#       YY: Green (10) or Red (20)
#       ZZZ: Count
LOCATION_NAME_TO_ID = {
    "System Upgrades (Green) Tier 1 Purchase 1": 1010001,
    "System Upgrades (Green) Tier 1 Purchase 2": 1010002,
    "System Upgrades (Green) Tier 1 Purchase 3": 1010003,
    "System Upgrades (Green) Tier 1 Purchase 4": 1010004,
    "System Upgrades (Green) Tier 1 Purchase 5": 1010005,
    "System Upgrades (Green) Tier 1 Purchase 6": 1010006,
    "System Upgrades (Green) Tier 1 Purchase 7": 1010007,
    "System Upgrades (Green) Tier 1 Purchase 8": 1010008,
    "System Upgrades (Green) Tier 1 Purchase 9": 1010009,

    "System Upgrades (Green) Tier 2 Purchase 1": 1020001,
    "System Upgrades (Green) Tier 2 Purchase 2": 1020002,
    "System Upgrades (Green) Tier 2 Purchase 3": 1020003,
    "System Upgrades (Green) Tier 2 Purchase 4": 1020004,
    "System Upgrades (Green) Tier 2 Purchase 5": 1020005,
    "System Upgrades (Green) Tier 2 Purchase 6": 1020006,
    "System Upgrades (Green) Tier 2 Purchase 7": 1020007,
    "System Upgrades (Green) Tier 2 Purchase 8": 1020008,

    "System Upgrades (Green) Tier 3 Purchase 1": 1030001,
    "System Upgrades (Green) Tier 3 Purchase 2": 1030002,
    "System Upgrades (Green) Tier 3 Purchase 3": 1030003,
    "System Upgrades (Green) Tier 3 Purchase 4": 1030004,
    "System Upgrades (Green) Tier 3 Purchase 5": 1030005,
    "System Upgrades (Green) Tier 3 Purchase 6": 1030006,
    "System Upgrades (Green) Tier 3 Purchase 7": 1030007,
    "System Upgrades (Green) Tier 3 Purchase 8": 1030008,
    "System Upgrades (Green) Tier 3 Purchase 9": 1030009,

    "System Upgrades (Red) Tier 1 Purchase 1": 1040001,
    "System Upgrades (Red) Tier 1 Purchase 2": 1040002,
    "System Upgrades (Red) Tier 1 Purchase 3": 1040003,
    "System Upgrades (Red) Tier 1 Purchase 4": 1040004,

    "System Upgrades (Red) Tier 2 Purchase 1": 1050001,
    "System Upgrades (Red) Tier 2 Purchase 2": 1050002,
    "System Upgrades (Red) Tier 2 Purchase 3": 1050003,
    "System Upgrades (Red) Tier 2 Purchase 4": 1050004,
    "System Upgrades (Red) Tier 2 Purchase 5": 1050005,

    "System Upgrades (Red) Tier 3 Purchase 1": 1060001,
    "System Upgrades (Red) Tier 3 Purchase 2": 1060002,

    "Earn 8 Green XP": 1110008,
}


# Each Location instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Location class and override the "game" field.
class RailRouteLocation(Location):
    game = "Rail Route"


# Let's make one more helper method before we begin actually creating locations.
# Later on in the code, we'll want specific subsections of LOCATION_NAME_TO_ID.
# To reduce the chance of copy-paste errors writing something like {"Chest": LOCATION_NAME_TO_ID["Chest"]},
# let's make a helper method that takes a list of location names and returns them as a dict with their IDs.
# Note: There is a minor typing quirk here. Some functions want location addresses to be an "int | None",
# so while our function here only ever returns dict[str, int], we annotate it as dict[str, int | None].
def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: LOCATION_NAME_TO_ID[location_name] for location_name in location_names}


def create_all_locations(world: RailRouteWorld) -> None:
    create_regular_locations(world)
    #create_events(world)


def create_regular_locations(world: RailRouteWorld) -> None:
    # Finally, we need to put the Locations ("checks") into their regions.
    # Once again, before we do anything, we can grab our regions we created by using world.get_region()
    menu = world.get_region("Menu")
    system_upgrades_green_tier_1 = world.get_region("Tier 1 System Upgrades (Green)")
    system_upgrades_green_tier_2 = world.get_region("Tier 2 System Upgrades (Green)")
    system_upgrades_green_tier_3 = world.get_region("Tier 3 System Upgrades (Green)")

    # A simpler way to do this is by using the region.add_locations helper.
    # For this, you need to have a dict of location names to their IDs (i.e. a subset of location_name_to_id)
    # Aha! So that's why we made that "get_location_names_with_ids" helper method earlier.
    # You also need to pass your overridden Location class.
    system_upgrades_green_tier_1_locations = get_location_names_with_ids(
        ["System Upgrades (Green) Tier 1 Purchase 1",
         "System Upgrades (Green) Tier 1 Purchase 2",
         "System Upgrades (Green) Tier 1 Purchase 3",
         "System Upgrades (Green) Tier 1 Purchase 4",
         "System Upgrades (Green) Tier 1 Purchase 5",
         "System Upgrades (Green) Tier 1 Purchase 6",
         "System Upgrades (Green) Tier 1 Purchase 7",
         "System Upgrades (Green) Tier 1 Purchase 8",
         "System Upgrades (Green) Tier 1 Purchase 9"]
    )

    system_upgrades_green_tier_2_locations = get_location_names_with_ids(
        ["System Upgrades (Green) Tier 2 Purchase 1",
         "System Upgrades (Green) Tier 2 Purchase 2",
         "System Upgrades (Green) Tier 2 Purchase 3",
         "System Upgrades (Green) Tier 2 Purchase 4",
         "System Upgrades (Green) Tier 2 Purchase 5",
         "System Upgrades (Green) Tier 2 Purchase 6",
         "System Upgrades (Green) Tier 2 Purchase 7",
         "System Upgrades (Green) Tier 2 Purchase 8"]
    )

    system_upgrades_green_tier_3_locations = get_location_names_with_ids(
        ["System Upgrades (Green) Tier 3 Purchase 1",
         "System Upgrades (Green) Tier 3 Purchase 2",
         "System Upgrades (Green) Tier 3 Purchase 3",
         "System Upgrades (Green) Tier 3 Purchase 4",
         "System Upgrades (Green) Tier 3 Purchase 5",
         "System Upgrades (Green) Tier 3 Purchase 6",
         "System Upgrades (Green) Tier 3 Purchase 7",
         "System Upgrades (Green) Tier 3 Purchase 8",
         "System Upgrades (Green) Tier 3 Purchase 9"]
    )


    system_upgrades_green_tier_1.add_locations(system_upgrades_green_tier_1_locations, RailRouteLocation)
    system_upgrades_green_tier_2.add_locations(system_upgrades_green_tier_2_locations, RailRouteLocation)
    system_upgrades_green_tier_3.add_locations(system_upgrades_green_tier_3_locations, RailRouteLocation)

#   Score check locations

    green_xp_locations = get_location_names_with_ids(["Earn 8 Green XP"])

    menu.add_locations(green_xp_locations, RailRouteLocation)


#   Red train system upgrades
    if world.options.red_trains:
        system_upgrades_red_tier_1 = world.get_region("Tier 1 System Upgrades (Red)")
        system_upgrades_red_tier_2 = world.get_region("Tier 2 System Upgrades (Red)")
        system_upgrades_red_tier_3 = world.get_region("Tier 3 System Upgrades (Red)")

        system_upgrades_red_tier_1_locations = get_location_names_with_ids(
            ["System Upgrades (Red) Tier 1 Purchase 1",
             "System Upgrades (Red) Tier 1 Purchase 2",
             "System Upgrades (Red) Tier 1 Purchase 3",
             "System Upgrades (Red) Tier 1 Purchase 4"]
        )

        system_upgrades_red_tier_2_locations = get_location_names_with_ids(
            ["System Upgrades (Red) Tier 2 Purchase 1",
             "System Upgrades (Red) Tier 2 Purchase 2",
             "System Upgrades (Red) Tier 2 Purchase 3",
             "System Upgrades (Red) Tier 2 Purchase 4",
             "System Upgrades (Red) Tier 2 Purchase 5"]
        )

        system_upgrades_red_tier_3_locations = get_location_names_with_ids(
            ["System Upgrades (Red) Tier 3 Purchase 1",
             "System Upgrades (Red) Tier 3 Purchase 2"]
        )

        system_upgrades_red_tier_1.add_locations(system_upgrades_red_tier_1_locations, RailRouteLocation)
        system_upgrades_red_tier_2.add_locations(system_upgrades_red_tier_2_locations, RailRouteLocation)
        system_upgrades_red_tier_3.add_locations(system_upgrades_red_tier_3_locations, RailRouteLocation)




def create_events(world: RailRouteWorld) -> None:
    # Sometimes, the player may perform in-game actions that allow them to progress which are not related to Items.
    # In our case, the player must press a button in the top left room to open the final boss door.
    # AP has something for this purpose: "Event locations" and "Event items".
    # An event location is no different than a regular location, except it has the address "None".
    # It is treated during generation like any other location, but then it is discarded.
    # This location cannot be "sent" and its item cannot be "received", but the item can be used in logic rules.
    # Since we are creating more locations and adding them to regions, we need to grab those regions again first.
    top_left_room = world.get_region("Top Left Room")
    final_boss_room = world.get_region("Final Boss Room")

    # One way to create an event is simply to use one of the normal methods of creating a location.
    button_in_top_left_room = RailRouteLocation(world.player, "Top Left Room Button", None, top_left_room)
    top_left_room.locations.append(button_in_top_left_room)

    # We then need to put an event item onto the location.
    # An event item is an item whose code is "None" (same as the event location's address),
    # and whose classification is "progression". Item creation will be discussed more in items.py.
    # Note: Usually, items are created in world.create_items(), which for us happens in items.py.
    # However, when the location of an item is known ahead of time (as is the case with an event location/item pair),
    # it is common practice to create the item when creating the location.
    # Since locations also have to be finalized after world.create_regions(), which runs before world.create_items(),
    # we'll create both the event location and the event item in our locations.py code.
    button_item = items.RailRouteItem("Top Left Room Button Pressed", ItemClassification.progression, None, world.player)
    button_in_top_left_room.place_locked_item(button_item)

    # A way simpler way to do create an event location/item pair is by using the region.create_event helper.
    # Luckily, we have another event we want to create: The Victory event.
    # We will use this event to track whether the player can win the game.
    # The Victory event is a completely optional abstraction - This will be discussed more in set_rules().
    final_boss_room.add_event(
        "Final Boss Defeated", "Victory", location_type=RailRouteLocation, item_type=items.RailRouteItem
    )

    # If you create all your regions and locations line-by-line like this,
    # the length of your create_regions might get out of hand.
    # Many worlds use more data-driven approaches using dataclasses or NamedTuples.
    # However, it is worth understanding how the actual creation of regions and locations works,
    # That way, we're not just mindlessly copy-pasting! :)
