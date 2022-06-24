# -*- coding: utf-8 -*-
# create a function to extract IP addresses from a file and place inside a new file

import re
import pandas as pd

def extract_IP_address(file):
    
    # open and read file into separate lines
    
    with open(file) as fh:
        fstring = fh.read().splitlines()
        
    # create string pattern to be identifed - 00.00.0000.00
        
    pattern = re.compile(r'(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})')
    
    # create list for valid and invalid string patterns
    
    valid = []
    invalid = []
    
    #for loop to search through lines for string patterna and append into list
    
    for line in fstring:
        line = line.rstrip()
        result = pattern.search(line)
        
        if result:
            valid.append(line)
        else:
            invalid.append(line)
            
    # create dataframe of new valid list containing IP addresses
            
    df = pd.DataFrame(valid, columns = ['IP Addresses'])
    
    # export to new file
    
    df.to_csv('IP_addresses.csv', sep = ',', index = False)
