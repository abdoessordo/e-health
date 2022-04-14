
let add_med_btn = document.querySelector("#add_btn_med");
let add_trait_btn = document.querySelector("#add_btn_trait");

let med_form = document.querySelector("#med-form");
let trait_form = document.querySelector("#trait-form");

btns = [add_med_btn, add_trait_btn]

let new_med = `<div class="row">
                    <div class="col-4">
                        <label for="exampleInputEmail1">Nom Medicament</label>
                        <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter medicament">
                    </div>
                    <div class="col-2">
                        <label for="exampleInputEmail1">Quantite par jour</label>
                        <input type="number" class="form-control" id="exampleInputEmail1" value="1">

                    </div>
                    <div class="col-6">
                        <label for="exampleInputEmail1">Description d utilisation</label>
                        <textarea class="form-control" id="exampleFormControlTextarea1" rows="1"></textarea>

                    </div>
                </div>`

let new_trait = `<div class="row">
                        <div class="col-4">
                            <label for="exampleInputEmail1">Nom Traitement</label>
                            <input type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter traitement">
                        </div>

                        <div class="col-8">
                            <label for="exampleInputEmail1">Description du Traitement</label>
                            <textarea class="form-control" id="exampleFormControlTextarea1" rows="1"></textarea>

                        </div>
                    </div>`


btns.forEach(btn => {
    btn.addEventListener('click', (btn)=>{
        let id = btn['target']['id']
        if(id == 'add_btn_med'){
            med_form.innerHTML += new_med
        }else if(id == 'add_btn_trait'){
            trait_form.innerHTML += new_trait
        }
    })
});


