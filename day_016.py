#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 15:50:19 2021

@author: juju
"""

'''import turtle

timmy = turtle.Turtle()
timmy.color("coral")
timmy.shape("turtle")
timmy.forward(100)'''

from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Locations", ["New York", "Palo Alto", "Berkeley"])
table.add_column("Year", ["2014", "2018", "2020"])
table.align = 'l'
print(table)