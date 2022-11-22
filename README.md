After discussing our usecase and its applicability in the industry with to the representatives from Niras a couple of weeks ago, we decided that for our work tool to be more usefull, we had to create a CSV, where the name, type and quantity of each bulding element is displayed. This makes categorizing the prices easy, and the economically responisble parties of the contractor could quickly make calculations and decisions of which parts of the bulding that are the higest cost drivers.

Since the IFC files we have lloked at have defined its parameters differently and in different locations, we have made our code to specifically work for the ‘Duplex A’, to illustrate how the work tool should be utilized. This means that making sure materials and structural element properties are defined properly in the IFC would require a code that is  simpler, quicker, and useable for any IFC file.
    -Could show examples of this

![Alt text](Skjermbilde-2022-11-22-kl.-11.50.36.svg)

The work tool works in three different part. The first part  consists of is using IfcOpenshell attributes  .byType and RelDefinesByProperties to extract both the materials and the material quantities required by the MOLIO JSON file. Before the extraction we check that all elements being are extracted are defined as LoadBearing = True, so that as the use case states, we calculate the estimated cost for the main structural elements of the building. The second part is categorizing which materials and quantitative properties define the specific element and the third is linking it up to the price fitting that specific description. Fourth and lastly the code creates the CSV file, that you could open straigth into Numbers to start visualizing costs. 
The main difference from this final product and the earlier handed in versions is that the scope of the work tool is narrower, making it more specific, but also more detailed. The reason for this is to show that if it works for these specific cases, it could work for others. 



 