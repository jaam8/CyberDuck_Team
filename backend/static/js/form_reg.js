let last_name = document.querySelector("#last_name");
let first_name = document.querySelector("#first_name");
let patronymic = document.querySelector("#patronymic");
let phone_number = document.querySelector("#phone_number");
let number_of_snils = document.querySelector("#number_of_snils");
let series_number = document.querySelector("#series_number");
let issue_date = document.querySelector("#issue_date");
let who_issued = document.querySelector("#who_issued");
let department_code = document.querySelector("#department_code");
let dob = document.querySelector("#dob");
let place_of_birth = document.querySelector("#place_of_birth");


let users = {};


function Users(last_name, first_name, patronymic, phone_number, number_of_snils, series_number, issue_date, who_issued, department_code, dob, place_of_birth) {
    this.last_name = last_name;
    this.first_name = first_name;
    this.patronymic = patronymic;
    this.phone_number = phone_number;
    this.number_of_snils = number_of_snils;
    this.series_number = series_number;
    this.issue_date = issue_date;
    this.who_issued = who_issued;
    this.department_code = department_code;
    this.dob = dob;
    this.place_of_birth = place_of_birth;
}

function Id(users) {
    return Object.keys(users).length;
}

function valid() {
    let last_name, first_name, patronymic, phone_number, number_of_snils, series_number, issue_date, who_issued,
        department_code, dob, place_of_birth;
    if (last_name.value === '') {
        last_name.style.border = "1px solid red";

        document.getElementById("last_name_err").style.display = "block";
        last_name.focus();
        return false;
    } else {
        last_name_User = last_name.value;
    }
    if (first_name.value === '') {
        first_name.style.border = "1px solid red";

        document.getElementById("first_name_err").style.display = "block";
        first_name.focus();
        return false;
    } else {
        first_name_User = first_name.value;
    }
    if (patronymic.value === '') {
        patronymic.style.border = "1px solid red";

        document.getElementById("patronymic_err").style.display = "block";
        patronymic.focus();
        return false;
    } else {
        patronymic_User = patronymic.value;
    }
    if (phone_number.value === '') {
        phone_number.style.border = "1px solid red";
        document.getElementById("IDerr").style.display = "block";
        phone_number.focus();
        return false;
    } else if ((phone_number.value.length < 12) || (phone_number.value.length > 12)) {
        phone_number.style.border = "1px solid red";
        document.getElementById("IDLenthErr").style.display = "block";
        phone_number.focus();
        return false;
    } else {
        phone_number_User = phone_number.value;
    }

    if (number_of_snils.value === '') {
        number_of_snils.style.border = "1px solid red";
        document.getElementById("number_of_snils_Err").style.display = "block";
        number_of_snils.focus();
        return false;
    } else {
        number_of_snils_User = number_of_snils.value;
    }

    if (series_number.value === '') {
        series_number.style.border = "1px solid red";
        document.getElementById("series_number_Err").style.display = "block";
        series_number.focus();
        return false;
    } else {
        series_number_User = series_number.value;
    }
    if (issue_date.value === '') {
        issue_date.style.border = "1px solid red";
        document.getElementById("issue_date_Err").style.display = "block";
        issue_date.focus();
        return false;
    } else {
        issue_date_User = issue_date.value;
    }
    if (who_issued.value === '') {
        who_issued.style.border = "1px solid red";
        document.getElementById("who_issued_Err").style.display = "block";
        who_issued.focus();
        return false;
    } else {
        who_issued_User = who_issued.value;
    }
    if (department_code.value === '') {
        department_code.style.border = "1px solid red";
        document.getElementById("department_code_Err").style.display = "block";
        department_code.focus();
        return false;
    } else {
        department_code_User = department_code.value;
    }
    if (dob.value === '') {
        dob.style.border = "1px solid red";
        document.getElementById("dob_Err").style.display = "block";
        dob.focus();
        return false;
    } else {
        dob_User = dob.value;
    }
    if (place_of_birth.value === '') {
        place_of_birth.style.border = "1px solid red";
        document.getElementById("place_of_birth_Err").style.display = "block";
        place_of_birth.focus();
        return false;
    } else {
        place_of_birth_User = place_of_birth.value;
    }


    if (last_name_User != null && first_name_User != null && patronymic_User != null && phone_number_User != null && number_of_snils_User != null && series_number_User != null && issue_date_User != null && who_issued_User != null && department_code_User != null && dob_User != null&& place_of_birth_User != null) {
        const User = new Users(last_name_User, first_name_User, patronymic_User, phone_number_User, number_of_snils_User, series_number_User, issue_date_User, who_issued_User,
            department_code_User, dob_User, place_of_birth_User);
        const userID = Id(users);
        users[userID] = User;
        console.log(User);
        return true;
    }
}

function Verify(inp, ind) {
    if (inp.value !== '') {
        inp.style.border = "1px solid silver";
        document.getElementById(ind).style.display = "none";
        return true;
    }
}

function tel_Verify() {
    if (phone_number.value !== '') {
        if (phone_number.value.length === 12) {
            document.getElementById("IDLenthErr").style.display = "none";
            return true;
        }
        phone_number.style.border = "1px solid silver ";
        document.getElementById("IDerr").style.display = "none";
        return true;
    }

}
