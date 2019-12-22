# Practice Project: Automate the Boring Stuff ch 5
# Building a fantasy inventory

# given sample inventory
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

# Inventory display function
def displayInventory(inventory):
    print('Inventory:')
    item_total = 0  # running total of items
    for k, v in inventory.items():
        print(str(v) + " " + str(k))
        item_total += v
    print("Total number of items: " + str(item_total))

displayInventory(stuff) # test run

# inventory addition function
def addToInventory(inventory, addedItems):
    # Code here
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] += 1
        else:
            inventory[i] = 1
    return(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

