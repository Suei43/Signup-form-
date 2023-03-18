setTimeout(()=>{
    $('#message').fadeOut('slow');
    // location.reload()
}, 3000);

let checkbox = document.getElementById("agree-term");

function Check() {
    if (!(checkbox.checked)) {
        checkbox.classList.remove('checked');
    } else {
        checkbox.classList.add('checked');
    }
}