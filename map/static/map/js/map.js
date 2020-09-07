
$(document).ready(function () {

    let country_data = JSON.parse(document.getElementById('country_data').textContent);
    // console.log(createSeries(country_data))
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
                color: "#1A1A1D",
                fontWeight: "bold",
            }
        },

        chart: {
            animation: false, // Disable animation, especially for zooming
            backgroundColor: "#CCCCCC",
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
                to: 3000,
                color: "#488f31"
            }, {
                from: 3000,
                to: 10000,
                color: "#ffa600"

            }, {
                from: 10000,
                color: "#f95d6a"
            }]
        },

        mapNavigation: {
            enabled: true
        },
        // Limit zoom range
        yAxis: {
            minRange: 2300
        },

        tooltip: {
            useHTML: true
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
                    var hoverCases = this.hoverCases; // Used by pie only
                    return '<b>' + this.name + ' Stats</b><br />' +
                        Highcharts.map([
                            ['Cases', this.cases, cases_color],
                            ['Deaths', this.deaths, deaths_color],
                            ['Recovered', this.recovered, recovered_color]
                        ], function (line) {
                            return '<span style="color:' + line[2] +
                                // Colorized bullet
                                '">\u25CF</span> ' +
                                // Party and votes
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
    function createSeries(obj_in) {
        var obj_out = [];
        obj_in.forEach(function (obj) {
            obj_out.push({
                name: obj["country"],
                code: obj["code"],
                cases: obj["cases"],
                todayCases: obj["todayCases"],
                deaths: obj["deaths"],
                recovered: obj["recovered"],
                population: obj["country_population"],
                casesPerOneMillion: obj["casesPerOneMillion"],
                deathsPerOneMillion: obj["deathsPerOneMillion"],
            });
        });
        // console.log("begin", obj_out);
        return obj_out;
    };
});