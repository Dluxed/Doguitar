//API REQUEST
const API_URL = "https://api.uberchord.com/v1/chords/";
const xhr = new XMLHttpRequest();

//DECLARATIONS
const chordButtons = document.getElementById("chordButtons");
const colIndex = document.getElementById("colIndex");
const rowIndex = document.getElementById("rowIndex");
const diapason = document.getElementById("diapason");
var strings = [];

var string1 = [12];
for(let i=0; i<12; i++){
    string1[i] = 0;    
}

function onRequestHandler() {
    if(this.readyState == 4 && this.status == 200){
        const data = JSON.parse(this.response);
        
        strings = data[0].strings;

        console.log(data[0]);

        console.log(data[0].strings);
        console.log(data[0].strings[0]);
        string1[0] = data[0].strings[0];
    }
}

xhr.addEventListener("load", onRequestHandler);
xhr.open("GET", API_URL + "C");
xhr.send();

function getChord(chordName){
    xhr.addEventListener("load", onRequestHandler);
    xhr.open("GET", API_URL + chordName);
    xhr.send();
}



//MAIN CHORDS 
const chordsNatural = ["C", "D", "E", "F", "G", "A", "B"];
const stringsAir = ["E", "B", "G", "D", "A", "E"];

//TEST FUNCTION
    function wenasNoches(value) {
            console.log("Chord: " + value);
        }


//CHORD SELECT BUTTONS
for(let i=0; i<6; i++){
    chordButtons.innerHTML += '<button id="chordButton'+ chordsNatural[i] +'" value="'+ chordsNatural[i] +'" class="bg-sky-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded" onclick="getChord(this.value)">'+ chordsNatural[i] +'</button>'
}

//CORD INDEX
for(let i=1; i < 13; i++){
    colIndex.innerHTML += "<span class='w-4'>" + i + "</span>";
}

//ROW INDEX
for(let i=1; i<=6; i++){
    rowIndex.innerHTML += "<h1>"+ i +"</h1>";
}

/*//DIAPASON
for(let i=1; i<=72; i++){
    diapason.innerHTML += "<h1 class='text-center border-r-4 border-b-2 border-white'>"+ "-X-" +"</h1>";
}
*/
