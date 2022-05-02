let calendar = document.querySelector('.calendar')
let month_list = calendar.querySelector('.month-list')
let month_picker = calendar.querySelector('#month-picker')
const month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']


remove_selected = () => {
    let all_days = document.querySelectorAll(".calendar-day-hover")
    all_days.forEach(day => {
        day.classList.remove('selected-day')
    })
}

get_selected_date = (day, month, year) => {
    month = month_names.indexOf(month) + 1
    if (month < 10) {
        month = `0${month}`
    }

    if (parseInt(day) < 10) {
        day = `0${day}`
    }
    let selected_date = `${year}-${month}-${day}`

    console.log(selected_date);
    document.querySelector("#appointement-date").value = selected_date
}

listned_to_date_select = (month, year) => {
    let all_days = document.querySelectorAll(".calendar-day-hover")
    all_days.forEach(day => {
        day.addEventListener("click", () => {
            remove_selected()
            day.classList.add('selected-day')
            let selected_day = day.innerHTML.split("<h3>")[1].split("<span></span>")[0].trim()
            console.log(selected_day);
            get_selected_date(selected_day, month, year)
        })
    });

}


isLeapYear = (year) => {
    return (year % 4 === 0 && year % 100 !== 0 && year % 400 !== 0) || (year % 100 === 0 && year % 400 === 0)
}

getFebDays = (year) => {
    return isLeapYear(year) ? 29 : 28
}

generateCalendar = (month, year) => {

    let calendar_days = calendar.querySelector('.calendar-days')
    let calendar_header_year = calendar.querySelector('#year')

    let days_of_month = [31, getFebDays(year), 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    calendar_days.innerHTML = ''

    let currDate = new Date()
    if (!month) month = currDate.getMonth()
    if (!year) year = currDate.getFullYear()

    let curr_month = `${month_names[month]}`
    month_picker.innerHTML = curr_month
    calendar_header_year.innerHTML = year

    // get first day of month

    let first_day = new Date(year, month, 1)

    for (let i = 0; i <= days_of_month[month] + first_day.getDay() - 1; i++) {
        let day = document.createElement('div')
        if (i >= first_day.getDay()) {
            day.classList.add('calendar-day-hover', 'text-muted')
            day.innerHTML = `
            <h3>
                ${i - first_day.getDay() + 1}
                <span></span> 
                <span></span> 
                <span></span> 
                <span></span>
            </h3>`
            if (i - first_day.getDay() + 1 === currDate.getDate() && year === currDate.getFullYear() && month === currDate.getMonth()) {
                day.classList.add('curr-date')
            }
        }
        calendar_days.appendChild(day)
    }
    listned_to_date_select(curr_month, year)
}


month_names.forEach((e, index) => {
    let month = document.createElement('div')
    month.innerHTML = `<div data-month="${index}"><h3>${e}</h3></div>`
    month.querySelector('div').onclick = () => {
        month_list.classList.remove('show')
        curr_month.value = index
        generateCalendar(index, curr_year.value)
    }
    month_list.appendChild(month)
})


month_picker.onclick = () => {
    month_list.classList.add('show')
}

let currDate = new Date()

let curr_month = {
    value: currDate.getMonth()
}
let curr_year = {
    value: currDate.getFullYear()
}

generateCalendar(curr_month.value, curr_year.value)

document.querySelector('#prev-year').onclick = () => {
    --curr_year.value
    generateCalendar(curr_month.value, curr_year.value)
}

document.querySelector('#next-year').onclick = () => {
    ++curr_year.value
    generateCalendar(curr_month.value, curr_year.value)
}

const all_intervals = document.querySelectorAll(".calendar-time .interval")

remove_active_all = () => {
    all_intervals.forEach(interval => {
        interval.classList.remove("active")
    })
}

all_intervals.forEach(interval => {
    interval.addEventListener("click", () => {
        remove_active_all()
        interval.classList.add("active")
        let time = interval.querySelector("h4").innerHTML.trim()
        document.querySelector("#appointement-time").value = time
    })
})
