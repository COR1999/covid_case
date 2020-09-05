
$(document).ready(function () {

    let country_data = JSON.parse(document.getElementById('country_data').textContent);
    // console.log(country_data[0])
    var my_json = [
        {
            "country": "England",
            "code": "GB",
            "Confirmed": "3000",
            "Deaths": "100",
            "Recovered": "2900",
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
            "Confirmed": "1000",
            "Deaths": "333",
            "Recovered": "1"
        }];

    var confirmed_color = 'yellow'
    var deaths_color = 'red'
    var recovered_color = 'green'
    var json_array = [];
    for (i = 0; i < my_json.length; i++) {
        json_array.push([my_json[i].code, parseInt(my_json[i].Confirmed),
        parseInt(my_json[i].Deaths),
        parseInt(my_json[i].Recovered)]);
    }
    // console.log(json_array[0][0])
    let chart_container = document.getElementById("container")
    console.log(country_data)
    var chart = Highcharts.mapChart(chart_container, {

        title: {
            text: 'Covid Cases'
        },

        chart: {
            animation: false // Disable animation, especially for zooming
        },

        colorAxis: {
            dataClasses: [{
                name: 'Deaths',
                color: deaths_color
            }, {
                name: 'Recovered',
                color: recovered_color

            }, {
                name: 'Confirmed',
                color: confirmed_color,
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
            data: createSeries(country_data["fields"]),
            name: "test",
            borderColor: '#FFF',
            showInLegend: false,
            joinBy: ['iso-a2', 'code'],
            keys: ['code', "country", 'Confirmed', 'Deaths', 'Recovered'],
            tooltip: {
                headerFormat: '',
                pointFormatter: function () {
                    var hoverCases = this.hoverCases; // Used by pie only
                    return '<b>' + this.name + ' Stats</b><br />' +
                        Highcharts.map([
                            ['Confirmed', this.Confirmed, confirmed_color],
                            ['Deaths', this.Deaths, deaths_color],
                            ['Recovered', this.Recovered, recovered_color]
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
                Confirmed: obj["Confirmed"],
                Deaths: obj["Deaths"],
                Recovered: obj["Recovered"]
            });
        });
        // console.log("begin", obj_out);
        return obj_out;
    };
});