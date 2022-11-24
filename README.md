# Changes
After discussing our usecase and its applicability in the industry with the two representatives from Niras, we decided that for our work tool to be more usefull, we had to create CSVs, where the name, type, quantity and price of each bulding element were displayed. This output makes categorizing the prices easier, and contractors will quickly be able to make calculations and decisions on which parts of the bulding are the largest cost drivers. Other changes consist of extracting more infomation from the IFC model, to create more precise cost estimates. 

# Goal
Because of the changes made, the overall goal of the work tool is tweaked to be in favor of the financial analytics part of the contractors. The tool will assist in evaluating where the cost of the main structure has its largest potential of cost cut.  


# How it works
The work tool works in three different part. The first part consists of is using IfcOpenshell attributes  .byType and RelDefinesByProperties to extract both the materials and the material quantities required by the MOLIO JSON file. Before the extraction we check that all elements being are extracted are defined as LoadBearing = True, so that as the use case states, we calculate the estimated cost for the main structural elements of the building. The second part is categorizing which materials and quantitative properties define the specific element and the third is linking it up to the price fitting that specific description. Fourth and lastly the code creates the CSV file, that you could open straigth into Numbers to start visualizing costs. 
The main difference from this final product and the earlier handed in versions is that the scope of the work tool is narrower, making it more specific, but also more detailed. The reason for this is to show that if it works for these specific cases, it could work for others. 

![Alt text](Images/utklipp.jpg?raw=true "Example of extracted information about foundation footing")

# note:
Since the IFC files we have looked at have defined its parameters differently and in different locations, we have made our code to specifically work for the ‘Duplex A’, to illustrate how the work tool should be utilized. This means that making sure materials and structural element properties are defined properly in IFCs would require a code that is simpler, quicker, and useable for any IFC file.

It should also be noted that the price file from MOLIO is an incomplete pricecatalog where all prices are multiplied with a arbritary numbers, and can therefore not be used for realistic calculations of price. Because of this we have chosen the pricing elements which resembles the building elements in the model. 

<img width="279" alt="Skjermbilde 2022-11-24 kl  08 51 44" src="https://user-images.githubusercontent.com/113243733/203727600-963a57d3-9db5-462b-b4b0-6d0ad5dc13fe.png"> <img width="527" alt="Skjermbilde 2022-11-24 kl  09 14 27" src="https://user-images.githubusercontent.com/113243733/203728949-c83c6947-b295-4eaf-b98a-d43e4f1872d3.png">



 
