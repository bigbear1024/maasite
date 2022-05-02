// Set the date we're counting down to
var countDownDate1_1 = new Date("Nov 18, 2025");

// Update the count down every 1 second
var x = setInterval(function () {

    // Get today's date and time
    var now = new Date();

    // Find the distance between now and the count down date
    var distance = countDownDate1_1 - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the element with id="demo"
    document.getElementById("1-1").innerHTML = days + "天" + hours + "小時"
        + minutes + "分鐘" + seconds + "秒";;


    // If the count down is finished, write some text 
    if (distance < 0) {
        clearInterval(x);
        document.getElementById("1-1").innerHTML = "履約期限已到期";
    }
}, 1000);

// Set the date we're counting down to
var countDownDate1_2 = new Date("Jul 26, 2025");

// Update the count down every 1 second
var y = setInterval(function () {

    // Get today's date and time
    var now = new Date();

    // Find the distance between now and the count down date
    var distance = countDownDate1_2 - now;

    // Time calculations for days, hours, minutes and seconds
    var days = Math.floor(distance / (1000 * 60 * 60 * 24));
    var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    // Display the result in the element with id="demo"
    document.getElementById("1-2").innerHTML = days + "天" + hours + "小時"
        + minutes + "分鐘" + seconds + "秒";;


    // If the count down is finished, write some text 
    if (distance < 0) {
        clearInterval(y);
        document.getElementById("1-2").innerHTML = "履約期限已到期";
    }
}, 1000);