const ctx = document.getElementById('stockchart');

(async function() {

    new Chart(
        ctx,
        {
        type: 'line',
        options: {
            responsive: true,
            animation: false,
            elements: {
            point:{
                radius: 0
                },
            },
            plugins: {
            title: {
                display: true,
                text: ticker + ' Stock Chart'
            },
            legend: {
                display: false
            },
            tooltip: {
                //enabled: false
            }
            }
        },
        data: {
            labels: time,
            datasets: [
            {
                label: 'Closing price ($)',
                data: y_axis,
                borderColor: '#FF6384',
                borderWidth: 2,
                pointHitRadius: 7,
            }
            ]
        }
        }
    );
    })();