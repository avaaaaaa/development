import FetchWrapper from "./test2.js";
import { API_KEY } from "./.data.js";

const API = new FetchWrapper(`https://v6.exchangerate-api.com/v6/${API_KEY}`);
const baseDropdown = document.querySelector("#base-currency");
const targetDropdown = document.querySelector("#target-currency");
const conversionResult = document.querySelector("#conversion-result");
const swapButton = document.querySelector("#swap-button");
const baseInput = document.querySelector("#base-input");
let saveData = "";


const init = () => {
    // create dropdowns
    // https://www.exchangerate-api.com/docs/supported-codes-endpoint
    API.get("/codes")
    .then(data => {
        //console.log(data);
        const entryHtml = data.supported_codes.map(
            entry => `<option value="${entry[0]}">[${entry[0]}]  ${entry[1]}</option>`);
        const htmlString = entryHtml.join("");
        baseDropdown.innerHTML = htmlString;
        targetDropdown.innerHTML = htmlString;
    })
    .finally(() => {
        // initiate saveData
        updateData();
    });
}

const checkInput = () => Number(baseInput.value);

const updateData = () => {
    // https://www.exchangerate-api.com/docs/standard-requests
    return API.get(`/latest/${baseDropdown.value}`)
    .then(data => {
        //console.log(data);
        saveData = data;
    })
    .catch(error => console.error(error));
}

const handleChange = () => {
    updateData().finally(() => {
        showResult();
    });
}

const handleSwap = () => {
    [baseDropdown.value, targetDropdown.value] = [targetDropdown.value, baseDropdown.value];
    // this does not trigger change event on dropdowns
    // thus, we need to call handleChange() manually
    handleChange();
}

const handleInput = () => {
    showResult();
}

const showResult = () => {
    const result = checkInput();
    if(Number.isNaN(result)){
        conversionResult.textContent = "invalid input";
        return
    }
    const conversion = saveData.conversion_rates[targetDropdown.value];
    conversionResult.textContent = conversion * result;
}


baseDropdown.addEventListener("change", handleChange);

targetDropdown.addEventListener("change", handleChange);

swapButton.addEventListener("click", handleSwap);

baseInput.addEventListener("keyup", handleInput);


init();