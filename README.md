# Christmas Shopping List Manager


## Description

Christmas shopping List Manager is a script to assist with Christmas shopping and keeping up with gifts. Do you have multiple kids? Can't remember everything they want? Christmas Shopping List Manager will help you manage and maintain everything you need for Christmas. 

## Source Files

christmas_shopping_list.py

## How to use

There are four main requirements of the Christmas Shopping List. 
    *You need to add gifts and who they are for.
    *You need to be able to mark purchased on the gift.
    *You need to be able to remove gifts from the list
    *You need to be able to view the list.

You can use -h for assistance and explain the options on how to use as well. Every gift that is added is given a gift ID which you will see when you list out gifts. You will be able to use these IDs to mark purchased or remove from list.

To ADD a gift you will simply type the below
python christmas_shopping_list.py -a "gift" and who its for "name".
Example - python christmas_shopping_list.py -a "Lego Set" "Brian"

To MARK your gift as purchased.
Example - python christmas_shopping_list.py -m "gift ID" 

To REMOVE gift from your list.
Example - python christmas_shopping_list.py -r "gift ID"

To VIEW list.
Example - python christmas_shopping_list.py -l