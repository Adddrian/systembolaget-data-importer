#!/bin/bash


wget -O data.xml https://www.systembolaget.se/api/assortment/products/xml


python3 systembolaget-parser.py
