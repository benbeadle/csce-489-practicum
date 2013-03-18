CSCE 489 Practicum: Google Charts
===================
<hr />
Intro
==========
Google Charts is a simple API that allows you to not only visualize data on websites, but is extremely simple to use, and automatically provides an interactive environment that allows the user to do more than just view the presentation of data. At the time of this writing, there are 14 different ways (read: graphs) you can display your data. Not only that, but Google provides simple ways of retrieving the data you want displayed from a myriad of sources. There is even an [interactive playground](https://code.google.com/apis/ajax/playground/?type=visualization#pie_chart) Google provides for you to play around with the different types of charts and ways to manipulate the data.

<hr />
Instructions: 5 Easy Steps
==========

Load the libraries
=
To start using Google Charts, all you need to do is add an external Javascript file, and add a few lines of code. Add the following lines inside the HEAD tag of your HTML page:

    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      //You must load a certain package depending on the Chart you are using.
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        //Code to create/display the chart goes here
      }
    </script>

to the head of your HTML file. This is all you have to do to begin playing with Google Charts. It's magic! Once all of the APIs are loaded, Google will execute drawChart, where you can create the chart, add data and options, and finally display it.

Choose your chart
=
TODO

Prepare your data
=
Google provides many ways of providing your new Chart with the data it needs and more importantly in the format it requires. In the end, all data must be in the <code>google.visualization.DataTable</code> format. This DataTable type is really just a fancy two-dimensional table which has a column type/label/(optional)id and the rows which represent the data. Your data must be formatted correctly for your Chart of choice. You can read the documentation specific for your chart to read on how you must format the data.

4. Add your options
4. Add your chart
5. Make it interactive (optional)

Don't forget the Image Charts API
