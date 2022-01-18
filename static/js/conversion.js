function convert() {
    fetch("http://data.fixer.io/api/latest?access_key=93cae40df10b0521f99e1271a38794b9&base=EUR&symbols=INR,USD")
        .then(response => response.json())
        .then(data => {
            if (document.getElementById("select-value").value === "USD") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * data.rates.USD
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
            } else if (document.getElementById("select-value").value === "INR") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * data.rates.INR
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
            } else if (document.getElementById("select-value").value === "EUR") {
                for (var element of document.getElementsByClassName("change")) {
                    element.innerHTML = element.getAttribute("value")
                }
            }
        }).catch(reject => {
            console.log(reject)
            if (document.getElementById("select-value").value === "USD") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * 1.14
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
            } else if (document.getElementById("select-value").value === "INR") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * 84.81
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
            } else if (document.getElementById("select-value").value === "EUR") {
                for (var element of document.getElementsByClassName("change")) {
                    element.innerHTML = element.getAttribute("value")
                }
            }
        });
}