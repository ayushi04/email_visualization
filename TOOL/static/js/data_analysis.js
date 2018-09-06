var colNames;

//This method get the value of input parameter passed by backend (python code)
// and sends it to javascript variable
function getParameterByName(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
    results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}

function dynamicallyLoadSelectList(divId,datasetPath) {
	console.log('----dynamicallyLoadSelectList---');
  var colNames;
	d3.csv(datasetPath, function(error, csv) {
      colNames = d3.values(csv)[0];
      console.log(colNames);
      
    var htmlstr = '';
    for (k in colNames) {
  		if (k != 'classLabel' && k != 'id') {
  		  htmlstr = htmlstr.concat('<input type="checkbox" class="dim" value="' + k + '">' + k + '<br>');
  	      }
  	}
  console.log(htmlstr);
  htmlstr="<table><tr><td>HOURS>50</td></tr> <tr><td>DOD_HOSP NOT NULL</td></tr> <tr><td>DOD IS NULL</td></tr> <tr><td>INPUTS IN (Sodium Bicarbonate)</td></tr> <tr><td>LABNAME IN (LACTATE)</td></tr>";
  htmlstr=htmlstr.concat("<tr><td>GENDER==F</td></tr> <tr><td>LOS>=5</td></tr> <tr><td>DOD IS NULL</td></tr> <tr><td>INPUTS IN (Magnesium)</td></tr> <tr><td>INPUTS IN (KCL)</td></tr>");
  htmlstr=htmlstr.concat("</table>")
	$(divId).html(htmlstr);
  });
}

function loadImg(url, w, h,mapid,parent,imgType,datasetPath) {
  var MIN_ZOOM = -1;
  var MAX_ZOOM = 5;
  var INITIAL_ZOOM = 1;
  var ACTUAL_SIZE_ZOOM = 3;
  var map = L.map(mapid, {
    minZoom: MIN_ZOOM,
    maxZoom: MAX_ZOOM,
    center: [0, 0],
    zoom: INITIAL_ZOOM,
    crs: L.CRS.Simple
  });
  //var imgType='_'+ $('#changeImgType').val();
  var southWest = map.unproject([0, h], ACTUAL_SIZE_ZOOM);
  var northEast = map.unproject([w, 0], ACTUAL_SIZE_ZOOM);
  console.log(southWest, northEast);
  var bounds = new L.LatLngBounds(southWest, northEast);

  L.imageOverlay(url, bounds).addTo(map);
  map.setMaxBounds(bounds);

  map.on('click', function(e) {
    var x = (e.latlng.lat) / (southWest.lat - northEast.lat);
    var y = (e.latlng.lng) / (-southWest.lng + northEast.lng);
    console.log(x + ':' + y);
    $('#loading').html('<img src="loading.gif"> loading...');
    $('#table2').html('-');
    $('#table3').html('-');
    console.log(x,y,datasetPath);
    $.ajax({
      url: "/highlightPattern",
      data: {
        x: x,
        y: y,
        datasetPath: datasetPath,
      },
      contentType: 'application/json; charset=utf-8',
      success: function(result) {
        console.log('highlightPattern done!!');
        //$("#div1").html("<img src='static/output/img_bea.png'></img>");
        /*result = JSON.parse(result);
        subspace = result['dim'];
        var rowPoints = JSON.parse(result['rowPoints']);
        var colPoints = JSON.parse(result['colPoints']);
        var rowPoints_save = JSON.parse(result['rowPoints_save']);
        var colPoints_save = JSON.parse(result['colPoints_save']);
        var allFig= result['allFig'];
        console.log('subspace'+subspace);
        console.log(JSON.parse(result['rowPoints']));
        console.log(JSON.parse(result['colPoints']));
        console.log(JSON.parse(result['dist']), JSON.parse(result['pair']));
        $('#'+mapid).remove();
        $('#'+parent).append('<div id="'+mapid+'" style="width: 500px; height: 400px;"></div>')
        d = new Date();
        if(imgType=='closed') {
        loadImg("/static/output/temp_closed.png?" + d.getTime(),"/static/output/temp_closed_composite.png?" + d.getTime(), 2229, 2058,mapid,mapid2,parent,parent2,'closed');
        $('#loading').html('-');
        var fname = 'output/legend_'+imgType+'.html?' + d.getTime();
        $('#loading').html('-');
        }
        else {
          loadImg("/static/output/temp_heidi.png?" + d.getTime(),"/static/output/temp_heidi_composite.png?" + d.getTime(), 2229, 2058,mapid,mapid2,parent,parent2,'heidi');
          $('#loading').html('-');
          }
        $('#table2').html(convertJsonToTable(JSON.parse(result['rowPoints']),'col'));
        $('#table3').html(convertJsonToTable(JSON.parse(result['colPoints']),'row'));
        //drawGraph(JSON.parse(result['dist']), JSON.parse(result['pair']));
        drawParallelCoordinate('parallelPlot');
        drawGiantWheel('#windrose1');
        $('#pointsPlots').html('');
        console.log('adding crovhd visualization to gui!!');
        $('#crovhd').html('<img src="/static/output/rowColPoints.png?'+ d.getTime() +'">');
        drawPointsComparison('pointsPlots',rowPoints_save,colPoints_save,subspace);
        //uploadHistorgram();
        */
       
      },
      error: function(result) {
        console.log(result);
      }
    });
    
  });
}


function updateImage() {
  console.log('---updateImage---');
  var equations = [];
  var panel=$('#bitvector');
  var inputs=panel.find('input');
  for (var i=0;i<inputs.length;i++) {
    if(inputs[i].value!='')
      equations.push(inputs[i].value);
  }
  equations = equations.join(':');
  $('#loading').html("<img src={{ url_for('static',filename='loading.gif') }}> loading...");
  console.log(equations);
  $.ajax({
    url:"/image",
    data: {
      equations: equations,
      datasetPath: datasetPath
    },
    contentType: 'application/json; charset=utf-8',
    success: function(result) {
     console.log(result);
      var result1=JSON.parse(result);
      if(result1.hasOwnProperty('error')) {
        var message=result1['error'];
        $('.error_msg').html(message);
        $('.alert_msg').css("display", "inline-block");
      }
      else{
        $('#mapid').remove();
        $('#parent').append('<div id="mapid" style="width: 500px; height: 400px;"></div>')
        d = new Date();
        //(url, w, h,mapid,parent,imgType)
        loadImg("/static/output/consolidated_img.png?" + d.getTime(), 2229, 2058,'mapid','parent','heidi',datasetPath);
        $('#loading').html('-');
        var fname = '/static/output/legend_heidi.html?' + d.getTime();
        $('#legend').load(fname);
      }
    },
     error: function(error) {
                console.log('ERROR',error);
            } 
  });

}

function colorFilter(parent,color_val) {
  console.log('ColorFilter');
  $('#loading').html('<img src="static/image/loading.gif"> loading...');
  $.ajax({
    url: "/visualDashboard",
    data: {
      color_value: color_val,
      datasetPath: datasetPath
    },
    contentType: 'application/json; charset=utf-8',
    success: function(result) {
      console.log(result);
      var result=JSON.parse(result);
      var b1=parseInt(result['b1']);
      var b2=parseInt(result['b2']);
      var b1_s=parseInt(result['b1_s']);
      var b2_s=parseInt(result['b2_s']);

      /*$('#'+m1).remove();
      $('#'+p1).append('<div id="'+m1+'" style="width: 500px; height: 400px;"></div>')
      $('#'+m2).remove();
      $('#'+p2).append('<div id="'+m2+'" style="width: 500px; height: 400px;"></div>')
      d = new Date();
      if(imgType=='heidi')
        loadImg("/static/output/temp_heidi.png?" + d.getTime(),"/static/output/temp_heidi_composite.png?" + d.getTime(), 2229, 2058,m1,m2,p1,p2,imgType);
      else
        loadImg("/static/output/temp_closed.png?" + d.getTime(),"/static/output/temp_closed_composite.png?" + d.getTime(), 2229, 2058,m1,m2,p1,p2,imgType);
      */
      var data = [{ type: 'category',
                    x: [0], y:[0],
                    marker: {size: 28, color:'850000'},
                    showlegend: false
                  },
                    { values: [b1, b1_s-b1, b2_s],
                    rotation: 90,
                    text: ['', ''],
                    marker: {colors:['rgba(255, 127, 0, .5)','rgba(100, 255, 255, 0)','rgba(255, 255, 255, 0)']},
                    hole: .5,
                    type: 'pie',
                    showlegend: false
                    }];
var data2 = [{ type: 'category',
                    x: [0], y:[0],
                    marker: {size: 28, color:'850000'},
                    showlegend: false
                  },
                    { values: [b2, b2_s-b2, b1_s],
                    rotation: 90,
                    text: ['', ''],
                    marker: {colors:['rgba(255, 127, 0, .5)','rgba(100, 255, 255, 0)','rgba(255, 255, 255, 0)']},
                    hole: .5,
                    type: 'pie',
                    showlegend: false
                    }];

                    var layout = {
                    shapes:[{
                    type: 'path',
                    fillcolor: '850000',
                    line: {
                    color: '850000'
                    }
                    }],
                    title: '#patients (ExpiryFlag=1)',
                    height: 500,
                    width: 600,
                    xaxis: {type:'category',zeroline:false, showticklabels:false,
                    showgrid: false, range: [-1, 1]},
                    yaxis: {type:'category',zeroline:false, showticklabels:false,
                    showgrid: false, range: [-1, 1]}
                    };

                    Plotly.newPlot('b1', data, layout);
      
                    Plotly.newPlot('b2', data2, layout);
      $('#loading').html('-');
    }
  });

}