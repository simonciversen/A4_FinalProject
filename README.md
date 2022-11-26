# A4 Usecase, Cost Estimation.

## Changes

* Creating .csv
* More narrow scope, focus moved to foundations, beams, columns, slabs and walls

After discussing our usecase and its applicability in the industry with the two representatives from Niras, we decided that to make our work tool more usefull, we had to create CSVs, where the name, type, quantity and price of each bulding element were displayed. This output will make categorizing the prices easier, and contractors will quickly be able to make calculations and decisions on which parts of the bulding are the largest cost drivers. Another difference in this final product compared to the earlier handed in versions, is that the scope of the work tool is narrower, making it more specific, but also more detailed. This means extracting more infomation from the IFC model, to create more precise cost estimates.

---

## Goal
* To give a cost estimate of the main structural elements of a project at an early design stage.

Eventhough the overall goal of the work tool is still the same as before, because of the changes made, the work tool could be especially helpful in the financial analytics of the contractors building plans. The tool will assist in evaluating where the cost of the main structure has its largest potential of cost cut.  

---

## Description of The Process & Usecase
The BPMN for the usecase states that the bulding information model will be altered, properties from the IFC will be extracted and matched with corresponding price data, and checked if is satisfactory (see diagram below). To be clear, the tool will not on its own check if costs are satisfactory or alter the BIM model, because doing so would depend on the budget of the contracor among other things. The BPMN below describes with what intention the work tool was made. The work tool itself takes part in the extraction of the right information, and the calculations of costs. 

The usecase of the project is primarily for the contractor to visualize for a client where the largest costs lie, and preferably come with alternative methods of reducing the cost after analysis of the output data. The tool will also create a quick way of comparing the the same structure made with different materials, say if a client wants a main structure buildt with CLT instead of conrete. Secondary it would be useful to apply this tool in interactions with subcontractors to see what costs one could expect if a contractor were to outsource parts of the building process, which is rather common.
![Alt text](Images/diagram.svg)

---

## How it works
First part (Extraction)
>
> * Count spesific IFC by name (IfcWall)
> * Extraction of only loadbearing elements
> * Classification description
> * Extracting element properties
>

Second part (Pricing)
>
> * Matching price data with spesific element type
> 

Third part (Output)
>
> * Create .csv for each elements
> 

### Generally
The work tool essentially works in the three different parts described above. The first part consists of is using ```IfcOpenshell``` attributes ```.byType```, ```.ÌsDefinedBy```, ```.RelatingPropertyDefinition``` and ```RelDefinesByProperties``` to extract both the materials, classification descriptions and material quantities required by the MOLIO JSON file. Before the extraction the tool also checks that all elements being extracted are defined as ```LoadBearing = True```, so that as the use case states, we calculate the estimated cost for the main structural elements of the building. In the second part, the work tool will categorize which exact materials and quantitative properties define the specific element, and then link it up to the price fitting that specific description. Lastly the code creates the CSV files, that you could use directly to visualizing costs, and create analysis. 

NB! This code is only an example of how the work tool could be utilized, choosing price data and material properties that make approximate calculations of the cost of each bulding element. The 'total price' calculated from this model will therefore not be realistic or usable as a realistic cost estimate (read 'note'). Each extracted element has spesifically definded properties in the IFC model, and below is a description of how the code  creates the desired output for each elements in the model Duplex_A_20110907.ifc. 

#### Beams:
For the beams in the ifc model the work tool differentiates in both which type of material (Steel or Concrete) and what thickness the beams are. Since the MOLIO price data has a limited number of beams with a spesific descriptions, we have chosen the MOLIO elements that fit the IFC elements the best. 


#### Walls:
When building the code for part one of the walls we encountered some challenges due to the fact that all walls in the IFC model were quite poorly labeled. The biggest issue was that part of the foundation was classified as IfcWallStandardCase, same as all the other walls in the model. To make the work tool usable we worked around this problem by defining walls below ground (```BaseConstrain = T/FDN```) in a certain price class and walls above as another (read 'note'). Another problem with the model was that none of 1. and 2. floor walls were defined as loadbearing even though they were designed to be loadbearing. That makes all the walls extracted from the model part of the external and internal foundation of the structure, eventhough the code is able to perform calculations for walls on all levels. The wall materials are catergorized into three different material categories, which are then categorised into different thicknesses.

#### Slabs:
The model has differentiated between the loadbrearing slabs and the finishes of the model. That being said it has classified all horisontal components realting to the slabs as being loadbearing, meaning such as ceramic floor finishes are also defined as loadbearing. We have taken this into account and only extracted the three structural categorial components present in the model and categorized each material with thickness. 

#### Columns
If the count of each extracted element type is below one, the code will notice and display a message saying there are no 'elements' in the model. Such is the case for columns.

### Visualisation
The .csv files are set up to be easy to use, with all text based descriptopns on the left most columns and the numerical values to the right. This makes it easy to create diagrams and other visualisations of the data, for example CumSum.
A brief example of how the output data could be visualized:

<img width="966" alt="Skjermbilde 2022-11-24 kl  10 49 39" src="https://user-images.githubusercontent.com/113243733/203752402-c1bff2c4-9043-4c74-b6f3-173f1bbe1936.png">

---

# note:
Since the IFC files we have looked at have defined its parameters differently and in different locations, we have made our code to specifically work for the ‘Duplex A’, to illustrate how the work tool should be utilized. This means that making sure materials and structural element properties are defined properly in IFCs would require a code that is simpler, quicker, and useable for any IFC file.

It should also be noted that the price file from MOLIO is an incomplete pricecatalog where all prices are multiplied with a arbritary numbers, and can therefore not be used for realistic calculations of price. Because of this we have chosen the pricing elements which resembles the building elements in the model. 

<img width="279" alt="Skjermbilde 2022-11-24 kl  08 51 44" src="https://user-images.githubusercontent.com/113243733/203727600-963a57d3-9db5-462b-b4b0-6d0ad5dc13fe.png"> <img width="527" alt="Skjermbilde 2022-11-24 kl  09 14 27" src="https://user-images.githubusercontent.com/113243733/203728949-c83c6947-b295-4eaf-b98a-d43e4f1872d3.png">



 
