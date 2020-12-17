// This file represents the code for displaying the portfolio chart on index.html
// Uses CanvasJS

window.onload = function () {
  var dataPoints = [];

  var chart = new CanvasJS.Chart("portfolioChart", {
    animationEnabled: true,
    theme: "light2",  // "light1", "light2", "dark1", "dark2",
    exportEnabled: true,
    title: {
      text: "Portfolio"
    },
    subtitles:[{
      text: ""
    }],
    axisX: {
      interval: 1,
      valueFormatString: "MMM"
    },
    axisY: {
      prefix: "$",
      title: "Price"
    },
    toolTip: {
      content: ""
    }.
    data: [{
      type: "candlestick",
      yValueFormatString: "$##0.00",
      dataPoints: dataPoints
    }]
  });
};
