// TODO
import FetchWrapper from "./fetch-wrapper.js";
import {startLoader, stopLoader} from "./helpers.js";

const API = new FetchWrapper("https://api.github.com");
const username = document.querySelector("#github-username");
const form = document.querySelector("#repos-form");
const list = document.querySelector("#repos-list");
const button = document.querySelector("#get-repos");

form.addEventListener("submit", event => {
    event.preventDefault();
    startLoader(button);
    API.get(`/users/${username.value}/repos`).then(data => {
        //console.log(data);
        const entryHtml = data.map(entry => {
            const name = entry.full_name;
            const description = entry.description;
            const url = entry.html_url;
            return `<li>
            <a href="${url}" target="_blank">
                <h2>${name}</h2>
                <p>${description}</p>
            </a>
            </li>`;
        });
        list.innerHTML = entryHtml.join("");
        
    }).finally(()=>{
        stopLoader(button, "Get repos");
    })
});
