//  https://www.highcharts.com/demo/maps/map-pies
//  changed this example to my needs
$(document).ready(function () {

    let country_data = JSON.parse(document.getElementById('country_data').textContent);
    
    
    // Move into Test.js
    var my_json = [
        {
            "country": "England",
            "code": "GB",
            "cases": "3000",
            "deaths": "100",
            "recovered": "2900",
            "deaths_per_100k": "number of deaths/population"

        }, {
            "country": "Ireland",
            "code": "IE",
            "Confirmed": "3000",
            "Deaths": "100",
            "Recovered": "2900",
        }, {
            "country": "France",
            "code": "FR",
            "cases": "1000",
            "deaths": "333",
            "recovered": "1"
        }];

    var cases_color = '#ffa600'
    var deaths_color = '#d45087'
    var recovered_color = '#003f5c'


    // Pass from settings.py
    var green_threshold = 3000
    var red_threshold = 10000

    var json_array = [];
    for (i = 0; i < my_json.length; i++) {
        json_array.push([my_json[i].code, parseInt(my_json[i].Confirmed),
        parseInt(my_json[i].Deaths),
        parseInt(my_json[i].Recovered)]);
    }
    let chart_container = document.getElementById("container")
    var chart = Highcharts.mapChart(chart_container, {
        title: {
            text: 'Covid Cases',
            style: {
                color: "#41b085",
                fontWeight: "bold",
            }
        },

        chart: {
            animation: false,
            backgroundColor: "#bee0d3",
        },
        legend: {
            title: {
                text: 'Cases per 1 million population',
                style: {
                    color: "#026670"
                }
            },
            align: 'left',
            verticalAlign: 'bottom',
            floating: true,
            layout: 'vertical',
            valueDecimals: 0,
            backgroundColor: (Highcharts.theme && Highcharts.theme.legendBackgroundColor) || 'rgba(255, 255, 255, 0.85)',
            symbolRadius: 0,
            symbolHeight: 14
        },

        colorAxis: {
            dataClasses: [{
                to: green_threshold,
                color: "#488f31"
            }, {
                from: green_threshold,
                to: red_threshold,
                color: "#ffa600"

            }, {
                from: red_threshold,
                color: "#f95d6a"
            }]
        },

        mapNavigation: {
            enabled: true
        },
        yAxis: {
            minRange: 1000
        },
        tooltip: {
            useHTML: true,
        },
        series: [{
            mapData: Highcharts.maps['custom/world'],
            data: country_data,
            name: "test",
            borderColor: '#FFF',
            showInLegend: false,
            joinBy: ['iso-a2', 'code'],
            colorKey: "casesPerOneMillion",
            keys: ['code', "country", 'confirmed', 'deaths', 'recovered'],
            tooltip: {
                headerFormat: '',
                pointFormatter: function () {
                    var hoverCases = this.hoverCases;
                    return '<b>' + this.name + '</b><br />' +
                        Highcharts.map([
                            ['Cases', this.cases, cases_color],
                            ['Deaths', this.deaths, deaths_color],
                            // Some country dont report recovered numbers and these show as 0
                            ['Recovered', this.recovered, recovered_color]
                        ], function (line) {
                            return '<span style="color:' + line[2] +
                                '">\u25CF</span> ' +
                                (line[0] === hoverCases ? '<b>' : '') +
                                line[0] + ': ' +
                                Highcharts.numberFormat(line[1], 0) +
                                (line[0] === hoverCases ? '</b>' : '') +
                                '<br/>';
                        }).join("")
                }
            }
        }]
    });
    
});