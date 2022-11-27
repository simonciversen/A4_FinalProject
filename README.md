>
>NB! Input file was too big to upload, remember to unzip before using the work tool.
>
# A4 Use Case: Cost Estimation

## Goal
* To give a cost estimate of the main structural elements of a building project at an early design stage.

---
## Changes from previous assignments

* Creating .csv files as output
* More narrow scope, focus moved to foundations, beams, columns, slabs and walls

After discussing our use case and its applicability in the building industry with the two representatives from Niras, we changed our work-tool to make it more relevant towards the industry aspect. We changed our workflow to create outputs in form of .csv files, where the name, type, price classification, unit price, quantities and total price of each bulding element were displayed. This output will make categorizing the prices easier and allow for a visualization of the price factors. Contractors will quickly be able to display the building cost and see where the largets cost drivers are located.
Another difference in this final product compared to the earlier handed in versions, is that the scope of the work tool is narrower, making it more specific, but also more detailed. This means extracting more infomation from the IFC model, to create more precise cost estimates. We have changed our bpmn diagram for the use case as well, narrowing it down to the actual worktool we have made and ignoring steps outside our scope included in previous assignment. 

---

## Description of Work tool & Use Case

The BPMN diagram demonstrates our work tool. After loading a architectural model we identify all loadbearing elements in the building and extract walls, beams, columns, slabs and footings. We then extract the elements material properties such as length/area/width and classify each element based on these properties. By matching each classified element with a price category from the Molio cost data, the worktool calculates price estimates and exports csv. files for each building element category. 

These cost estimates in the form of csv. files are intended to be used by a contracting firm calculating on a project for a client. By running our work-tool on a architectural model given to them from a client, or a model they have made themselves, they will have a visual representation in form of a spreadsheet with building elements and corresponding prices, as well as plots and graphs displaying where most of the cost for the building is located. This cost information for the building is then intended to be used to make necessary changes based on budget, and give a basis for exploring alternative materials and building layouts.  For example if steel prices have risen recently, and by running the work-tool it becomes clear that steel takes a bigger part of the  budget than expected, the contractor can decide to use a substitute material in the further design process. 
![Alt text](Images/diagram.svg)

---

## How it works
First part: Extraction
>
> * Count specific IFC by name (e.g. IfcWall)
> * Extraction of only loadbearing elements
> * Classification description
> * Extracting element properties
>

Second part: Pricing
>
> * Matching price data with classification description for element types
> 

Third part: Output
>
> * Creating .csv file for each of the elements
> 

### Generally
The work tool essentially works in the three different parts described above. The first part consists of it using ```IfcOpenshell``` attributes ```.byType```, ```.ÌsDefinedBy```, ```.RelatingPropertyDefinition``` and ```RelDefinesByProperties``` to extract both the materials, classification descriptions and material quantities required by the MOLIO JSON file. Before the extraction the tool also checks that all elements being extracted are defined as ```LoadBearing = True```, so that as the use case states, we calculate the estimated cost for the main structural elements of the building. In the second part, the work tool will categorize which exact materials and quantitative properties define the specific element, and then link it up to the price fitting that specific description. Lastly the code creates the .csv files, that you could use directly to visualizing costs, and create analysis. 

NB! This code is only an example of how the work tool could be utilized, choosing price data and material properties that make approximate calculations of the cost of each bulding element. The 'total price' calculated from this model will therefore not be realistic or usable as a realistic cost estimate (read 'note'). Each extracted element has spesifically definded properties in the IFC model, and below is a description of how the code  creates the desired output for each elements in the model Duplex_A_20110907.ifc. 

#### Beams:
For the beams in the IFC model the work tool differentiates in both which type of material and what thickness the beams are. Since the MOLIO price data has a limited number of beams with a spesific descriptions, we have chosen the MOLIO elements that fit the IFC elements the best. 

#### Footings:
Unlike the rest of the IFC elements IfcFooting does not contain the atribute ```LoadBearing = True```. Being that all footings are loadbearing we have assumed this to be true for the 'Duplex A' model aswell. Another assumtpion is that all footings are made from concrete, so the code only differentiates pricing with the thickness.


#### Walls:
When building the extraction part of the code for the walls we encountered some challenges due to the fact that all walls in the IFC model were quite poorly labeled. The biggest issue was that part of the foundation was classified as IfcWallStandardCase, same as all the other walls in the model. To make the work tool usable we worked around this problem by defining walls below ground (```BaseConstrain = T/FDN```) in a certain price class and walls above as in another (read 'note'). Another problem with the model was that none of 1. and 2. floor walls were defined as loadbearing even though they were designed to be loadbearing. That makes all the walls extracted from the model part of the external and internal foundation of the structure, eventhough the code is able to perform calculations for walls on all levels. The wall materials are catergorized into three different material categories, which are then categorised into different thicknesses.

#### Slabs:
The model has differentiated between the loadbearing slabs and the floor finishes in the model. That being said it has classified all horizontal components relating to the slabs as being loadbearing, meaning such as ceramic floor finishes are also defined as loadbearing. We have taken this into account and only shown the three structural categorical components present in the model and differentiated each material with their thickness. 


#### Columns:
If the count of each extracted element type is below one, the code will notice and display a message saying there are no 'elements' in the model. Such is the case for columns.

### Visualization
The .csv files are set up to be easy to use, with all text based descriptions on the left most columns and the numerical values to the right. This makes it easy to create diagrams and other visualisations of the data, for example CumSum.
A brief example of how the output data could be visualized:

<img width="966" alt="Skjermbilde 2022-11-24 kl  10 49 39" src="https://user-images.githubusercontent.com/113243733/203752402-c1bff2c4-9043-4c74-b6f3-173f1bbe1936.png">

---

## What is the business and societal value offered by this tool?

The tool provides value for the business by creating a visualization of the costs associated with the different elements used in the building model by just loading a building model, setting prices for the different element types and material from e.g. Molio price data and running the script. This will allow for the business to quickly see which changes are necessary in regard to budget, and what the cost effect of these changes and modifications will be. The work-tool will make cost estimating much easier than if the contractor where to make these calculations manually, and therefore free resources which again saves them money. 

 By using this work-tool for cost estimation it will as mentioned save the company resources previously used on manually calculating prices, this is resources the company now can use for focusing on other tasks such as waste management and optimizing transportation of material (less Co2). 

---

# note:
Since the IFC files we have looked at have defined its parameters differently and in different locations, we have made our code to specifically work for the ‘Duplex A’, to illustrate how the work tool should be utilized. This means that making sure materials and structural element properties are defined properly in IFCs would require a code that is simpler, quicker, and useable for any IFC file.

It should also be noted that the price file from MOLIO is an incomplete price catalogue where all prices are multiplied with a arbritary numbers, and can therefore not be used for realistic calculations of price. Because of this we have chosen the pricing elements which most resembles the building elements in the model. 

<img width="279" alt="Skjermbilde 2022-11-24 kl  08 51 44" src="https://user-images.githubusercontent.com/113243733/203727600-963a57d3-9db5-462b-b4b0-6d0ad5dc13fe.png"> <img width="527" alt="Skjermbilde 2022-11-24 kl  09 14 27" src="https://user-images.githubusercontent.com/113243733/203728949-c83c6947-b295-4eaf-b98a-d43e4f1872d3.png">



 



 
