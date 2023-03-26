//API REQUEST
const API_URL = "https://api.uberchord.com/v1/chords/";
const xhr = new XMLHttpRequest();

//DECLARATIONS
const chordButtons = document.getElementById("chordButtons");
const colIndex = document.getElementById("colIndex");
const rowIndex = document.getElementById("rowIndex");
const diapason = document.getElementById("diapason");
var strings = [];

//Request function
function onRequestHandler() {
    if(this.readyState == 4 && this.status == 200){
        const data = JSON.parse(this.response);
        var c = 0;
        for(let i=10; i>=0; i-=2){
            strings[c] = data[0].strings[i];
            c ++;
        }
    }
}


function getChord(chordName){
    xhr.addEventListener("load", onRequestHandler);
    xhr.open("GET", API_URL + chordName);
    xhr.send();
    showChord();
}



//MAIN CHORDS 
const chordsNatural = ["C", "D", "E", "F", "G", "A", "B"];
const stringsAir = ["E", "B", "G", "D", "A", "E"];

//CHORD SELECT BUTTONS
for(let i=0; i<6; i++){
    chordButtons.innerHTML += '<button id="chordButton'+ chordsNatural[i] +'" value="'+ chordsNatural[i] +'" class="bg-sky-500 hover:bg-blue-700 text-white font-bold py-2 px-4 border border-blue-700 rounded" onclick="getChord(this.value)">'+ chordsNatural[i] +'</button>'
}

//TAB INDEX
for(let i=1; i < 13; i++){
    colIndex.innerHTML += "<span class='w-4'>" + i + "</span>";
}

//DIAPASON
function showChord(){
    //Limpia el diapason
    diapason.innerHTML = "";
    rowIndex.innerHTML = "";
    //Lee el arreglo e imprime en consecuencia
    for(let i=1; i<=6; i++){
        if (strings[i-1] == "X") {
            rowIndex.innerHTML += "<div class='row-start-"+i+" text-center'>X</div>";
            printRow("");
        }else if(strings[i-1] == "0"){
            rowIndex.innerHTML += "<div class='row-start-"+i+" p-1 pr-2'><div class='w-4 h-4 rounded-full border-2 border-white'></div></div>";
            printRow("");
        }else {
            printRow(strings[i-1]);
        }
    }
}

//Imprime en el diapason
function printRow(value){
    //diapason.innerHTML += "<div class='col-span-12 w-full text-center border-r-4 border-b-2 border-white'>"+ value +"</div>";
    for(let i=0; i<12; i++){
        if(value == i+1){
            diapason.innerHTML += "<div class='text-center border-r-2 border-b-1 border-white'><div class='row-start-4 rounded-full bg-sky-500 w-6 h-6 mx-auto'>"+value+"</div></div>";
        }else {
            diapason.innerHTML += "<div class='text-center border-r-2 border-b-1 border-white p-2'></div>";
        }
    }
}


//Initial request
//document.addEventListener("DOMContentLoaded", getChord('C'));

