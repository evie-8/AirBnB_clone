# Airbnb Clone project
![alt text](./airbnb.png)             
## Description
Creating the console / command interpreter for our AirBnB clone
## the HBNB console                                                                                                   
----
Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:

   -Create a new object (ex: a new User or a new Place)  
   -Retrieve an object from a file, a database etc…  
   -Do operations on objects (count, compute stats, etc…)  
   -Update attributes of an object  
   -Destroy an object  
   
## Commands and how to use it                                                                                     
the command interpreter allow us to handle our data requirements with the following commands
                                                                                                                      
| Command | Function | Usage |                                                                                             
| ------- | ------------------------------------ | ---------------------------------------------|
| create | create a new instace of a class | create <class> |
| show | show the info of an instance of a class | show <class> <id> or class.show(id)|
| destroy | destroy a instance of a class | destroy <class> <id> or class.destroy(id)|
| update | update the info of the objects in an instance | update class attr_name attr_val |
| all | update the info of the objects in an instance | all <class> or all or class.all()
| quit | exit the console | Ctrl-D |
| help | show the help of the commands | help <command> |
|count | counts instances of class | class.count() |

## Objects
this is the objects that you can pass to the command console

| Object | Function |                                                                                                
| ------- | -------- |
| city | city of the reservation |
| state | country state of the reservation |
| place | Name of the place of reservation |
| user | Name of the user who reserves|
| amenity | Benefits of the place |
| review | review of the room and the guest |

### Start using the console
start the console with
```./console```
you will see:
```(hbnb)```
and can start to use the hbnb console
## How to use the HBNB console
### Syntax:
``` <command> <classname> <id>```
id don't apply to create command
### For help:
```help <command>```
### Examples:
#### For Help:
```
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb) help create
creating class instances.
         Usage: create <class_name>

```
#### For standard commands:
```
(hbnb) create User
e2635607-8b24-4871-ab83-dcdabd4409b8
```
It will create a new User
``` 
(hbnb) create BaseModel
257be31a-f2cc-4052-9fb4-24308369d002
(hbnb)
 ```
 It will create a new BaseModel and show the objects of the instance
#### show command
Usage <classname>.show(id) or show class_name id
```257be31a-f2cc-4052-9fb4-24308369d002
(hbnb) show User e2635607-8b24-4871-ab83-dcdabd4409b8
[User] (e2635607-8b24-4871-ab83-dcdabd4409b8) {'id': 'e2635607-8b24-4871-ab83-dcdabd4409b8', 'created_at': datetime.datetime(2023, 7, 16, 23, 37, 7, 942810), 'updated_at': datetime.datetime(2023, 7, 16, 23, 37, 7, 942861)}
(hbnb) BaseModel.show(257be31a-f2cc-4052-9fb4-24308369d002)
[BaseModel] (257be31a-f2cc-4052-9fb4-24308369d002) {'id': '257be31a-f2cc-4052-9fb4-24308369d002', 'created_at': datetime.datetime(2023, 7, 16, 23, 37, 53, 61476), 'updated_at': datetime.datetime(2023, 7, 16, 23, 37, 53, 61522)}
(hbnb)
```
#### all command
Usage all <class_name | all | class_name.all()
```
(hbnb) all
["[BaseModel] (a9e6c8d5-571a-4020-be30-6ffdaf1763d5) {'id': 'a9e6c8d5-571a-4020-be30-6ffdaf1763d5', 'created_at': datetime.datetime(2023, 7, 16, 23, 43, 19, 812244), 'updated_at': datetime.datetime(2023, 7, 16, 23, 43, 19, 812303), 'name': 'My_First_Model', 'my_number': 89}"]
```
```
(hbnb) User.all()
["[User] (ff0035fc-f666-47ce-9d2d-ea659304d116) {'id': 'ff0035fc-f666-47ce-9d2d-ea659304d116', 'created_at': datetime.datetime(2023, 7, 16, 23, 43, 24, 582770), 'updated_at': datetime.datetime(2023, 7, 16, 23, 43, 24, 582792), 'first_name': 'Betty', 'last_name': 'Bar', 'email': 'airbnb@mail.com', 'password': 'root'}", "[User] (e47c16ab-9c26-4b00-8ae3-7481117a23e5) {'id': 'e47c16ab-9c26-4b00-8ae3-7481117a23e5', 'created_at': datetime.datetime(2023, 7, 16, 23, 43, 24, 583382), 'updated_at': datetime.datetime(2023, 7, 16, 23, 43, 24, 583398), 'first_name': 'John', 'email': 'airbnb2@mail.com', 'password': 'root'}"]
```
#### count command

```
(hbnb) User.count()
2
```
### destroy command
```
(hbnb) destroy User ff0035fc-f666-47ce-9d2d-ea659304d116
(hbnb) show User ff0035fc-f666-47ce-9d2d-ea659304d116
** no instance found **
```
## Authors
[Franklinson](https://github.com/Franklinson)  
[evie-8](https://github.com/evie-8)
