CSCE 489 Practicum: Google Charts
===================
<hr />
Intro
==========
Google Charts is a simple API that allows you to not only visualize data on websites, but is extremely simple to use, and automatically provides an interactive environment that allows the user to do more than just view the presentation of data. At the time of this writing, there are 14 different ways (read: graphs) you can display your data. Not only that, but Google provides simple ways of retrieving the data you want displayed from a myriad of sources. There is even an [interactive playground](https://code.google.com/apis/ajax/playground/?type=visualization#pie_chart) Google provides for you to play around with the different types of charts and ways to manipulate the data.

<hr />

Example
=

To create the following chart:



    <html>
    <head>
        <script type="text/javascript" src="https://www.google.com/jsapi"></script>
        <script type="text/javascript">
        var data = [
            ["Pony", "Value"],
            ["Twilight Sparkle", 335.9027976407598],
            ["Rainbow Dash", 214.0516842973825],
            ["Pinkie Pie", 208.47923663449154],
            ["Fluttershy",174.49897261904653],
            ["Rarity", 102.91225114250258],
            ["Applejack", 84.51268612411526]
        ];
        
        //This is defined globally, instead of in drawChart, so other
        //things can interact with it like the select event.
        var chart;
        
        var options = {
            title: "Pony Statistics",
            height: 400,
            width: 600,
            backgroundColor: "#FAAFBA",
            chartArea: {
                width: "100%",
                height: "100%"
            },
            legend: {
                position: "left",
                alignment: "center"
            },
                pieSliceText: "percentage",
                pieSliceBorderColor: "#6C2DC7",
            tooltip: {
                text: "percentage" //Tell the tooltip to show the percentage
            }
        }
        
        //Called when the user selects a slice of the pie.
        function ponySelected(event) {
            //Pie Charts can only have one element selected
             var selection = chart.getSelection()
        
            //If you click a pony that was already selected, it deselects it
            if(selection.length == 0) {
              document.getElementById("selection").innerHTML = "Select a pony to view stats.";
              return;
            }
            
            var pony = data[selection[0].row+1];
            
            document.getElementById("selection").innerHTML = "You selected " +
                pony[0] + " with a value of " + pony[1];
         }
        //Called when the APIs are ready to play
        function drawChart() {
            var arrayTable = google.visualization.arrayToDataTable(data, false);//false means first column is a label column 
            chart = new google.visualization.PieChart(document.getElementById('pie_chart'));
            chart.draw(arrayTable, options);
            google.visualization.events.addListener(chart, 'select', ponySelected);
        }
        
        
        //You must load a certain package depending on the Chart you are using.
        google.load("visualization", "1", {packages:["corechart"]});
        google.setOnLoadCallback(drawChart);
        </script>
    </head>
    <body>
        <div id="pie_chart"></div>
        <div id="selection"></div>
    </body>
    </html>




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
        //Code to create/display the chart goes here (view solution below)
      }
    </script>

NOTE: Different chart types call for different packages to be loaded. In the example above, I chose "corechart" Since I am trying to create the Pie Chart above.

This is all you have to do to begin playing with Google Charts. It's magic! Once all of the APIs are loaded, Google will execute drawChart, where you can create the chart with your data and options you will later specify.


Prepare your data
=
Google provides many ways of providing your new Chart with the data it needs and more importantly in the format it requires. In the end, all data must be in the <code>google.visualization.DataTable</code> format. This DataTable type is really just a fancy two-dimensional table which has a column type/label/(optional)id and the rows which represent the data. There are X different ways of aquiring and formatting your data:

1. Create a [DataTable or DataView](https://developers.google.com/chart/interactive/docs/datatables_dataviews) object. This can be completed by manually adding columns/rows, creating one from an array, using a JS literal, or sending a datasource query. 
2. Populate the data [server-side](https://developers.google.com/chart/interactive/docs/php_example). This would include making an ajax call to an api which formats the output accordingly.
3. [Query a data source](https://developers.google.com/chart/interactive/docs/queries) which follows the Chart Tools Datasource protocol. For example, you can easily query a [Google Docs Spreadsheet](https://developers.google.com/chart/interactive/docs/datatables_dataviews#query) that has data.

Your data must be formatted correctly for your Chart of choice. You should read the documentation specific for your chart to make sure you are following the format accordingly. 

Let's say I have an array of Ponies and Statistics and I'd like to turn [into a DataTable](https://developers.google.com/chart/interactive/docs/datatables_dataviews#arraytodatatable). The code would look like this:

    var data = [
        ["Pony", "Value"],
        ["Twilight Sparkle", 335.9027976407598],
        ["Rainbow Dash", 214.0516842973825],
        ["Pinkie Pie", 208.47923663449154],
        ["Fluttershy",174.49897261904653],
        ["Rarity", 102.91225114250258],
        ["Applejack", 84.51268612411526]
    ]
    var arrayTable = google.visualization.arrayToDataTable(data, false); //false means the first column is a label column

Do note, that calling the <code>arrayToDataTabe</code> method must be done after the APIs have loaded, aka in the <code>drawChart</code> method you have defined.

Customize Your Chart
=
So what about the axis titles, the chart title, or customizing the tooltips? Google Charts allows you to [customize a lot](https://developers.google.com/chart/interactive/docs/customizing_charts) to make it look and feel exactly like you want it. Let's say I wanted to change the title and put the legend on the left side for my Pony Statistics Pie Chart. Also, looking at the data above, you can see that the numbers are not in percentages, which would be confusing for the user to manually calculate their percentages. Luckily, with Google Charts, you can easily set all of this in your options:
    
    var options = {
        title: "Pony Statistics",
        height: 250,
        width: 250,
        backgroundColor: "#FAAFBA",
        chartArea: {
            width: "100%",
            height: "100%"
        },
        legend: {
            position: "left",
            alignment: "center"
        },
        pieSliceText: "percentage",
        pieSliceBorderColor: "#6C2DC7",
        tooltip: {
            text: "percentage" //Tell the tooltip to show the percentage
        }
    }

As you can see from this simple example, there are a lot of options to set! In fact, while there are options available to all charts, you can check out the available options for your specific chart on the documentation page. Check out the [Pie Chart](https://developers.google.com/chart/interactive/docs/gallery/piechart#Configuration_Options) documentation to see what some of the above settings mean.

Add your chart
=

Now it's time add your chart to the page and display it for your user. There are two things you need to do,
1. Make sure you have a div labeled with an id somewhere on your page, like this:

    <body>
        <div id="pie_chart" /><!-- You can optionally set style like height/width here -->
    </body>

2. Attach the chart to the page. You need to do this in the drawChart method due to the fact that you have to wait for all of the APIs to load as you can see when you loaded your libraries. The method to draw your chart should look something like this:

    var chart; //Make this global so other methods, like the optional one in the next section can use it!
    function drawChart() {
        chart = new google.visualization.PieChart(document.getElementById('pie_chart'));
        chart.draw(arrayTable, options);
    }

There are many other ways to [draw your chart](https://developers.google.com/chart/interactive/docs/drawing_charts). Each type has advantages and disadvantages, it just depends on how your data is compiled/stored which way might be easiest.


Make it interactive (optional)
=

Google Charts allows you to make your chart [interactive](https://developers.google.com/chart/interactive/docs/events). For example, let's say with the Pie Chart above, we want to know when the user clicks on a result to show that specific pony. You can add an event listener to your chart to be notified when the user does so:
    
    function ponySelected(event) {
         var selection = chart.getSelection()
        
        //If you click a pony that was already selected, it deselects it
        if(selection.length == 0) {
          document.getElementById("selection").innerHTML = "Select a pony to view stats.";
          return;
        }
        
        var pony = data[selection[0].row+1];
        
        document.getElementById("selection").innerHTML = "You selected " +
          pony[0] + " with a value of " + pony[1];
    }
    
    function drawChart() {
        //Code from previous step
        google.visualization.events.addListener(chart, 'select', ponySelected);
    }


Don't forget the Image Charts API
