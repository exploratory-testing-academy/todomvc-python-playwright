# todomvc-python-playwright
To Do MVC is a popular frontend developer repeat problem for trying out frontend technologies and as such provides nice set of baseline tests (in javascript + mocha + selenium). This project is about exploring the application with different set of test tools, namely python + pytest + playwright. 

Site with various implementations: https://todomvc.com 

Claims collection as titles of tests 

´´´
 No Todos
        ✓ should hide #main and #footer (201ms)
      New Todo
        ✓ should allow me to add todo items (548ms)
        ✓ should clear text input field when an item is added (306ms)
        ✓ should trim text input (569ms)
        ✓ should show #main and #footer when items added (405ms)
      Mark all as completed
        ✓ should allow me to mark all items as completed (1040ms)
        ✓ should allow me to clear the completion state of all items (1014ms)
        ✓ complete all checkbox should update state when items are completed (1413ms)
      Item
        ✓ should allow me to mark items as complete (843ms)
        ✓ should allow me to un-mark items as complete (978ms)
        ✓ should allow me to edit an item (1155ms)
        ✓ should show the remove button on hover
      Editing
        ✓ should hide other controls when editing (718ms)
        ✓ should save edits on enter (1093ms)
        ✓ should save edits on blur (1256ms)
        ✓ should trim entered text (1163ms)
        ✓ should remove the item if an empty text string was entered (1033ms)
        ✓ should cancel edits on escape (1115ms)
      Counter
        ✓ should display the current number of todo items (462ms)
      Clear completed button
        ✓ should display the number of completed items (873ms)
        ✓ should remove completed items when clicked (898ms)
        ✓ should be hidden when there are no items that are completed (893ms)
      Persistence
        ✓ should persist its data (3832ms)
      Routing
        ✓ should allow me to display active items (871ms)
        ✓ should allow me to display completed items (960ms)
        ✓ should allow me to display all items (1192ms)
        ✓ should highlight the currently applied filter (1095ms)
´´´
