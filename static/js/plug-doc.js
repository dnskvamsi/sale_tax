function doc() {
    filename = '';
    var preHtml =
        "<html xmlns:o='urn:schemas-microsoft-com:office:office' xmlns:w='urn:schemas-microsoft-com:office:word' xmlns='http://www.w3.org/TR/REC-html40'><head><meta charset='utf-8'><title>Export HTML To Doc</title></head><body>";
    var postHtml = "</body></html>";
    var doc = "";
    for (let element of document.getElementsByClassName("head")) {
        doc = doc + element.getElementsByClassName("qty1")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("item-description1")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("price1")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("tax1")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("item-total")[0].innerText + "&emsp" + "&emsp"
        doc = doc + "<br>";
    }

    for (let element of document.getElementsByClassName("values")) {
        doc = doc + element.getElementsByClassName("qty")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("item-description")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("price")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("tax")[0].innerText + "&emsp" + "&emsp"
        doc = doc + element.getElementsByClassName("total")[0].innerText + "&emsp" + "&emsp"
        doc = doc + "<br>";
    }
    var html = preHtml + doc + postHtml;
    var blob = new Blob(['\ufeff', html], {
        type: 'application/msword'
    });

    // Specify link url
    var url = 'data:application/vnd.ms-word;charset=utf-8,' + encodeURIComponent(html);

    // Specify file name
    filename = filename ? filename + '.doc' : 'document.doc';

    // Create download link element
    var downloadLink = document.createElement("a");

    document.body.appendChild(downloadLink);

    if (navigator.msSaveOrOpenBlob) {
        navigator.msSaveOrOpenBlob(blob, filename);
    } else {
        // Create a link to the file
        downloadLink.href = url;

        // Setting the file name
        downloadLink.download = filename;

        //triggering the function
        downloadLink.click();
    }

    document.body.removeChild(downloadLink);
}