

/* AJAX */
const meds = document.querySelector('#med-name-1');
function search(event){
    
    const x =event.target.getAttribute("id").split("-")[2]
    
    const result = document.querySelector("#result-"+x);
    console.log(result)
    result.style.display="block"
    const val = { 'med': event.target.value+String.fromCharCode(event.keyCode) };
    fetch('/ordonnance/get_med',{
    method: 'POST',
    'Content-Type': 'application/json',
    body: JSON.stringify(val),
  })
  .then(response => response.json())
  .then(data=>{

    
    console.log(data)
    for(i=0;i<5;i++){
        try{
        result.removeChild(result.firstChild);
        }
        catch(error){

        }
    }
    for(i=0;i<5;i++){
        med_det=data[i]["fields"]
        opt=document.createElement("option")
        opt.value=data[i]["pk"]
        opt.className="ajax_option"
        opt.textContent=med_det["nom"]+" "+med_det["dosage1"]
        result.appendChild(opt)
    }
    
    
  
})
}
try{
    meds.addEventListener('keydown', search,false);}

catch(error){}

const select_element = document.querySelector('#result-1');

function toggle_off(evt){
     optionSelected = event.target.options[event.target.selectedIndex]
     text = optionSelected.textContent;
     console.log(event.target.previousSibling)
     event.target.previousSibling.value=text
     event.target.style.display="none"
}
try{
select_element.addEventListener('change', toggle_off,false);}
catch(error){}
/* AJAX */
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
        inner_row=document.createElement('div')
        label=document.createElement('label')
        select=document.createElement('select')
        input=document.createElement('input')
        label.textContent="Drug Name"
  
        input.className="input-ajax"
        input.placeholder="Enter Drug"
        input.id ="med-name-"+row_num
        select.id="result-"+row_num
        select.name="med"
        select.size=5
        select.hidden=true
        select.className="select-ajax"
        row.appendChild(inner_row)
        inner_row.appendChild(label)
        inner_row.appendChild(input)
        inner_row.appendChild(select)
        

        row.innerHTML += `
            

            <div>
                <label for="">Quantity Per day</label>
            <input class="primary ajax-primary" type="number" name="quant" value="1">

            </div>

            <div>
                <label for="">Usage Description</label>
                    <textarea class="primary " rows="1" name="desc" placeholder="Enter Descpritption"></textarea>
            </div>

            <div>
                <span id="delete-row-${row_num}" onclick=delete_row(this.id) class="material-icons-sharp">delete</span>
            </div>
        `
    } else if (type === 'trait') {
           row.innerHTML = `
            <div>
                <label for="">Traitement</label>
                 <input class="primary" type="text" name="traitements" placeholder="Enter Traitement">
            </div>

            <div>
                <label for="">Traitement Description</label>
                    <textarea class="primary" rows="1" name="desc"placeholder="Enter Descpritption"></textarea>
            </div>
            <div>
                                <label for="">Traitement Price</label>
                                <input class="primary" type="number" placeholder="Enter Price"></input>
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


const add_row = (event) => {
    event = event || window.event; // for firefox
    type=event.target.getAttribute("type_btn")
    let new_row = create_row(type, i)
    let form_holder = document.querySelector(`#form-${type}>.rows`);
    try{
    form_holder.appendChild(new_row);}
    catch(error){
        i--;
            console.log(form_holder)
            console.log(new_row)
            console.log(event.target)
    }
    if (type=="med"){
    document.querySelector(`#${input.id}`).addEventListener('keydown', search,false);
    document.querySelector(`#${select.id}`).addEventListener('change', toggle_off,false);}
}
const add_more = document.querySelector('#add_btn_med');
add_more.addEventListener('click', add_row,false);