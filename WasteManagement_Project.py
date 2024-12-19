#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Data Science Project Submission
Group Members: Dalia and Vidushi
Date: April 2nd, 2024
Purpose of the program:
Compare waste, recycling, and energy data in Singapore
"""

import csv 
import numpy as np
import matplotlib.pyplot as plt 
filename ="waste_2003_2017.csv"

# READING THE DATA
def read_file(filename):
    """
    defining a function for reading the file
    Parameters
    ----------
    filename : string
        the string "2003_2017_waste.csv" contains the file from which we are 
        reading data from

    Returns 
    -------
    dictionary : dictionary
    creating a dictionary where key is the column header
    and value is the column's list of values  
    """
    with open(filename, "r") as file: 
        # using csv reader to read the file 
        file_data = csv.reader(file) 
        # initializing a dictionary and data list
        dictionary = {} 
        data = [] 
        
        for lst in file_data:
            new_list = []
            for element in lst:
                # checking if data contains digits 
                if element.isdigit():
                    # converting them into integers
                   element = float(element)
                    
                # adding new elements to the list
                new_list.append(element)
            data.append(new_list)
        # defining header row in data 
        header = data[0]
        # creating a dictionary where key is the column header
        # and value is the column's list of values 
        for i in range(len(header)):
            dictionary[header[i]] = []
            for row in data[1:]:
                dictionary[header[i]].append(row[i])
    return dictionary

# PRODUCING 1ST VISUALIZATION

def wastecategory_graph(dictionary):
    """
    defining a function for plotting a stacked bar graph that depicts proportion of waste
    that has been generated, and thereafter recycled for each category of waste
    
    Parameters
    ----------
    dictionary : dictionary
    
    Returns 
    -------
    waste2016.png: plotted graph 
    """
    # defining dataset for waste categories for x-axis 
    waste_type_axis = dictionary["waste_type"][197:209]
    # defining datasets for waste generated and recycled
    generated_axis = dictionary["total_waste_generated_tonne"][197:209]
    recycled_axis = dictionary["total_waste_recycled_tonne"][197:209]
    # plotting "total generated waste"
    plt.bar(waste_type_axis, generated_axis, label='total generated', color = 'skyblue')
    # plotting "total recycled waste"
    plt.bar(waste_type_axis, recycled_axis, label ='total recycled', color = 'orange', bottom = generated_axis)
    # labelling and adjusting the graph
    plt.title("waste generated from each category in 2016")
    plt.ylabel("amount of waste (tons)")
    plt.xlabel("waste category")
    plt.legend()
    plt.xticks(rotation=90)
    plt.show()
    plt.savefig("waste2016.png", bbox_inches = "tight")




# PRODUCING 2ND VISUALIZATION

def recyclingrates_graph(dictionary):
    """
    defining a function for plotting a line plot that depicts recycling rates 
    for 5 different waste categories every year
    
    Parameters
    ----------
    dictionary : dictionary
    
    Returns 
    -------
    wasterecyclingrates.png: plotted graph 
    """
    
    for i in range(len(dictionary["recycling_rate"])):
        dictionary["recycling_rate"][i] = float(dictionary["recycling_rate"][i])
    # creating a dictionary for collecting data regarding glass waste's
    # recycling rates per year
    # the dictionary contains 3 keys for storing waste type, recycling rate and year values
    glass_dict = {"waste_type":[], "recycling_rate":[], "year":[]} 
    # adding values to each key in the dictionary 
    for i in range(len(dictionary["waste_type"])):
        if dictionary["waste_type"][i] == "Glass":
            glass_dict["waste_type"]+= [dictionary["waste_type"][i]]
            glass_dict["recycling_rate"] += [dictionary["recycling_rate"][i]]
            glass_dict["year"] += [dictionary["year"][i]]
            
    # plotting and labelling a line plot with the recycling rate and year
    plt.plot(glass_dict["year"], glass_dict['recycling_rate'], color = 'blue', label = "glass")
    
    # creating a dictionary for collecting data regarding plastic waste's
    # recycling rates per year
    # the dictionary contains 3 keys for storing waste type, recycling rate and year values
    plastics_dict = {"waste_type":[], "recycling_rate":[], "year":[]} 
    # adding values to each key in the dictionary 
    for i in range(len(dictionary["waste_type"])):
        if dictionary["waste_type"][i] == "Plastics":
            plastics_dict["waste_type"]+= [dictionary["waste_type"][i]]
            plastics_dict["recycling_rate"] += [dictionary["recycling_rate"][i]]
            plastics_dict["year"] += [dictionary["year"][i]]
   
    # plotting and labelling a line plot with the recycling rate and year
    plt.plot(plastics_dict["year"], plastics_dict['recycling_rate'], color = 'red', label = "plastic")
    
    # creating a dictionary for collecting data regarding cardboard/paper waste's
    # recycling rates per year
    # the dictionary contains 3 keys for storing waste type, recycling rate and year values
    cardboard_dict = {"waste_type":[], "recycling_rate":[], "year":[]} 
    # adding values to each key in the dictionary 
    for i in range(len(dictionary["waste_type"])):
        if dictionary["waste_type"][i] == "Paper/Cardboard":
            cardboard_dict["waste_type"]+= [dictionary["waste_type"][i]]
            cardboard_dict["recycling_rate"] += [dictionary["recycling_rate"][i]]
            cardboard_dict["year"] += [dictionary["year"][i]]
    # plotting and labelling a scatter plot with the recycling rate and year
    plt.plot(cardboard_dict["year"], cardboard_dict['recycling_rate'], color = 'green', label = "paper/cardboard")
    
    
    ferrous_dict = {"waste_type":[], "recycling_rate":[], "year":[]} 
    # adding values to each key in the dictionary 
    for i in range(len(dictionary["waste_type"])):
        if dictionary["waste_type"][i] == "Ferrous Metals":
            ferrous_dict["waste_type"]+= [dictionary["waste_type"][i]]
            ferrous_dict["recycling_rate"] += [dictionary["recycling_rate"][i]]
            ferrous_dict["year"] += [dictionary["year"][i]]
            
    # plotting and labelling a line plot with the recycling rate and year
    plt.plot(ferrous_dict["year"], ferrous_dict['recycling_rate'], color = 'orange', label = "ferrous metals")
    
    nonferrous_dict = {"waste_type":[], "recycling_rate":[], "year":[]} 
    # adding values to each key in the dictionary 
    for i in range(len(dictionary["waste_type"])):
        if dictionary["waste_type"][i] == "Non-ferrous Metals":
            nonferrous_dict["waste_type"]+= [dictionary["waste_type"][i]]
            nonferrous_dict["recycling_rate"] += [dictionary["recycling_rate"][i]]
            nonferrous_dict["year"] += [dictionary["year"][i]]
            
    # plotting and labelling a line plot with the recycling rate and year
    plt.plot(nonferrous_dict["year"], nonferrous_dict['recycling_rate'], color = 'pink', label = "non-ferrous metals")

    
    # labelling the axes and title for the main plot 
    plt.title("Recycling Rate for Popular Waste Categories Every Year")
    plt.xlabel('Year')
    plt.ylabel('Recycling Rate')
    plt.legend()
    plt.legend(loc= (1.04, 1))
    plt.show()  
    plt.savefig("wasterecyclingrates.png", bbox_inches = "tight")
    
    
def make_waste_dict(dictionary, waste_type):
    """
    defining a function for creating a dictionary containing 3 keys
    to collect values for waste type, calculated energy saved 
    (energy saved per ton recycled * total recycled amount), and year.
    
    
    Parameters
    ----------
    dictionary : dictionary
    waste_type: values that come under "waste_type" column in the dictionary
    
    Returns 
    -------
    energy_dict: dictionary 
    this dictionary contains the calculated energy saved for all given waste types 
    
    """
    
    # creating a dicionary to collect data for values for 3 keys 
    energy_dict = {'waste_type' : waste_type, 'calc_energy': [], 'year': []}
    
    for i in range(len(dictionary['waste_type'])):
        # checking if waste type matches what is given 
        if dictionary['waste_type'][i] == waste_type:
            # calculating energy saved 
            energy_saved = dictionary["total_waste_recycled_tonne"][i] * dictionary["energy_saved_per_ton (kWh)"][i]
            # print energy_saved
            # appending the values for the keys calculated energy and year
            energy_dict['calc_energy'].append(energy_saved)
            energy_dict['year'].append(dictionary['year'][i])
    # print(energy_dict)            
    return energy_dict

# PRODUCING 3RD VISUALIZATION

def plot_waste(list_of_waste):
    """
    defining a function for plotting a 5 category grouped bar graph for energy saved by recycling 
    plastic, paper/cardboard, glass, ferrous and non-ferrous metal from years 2003-2017
    
    Parameters
    ----------
    list_of_waste: this is a list containing the categories of waste 
    we want to plot a graph for 
    
    Returns 
    -------
    energysaved.png: plotted graph 
    """
    # CITATION: for this function, I have received help from TA Jeffrey Pan
    # who helped me with the application for NUMPY in order 
    # to plot this 5 category bar graph
    
    # adjusting the size and width of the figure and bars 
    plt.figure(figsize=(10, 8))
    width = 1/(len(list_of_waste) + 1) 
    
    # iterating through the list and keeping track of the index 
    for i, waste_dict in enumerate(list_of_waste): 
        #print(waste_dict)
        N = len(waste_dict["year"])
        # creating an array of equal intervals for the years on the x-axis 
        ind = np.arange(N) 
        # plotting a grouped bar graph 
        plt.bar(ind + i * width, waste_dict["calc_energy"], width, label= waste_dict["waste_type"])
    
    # labelling and adjusting the graph 
    plt.xlabel("years")
    plt.ylabel("energy saved (in kWh)")
    plt.title("energy saved by recycling from 2003-2016")
    plt.xticks(ind + width * len(list_of_waste) / 2, waste_dict["year"])
    plt.legend(loc= "best")
    plt.xticks(rotation=90)
    plt.show()
    plt.savefig("energysaved.png", bbox_inches = "tight")
    




# calling all my functions         
def main():
         dictionary = read_file("waste_2003_2017.csv")
         #print(dictionary)
        # plotting the first 3 visualizations 
         wastecategory_graph(dictionary)
         recyclingrates_graph(dictionary)
        # creating dictionaries for 5 categories
         plastics = make_waste_dict(dictionary, "Plastics")
         cardboard = make_waste_dict(dictionary, "Paper/Cardboard")
         ferrous = make_waste_dict(dictionary, "Ferrous Metals")
         non_ferrous = make_waste_dict(dictionary, "Non-ferrous Metals")
         glass = make_waste_dict(dictionary, "Glass")
        # creating a list of waste, that will be a parameter for plotting the graph
         list_of_waste = [plastics, cardboard, ferrous, glass, non_ferrous]
        # plotting the 3rd visualization 
         plot_waste(list_of_waste)
       
    
     

    
main()
