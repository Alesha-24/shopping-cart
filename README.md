# Alesha Gulamhusein - OPIM 243: Shopping Cart Project 

## Installation
Use GitHub.com to first fork and then download or 'clone' the project repository onto your computer.  It is helpful to choose an easily accessible download location like the Desktop.  

After cloning the repo you can then use GitHub Desktop Software to access  the project repository or naivagte their using the command-line below:

```sh
 cd ~/Desktop
```

## Environment Set Up

Create and activate a new Anaconda virtual environment:

```sh
conda create -n shopping-env python=3.7 # (first time only)
conda activate shopping-env
```

From within this virtual environment, you can run the Python script from the command-line:

```sh
python shopping_cart.py
```

## Using the Code
You can use this code by entering a product identification number from the specficed inventory list when prompted by the program. If the number entered doesn't exist the program will prompt you to enter a different number. Once you have finished type 'DONE'. Then the program will then automatically calculate the total of all products purchased, including tax. It will then print a receipt with the details of the purchase. 

## Configuring Sales Tax Rates
You can use the ".env" to configure the sales tax rate based on your location. This will then automatically update in the rest of the code.  This feature allows the program to be shared with grocery stores in other states as well. 

## Writing Receipts to File 
In addition to being displayd at the end of the checkout proccess, the program also writes out the receipt sinformation into a new ".txt" file which can be found in the "receipts" directory inside the project repository. Each text file is  named according to the date and time the checkout process started. 