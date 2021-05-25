# AirBnB_clone -The Console-

Anthony Armour and Jay Calhoun's submission for project AirBnb_clone - The Console

## General info

The console is a devolper interface for the AirBnB_clone storage engines

## Usability

Our AirBnB console has currently all of the following commands implemented:

  * `create` creates an instance of the input class
  * `EOF` ctrl+d terminates the HBNBCommand loop
  * `quit` terminates the HBNBCommand loop
  * `show` prints the string representaion of input object
  * `destroy` deletes the input object
  * `all` prints the string representation of all instances
  * `update` updates an instance based on class name and id
## Usage

Enter the console module through the AirBnB-clone package:
```
python3 console.py
```
Then you are free to use any of the above useable commands as shown below:

```
(hbnb) [COMMAND] [ARGUMENTS]
```
## Methods and Arguments

### Methods

  * [class_name.destroy(id)]
  	* deletes the input object
  * [class_name.show(id)]
  	* prints the string representation of an input object
  * [class_name.count()]
  	* prints the number of instances of an input class
  * [class_name.all()]
  	* prints the string representation of all instances
  * [class_name.update(id, (attribute name, attribute value) or (object dictionary))]
  	* updates an instance based on class name and id

### Arguments

* id
  * unique identity attribute for all instances
* class_name
  * class name of input object
* attribute_name
  * name of attribute to change for input object
* attribute_value
  * value to set at input object's input attribute
* object_dictionary
  * object dictionary representing attribute names and values
  	* EXAMPLE: {attribute_name: attribute_value}