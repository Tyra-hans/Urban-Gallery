function CopyFunction() {
    var copyText = document.getElementById("myInput");
    copyText.select();
    document.execCommand("copy");
    alert("Copied the text: " + copyText.value);
}