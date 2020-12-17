# Boreal (the largely stationary) Caribou
 
Visualising tracking data of Woodland Caribou.

### Table of Contents

 1. Installation
 2. Motivation
 3. File Descriptions
 4. Results
 5. Issues
 6. Licensing, Authors, and Acknowledgements

## 1. Installation

To get this inital code running, you will only need the standard Anaconda distribution of Python 3.

## 2. Motivation

As I try to improve my ability I am looking for tasks that catch my attention. I was interested in finding a suitable way of visualising latitudinal/longitudinal distance data in a simple and clear manner. I haven't tackled this kind of data before so thought what the hell.

The data I've chosen is the Caribou Location Tracking that contains tracking data of 260 woodland caribou from British Columbia, Canada between 1988 and 2016. 

## 3. File Descriptions
Three python files:

CaribouLocation.py : contains main file that reads in data and calculated distance
haversine.py : contains function gcd (great circle distance) for calculating distance between to gps points in radians
row_calculate : contains function to cycle through each animal_id in dataframe and calculate the distance travelled by each

## 4. Results
Will fill this in when I find some :) 

## 5. Issues

None (WooHoo!(for the moment))

## 6. Licenses
I have yet to write this up fully but in the mean time you fancy a gander at the dataset itself you will find it on kaggle [here](https://www.kaggle.com/jessemostipak/caribou-location-tracking?select=locations.csv) along with documentation, licenses etc. for the data

For my incredibly 'valuable' code see below (standard MIT license):

Copyright 2020 Ben Stone

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


