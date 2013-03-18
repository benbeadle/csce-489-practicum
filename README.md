CSCE 489 Practicum: Google Charts
===================

Intro
==========
Google Charts is a simple API that allows you to not only visualize data on websites, but is extremely simple to use, and automatically provides an interactive environment that allows the user to do more than just view the presentation of data. At the time of this writing, there are 14 different ways (read: graphs) you can display your data. Not only that, but Google provides simple ways of retrieving the data you want displayed from a myriad of sources. There is even an [interactive playground](https://code.google.com/apis/ajax/playground/?type=visualization#pie_chart) Google provides for you to play around with the different types of charts and ways to manipulate the data.


Instructions: 5 Easy Steps
==========

Load the libraries
=
To start using Google Charts, all you need to do is add a external Javascript file, and add a few lines of code. You must load three libraries:
1. The JSAPI
2. The Visualization Package
3. The Chart

Here's an example HTML file to load the Google Charts library:
<blockquote>
<html>
  <head>
  <code>
    <script type="text/javascript" src="https://www.google.com/jsapi"></script>
    <script type="text/javascript">
      //Tell Google to load the Visualization API. Certain Charts have different packages. This example is the Pie Chart
      google.load("visualization", "1", {packages:["corechart"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {
        //Here is where you will create your chart and display it
      }
    </script
  </code>
  </head>
  <body>
    <!--You must provide the API with a DIV to draw your Chart in. You can provide the width
    <div id="chart_div" style="width: 900px; height: 500px;"></div>
  </body>
</html>
</blockquote>
2. Prepare your data
3. Choose your chart
4. Add your options
4. Add your chart
5. Make it interactive (optional)

Don't forget the Image Charts API
