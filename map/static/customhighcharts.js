var json = [{
    "country": "Ireland",
    "code": "IRL",
    "Confirmed": "3000",
    "Deaths": "100",
    "Recovered": "2900",
}, {
    "country": "England",
    "code": "ENG",
    "Confirmed": "3000",
    "Deaths": "100",
    "Recovered": "2900",

}];



var chart = Highcharts.mapChart('container', {
    title: {
        text: 'USA 2016 Presidential Election Results'
    },

    chart: {
        animation: false // Disable animation, especially for zooming
    },

    colorAxis: {
        dataClasses: [{
            from: -1,
            to: 0,
            color: 'rgba(244,91,91,0.5)',
            name: 'Deaths'
        }, {
            from: 0,
            to: 1,
            color: 'rgba(124,181,236,0.5)',
            name: 'Recovered'
        }, {
            from: 2,
            to: 3,
            name: 'Cases',
            color: CasesColor
        }, {
            from: 3,
            to: 4,
            name: 'Green',
            color: grnColor
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

    // Default options for the pies
    plotOptions: {
        mappie: {
            borderColor: 'rgba(255,255,255,0.4)',
            borderWidth: 1,
            tooltip: {
                headerFormat: ''
            }
        }
    },

    series: [{
        mapData: Highcharts.maps['custom/world'],
        data: data,
        name: 'name',
        borderColor: '#FFF',
        showInLegend: false,
        joinBy: ['iso-a3', 'code'],
        keys: ['id', 'demVotes', 'repVotes', 'libVotes', 'grnVotes',
            'sumVotes', 'value', 'pieOffset'],
        tooltip: {
            headerFormat: '',
            pointFormatter: function () {
                var hoverStats = this.hoverStats; // Used by pie only
                return '<b>' + this.id + ' votes</b><br/>' +
                    Highcharts.map([
                        ['Cases', this.Cases, CasesColor],
                        ['Deaths', this.Deaths, DeathsColor],
                        ['Recovered', this.Recovered, RecoveredColor],
                        ['Green', this.grnVotes, grnColor]
                    ].sort(function (a, b) {
                        return b[1] - a[1]; // Sort tooltip by most votes
                    }), function (line) {
                        return '<span style="color:' + line[2] +
                            // Colorized bullet
                            '">\u25CF</span> ' +
                            // Party and votes
                            (line[0] === hoverVotes ? '<b>' : '') +
                            line[0] + ': ' +
                            Highcharts.numberFormat(line[1], 0) +
                            (line[0] === hoverVotes ? '</b>' : '') +
                            '<br/>';
                    }).join('') +
                    '<hr/>Total: ' + Highcharts.numberFormat(this.sumVotes, 0);
            }
        }
    }, {
        name: 'Separators',
        id: 'us-all',
        type: 'mapline',
        data: Highcharts.geojson(Highcharts.maps['custom/world'], 'mapline'),
        color: '#707070',
        showInLegend: false,
        enableMouseTracking: false
    }, {
        name: 'Connectors',
        type: 'mapline',
        color: 'rgba(130, 130, 130, 0.5)',
        zIndex: 5,
        showInLegend: false,
        enableMouseTracking: false
    }]
});


chart.redraw();