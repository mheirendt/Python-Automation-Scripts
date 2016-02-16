import arcpy
import xml.dom.minidom as DOM
from arcpy import env

##local variables
#directory in which Service Definitions will be created and staged
wrkspc = arcpy.GetParameterAsText(0)
#Map document that will be shared as an ArcGIS Map Service
mapDoc = arcpy.GetParameterAsText(1)
newType = 'esriServiceDefinitionType_Replacement'
outServiceDefinition = wrkspc + "\\ServiceDefinitions\\Production.sd"
con = arcpy.GetParameterAsText(2)
#Name of the map service that will be either replaced or created
service = arcpy.GetParameterAsText(3)
sddraft = wrkspc+ "\\ServiceDefinitions\\" + service + '.sddraft'
sd = wrkspc + "\\ServiceDefinitions\\" +service + '.sd'
summary = arcpy.GetParameterAsText(4)
tags = arcpy.GetParameterAsText(5)
try:
    arcpy.Delete_management(outServiceDefinition)
except: pass
##creates service definition draft with variables
analysis = arcpy.mapping.CreateMapSDDraft(mapDoc, sddraft, service, 'ARCGIS_SERVER', con, True, None, summary, tags)


newType = 'esriServiceDefinitionType_Replacement'
xml = sddraft
doc = DOM.parse(xml)
descriptions = doc.getElementsByTagName('Type')
for desc in descriptions:
    if desc.parentNode.tagName == 'SVCManifest':
        if desc.hasChildNodes():
            desc.firstChild.data = newType
outXml = xml    
f = open(outXml, 'w')     
doc.writexml( f )     
f.close()

##stages and uploads the service if the sddraft analysis did not contain errors
if analysis['errors'] =={}:
    arcpy.StageService_server(sddraft, sd)
else:
    print analysis['errors']

##Set variables for uploading to server
#Link to newly created .SD file
inSDFile = outServiceDefinition
#Link to a server connection .ags file
inServer = arcpy.GetParameterAsText(6)
#Folder in ArcGIS Server for the service to be uploaded to
inFolder = arcpy.GetParameterAsText(7)

##Load the service definition to Arc Server
arcpy.UploadServiceDefinition_server(inSDFile, inServer, "", "", "EXISTING", inFolder)