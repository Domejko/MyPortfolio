var tablinks = document.getElementsByClassName('tab-links');
var tabcontent = document.getElementsByClassName('tab-content');

function opentab(tabname) {
    for (var tablink of tablinks) {
        tablink.classList.remove('active-link');
    }
    for (var tabcon of tabcontent) {
        tabcon.classList.remove('active-tab');
    }
    event.target.classList.add('active-link');
    document.getElementById(tabname).classList.add('active-tab');
}