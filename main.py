import ifcopenshell
import json
import csv

with open('input/Molio Nybyggeri - Bygningsdele 2021 Demo.json', 'r') as file_object:
    data = json.load(file_object)

model = ifcopenshell.open("model/Duplex_A_20110907.ifc")

##WALLS in the model
with open("output/walls.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Type", "Price classification", "Unit price (kr/lb.m)", "Width (m)", "Length (m)", "Total price (kr)"]
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    thewriter.writeheader()
    
    walls_required = 1
    walls_in_model = len(model.by_type("IfcWall"))
    total_wall_length = 0
    total_wall_price = 0

    if (walls_required <= walls_in_model):
        print("\nThere are "+str(walls_in_model)+" walls in the model in total, in which the following is loadbearing:")
    
        for entity in model.by_type("IfcWall"):
            for relDefinesByProperties in entity.IsDefinedBy:
                for wall_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:

                    if wall_prop.Name == 'LoadBearing':                                     
                        lb_wall = wall_prop.NominalValue.wrappedValue

                    if wall_prop.Name == 'Length' and lb_wall == True:
                        wall_length = wall_prop.NominalValue.wrappedValue
                        total_wall_length += wall_prop.NominalValue.wrappedValue
                        print("Length:", wall_length, "m")

                    if wall_prop.Name == 'Width' and lb_wall == True:
                        wall_width = wall_prop.NominalValue.wrappedValue
                        print("Width:", wall_width, "m")

                    if wall_prop.Name == 'Base Constraint' and lb_wall == True:
                        wall_level = wall_prop.NominalValue.wrappedValue
                        print("Level:", wall_level)
                    
                            
                for wall_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if wall_prop.Name == "Classification Description" and lb_wall == True:
                        type_of_wall = wall_prop.NominalValue.wrappedValue
                        print("Type:", type_of_wall)
                        
                        if type_of_wall == "Concrete Structural Walls" and wall_level == "T/FDN":
                            if wall_width == 0.417:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Kælderydervæg af uarmeret beton, tykkelse 450 mm, højde 2,5 m":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_wall_price += price
                                        print("Price classification:", name)
                                        print("Unit price:", price, "kr/lb.m")
                                        print("Total price:", price*wall_length, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":wall_name, "Type":type_of_wall, "Price classification":name, "Unit price (kr/lb.m)":price, "Width (m)": wall_width, "Length (m)":wall_length, "Total price (kr)":price*wall_length})

                            elif wall_width == 0.435:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Fundament af beton, t = 350 mm, h = 900 mm, for indervæg":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_wall_price += price
                                        print("Price classification:", name)
                                        print("Unit price:", price, "kr/lb.m")
                                        print("Total price:", price*wall_length, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":wall_name, "Type":type_of_wall, "Price classification":name, "Unit price (kr/lb.m)":price, "Width (m)": wall_width, "Length (m)":wall_length, "Total price (kr)":price*wall_length})

                        elif type_of_wall == "Concrete Structural Walls" and wall_level != "T/FDN":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Ydervæg af betonelementer med isolering afsluttet med strukturpuds":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_wall_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price, "kr/lb.m")
                                    print("Total price:", price*wall_length, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":wall_name, "Type":type_of_wall, "Price classification":name, "Unit price (kr/lb.m)":price, "Width (m)": wall_width, "Length (m)":wall_length, "Total price (kr)":price*wall_length})
                       
                        elif type_of_wall == "Masonry Structural Walls" and wall_level != "T/FDN":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Facadeelement af tegl - isolering - beton, tykkelse 550 mm":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_wall_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price,  "kr/lb.m")
                                    print("Total price:", price*wall_length, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":wall_name, "Type":type_of_wall, "Price classification":name, "Unit price (kr/lb.m)":price, "Width (m)": wall_width, "Length (m)":wall_length, "Total price (kr)":price*wall_length})
                        else:
                            print("No concrete or masonry structural walls in model")
                                    

                
                for wall_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if wall_prop.Name == "Reference" and lb_wall == True:
                        wall_name = str(wall_prop.NominalValue.wrappedValue)
                        print("Name:", wall_name)
                  
        print("  ")
        print("The total length of loadbearing walls is:", total_wall_length, "m")
        print("The total price for all loadbearing walls is", total_wall_price*total_wall_length, "kr")


    
            
    else:
        print ('There are no walls in the model')


##SLABS in the model
with open("output/slabs.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Type", "Price classification", "Unit price (kr/m2)", "Thickness (m)", "Area (m2)", "Total price (kr)"]
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    thewriter.writeheader()
    
    slabs_required = 1
    slabs_in_model = len(model.by_type("IfcSlab"))
    total_slab_area = 0
    total_slab_price = 0

    if (slabs_required <= slabs_in_model):
        print("\nThere are "+str(slabs_in_model)+" slabs in the model in total, in which the following is loadbearing:")
    
        for entity in model.by_type("IfcSlab"):
            for relDefinesByProperties in entity.IsDefinedBy:
                for slab_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:

                    if slab_prop.Name == 'LoadBearing':                                     
                        lb_slab = slab_prop.NominalValue.wrappedValue

                    if slab_prop.Name == 'Area' and lb_slab == True:
                        slab_area = slab_prop.NominalValue.wrappedValue
                        total_slab_area += slab_prop.NominalValue.wrappedValue
                        print("Area:", slab_area, "m2")

                    if slab_prop.Name == 'Thickness' and lb_slab == True:
                        slab_thickness = slab_prop.NominalValue.wrappedValue
                        print("Thickness:", slab_thickness, "m")

                    if slab_prop.Name == 'Unnamed (0.15)' and lb_slab == True:
                        slab_material = slab_prop.NominalValue.wrappedValue
                        print("Material:", slab_material)
                    
                    

                        
                for slab_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if slab_prop.Name == "Classification Description" and lb_slab == True:
                        type_of_slab = slab_prop.NominalValue.wrappedValue
                        print("Type:", type_of_slab)
                        
                        if type_of_slab == "Structural Floor Decks":
                            if slab_thickness == 0.127:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Præfabrikerede dækementer af beton, 180 x 1.197 x 7.200 mm":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_slab_price += price
                                        print("Price classification:", name)
                                        print("Unit price:", price, "kr/m2")
                                        print("Total price:", price*slab_area, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":slab_name, "Type":type_of_slab, "Price classification":name, "Unit price (kr/m2)":price, "Thickness (m)": slab_thickness, "Area (m2)":slab_area, "Total price (kr)":price*slab_area})

                            elif slab_thickness == 0.15:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Præfabrikerede dækementer af beton, 215 x 1.197 x 7.200 mm":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_slab_price += price
                                        print("Price classification:", name)
                                        print("Unit price:", price, "kr/m2")
                                        print("Total price:", price*slab_area, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":slab_name, "Type":type_of_slab, "Price classification":name, "Unit price (kr/m2)":price, "Thickness (m)": slab_thickness, "Area (m2)":slab_area, "Total price (kr)":price*slab_area})

                            elif slab_thickness == 0.3050000000000001:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Præfabrikerede dækelementer af træ for montering i samme bolig" and data[i]["number"]== "(23)25.40,01":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_slab_price += price
                                        print("Price classification:", name)
                                        print("Unit price:", price, "kr/m2")
                                        print("Total price:", price*slab_area, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":slab_name, "Type":type_of_slab, "Price classification":name, "Unit price (kr/m2)":price, "Thickness (m)": slab_thickness, "Area (m2)":slab_area, "Total price (kr)":price*slab_area})
                            
                            else:
                                print("Structural floor deck has other thickness")

                        elif type_of_slab == "Wood Flooring":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Bøgeparket, 22 mm, type Harmony, på strøer pr. 420 mm/isolering":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_slab_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price, "kr/m2")
                                    print("Total price:", price*slab_area, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":slab_name, "Type":type_of_slab, "Price classification":name, "Unit price (kr/m2)":price, "Thickness (m)": slab_thickness, "Area (m2)":slab_area, "Total price (kr)":price*slab_area})

                        elif type_of_slab == "Tile Flooring":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Gulvfliser, 100 x 100 x 9 mm, at lægge på underlag af beton":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_slab_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price, "kr/m2")
                                    print("Total price:", price*slab_area, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":slab_name, "Type":type_of_slab, "Price classification":name, "Unit price (kr/m2)":price, "Thickness (m)": slab_thickness, "Area (m2)":slab_area, "Total price (kr)":price*slab_area})

                        else:
                            print("No Structural floor decks, wood or tile flooring")
                                    
                for slab_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if slab_prop.Name == "Reference" and lb_slab == True:
                        slab_name = str(slab_prop.NominalValue.wrappedValue)
                        print("Name:", slab_name)

        print("  ")
        print("The total area of loadbearing slabs is:", total_slab_area, "m2")
        print("The total price for all slabs is", total_slab_price*total_slab_area, "kr")

    
            
    else:
        print ('There are no slabs in the model')


##BEAMS in the model
with open("output/beams.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Type", "Price classification", "Unit price (kr/lb.m)", "Depth (m)", "Length (m)", "Total price (kr)"]
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    thewriter.writeheader()
    
    beams_required = 1
    beams_in_model = len(model.by_type("IfcBeam"))
    total_beam_length = 0
    total_beam_price = 0

    if (beams_required <= beams_in_model):
        print("\nThere are "+str(beams_in_model)+" beams in the model in total, in which the following is loadbearing:")
    
        for entity in model.by_type("IfcBeam"):
            for relDefinesByProperties in entity.IsDefinedBy:
                for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if beam_prop.Name == 'LoadBearing':                                     
                        lb_beam = beam_prop.NominalValue.wrappedValue
                    
                           
                for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if beam_prop.Name == "Beam Material" and lb_beam == True:
                        type_of_beam = beam_prop.NominalValue.wrappedValue
                        print("Type:", type_of_beam)

                    if beam_prop.Name == "d" and lb_beam == True:
                        width_beam = beam_prop.NominalValue.wrappedValue
                        print("Depth:", width_beam)
                        
                        if type_of_beam == "Metal - Steel - 345 MPa" and width_beam == 0.407:
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Stålbjælke/drager med isolering på 3 sider (BS-60)":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_beam_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price, "kr/lb.m")
                                    print("Total price:", price*length_beam, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":beam_name, "Type":type_of_beam, "Price classification":name, "Unit price (kr/lb.m)":price, "Depth (m)": width_beam, "Length (m)":length_beam, "Total price (kr)":price*length_beam})

                        elif type_of_beam == "Metal - Steel - 345 MPa" and width_beam == 0.303:
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Stålbjælke/drager med isolering på 3 sider (BS-30)":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_beam_price += price
                                    print("Price classification:", name)
                                    print("Unit price:", price, "kr/lb.m")
                                    print("Total price:", price*length_beam, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":beam_name, "Type":type_of_beam, "Price classification":name, "Unit price (kr/lb.m)":price, "Depth (m)": width_beam, "Length (m)":length_beam, "Total price (kr)":price*length_beam})
                

                        elif type_of_beam == "Concrete - 30 MPa" and width_beam == 0.3:
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="300 x 720 mm rektangulær betonbjælke":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_beam_price += price
                                    print("Unit price:", price, "kr/lb.m")
                                    print("Total price:", price*length_beam, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":beam_name, "Type":type_of_beam, "Price classification":name, "Unit price (kr/lb.m)":price, "Depth (m)": width_beam, "Length (m)":length_beam, "Total price (kr)":price*length_beam})

                        elif type_of_beam == "Concrete - 30 MPa" and width_beam == 0.25:
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]=="Betonbjælke 250 x 400 mm, ikke synlig flade":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_beam_price += price
                                    print("Unit price:", price, "kr/lb.m")
                                    print("Total price:", price*length_beam, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":beam_name, "Type":type_of_beam, "Price classification":name, "Unit price (kr/lb.m)":price, "Depth (m)": width_beam, "Length (m)":length_beam, "Total price (kr)":price*length_beam})
                              
                        else:
                            print("The beam is a different type of beam than those listed in code, need to update code with correct beam and attached price")
                            print(" ")
                                    
                              
                for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if beam_prop.Name == "Reference" and lb_beam == True:
                        beam_name = str(beam_prop.NominalValue.wrappedValue)
                        print("Name:", beam_name)

                for beam_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if beam_prop.Name == 'Span' and lb_beam == True:
                        length_beam = beam_prop.NominalValue.wrappedValue
                        total_beam_length += beam_prop.NominalValue.wrappedValue
                        print("Length:", length_beam, "m")


        print("  ")
        print("The total length of loadbearing beams is:", total_beam_length, "m")
        print("The total price for all beams is", total_beam_price*total_beam_length, "kr")
            
    else:
        print ('There are no beams in the model')


##COLUMNS in the model
with open("output/columns.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Type", "Price classification", "Unit price (kr/lb.m)", "Thickness (m)", "Length (m)", "Total price (kr)"]
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    thewriter.writeheader()
    
    columns_required = 1
    columns_in_model = len(model.by_type("IfcColumn"))
    total_column_length = 0
    total_column_price = 0

    if (columns_required <= columns_in_model):
        print("\nThere are "+str(columns_in_model)+" columns in the model in total, in which the following is loadbearing:")
    
        for entity in model.by_type("IfcColumn"):
            for relDefinesByProperties in entity.IsDefinedBy:

                for column_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if column_prop.Name == 'LoadBearing':                                     
                        lb_column = column_prop.NominalValue.wrappedValue
                    
                    if column_prop.Name == "Thickness" and lb_column == True:
                        thickness_column = column_prop.NominalValue.wrappedValue
                        print("Thickness:", thickness_column)
                    
                for column_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if column_prop.Name == "Column Material" and lb_column == True:
                        type_of_column = column_prop.NominalValue.wrappedValue
                        print("Type:", type_of_column)
                        
                        if type_of_column == "Concrete column":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]== "Betonsøjle præfabr. 300 x 300 x 3.000 mm":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_column_price += price
                                    print("Unit price: %f" %data[i]["price"], "kr/lb.m")
                                    print("Total price:", price*length_column, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":column_name, "Type":type_of_column, "Price classification":name, "Unit price (kr/lb.m)":price, "Thickness (m)": thickness_column, "Length (m)":length_column, "Total price":price*length_column})

                        elif type_of_column == "Steel column":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]== "Stålsøjle med brandisolering på 4 sider (BS-60)":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_column_price += price
                                    print("Unit price: %f" %data[i]["price"], "kr/lb.m")
                                    print("Total price:", price*length_column, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":column_name, "Type":type_of_column, "Price classification":name, "Unit price (kr/lb.m)":price, "Thickness (m)": thickness_column, "Length (m)":length_column, "Total price":price*length_column})

                        elif type_of_column == "Wood column":
                            g = ''
                            for i in range(1, len(data)):
                                if g in data[i]["name"]== "Søjle af lamineret tømmer i søjlesko":
                                    name = data[i]["name"]
                                    price = data[i]["price"]
                                    total_column_price += price
                                    print("Unit price: %f" %data[i]["price"], "kr/lb.m")
                                    print("Total price:", price*length_column, "kr")
                                    print("    ")
                                    thewriter.writerow({"Name":column_name, "Type":type_of_column, "Price classification":name, "Unit price (kr/lb.m)":price, "Thickness (m)": thickness_column, "Length (m)":length_column, "Total price":price*length_column})

                        else:
                            print("No columns for input concrete, steel or wood. Change parameters if columns present in model.")
                              
                for column_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if column_prop.Name == "Reference" and lb_column == True:
                        column_name = str(column_prop.NominalValue.wrappedValue)
                        print("Name:", column_name)

                    if column_prop.Name == 'Span' and lb_column == True:
                        length_column = column_prop.NominalValue.wrappedValue
                        total_column_length += column_prop.NominalValue.wrappedValue
                        print("Length:", length_column, "m")


        print("  ")
        print("The total length of loadbearing columns is:", total_column_length, "m")
        print("The total price for all columns is", total_column_price*total_column_length, "kr")

    
            
    else:
        print(" ")
        print('! There are no columns in the model')


##FOOTINGS in the model
with open("output/foootings.csv", "w", newline="") as csvfile:
    fieldnames = ["Name", "Type", "Price classification", "Unit price (kr/lb.m)", "Thickness (m)", "Length (m)", "Total price (kr)"]
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t")
    thewriter.writeheader()

    footings_required = 1
    footings_in_model = len(model.by_type("IfcFooting"))
    total_footings_length = 0
    total_footings_price = 0


    if (footings_required <= footings_in_model):
        print("\nThere are "+str(footings_in_model)+" footings in the model in total, in which the following is loadbearing:")
    
        for entity in model.by_type("IfcFooting"):
            for relDefinesByProperties in entity.IsDefinedBy:
                
    
                for footing_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:  
                    if footing_prop.Name == 'Length':
                        length_footing = footing_prop.NominalValue.wrappedValue
                        total_footings_length += footing_prop.NominalValue.wrappedValue
                        print("Length:", length_footing, "m")

                    if footing_prop.Name == 'Foundation Thickness':
                        thickness_footing = footing_prop.NominalValue.wrappedValue
                        print("Thickness:", thickness_footing, "m")
                                      
                for footing_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties:
                    if footing_prop.Name == "Classification Description":
                        type_of_footing = footing_prop.NominalValue.wrappedValue
                        print("Type:", type_of_footing)
                        
                        if type_of_footing == "Shallow Foundations":
                            if thickness_footing == 0.3:
                                g = ''
                                for i in range(1, len(data)):
                                    if g in data[i]["name"]=="Fundament af beton at støbe i rende, t = 310 mm, h = 1,1 m":
                                        name = data[i]["name"]
                                        price = data[i]["price"]
                                        total_footings_price += price
                                        print("Price classification:", name)
                                        print("Unit price: %f" %data[i]["price"], "kr/lb.m")
                                        print("Total price:", price*length_footing, "kr")
                                        print("    ")
                                        thewriter.writerow({"Name":footing_name, "Type":type_of_footing, "Price classification":name, "Unit price (kr/lb.m)":price, "Thickness (m)": thickness_footing, "Length (m)":length_footing, "Total price (kr)":price*length_footing})
                            
                            else:
                                print("No shallow footings with thickness 0.3, add thickness and find equivalent name")

                        else:
                            print("No shallow footings, add more types to code")
                      
               
                for footing_prop in relDefinesByProperties.RelatingPropertyDefinition.HasProperties: 
                    if footing_prop.Name == "Material":
                        footing_name = footing_prop.NominalValue.wrappedValue
                        print("Name:", footing_name)
                    
        print("  ")
        print("The total length of loadbearing footings is:", total_footings_length, "m")
        print("The total price for all footings is:", total_footings_price*total_footings_length, "kr")
                
    else:
        print ('There are no footings in the model')