Command Line Checkbook Application
You will be creating a command line checkbook application that allows users to track their finances with a command line interface.

When run, the application should welcome the user, and prompt them for an action to take:

view current balance
add a debit (withdrawal)
add a credit (deposit)
exit
The application should persist between times that it is run, that is, if you run the application, add some credits, exit the application and run it again, you should still see the balance that you previously created. In order to do this, your application will need to store it's data in a text file. Consider creating a file where each line in the file represents a single transaction.

Here is an example of what using the program might look like:


    $ python checkbook.py

    ~~~ Welcome to your terminal checkbook! ~~~

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 5
    Invalid choice: 5

    Your choice? 1

    Your current balance is $100.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 2

    How much is the debit? $50

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 1

    Your current balance is $50.00.

    What would you like to do?

    1) view current balance
    2) record a debit (withdraw)
    3) record a credit (deposit)
    4) exit

    Your choice? 4

    Thanks, have a great day!
