// app-data.js

export const macros = ["carbs", "protein", "fat"];
const macroCalories = [4, 4, 9];

export default class AppData {
    constructor () {
        this.items = [];
    }

    addFood (newFood) {
        this.items.push(newFood);
    }

    getTotal (key) {
        if(key === "calories"){
            return this.items.reduce((total, current) => total + current.calories, 0);
        }

        if(!macros.includes(key)){
            throw new Error("invalid key:", key);
        }

        return this.items.reduce((total, current) => total + current[key], 0);
    }
}

export class Food {
    constructor(name, ...macroValues){
        /**
         * macroValues must be passed as the same order in the macros array
         */
        this.name = name;
        for(let i = 0; i < macros.length; i++){
            this[macros[i]] = Number.parseInt(macroValues[i]);
        }
    }

    get calories(){
        let sum = 0;
        for(let i = 0; i < macros.length; i++){
            sum += this[macros[i]] * macroCalories[i];
        }
        return sum;
    }
}
