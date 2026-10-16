// index.js
import FetchWrapper from "./fetch-wrapper.js";
import {capitalize} from "./helpers.js";
import AppData, {Food, macros} from "./app-data.js";
import snackbar from "snackbar";
import Chart from "chart.js/auto";


const API = new FetchWrapper("https://firestore.googleapis.com/v1/projects/jsdemo-3f387/databases/(default)/documents/gfefinalproject3");
const form = document.querySelector("#create-form");
const nameDropdown = document.querySelector("#create-name");
const carbsInput = document.querySelector("#create-carbs");
const proteinInput = document.querySelector("#create-protein");
const fatInput = document.querySelector("#create-fat");
const foodList = document.querySelector("#food-list");
const totalCalories = document.querySelector("#total-calories");
const context = document.querySelector("#app-chart");

const appData = new AppData();
let chartInstance = null;


const addFood = () => {
    const name = nameDropdown.value;
    const carbs = carbsInput.value;
    const protein = proteinInput.value;
    const fat = fatInput.value;

    const requestBody = {
        fields: {
            name: {stringValue: name},
            carbs: {integerValue: carbs},
            protein: {integerValue: protein},
            fat: {integerValue: fat}
        }
    }

    API.post("/", requestBody)
    .then(data => {
        console.log(data); 
        if(data.error){
            throw data.error;
        }
        const newFood = new Food(name, carbs, protein, fat);
        appData.addFood(newFood);   // update appData with the new food
        renderFood(newFood);   // render the new food under the Log section
        updateChart(newFood);  // update the chart after adding the new food
        updateTotalCalories();  // update total calories
        snackbar.show("Food added successfully.");  // show the snackbar
        form.reset();   // reset the inputs
    }).catch(error => {
        console.error(error);
        snackbar.show("Some data is missing.")
    });
}

const renderFood = (food) => {
  const HTMLEntry = _createHTMLForItem(food);
  foodList.insertAdjacentHTML("beforeend", HTMLEntry);
}

const init = async () => {
    const data = await API.get("/");
    //console.log(data);
    //console.log(data.documents[0].fields);  // name, carbs, protein, fat
    //console.log(data.documents[0].fields.name);  // stringValue: pasta
    //console.log(data.documents[0].fields.carbs);  // integerValue: 1
    
    if(!data.documents){  // check if data is {}
      renderChart();
      return
    }

    const HTMLEntriesForItems = data.documents.map(
      item => {
        const name = item.fields.name.stringValue;
        const carbs = item.fields.carbs.integerValue;
        const protein = item.fields.protein.integerValue;
        const fat = item.fields.fat.integerValue;
        
        const food = new Food(name, carbs, protein, fat);
        appData.addFood(food);  // fill appData with the existed items

        return _createHTMLForItem(food);
      });
  
    //console.log(HTMLEntriesForItems);
    foodList.innerHTML = HTMLEntriesForItems.join("");
    renderChart();
    updateTotalCalories();
}

const _createHTMLForItem = (food) => {
  const HTMLForItem = `
  <li class="card">
    <div>
      <h3 class="name">${capitalize(food.name)}</h3>
      <div class="calories">${food.calories} calories</div>
      ${_createHTMLForMacros(food)}
    </div>
  </li>`;
  return HTMLForItem;
}

const _createHTMLForMacros = (food) => {
  const HTMLForMacros = macros.map(macro =>
    `<li class="${macro}"><div>${macro}</div><div class="value">${food[macro]}g</div></li>`
  );
  return `<ul class="macros">${HTMLForMacros.join("")}</ul>`
}

const renderChart = () => {
  // render the chart under the Stats section
  chartInstance = new Chart(context, {
      type: "bar",
      data: {
        labels: macros,
        datasets: [
          {
            label: "Macronutrients",
            data: macros.map(macro => appData.getTotal(macro)),
            backgroundColor: ["#25AEEE", "#FECD52", "#57D269"],
            borderWidth: 3, // example of other customization
          },
        ],
      },
      options: {
        scales: {
          y: {
            beginAtZero: true
          }
        }
      }
    });
}

const updateChart = (food) => {
  //console.log(chartInstance);
  for(let i = 0; i < macros.length; i++){
    chartInstance.data.datasets[0].data[i] += food[macros[i]];  // first, update the data array
  }
  chartInstance.update();   // then, update the chart
}

const updateTotalCalories = () => {
  totalCalories.textContent = appData.getTotal("calories");
}


form.addEventListener("submit", event => {
    event.preventDefault();
    addFood();
});

init();