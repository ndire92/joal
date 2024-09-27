document.addEventListener("DOMContentLoaded", function() {
    // Your Chart.js code here
	const djangoData = {
            labels: [
                {% for act in acts %}
                    "{{ act.ActPech_Artisan }}",
                {% endfor %}
            ],
            datasets: [
                {
                    label: '2020',
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1,
                    data: [
                        {% for act in acts %}
                            {% if act.annee_modification == 2020 %}
                                {{ act.NbrActeur }},
                            {% else %}
                                0,
                            {% endif %}
                        {% endfor %}
                    ],
                    hidden: false
                },
                {
                    label: '2021',
                    backgroundColor: 'rgba(54, 162, 235, 0.2)',
                    borderColor: 'rgba(54, 162, 235, 1)',
                    borderWidth: 1,
                    data: [
                        {% for act in acts %}
                            {% if act.annee_modification == 2021 %}
                                {{ act.NbrActeur }},
                            {% else %}
                                0,
                            {% endif %}
                        {% endfor %}
                    ],
                    hidden: true
                },
                {
                    label: '2022',
                    backgroundColor: 'rgba(255, 206, 86, 0.2)',
                    borderColor: 'rgba(255, 206, 86, 1)',
                    borderWidth: 1,
                    data: [
                        {% for act in acts %}
                            {% if act.annee_modification == 2022 %}
                                {{ act.NbrActeur }},
                            {% else %}
                                0,
                            {% endif %}
                        {% endfor %}
                    ],
                    hidden: true
                }
            ]
        };

        // Get the canvas element
        const ctx = document.getElementById('acteur').getContext('2d');

        // Create the chart
        const acteur = new Chart(ctx, {
            type: 'bar',
            data: djangoData,
            options: {
                scales: {
                    yAxes: [{
                        ticks: {
                            beginAtZero: true
                        }
                    }]
                }
            }
        });

        // Function to toggle visibility of bars for a specific year
        function toggleVisibility(yearIndex) {
            const dataset = acteur.data.datasets[yearIndex];
            dataset.hidden = !dataset.hidden;
            acteur.update();
        }
  
  
});

