try {

    const sideMenu = document.querySelector("aside")
    const menuBtn = document.querySelector("#menu-btn")
    const closeBtn = document.querySelector("#close-btn")
    const themeToggler = document.querySelector("#theme-toggler")


    // show sidebar
    menuBtn.addEventListener('click', () => {
        sideMenu.style.display = 'block';
    })

    // close sidebar
    closeBtn.addEventListener('click', () => {
        sideMenu.style.display = 'none';
    })

    // change theme
    themeToggler.addEventListener('click', () => {
        document.body.classList.toggle('dark-theme-variables')
        themeToggler.querySelector("span:first-child").classList.toggle('active')
        themeToggler.querySelector("span:last-child").classList.toggle('active')
    })



} catch (error) {

}

// drop down menu
const dropMenu = (btn) => {
    btn.querySelector("span").classList.toggle("flip_180")

    let dropdown = document.querySelector("ul.drop-down-content")
    dropdown.classList.toggle("show-drop-down")
}

// ADD FORM ROW
let i = 1;

const get_row_num = (id) => {
    return id.split('-')[2]
}

const create_row = (type, row_num) => {
    i++;
    let row = document.createElement('div')
    row.setAttribute('id', `row-${++row_num}`)
    row.setAttribute('class', 'form-row')
    if (type === 'med') {
        row.innerHTML = `
            <div>
                <label for="">Drug Name</label>
                <input class="primary" type="text" placeholder="Enter Drug">
            </div>

            <div>
                <label for="">Quantity Per day</label>
                <input class="primary" type="numebr" value="1">
            </div>

            <div>
                <label for="">Usage Description</label>
                <textarea class="primary" rows="1" placeholder="Enter Descpritption"></textarea>
            </div>

            <div>
                <span id="delete-row-${row_num}" onclick=delete_row(this.id) class="material-icons-sharp">delete</span>
            </div>
        `
    } else if (type === 'trait') {
        row.innerHTML = `
            <div>
                <label for="">Traitement</label>
                <input class="primary" type="text" placeholder="Enter Traitement">
            </div>

            <div>
                <label for="">Traitement Description</label>
                <textarea class="primary" rows="1" placeholder="Enter Descpritption"></textarea>
            </div>

            <div>
                <span id="delete-row-${row_num}" onclick=delete_row(this.id) class="material-icons-sharp">delete</span>
            </div>
        `
    }
    return row
}



const delete_row = (id) => {
    let row_id = `#row-${get_row_num(id)}`
    let row = document.querySelector(row_id)
    row.remove()
}


const add_row = (type) => {
    let new_row = create_row(type, i)
    let form_holder = document.querySelector(`#form-${type}>.rows`);
    form_holder.appendChild(new_row)
}
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
