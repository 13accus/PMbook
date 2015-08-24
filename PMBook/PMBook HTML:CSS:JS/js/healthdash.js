//piechart
google.load("visualization", "1", {packages:["corechart", "line","bar"]});
      google.setOnLoadCallback(drawChart);
      function drawChart() {

        //1=piechart
        //2=linegraph
        //3=stackedbargraph

        //1 Piechart
        //=============
        var data1 = google.visualization.arrayToDataTable([
          ['Status Reports', 'Number Received'],
          ['On time w/o Issues',     31],
          ['On time w/ Issues',      0],
          ['Late',  0],
          ['Not Received', 6],
        ]);

        var options1 = {
          title: ''
        };

        var chart1 = new google.visualization.PieChart(document.getElementById('piechart'));

        chart1.draw(data1, options1);

        //2 Linegraph
        //=============
        var data2 = new google.visualization.DataTable();
        data2.addColumn('string', 'Portfolio Score');
        data2.addColumn('number', 'Number of Active Projects');

        data2.addRows([
          ["30",  0],
          ["3/24",  20],
          ["1",  40],
          ["1",  60],
        ]);

        var options2 = {
        chart2: {
          title: 'Self-Reported Status',
          subtitle: 'Portfolio Status'
        },
        width: 900,
        height: 500
      };


        var chart2 = new google.charts.Line(document.getElementById('linechart_material'));

        chart2.draw(data2, options2);


      //Stackedbargraph
      //================

      var view3 = new google.visualization.DataView(data);
      view.setColumns([0, 
                        1,
                       { calc: "stringify",
                         sourceColumn: 1,
                         type: "string",
                         role: "annotation" },
                       2]);

 
      var data3 = google.visualization.arrayToDataTable([
        ['Genre', 'Fantasy & Sci Fi', 'Romance', 'Mystery/Crime', 'General',
         'Western', 'Literature', { role: 'annotation' } ],
        ['2010', 10, 24, 20, 32, 18, 5, ''],
        ['2020', 16, 22, 23, 30, 16, 9, ''],
        ['2030', 28, 19, 29, 30, 12, 13, '']
      ]);

 

      var options3 = {
        width: 600,
        height: 400,
        legend: { position: 'top', maxLines: 3 },
        bar: { groupWidth: '75%' },
        isStacked: true,
        hAxis: {minValue: 0}
      };
        

      var chart3 = new google.visualization.BarChart(document.getElementById("barchart_values"));
      chart3.draw(view3, options3);

      
      }


