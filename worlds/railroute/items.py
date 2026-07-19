from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Item, ItemClassification

if TYPE_CHECKING:
    from .world import RailRouteWorld

# Every item must have a unique integer ID associated with it.
# We will have a lookup from item name to ID here that, in world.py, we will import and bind to the world class.
# Even if an item doesn't exist on specific options, it must be present in this lookup.

#these ids are sorta arbitrary rn? idk
ITEM_NAME_TO_ID = {
    "Autoblocks": 1010001,
    "Auto-accept Trains": 1010002,
    "Automatic Routing": 1010003,
    "Auto-reverse Trains": 1010004,
    "Manual Signal Route Preview": 1010005,
    "Signaling Safety": 1010006,
    "Platform Adjustments": 1010007,
    "Train Alerts": 1010009,

    "Intercity Contracts": 1020002,
    "Timetable Adjustments": 1020003,
    "Routing Queue": 1020004,
    "Departure Sensor": 1020005,
    "Arrival Sensor": 1020006,

    "Routing Sensor": 1030001,
    "Structural Contracts Manager": 1030002,
    "Financial Contracts Manager": 1030003,
    "Regional Contracts Manager": 1030004,
    "Faster Switches": 1030005,

    "Freights": 1040001,
    "Regional Trains": 1040002,
    "Shunting Commands": 1040003,
    "Shunting Tracks": 1040004,

    "Stabling Sensor": 1050001,
    "Urban Transit Contracts": 1050002,
    "Tunnels": 1050004,
    "Advanced Arrival Sensor": 1050005,

    "Regional Trains Stabling": 1060001,
    "Advanced Routing Sensor": 1060002,

    "Progressive Track Speed": 201,
    "Progressive Station Cap": 202,
    "Progressive Platform Cap": 203,
    "Progressive Contract Offers": 204,

    "System Upgrades (Green) Tier 1 Unlock": 101,
    "System Upgrades (Green) Tier 2 Unlock": 102,
    "System Upgrades (Green) Tier 3 Unlock": 103,
    "System Upgrades (Red) Tier 1 Unlock": 111,
    "System Upgrades (Red) Tier 2 Unlock": 112,
    "System Upgrades (Red) Tier 3 Unlock": 113,

    "Bonus Star": 5,
    "Money": 6

}

# Items should have a defined default classification.
# In our case, we will make a dictionary from item name to classification.
DEFAULT_ITEM_CLASSIFICATIONS = {
    "Autoblocks": ItemClassification.progression,
    "Auto-accept Trains": ItemClassification.useful,
    "Automatic Routing": ItemClassification.progression,
    "Auto-reverse Trains": ItemClassification.useful,
    "Manual Signal Route Preview": ItemClassification.useful,
    "Signaling Safety": ItemClassification.useful,
    "Platform Adjustments": ItemClassification.useful,
    "Train Alerts": ItemClassification.useful,

    "Intercity Contracts": ItemClassification.progression,
    "Timetable Adjustments": ItemClassification.useful,
    "Routing Queue": ItemClassification.useful,
    "Departure Sensor": ItemClassification.useful,
    "Arrival Sensor": ItemClassification.useful,

    "Routing Sensor": ItemClassification.useful,
    "Structural Contracts Manager": ItemClassification.useful,
    "Financial Contracts Manager": ItemClassification.useful,
    "Regional Contracts Manager": ItemClassification.useful,
    "Faster Switches": ItemClassification.useful,

    "Freights": ItemClassification.progression,
    "Regional Trains": ItemClassification.progression,
    "Shunting Commands": ItemClassification.useful,
    "Shunting Tracks": ItemClassification.useful,

    "Stabling Sensor": ItemClassification.useful,
    "Urban Transit Contracts": ItemClassification.progression,
    "Tunnels": ItemClassification.progression,
    "Advanced Arrival Sensor": ItemClassification.useful,

    "Regional Trains Stabling": ItemClassification.useful,
    "Advanced Routing Sensor": ItemClassification.useful,

    "Progressive Track Speed": ItemClassification.progression | ItemClassification.useful,
    "Progressive Station Cap": ItemClassification.progression,
    "Progressive Platform Cap": ItemClassification.progression,
    "Progressive Contract Offers": ItemClassification.progression,

    "System Upgrades (Green) Tier 1 Unlock": ItemClassification.progression,
    "System Upgrades (Green) Tier 2 Unlock": ItemClassification.progression,
    "System Upgrades (Green) Tier 3 Unlock": ItemClassification.progression,
    "System Upgrades (Red) Tier 1 Unlock": ItemClassification.progression,
    "System Upgrades (Red) Tier 2 Unlock": ItemClassification.progression,
    "System Upgrades (Red) Tier 3 Unlock": ItemClassification.progression,

    "Bonus Star": ItemClassification.useful | ItemClassification.filler,
    "Money": ItemClassification.filler,
}


# Each Item instance must correctly report the "game" it belongs to.
# To make this simple, it is common practice to subclass the basic Item class and override the "game" field.
class RailRouteItem(Item):
    game = "Rail Route"


# Ontop of our regular itempool, our world must be able to create arbitrary amounts of filler as requested by core.
# To do this, it must define a function called world.get_filler_item_name(), which we will define in world.py later.
# For now, let's make a function that returns the name of a random filler item here in items.py.
def get_random_filler_item_name(world: RailRouteWorld) -> str:

    return "Money"


def create_item_with_correct_classification(world: RailRouteWorld, name: str) -> RailRouteItem:
    # Our world class must have a create_item() function that can create any of our items by name at any time.
    # So, we make this helper function that creates the item by name with the correct classification.
    # Note: This function's content could just be the contents of world.create_item in world.py directly,
    # but it seemed nicer to have it in its own function over here in items.py.
    classification = DEFAULT_ITEM_CLASSIFICATIONS[name]

    # It is perfectly normal and valid for an item's classification to differ based on the player's options.
    # In our case, Health Upgrades are only relevant to logic (and thus labeled as "progression") in hard mode.
    #if name == "Health Upgrade" and world.options.hard_mode:
    #    classification = ItemClassification.progression

    return RailRouteItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


# With those two helper functions defined, let's now get to actually creating and submitting our itempool.
def create_all_items(world: RailRouteWorld) -> None:
    # This is the function in which we will create all the items that this world submits to the multiworld item pool.
    # There must be exactly as many items as there are locations.
    # In our case, there are either six or seven locations.
    # We must make sure that when there are six locations, there are six items,
    # and when there are seven locations, there are seven items.

    # Creating items should generally be done via the world's create_item method.
    # First, we create a list containing all the items that always exist.

    itempool: list[Item] = [
        world.create_item("Autoblocks"),
        world.create_item("Auto-accept Trains"),
        world.create_item("Automatic Routing"),
        world.create_item("Auto-reverse Trains"),
        world.create_item("Manual Signal Route Preview"),
        world.create_item("Signaling Safety"),
        world.create_item("Platform Adjustments"),
        world.create_item("Train Alerts"),

        world.create_item("Intercity Contracts"),
        world.create_item("Timetable Adjustments"),
        world.create_item("Routing Queue"),
        world.create_item("Departure Sensor"),
        world.create_item("Arrival Sensor"),

        world.create_item("Routing Sensor"),
        world.create_item("Structural Contracts Manager"),
        world.create_item("Financial Contracts Manager"),
        world.create_item("Regional Contracts Manager"),
        world.create_item("Faster Switches"),

        world.create_item("Progressive Track Speed"),
        world.create_item("Progressive Station Cap"),
        world.create_item("Progressive Platform Cap"),
        world.create_item("Progressive Contract Offers"),

        world.create_item("Bonus Star"),
        world.create_item("Money")
    ]

    if world.options.red_trains:
        itempool.append(world.create_item("Freights"))
        itempool.append(world.create_item("Regional Trains"))
        itempool.append(world.create_item("Shunting Commands"))
        itempool.append(world.create_item("Shunting Tracks"))

        itempool.append(world.create_item("Stabling Sensor"))
        itempool.append(world.create_item("Urban Transit Contracts"))
        itempool.append(world.create_item("Tunnels"))
        itempool.append(world.create_item("Advanced Arrival Sensor"))

        itempool.append(world.create_item("Regional Trains Stabling"))
        itempool.append(world.create_item("Advanced Routing Sensor"))

    if world.options.system_upgrades_locked_behind_keys:
        itempool.append(world.create_item("System Upgrades (Green) Tier 1 Unlock"))
        itempool.append(world.create_item("System Upgrades (Green) Tier 2 Unlock"))
        itempool.append(world.create_item("System Upgrades (Green) Tier 3 Unlock"))

        if world.options.red_trains:
            itempool.append(world.create_item("System Upgrades (Red) Tier 1 Unlock"))
            itempool.append(world.create_item("System Upgrades (Red) Tier 2 Unlock"))
            itempool.append(world.create_item("System Upgrades (Red) Tier 3 Unlock"))

    # Archipelago requires that each world submits as many locations as it submits items.
    # This is where we can use our filler and trap items.
    # APQuest has two of these: The Confetti Cannon and the Math Trap.
    # (Unfortunately, Archipelago is a bit ambiguous about its terminology here:
    #  "filler" is an ItemClassification separate from "trap", but in a lot of its functions,
    #  Archipelago will use "filler" to just mean "an additional item created to fill out the itempool".
    #  "Filler" in this sense can technically have any ItemClassification,
    #  but most commonly ItemClassification.filler or ItemClassification.trap.
    #  Starting here, the word "filler" will be used to collectively refer to APQuest's Confetti Cannon and Math Trap,
    #  which are ItemClassification.filler and ItemClassification.trap respectively.)
    # Creating filler items works the same as any other item. But there is a question:
    # How many filler items do we actually need to create?
    # In regions.py, we created either six or seven locations depending on the "extra_starting_chest" option.
    # In this function, we have created five or six items depending on whether the "hammer" option is enabled.
    # We *could* have a really complicated if-else tree checking the options again, but there is a better way.
    # We can compare the size of our itempool so far to the number of locations in our world.

    # The length of our itempool is easy to determine, since we have it as a list.
    number_of_items = len(itempool)

    # The number of locations is also easy to determine, but we have to be careful.
    # Just calling len(world.get_locations()) would report an incorrect number, because of our *event locations*.
    # What we actually want is the number of *unfilled* locations. Luckily, there is a helper method for this:
    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))

    # Now, we just subtract the number of items from the number of locations to get the number of empty item slots.
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items

    # Finally, we create that many filler items and add them to the itempool.
    # To create our filler, we could just use world.create_item("Confetti Cannon").
    # But there is an alternative that works even better for most worlds, including APQuest.
    # As discussed above, our world must have a get_filler_item_name() function defined,
    # which must return the name of an infinitely repeatable filler item.
    # Defining this function enables the use of a helper function called world.create_filler().
    # You can just use this function directly to create as many filler items as you need to complete your itempool.
    itempool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    # But... is that the right option for your game? Let's explore that.
    # For some games, the concepts of "regular itempool filler" and "additionally created filler" are different.
    # These games might want / require specific amounts of specific filler items in their regular pool.
    # To achieve this, they will have to intentionally create the correct quantities using world.create_item().
    # They may still use world.create_filler() to fill up the rest of their itempool with "repeatable filler",
    # after creating their "specific quantity" filler and still having room left over.

    # But there are many other games which *only* have infinitely repeatable filler items.
    # They don't care about specific amounts of specific filler items, instead only caring about the proportions.
    # In this case, world.create_filler() can just be used for the entire filler itempool.
    # APQuest is one of these games:
    # Regardless of whether it's filler for the regular itempool or additional filler for item links / etc.,
    # we always just want a Confetti Cannon or a Math Trap depending on the "trap_chance" option.
    # We defined this behavior in our get_random_filler_item_name() function, which in world.py,
    # we'll bind to world.get_filler_item_name(). So, we can just use world.create_filler() for all of our filler.

    # Anyway. With our world's itempool finalized, we now need to submit it to the multiworld itempool.
    # This is how the generator actually knows about the existence of our items.
    world.multiworld.itempool += itempool

    # Sometimes, you might want the player to start with certain items already in their inventory.
    # These items are called "precollected items".
    # They will be sent as soon as they connect for the first time (depending on your client's item handling flag).
    # Players can add precollected items themselves via the generic "start_inventory" option.
    # If you want to add your own precollected items, you can do so via world.push_precollected().
    #if world.options.start_with_one_confetti_cannon:
        # We're adding a filler item, but you can also add progression items to the player's precollected inventory.
        #starting_confetti_cannon = world.create_item("Confetti Cannon")
        #world.push_precollected(starting_confetti_cannon)
