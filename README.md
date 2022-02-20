# Bookstore-Inventory-with-design-patterns

1. This is an in-memory database for a bookstore inventory. The bookstore story sells
books. Each book has a name, price, unique id and a quantity. The store uses sequential
integers for unique ids. Features:
• Add new books.
• Sell a book in the inventory.
• Add new copies of existing books
• Change the price of a book
• Find the price and/or quantity of a book by either name or id.

2. The inventory class keeps track of the store inventory but it is not persistent. Once the program stops running all data is lost

3. Hence we use momento pattern to copy the data in an Inventory object. The memento is serializable so it can be saved in a file. Given an Inventory object and a memento we can restore the Inventory object to a previous state. Given that a program may have many references to the Inventory object we can't just replace the Inventory object with the memento.


4. So now we can periodically create and save a memento of the Inventory object. But the memento can become rather large. (Inventory is just an example. If we were doing this for real our data could be 100's of megabytes.) So we would not want to save it after each operation.

5. For each operation that changes the state of the Inventory object create a command. The commands are made serializable. Keep in mind that we don't want to serialize the Inventory object each time we serialize a command. Also when we deserialize a command object we will have it operation on the Inventory object that is in-memory, which is likely not to be the same Inventory object that the command first operated on.

6. Now every time we perform an operation on an Inventory object, we can create a command, perform the command and save the command to disk. This way we will have a history of all the operations. If our program were to crash we can recover the last state by first loading the last memento and then replaying all the commands done since the last memento was created. 

7. Since the commands will always be small, which is not the case with the Inventory object, saving it to disk each time will not be very expensive. After a while the number of commands may get very large. When this happens one can create a new memento, save it to disk and remove the old commands. Of course this needs to be done in a safe manner. We make sure that the new memento is saved on disk before removing the old one and removing the old commands.

8. A decorator is created for Inventory objects. For every operation that changes the Inventory object's state the decorator will create the command, perform the command and save the command to a file.

# Design Patterns Used:
1. Momento Pattern
2. Decorator Pattern
3. Command Pattern