# Changes
* Creating usable CSVs
* More narrow scope,only focus on foundation, beams, columns, slabs and walls

After discussing our usecase and its applicability in the industry with the two representatives from Niras, we decided that to make our work tool more usefull, we had to create CSVs, where the name, type, quantity and price of each bulding element were displayed. This output will make categorizing the prices easier, and contractors will quickly be able to make calculations and decisions on which parts of the bulding are the largest cost drivers. Another difference from this final product and the earlier handed in versions is that the scope of the work tool is narrower, making it more specific, but also more detailed. This means extracting more infomation from the IFC model, to create more precise cost estimates.

# Goal
* To give a cost estimate of the main structural elements of a project at an early design stage.

Eventhough the overall goal of the work tool is still the same as before, because of the changes made, the work tool would be especially helpful in the financial analytics of the contractors building plans. The tool will assist in evaluating where the cost of the main structure has its largest potential of cost cut.  

# Description of The Process & Usecase
The usecase for the tool states that properties from the IFC will be extracted, matched with corresponding price data, and checked if is satisfactory (see diagram below). To be clear, the tool will not on its own check if costs are satisfactory, because doing so depends on the budget of the contracor among other things. The usecase describes with what intention the work tool was made. The work tool on its own takes part in calculating costs, to ensure that the expenses do not exceed the budget. 

![Alt text](Images/diagram.svg)

# How it works
The work tool works in four different part. The first part consists of is using IfcOpenshell attributes  .byType and RelDefinesByProperties to extract both the materials and the material quantities required by the MOLIO JSON file. Before the extraction the tool checks that all elements being extracted are defined as LoadBearing = True, so that as the use case states, we calculate the estimated cost for the main structural elements of the building. The second part is categorizing which materials and quantitative properties define the specific element and the third is linking it up to the price fitting that specific description. Fourth and lastly the code creates the CSV files, that you could use directly to visualizing costs, and create analysis. 
The main difference from this final product and the earlier handed in versions is that the scope of the work tool is narrower, making it more specific, but also more detailed. 

A brief example of how the output data could be visualized:

<img width="966" alt="Skjermbilde 2022-11-24 kl  10 49 39" src="https://user-images.githubusercontent.com/113243733/203752402-c1bff2c4-9043-4c74-b6f3-173f1bbe1936.png">

# note:
Since the IFC files we have looked at have defined its parameters differently and in different locations, we have made our code to specifically work for the ‘Duplex A’, to illustrate how the work tool should be utilized. This means that making sure materials and structural element properties are defined properly in IFCs would require a code that is simpler, quicker, and useable for any IFC file.

It should also be noted that the price file from MOLIO is an incomplete pricecatalog where all prices are multiplied with a arbritary numbers, and can therefore not be used for realistic calculations of price. Because of this we have chosen the pricing elements which resembles the building elements in the model. 

<img width="279" alt="Skjermbilde 2022-11-24 kl  08 51 44" src="https://user-images.githubusercontent.com/113243733/203727600-963a57d3-9db5-462b-b4b0-6d0ad5dc13fe.png"> <img width="527" alt="Skjermbilde 2022-11-24 kl  09 14 27" src="https://user-images.githubusercontent.com/113243733/203728949-c83c6947-b295-4eaf-b98a-d43e4f1872d3.png">



 
