function convert() {
    fetch("http://data.fixer.io/api/latest?access_key=93cae40df10b0521f99e1271a38794b9&base=EUR&symbols=INR,USD")
        .then(response => response.json())
        .then(data => {
            if (document.getElementById("select-value").value === "USD") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * data.rates.USD
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
                document.getElementById("EUR").removeAttribute("class")
                document.getElementById("USD").setAttribute("class", "active")
            } else if (document.getElementById("select-value").value === "INR") {
                for (var element of document.getElementsByClassName("change")) {
                    value = Number(element.getAttribute("value")) * data.rates.INR
                    element.innerHTML = (Math.ceil(value * 20) / 20).toFixed(2)
                }
                document.getElementById("EUR").removeAttribute("class")
                document.getElementById("INR").setAttribute("class", "active")
            } else if (document.getElementById("select-value").value === "EUR") {
                for (var element of document.getElementsByClassName("change")) {
                    // value = Number(element.getAttribute("value")) * data.rates.INR
                    element.innerHTML = element.getAttribute("value")
                    // (Math.ceil(value * 20) / 20).toFixed(2)
                }
            }
        });
}