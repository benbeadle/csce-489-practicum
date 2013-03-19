CSCE 489 Practicum: Google Charts
===================
<hr />
Intro
==========
Google Charts is a simple API that allows you to not only visualize data on websites, but is extremely simple to use, and automatically provides an interactive environment that allows the user to do more than just view the presentation of data. At the time of this writing, there are 14 different ways (read: graphs) you can display your data. Not only that, but Google provides simple ways of retrieving the data you want displayed from a myriad of sources. There is even an [interactive playground](https://code.google.com/apis/ajax/playground/?type=visualization#pie_chart) Google provides for you to play around with the different types of charts and ways to manipulate the data.

<hr />
Instructions: 5 Easy Steps
==========

Choose your chart
=
The first step to using Google Charts is selecting your choice of chart. You can view the [gallery](https://developers.google.com/chart/interactive/docs/gallery) on Google's documentation. You need to select your graph carefully depending on the data you have and what you are trying to convey to your user. Let's say I want to make a chart that looks like this:

![Screenshot](https://googledrive.com/host/0ByFjNR-5h19FOFBWbnVqLXlBaW8/Pony Placement Project - Google Charts.png)

As you can obviously tell, this is a [Pie Chart](https://developers.google.com/chart/interactive/docs/gallery/piechart).

Factoid: Developers have contributed other charts which you can view on the [Additional Charts](https://google-developers.appspot.com/chart/interactive/docs/more_charts.html) page. For example, you can integrate [Google Maps](https://google-developers.appspot.com/chart/interactive/docs/gallery/map) with data.

Load the libraries
=
To start using your chart with Google Charts, all you need to do is add an external Javascript file, and add a few lines of code. Add the following lines inside the HEAD tag of your HTML page:

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      //You must load a certain package depending on the Chart you are using.
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        //Code to create/display the chart goes here
      }
    </script>

NOTE: Different chart types call for different packages to be loaded. In the example above, I chose "corechart" Since I am trying to create the Pie Chart above.

This is all you have to do to begin playing with Google Charts. It's magic! Once all of the APIs are loaded, Google will execute drawChart, where you can create the chart with your data and options you will later specify.


Prepare your data
=
Google provides many ways of providing your new Chart with the data it needs and more importantly in the format it requires. In the end, all data must be in the <code>google.visualization.DataTable</code> format. This DataTable type is really just a fancy two-dimensional table which has a column type/label/(optional)id and the rows which represent the data. There are X different ways of aquiring and formatting your data:

1. Create a [DataTable or DataView](https://developers.google.com/chart/interactive/docs/datatables_dataviews) object. 
2. Populate the data [server-side](https://developers.google.com/chart/interactive/docs/php_example). This would include making an ajax call to an api which formats the output accordingly.
3. [Query a data source](https://developers.google.com/chart/interactive/docs/queries) which follows the Chart Tools Datasource protocol. For example, you can easily query a [Google Docs Spreadsheet](https://developers.google.com/chart/interactive/docs/datatables_dataviews#query) that has data.

Your data must be formatted correctly for your Chart of choice. You should read the documentation specific for your chart to make sure you are following the format accordingly. 

Let's say I have an array of  (array into a DataTable)[https://developers.google.com/chart/interactive/docs/datatables_dataviews#arraytodatatable], the code would look like this:

    

Customize Your Chart
=


4. Add your chart
5. Make it interactive (optional)

Don't forget the Image Charts API
