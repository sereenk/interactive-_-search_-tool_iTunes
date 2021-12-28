# Interactive Search Tool - iTunes API

![20200831204212_How-to-Stop-iTunes-from-Opening-Automatically-in-Windows-10](https://user-images.githubusercontent.com/59630489/147601881-a74403f3-d51f-44f2-ada9-4bc6064db581.jpeg)

In this project, I created an interactive search interface program that searches the iTunes store using the iTunes search API and creates a list of objects from the data retrieved. The output will show songs, movies and other media with respect to what the user searched.

## ABOUT THE ITUNES API:

The Search API allows you to search for content within the iTunes Store, App Store, iBooks Store, and the App Store. You can search for a variety of content; including applications, iBooks, movies, podcasts, music, music videos, audiobooks, and TV shows. For more information on the API, check it out on their website.

## PROGRAM BEHAVIORS:

The program will prompt the user to enter a search term, or type 'exit' to quit. The user enters a term, eg. "Dua Lipa". 
The program retrieves the specific data using the API,  converts it to a json object. It parses through the json to create an iTunes list of all media types information with respect to the relevant data.
The program then parses through the iTunes list (using classes) containing different data structures and data types and sorts it into three different objects - Songs, Movies, and Other Media.  
The program will then display Songs, Movies and Other Media related to the users' search term (Eg.  'Dua Lipa').

## SAMPLE OUTPUT


<img width="504" alt="iTunes_interactive_search_sample_output" src="https://user-images.githubusercontent.com/59630489/147602617-34256e0b-31c5-4e96-8931-f31f90239b5c.png">
