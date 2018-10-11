# Kshipra



## What does it do?
 

Natural Disasters are unavoidable but early detection of natural disaster can help save precious life and  property.
Most developed nations get early warnings about such calamities, but developing nations cannot afford to setup such a system.
This is where Kshipra ([pronounced ship-ra](https://www.howtopronounce.com/kshipra/)) steps in. 
Kshipra helps in detecting landslides and flood prone areas by taking into account the steepness of the slope, type of the soil and the installations around the specified location.
As soon as the Kshipra webpage is loaded the page will detect the User's location and will display the High Risk, Medium Risk and the Low Risk Areas around his/her location. If Kshipra detects that the user is in a dangerous place, it will alert the user and display the contact details to the nearest relief centre and a quick set of survival instructions will appear on the screen.




## How does it do it?

Kshipra goes through a three fold process to detect the potential high-risk areas:
  
1. It takes into account the altitutde of the hilly regions with the help of Azure Maps API and then looks for a path to the nearest peak. This peak shall tell us the amount of force with which the rain water might come down.
 
2. It then looks at the vegetation cover of the path leading to the peak, lack of which might cause slope failure. The vegetation cover data is extracted from [Azure Geo AI Data Science VM](https://docs.microsoft.com/en-us/azure/machine-learning/data-science-virtual-machine/geo-ai-dsvm-overview) (Geo-DSVM).
 
3. Lastly it learns from previous instances of landslides in the area. For this Kshipra relies on Global Landslide Catalog indexed by NASA Open Data Portal. The data will be imported into Kshipra as a .geojson file. This data is very comprehensive and includes the trigger of the event, exact coordinates of the incident and the severity of the landslide. This data will aid Kshipra in accurately determining the risk associated with a particular area.

## Conclusion

Kshipra,meaning remover of obstacle aims to follow on his name and protect,save the populace from a disaster which has been a prevelant problem in the world  
