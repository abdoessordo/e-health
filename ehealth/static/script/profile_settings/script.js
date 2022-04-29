
// show forms
const show_form = (id) => {
    switch (id) {
        case "insrurance-btn":
            document.querySelector("main .section-1 .rows.privacy-settings form").classList.toggle("hide-from")
            break;

        case "become-doctor-btn":
            document.querySelector(".rigth .section-1 .rows.privacy-settings form.become-doctor-form").classList.toggle("hide-from")
            break

        case "become-pharmacist-btn":
            document.querySelector(".rigth .section-1 .rows.privacy-settings form.become-pharmacist-form").classList.toggle("hide-from")
            break

        default:
            break;
    }
}

// Editing
const switching = (i) => {
    document.querySelectorAll(`.form-row input, .form-row button h4 `).forEach(inp => {
        inp.classList.remove('edit-on')
        inp.setAttribute("readonly", "")
        inp.classList.remove('red-color')
    })

    document.querySelector(`.form-row button#edit-${i} h4`).classList.add('red-color')
    inp = document.getElementById("input-" + i);
    inp.removeAttribute("readonly")
    inp.classList.toggle('edit-on')
}




window.addEventListener("click", e => {
    clicked = false
    let all_form_elements = document.querySelectorAll(`.form-row input, .form-row button h4 `);
    for (let i = 0; i < all_form_elements.length; i++) {
        console.log(all_form_elements[i]);
        if (e.target === all_form_elements[i]) {
            clicked = true
            break
        }
    }
    console.log(clicked);
    if (!clicked) {
        document.querySelectorAll(`.form-row input, .form-row button h4 `).forEach(inp => {
            inp.classList.remove('edit-on')
            inp.setAttribute("readonly", "")
            inp.classList.remove('red-color')
        })
    }
})

const privacy_toggle=document.getElementById("privacy")

privacy_toggle.addEventListener("change", e => {
    privacy=document.getElementById("input-privacy")
    privacy.value=event.target.value
})

const submit_btn_settings=document.getElementById("submit_btn_settings")

submit_btn_settings.addEventListener("click", e => {
    form1=document.getElementById("form-profile")
    form2=document.getElementById("form-assur")
    form3=document.getElementById("form-doc")
    form4=document.getElementById("form-pharma")
    fetch(form1.action, {method:'post', body: new FormData(form1)});
    fetch(form2.action, {method:'post', body: new FormData(form2)});
    fetch(form3.action, {method:'post', body: new FormData(form3)});
    fetch(form4.action, {method:'post', body: new FormData(form4)});
    console.log("CLIIIIIIIIIICKED")



})

