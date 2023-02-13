# todomvc-python-playwright
To Do MVC is a popular frontend developer repeat problem for trying out frontend technologies and as such provides nice set of baseline tests (in javascript + mocha + selenium). This project is about exploring the application with different set of test tools, namely python + pytest + playwright. 

Site with various implementations: https://todomvc.com 

Primary test target - vanilla JS https://todomvc.com/examples/vanillajs/

Claims collection as titles of tests at https://github.com/tastejs/todomvc/tree/master/tests

`
 No Todos
        ✓ should hide #main and #footer
      New Todo
        ✓ should allow me to add todo items
        ✓ should clear text input field when an item is added 
        ✓ should trim text input
        ✓ should show #main and #footer when items added
      Mark all as completed
        ✓ should allow me to mark all items as completed
        ✓ should allow me to clear the completion state of all items 
        ✓ complete all checkbox should update state when items are completed 
      Item
        ✓ should allow me to mark items as complete
        ✓ should allow me to un-mark items as complete
        ✓ should allow me to edit an item 
        ✓ should show the remove button on hover
      Editing
        ✓ should hide other controls when editing 
        ✓ should save edits on enter 
        ✓ should save edits on blur 
        ✓ should trim entered text
        ✓ should remove the item if an empty text string was entered
        ✓ should cancel edits on escape 
      Counter
        ✓ should display the current number of todo items
      Clear completed button
        ✓ should display the number of completed items
        ✓ should remove completed items when clicked
        ✓ should be hidden when there are no items that are completed
      Persistence
        ✓ should persist its data
      Routing
        ✓ should allow me to display active items
        ✓ should allow me to display completed items
        ✓ should allow me to display all items
        ✓ should highlight the currently applied filter
`
