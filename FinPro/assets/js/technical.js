Highcharts.theme = {
    colors: ['#2b908f', '#90ee7e', '#f45b5b', '#7798BF', '#aaeeee', '#ff0066',
        '#eeaaee', '#55BF3B', '#DF5353', '#7798BF', '#aaeeee'],
    chart: {
        backgroundColor: {
            linearGradient: {x1: 0, y1: 0, x2: 1, y2: 1},
            stops: [
                [0, '#212529'],
                [1, '#212229']
            ]
        },
        style: {
            fontFamily: '\'Unica One\', sans-serif'
        },
        plotBorderColor: '#606063'
    },
    title: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase',
            fontSize: '20px'
        }
    },
    subtitle: {
        style: {
            color: '#E0E0E3',
            textTransform: 'uppercase'
        }
    },
    xAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        title: {
            style: {
                color: '#A0A0A3'

            }
        }
    },
    yAxis: {
        gridLineColor: '#707073',
        labels: {
            style: {
                color: '#E0E0E3'
            }
        },
        lineColor: '#707073',
        minorGridLineColor: '#505053',
        tickColor: '#707073',
        tickWidth: 1,
        title: {
            style: {
                color: '#A0A0A3'
            }
        }
    },
    tooltip: {
        backgroundColor: 'rgba(0, 0, 0, 0.85)',
        style: {
            color: '#F0F0F0'
        }
    },
    plotOptions: {
        series: {
            dataLabels: {
                color: '#B0B0B3'
            },
            marker: {
                lineColor: '#333'
            }
        },
        boxplot: {
            fillColor: '#505053'
        },
        candlestick: {
            lineColor: 'white'
        },
        errorbar: {
            color: 'white'
        }
    },
    legend: {
        itemStyle: {
            color: '#E0E0E3'
        },
        itemHoverStyle: {
            color: '#FFF'
        },
        itemHiddenStyle: {
            color: '#606063'
        }
    },
    credits: {
        style: {
            color: '#666'
        }
    },
    labels: {
        style: {
            color: '#707073'
        }
    },

    drilldown: {
        activeAxisLabelStyle: {
            color: '#F0F0F3'
        },
        activeDataLabelStyle: {
            color: '#F0F0F3'
        }
    },

    navigation: {
        buttonOptions: {
            symbolStroke: '#DDDDDD',
            theme: {
                fill: '#505053'
            }
        }
    },

    // scroll charts
    rangeSelector: {
        buttonTheme: {
            fill: '#505053',
            stroke: '#000000',
            style: {
                color: '#CCC'
            },
            states: {
                hover: {
                    fill: '#707073',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                },
                select: {
                    fill: '#000003',
                    stroke: '#000000',
                    style: {
                        color: 'white'
                    }
                }
            }
        },
        inputBoxBorderColor: '#505053',
        inputStyle: {
            backgroundColor: '#333',
            color: 'silver'
        },
        labelStyle: {
            color: 'silver'
        }
    },

    navigator: {
        handles: {
            backgroundColor: '#666',
            borderColor: '#AAA'
        },
        outlineColor: '#CCC',
        maskFill: 'rgba(255,255,255,0.1)',
        series: {
            color: '#7798BF',
            lineColor: '#A6C7ED'
        },
        xAxis: {
            gridLineColor: '#505053'
        }
    },

    scrollbar: {
        barBackgroundColor: '#808083',
        barBorderColor: '#808083',
        buttonArrowColor: '#CCC',
        buttonBackgroundColor: '#606063',
        buttonBorderColor: '#606063',
        rifleColor: '#FFF',
        trackBackgroundColor: '#404043',
        trackBorderColor: '#404043'
    },

    // special colors for some of the
    legendBackgroundColor: 'rgba(0, 0, 0, 0.5)',
    background2: '#505053',
    dataLabelsColor: '#B0B0B3',
    textColor: '#C0C0C0',
    contrastTextColor: '#F0F0F3',
    maskColor: 'rgba(255,255,255,0.3)'
};

// Apply the theme
Highcharts.setOptions(Highcharts.theme);

Highcharts.chart('technical', {
    chart: {
        type: 'area',
        zoomType: 'xy',
        height: 489
    },

    credits: {
            enabled: false
        },

    title: {
        text: 'ETH-BTC Market Depth'
    },

    xAxis: {
        minPadding: 0,
        maxPadding: 0,
        plotLines: [{
            color: '#888',
            value: 0.1523,
            width: 1,
            label: {
                text: 'Actual price',
                rotation: 90
            }
        }],
        title: {
            text: 'Price'
        }
    },
    yAxis: [{
        lineWidth: 1,
        gridLineWidth: 1,
        title: null,
        tickWidth: 1,
        tickLength: 5,
        tickPosition: 'inside',
        labels: {
            align: 'left',
            x: 8
        }
    }, {
        opposite: true,
        linkedTo: 0,
        lineWidth: 1,
        gridLineWidth: 0,
        title: null,
        tickWidth: 1,
        tickLength: 5,
        tickPosition: 'inside',
        labels: {
            align: 'right',
            x: -8
        }
    }],
    legend: {
        enabled: false
    },
    plotOptions: {
        area: {
            fillOpacity: 0.2,
            lineWidth: 1,
            step: 'center'
        }
    },
    tooltip: {
        headerFormat: '<span style="font-size=10px;">Price: {point.key}</span><br/>',
        valueDecimals: 2
    },
    series: [{
        name: 'Bids',
        data: [
            [
                0.1524,
                0.948665
            ],
            [
                0.1539,
                35.510715
            ],
            [
                0.154,
                39.883437
            ],
            [
                0.1541,
                40.499661
            ],
            [
                0.1545,
                43.262994000000006
            ],
            [
                0.1547,
                60.14799400000001
            ],
            [
                0.1553,
                60.30799400000001
            ],
            [
                0.1558,
                60.55018100000001
            ],
            [
                0.1564,
                68.381696
            ],
            [
                0.1567,
                69.46518400000001
            ],
            [
                0.1569,
                69.621464
            ],
            [
                0.157,
                70.398015
            ],
            [
                0.1574,
                70.400197
            ],
            [
                0.1575,
                73.199217
            ],
            [
                0.158,
                77.700017
            ],
            [
                0.1583,
                79.449017
            ],
            [
                0.1588,
                79.584064
            ],
            [
                0.159,
                80.584064
            ],
            [
                0.16,
                81.58156
            ],
            [
                0.1608,
                83.38156
            ]
        ],
        color: '#03a7a8'
    }, {
        name: 'Asks',
        data: [
            [
                0.1435,
                242.521842
            ],
            [
                0.1436,
                206.49862099999999
            ],
            [
                0.1437,
                205.823735
            ],
            [
                0.1438,
                197.33275
            ],
            [
                0.1439,
                153.677454
            ],
            [
                0.144,
                146.007722
            ],
            [
                0.1442,
                82.55212900000001
            ],
            [
                0.1443,
                59.152814000000006
            ],
            [
                0.1444,
                57.942260000000005
            ],
            [
                0.1445,
                57.483850000000004
            ],
            [
                0.1446,
                52.39210800000001
            ],
            [
                0.1447,
                51.867208000000005
            ],
            [
                0.1448,
                44.104697
            ],
            [
                0.1449,
                40.131217
            ],
            [
                0.145,
                31.878217
            ],
            [
                0.1451,
                22.794916999999998
            ],
            [
                0.1453,
                12.345828999999998
            ],
            [
                0.1454,
                10.035642
            ],
            [
                0.148,
                9.326642
            ],
            [
                0.1522,
                3.76317
            ]
        ],
        color: '#fc5857'
    }]
});
