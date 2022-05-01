// Set the date we're counting down to
var countDownDate = new Date("Nov 18, 2025");

// Update the count down every 1 second
var x = setInterval(function () {

    // Get today's date and time
    var now = new Date();

    // Find the distance between now and the count down date
    var distance = countDownDate - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));

    // Display the result in the element with id="demo"
    document.getElementById("1-1").innerHTML = days + "d ";

    // If the count down is finished, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("1-1").innerHTML = "履約期限到期";
    }
}, 1000);