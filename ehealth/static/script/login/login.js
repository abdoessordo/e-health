// Login As
const login_as = document.querySelector(".landing .left main form .row.login-as h3.text-muted")
toggle_login_as_menu = (btn) => {
    btn.querySelector("span").classList.toggle("flip_180")
    document.querySelector("#login-as-menu").classList.toggle("hide")
}

set_login_as_value = (value, num) => {
    document.querySelector("input#login").value = num
    document.querySelector("#login-as-menu").classList.add("hide")
    login_as.innerHTML = value.innerHTML
    login_as.style.color = "#363949"
}