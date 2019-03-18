// create three different series types for rendering the data
const candlestickSeries = fc.seriesSvgCandlestick()
	.bandwidth(3);

const bollingerAverageSeries = fc.seriesSvgLine()
	.mainValue(d => d.bollinger.average)
	.crossValue(d => d.date);

const bollingerAreaSeries = fc.seriesSvgArea()
  .mainValue(d => d.bollinger.upper)
  .baseValue(d => d.bollinger.lower)
  .crossValue(d => d.date);

// merge into a single series that is associated with the chart
const mergedSeries = fc.seriesSvgMulti()
	.series([bollingerAreaSeries, candlestickSeries, bollingerAverageSeries]);

// adapt the d3 time scale to add discontinuities, so that weekends are removed
const xScale = fc.scaleDiscontinuous(d3.scaleTime())
  .discontinuityProvider(fc.discontinuitySkipWeekends());

const chart = fc.chartSvgCartesian(
    xScale,
    d3.scaleLinear()
  )
	.yOrient('left')
	.plotArea(mergedSeries);

// use the extent component to determine the x and y domain
const durationDay = 864e5;
const xExtent = fc.extentDate()
	.accessors([d => d.date])
  // pad by one day on either side of the scale
	.padUnit('domain')
	.pad([durationDay, durationDay])

// the y extent is based on the upper / lower values, which provide the two extremes
const yExtent = fc.extentLinear()
	.accessors([d => d.high, d => d.low])
	.pad([0.1, 0.1])

const parseDate = d3.timeParse("%d-%b-%y");

const bollinger = fc.indicatorBollingerBands()
    .value(d => d.open);

d3.csv('data.csv',
  row => ({
  	open: Number(row.Open),
  	close: Number(row.Close),
  	high: Number(row.High),
  	low: Number(row.Low),
  	date: parseDate(row.Date)
	})).then(data => {
  
  	// the CSV data is in reverse date order
  	data = data.reverse();
  
  	// compute the bollinger bands
  	const bollingerData = bollinger(data);
  
    // merge into a single series
    const mergedData = data.map((d, i) =>
      Object.assign({}, d, {
        bollinger: bollingerData[i]
      })
    );
   
    // set the domain based on the data
    chart.xDomain(xExtent(mergedData))
      .yDomain(yExtent(mergedData))

    // select and render
    d3.select('#chart-element')
      .datum(mergedData)
      .call(chart);
  });