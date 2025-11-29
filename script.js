document.addEventListener("DOMContentLoaded", () => {

    const stockForm = document.getElementById("stock-form");
    const stockSymbolInput = document.getElementById("stock-symbol");
    const predictBtn = document.getElementById("predict-btn");
    
    const predictionResultEl = document.getElementById("prediction-result");
    const sentimentResultEl = document.getElementById("sentiment-result");
    
    const chartCtx = document.getElementById("stock-chart").getContext("2d");
    let stockChart; 

    stockForm.addEventListener("submit", handlePrediction);

    async function handlePrediction(event) {
        event.preventDefault(); 
        
        const stockSymbol = stockSymbolInput.value.toUpperCase();
        if (!stockSymbol) {
            alert("Please enter a stock symbol.");
            return;
        }

        predictBtn.textContent = "Analyzing...";
        predictBtn.disabled = true;
        predictionResultEl.textContent = "Loading...";
        sentimentResultEl.textContent = "Loading...";

        try {
            const response = await fetch('http://127.0.0.1:5000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ symbol: stockSymbol }),
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.error || `HTTP error! Status: ${response.status}`);
            }

            const data = await response.json();
            
            updateUI(data);

        } catch (error) {
            console.error("Error fetching prediction:", error);
            predictionResultEl.textContent = "Error";
            sentimentResultEl.textContent = "Error";
            alert(`Error: ${error.message}`);
        } finally {
            predictBtn.textContent = "PREDICT THE FUTURE";
            predictBtn.disabled = false;
        }
    }

    function updateUI(data) {
        predictionResultEl.textContent = data.prediction_trend || "N/A";
        sentimentResultEl.textContent = data.sentiment_score || "N/A";

        if (stockChart) {
            stockChart.destroy(); 
        }

        stockChart = new Chart(chartCtx, {
            type: 'line',
            data: {
                labels: [...data.history.dates, ...data.forecast.dates],
                datasets: [
                    {
                        label: 'Historical Price',
                        data: data.history.prices,
                        borderColor: 'blue',
                        fill: false,
                    },
                    {
                        label: 'Forecasted Price',
                        data: [...Array(data.history.prices.length).fill(null), ...data.forecast.prices],
                        borderColor: 'green',
                        borderDash: [5, 5],
                        fill: false,
                    }
                ]
            },
            options: {
                responsive: true,
                plugins: {
                    title: {
                        display: true,
                        text: `Stock Price Prediction for ${stockSymbolInput.value.toUpperCase()}`
                    }
                },
                scales: {
                    x: {
                        title: { display: true, text: 'Date' }
                    },
                    y: {
                        title: { display: true, text: 'Price' }
                    }
                }
            }
        });
    }
});