# Python-Automation-Scripts
Scripts written in Python with the Arcpy module to automate repetitive mapping tasks in ArcGIS.


<b>Create Map Service</b>

Concept: Automate the process of updating a map service .sd file in ArcGIS Server

Set up instructions:

<ul>
<li>Clone repo or download as zip file</li>
<li>Setup Options:</li>
<ul><li>Create Custom tool in an ArcToolBox, add the necessary parameters in the order they appear in the array, and run the script from arcmap</li>
<li>Edit the script with Pythonwin and replace all instances of 'arcpy.getParameterAsText(i)' with your own directories and documents</li>
</ul>
<li>This script can be combined with a script to republish desired layers into WGS84 Web Mercater (Auxillery Sphere) and scheduled with the windows task schedule to automate the process of updating rest services to be consumed by custom web mapping applications.</li>
</ul>
