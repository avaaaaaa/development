* Food API
The food API used in the final project is hosted on Firebase.
Since anyone can read/add food entries to this API, we've made it possible for you to have your own space where you add/read food entries. For that, you have to replace the {namespace} with any random string.
Now, assuming nobody else used this {namespace}, you should see {} if you open the base URL in a new tab. If you see some data, you need to choose another {namespace}

The Base URL is: https://firestore.googleapis.com/v1/projects/jsdemo-3f387/databases/(default)/documents/{namespace}

If the API above's limit is exhausted, you can then use the following backup API: https://firestore.googleapis.com/v1/projects/jsdemo2-3f387/databases/(default)/documents/{namespace}


** this is the baseURL we chose for the Food API
https://firestore.googleapis.com/v1/projects/jsdemo-3f387/databases/(default)/documents/gfefinalproject


** TODOS
add food
render added food
show snackbar
list foods
define and import AppData class

/*
Method: GET
Endpoint: "/"

Method: POST
Endpoint: "/"
Example body:

{
  fields: {
    name: { stringValue: "pizza" },
    carbs: { integerValue: "10" },
    protein: { integerValue: "10" },
    fat: { integerValue: "10" }
  }
}
*/

/* tests:
Posts data when form is submitted
Does not hardcode answer
Clears the form when post is successful
Does not clear the form when Post fails

Adds entry to existing list
Renders entry when POST is successful

Shows snackbar with success message after successful POST
Shows snackbar with error message when POST fails

Lists saved entries
Handles responses with no entries

Renders graph after listing logged foods
Re-renders graph after logging new food

Shows total calories after listing logged foods
Updates total calories after logging new food
*/
